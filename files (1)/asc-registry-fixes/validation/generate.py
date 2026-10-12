"""Generate derived registry files from the control YAML (single source of truth).

Controls in controls/*.yaml are authoritative. Everything below is derived:
  - mappings/owasp-llm-top10.yaml
  - mappings/nist-ai-rmf.yaml
  - mappings/mitre-atlas.yaml
  - docs/controls.md
  - the control table inside README.md (between the ASC:CONTROLS markers)

Usage:
  python validation/generate.py          # rewrite derived files
  python validation/harness.py           # verifies they are in sync (CI)
"""
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BEGIN = "<!-- ASC:CONTROLS:BEGIN -->"
END = "<!-- ASC:CONTROLS:END -->"


def load_controls(root=ROOT):
    controls = []
    for f in sorted((root / "controls").glob("*.yaml")):
        controls.append(yaml.safe_load(f.read_text(encoding="utf-8")))
    return sorted(controls, key=lambda c: c["id"])


def load_tests(root=ROOT):
    by_control = {}
    for f in sorted((root / "tests").glob("*/*.json")):
        t = json.loads(f.read_text(encoding="utf-8"))
        by_control.setdefault(t["control"], []).append(t["id"])
    return by_control


def _mapping_file(controls, key, framework, note):
    lines = [
        "# GENERATED FILE - do not edit by hand.",
        "# Source of truth: controls/*.yaml  |  Regenerate: python validation/generate.py",
        f"framework: {framework}",
        "status: provisional",
        f"note: {note}",
        "",
        "mappings:",
    ]
    for c in controls:
        lines.append(f"  {c['id']}:")
        for v in c["framework_mappings"][key]:
            lines.append(f"    - {v}")
    return "\n".join(lines) + "\n"


def render_readme_table(controls, tests):
    rows = [
        "| ID | Title | OWASP LLM | NIST AI RMF | MITRE ATLAS | Test |",
        "|----|-------|-----------|-------------|-------------|------|",
    ]
    for c in controls:
        m = c["framework_mappings"]
        rows.append(
            "| {id} | {title} | {o} | {n} | {a} | {t} |".format(
                id=c["id"],
                title=c["title"],
                o=", ".join(m["owasp_llm"]),
                n=", ".join(m["nist_ai_rmf"]),
                a=", ".join(m["mitre_atlas"]),
                t=", ".join(tests.get(c["id"], [])) or "-",
            )
        )
    return "\n".join(rows)


def render_all(root=ROOT):
    controls, tests = load_controls(root), load_tests(root)
    out = {}
    out["mappings/owasp-llm-top10.yaml"] = _mapping_file(
        controls, "owasp_llm", "OWASP LLM Top 10",
        "OWASP edition/numbering to be confirmed - see MAPPING_REVIEW.md")
    out["mappings/nist-ai-rmf.yaml"] = _mapping_file(
        controls, "nist_ai_rmf", "NIST AI RMF",
        "Subcategory-level verification pending - see MAPPING_REVIEW.md")
    out["mappings/mitre-atlas.yaml"] = _mapping_file(
        controls, "mitre_atlas", "MITRE ATLAS",
        "Technique IDs pending verification - see MAPPING_REVIEW.md")

    catalog = ["# ASC Control Catalog", "",
               "_Generated from `controls/*.yaml`. Do not edit by hand._", ""]
    catalog += [f"- **{c['id']}** {c['title']} ({c['status']}, v{c['version']})" for c in controls]
    out["docs/controls.md"] = "\n".join(catalog) + "\n"

    readme_path = root / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    if BEGIN in readme and END in readme:
        head, rest = readme.split(BEGIN, 1)
        _, tail = rest.split(END, 1)
        out["README.md"] = f"{head}{BEGIN}\n{render_readme_table(controls, tests)}\n{END}{tail}"
    return out


def main():
    for rel, content in render_all().items():
        (ROOT / rel).write_text(content, encoding="utf-8")
        print(f"wrote {rel}")


if __name__ == "__main__":
    sys.exit(main())
