"""ASC Registry validation harness.

Validates every control and test against its JSON Schema, enforces registry
consistency rules, and verifies that derived files are in sync with the
controls. Collects ALL problems, then exits non-zero if any were found.

Usage:  python validation/harness.py
"""
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

import yaml
from jsonschema import Draft7Validator

import generate

ROOT = generate.ROOT
errors = []


def err(msg):
    errors.append(msg)
    print(f"  FAIL  {msg}")


def load_schema(name):
    path = ROOT / "schema" / name
    try:
        schema = json.loads(path.read_text(encoding="utf-8"))
        Draft7Validator.check_schema(schema)
        return Draft7Validator(schema)
    except Exception as exc:  # unreadable or invalid schema is fatal
        print(f"FATAL: schema {name} is invalid: {exc}")
        sys.exit(1)


def jsonable(obj):
    """YAML may parse bare dates as date objects; normalise to ISO strings."""
    return json.loads(json.dumps(obj, default=lambda o: o.isoformat()
                                 if isinstance(o, (date, datetime)) else str(o)))


def check_instance(validator, data, label):
    for e in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        loc = ".".join(str(p) for p in e.path) or "(root)"
        err(f"{label}: {loc}: {e.message[:140]}")


def main():
    print("ASC Registry Validation Harness v0.2.1")
    control_v = load_schema("control.schema.json")
    test_v = load_schema("test.schema.json")
    print("OK    schemas load and are valid")

    # ---- controls
    controls = {}
    for f in sorted((ROOT / "controls").glob("*.yaml")):
        label = f"controls/{f.name}"
        try:
            data = jsonable(yaml.safe_load(f.read_text(encoding="utf-8")))
        except yaml.YAMLError as exc:
            err(f"{label}: YAML parse error: {str(exc).splitlines()[0]}")
            continue
        if not isinstance(data, dict):
            err(f"{label}: top level must be a mapping")
            continue
        check_instance(control_v, data, label)
        cid = data.get("id")
        if cid and f.stem != cid:
            err(f"{label}: filename does not match id '{cid}'")
        if cid in controls:
            err(f"{label}: duplicate id {cid}")
        if cid:
            controls[cid] = data
        if data.get("created") and data.get("updated") and data["updated"] < data["created"]:
            err(f"{label}: 'updated' is earlier than 'created'")
    print(f"      {len(controls)} control file(s) checked")

    # ids sequential, never reused, no gaps
    nums = sorted(int(c.split("-")[1]) for c in controls if re.fullmatch(r"ASC-\d{3}", c))
    for expected, actual in zip(range(1, len(nums) + 1), nums):
        if expected != actual:
            err(f"control id gap: expected ASC-{expected:03d}, found ASC-{actual:03d}")
            break

    # ---- tests
    test_ids, tests_per_control, n_tests = set(), {}, 0
    for f in sorted((ROOT / "tests").glob("*/*.json")):
        label = f"tests/{f.parent.name}/{f.name}"
        n_tests += 1
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            err(f"{label}: JSON parse error: {exc}")
            continue
        check_instance(test_v, data, label)
        tid, cref = data.get("id"), data.get("control")
        if tid and f.stem != tid:
            err(f"{label}: filename does not match id '{tid}'")
        if tid in test_ids:
            err(f"{label}: duplicate id {tid}")
        test_ids.add(tid)
        if cref and cref not in controls:
            err(f"{label}: references unknown control {cref}")
        if cref:
            tests_per_control.setdefault(cref, []).append(tid)
    print(f"      {n_tests} test file(s) checked")

    for cid, c in controls.items():
        if c.get("status") == "active" and cid not in tests_per_control:
            err(f"{cid}: active control has no test")

    # ---- derived files in sync
    try:
        for rel, expected in generate.render_all().items():
            path = ROOT / rel
            if not path.exists() or path.read_text(encoding="utf-8") != expected:
                err(f"{rel}: out of date - run 'python validation/generate.py'")
    except Exception as exc:
        err(f"could not render derived files: {exc}")

    # ---- every other yaml/json file must at least parse
    for f in list((ROOT / "mappings").glob("*.yaml")):
        try:
            yaml.safe_load(f.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            err(f"mappings/{f.name}: YAML parse error: {str(exc).splitlines()[0]}")

    print()
    if errors:
        print(f"VALIDATION FAILED: {len(errors)} problem(s)")
        return 1
    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
