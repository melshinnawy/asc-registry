# ASC Registry

[![ASC Validation](https://github.com/melshinnawy/asc-registry/actions/workflows/validate.yml/badge.svg)](https://github.com/melshinnawy/asc-registry/actions/workflows/validate.yml)

**ASC (AI Security Controls) Registry** is an open standard for defining AI security controls as machine-readable, testable, monitorable, and versioned artifacts.

Unlike security frameworks published as static documents, ASC controls are designed to be implemented, validated, monitored, and integrated into engineering workflows, security operations, governance programs, and automation pipelines.

## Why ASC

1. Security guidance is fragmented across multiple frameworks.
2. Controls are often descriptive but not testable.
3. Security requirements are difficult to automate.
4. Validation approaches vary across organizations.
5. Security teams lack a common control language for AI systems.

ASC does not replace existing frameworks. It translates their guidance into controls that can be implemented, tested, monitored, audited, and automated.

## Design principles

Every ASC control must be **implementable**, **verifiable** (has a test), **monitorable**, **evidence-based** (cites recognized sources), and **machine-readable** (conforms to `schema/control.schema.json`).

## Controls (v0.2.1)

Identifiers are permanent and never reused. This table is generated from `controls/*.yaml`.

<!-- ASC:CONTROLS:BEGIN -->
| ID | Title | OWASP LLM | NIST AI RMF | MITRE ATLAS | Test |
|----|-------|-----------|-------------|-------------|------|
| ASC-001 | Prompt Injection Protection | LLM01 | MAP.2 | AML.T0051 | TEST-001 |
| ASC-002 | Retrieval Data Isolation | LLM06 | MANAGE.2 | AML.T0015 | TEST-002 |
| ASC-003 | Model Access Control | LLM02 | GOVERN.3 | AML.T0028 | TEST-003 |
| ASC-004 | Agent Permission Boundaries | LLM08 | MANAGE.4 | AML.T0043 | TEST-004 |
| ASC-005 | Output Validation and Guardrails | LLM01 | MEASURE.2 | AML.T0051 | TEST-005 |
| ASC-006 | AI Supply Chain Security | LLM05 | GOVERN.2 | AML.T0000 | TEST-006 |
| ASC-007 | Training Data Integrity | LLM03 | MEASURE.2 | AML.T0018 | TEST-007 |
| ASC-008 | AI Logging and Telemetry | LLM08 | MANAGE.4 | AML.T0027 | TEST-008 |
| ASC-009 | Secure Model Deployment | LLM05 | MANAGE.3 | AML.T0028 | TEST-009 |
| ASC-010 | AI Incident Response | LLM10 | MANAGE.5 | AML.T0043 | TEST-010 |
| ASC-011 | Model Monitoring Security | LLM08 | MANAGE.4 | AML.T0027 | TEST-011 |
| ASC-012 | AI Red Teaming | LLM01 | MEASURE.3 | AML.T0040 | TEST-012 |
| ASC-013 | Sensitive Data Protection | LLM06 | GOVERN.4 | AML.T0015 | TEST-013 |
| ASC-014 | Third-Party AI Risk Management | LLM05 | GOVERN.3 | AML.T0028 | TEST-014 |
| ASC-015 | Human Oversight and Approval | LLM10 | GOVERN.5 | AML.T0043 | TEST-015 |
<!-- ASC:CONTROLS:END -->

Framework mappings are **provisional** and under verification. See [MAPPING_REVIEW.md](MAPPING_REVIEW.md).

## Repository structure

```text
controls/     one YAML file per control (source of truth)
tests/        one JSON file per security test, grouped by area
mappings/     generated mappings to OWASP LLM, NIST AI RMF, MITRE ATLAS
schema/       JSON Schemas for controls and tests
validation/   harness.py (validator) and generate.py (derived files)
use-cases/    control profiles: secure-rag, secure-agent
docs/         catalog and namespace rules
```

## Validate locally

```bash
pip install -r requirements.txt
python validation/generate.py   # regenerate derived files after editing controls
python validation/harness.py    # exits non-zero on any problem
```

The same check runs in GitHub Actions on every push and pull request.

## Governance and contributing

- [GOVERNANCE.md](GOVERNANCE.md) - how the registry is maintained
- [RFC_PROCESS.md](RFC_PROCESS.md) - how controls are proposed
- [CONTRIBUTING.md](CONTRIBUTING.md) - how to contribute
- [SECURITY.md](SECURITY.md) - reporting vulnerabilities

## Roadmap

- **0.2.x** - Working schema validation and CI, unified test format, generated mappings (this release)
- **0.3.0** - Verified framework mappings, threat scenario and severity fields, URL-based references
- **1.0.0** - Reference implementations, versioned release bundle, machine-readable use-case profiles

## License

Apache License 2.0.
