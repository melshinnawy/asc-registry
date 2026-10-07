# ASC Registry

**ASC**** Security Controls) Registry** is an open standard for defining AI security controls as machine-readable, testable, and versioned artifacts.

Unlike traditional security frameworks that are published as static documents, ASC controls are designed to be implemented, validated, monitored, and integrated into engineering workflows.

---

## Mission

The mission of the ASC Registry is to provide a common language for AI security controls that can be used by:

- Security Architects
- AI Engineers
- Cloud Engineers
- Detection Engineers
- SOC Teams
- Auditors
- Governance and Risk Teams
- Security Researchers

---

## The Problem

Organizations implementing AI systems face three major challenges:

1. Security guidance is fragmented across multiple frameworks.
2. Controls are often descriptive but not testable.
3. Most security documentation cannot be integrated into automation pipelines.

This results in inconsistent implementations, duplicated effort, and difficult audits.

ASC addresses these challenges by defining controls in a structured, machine-readable format.

---

## Design Principles

Every ASC control must be:

### Implementable

Controls must provide practical implementation guidance.

### Verifiable

Controls must include validation requirements.

### Monitorable

Controls must identify monitoring requirements and security signals.

### Evidence-Based

Controls must include references to recognized sources, frameworks, or research.

### Machine-Readable

Controls must conform to a published schema and support automation.

---

## Example Control

```yaml
id: ASC-001

title: Prompt Injection Protection

status: active

risk:
  - Prompt Injection
  - Instruction Override
```

---

## Repository Structure

```text
asc-registry
│
├── README.md
├── GOVERNANCE.md
├── RFC_PROCESS.md
│
├── docs
│   └── namespace.md
│
├── schema
│   └── control.schema.json
│
├── controls
│   └── ASC-001.yaml
│
└── validation
    └── harness.py
```

---

## Namespace

ASC uses globally unique identifiers for controls.

Examples:

```text
ASC-001
ASC-002
ASC-003
```

Control identifiers are permanent and are never reused.

See:

```text
docs/namespace.md
```

for detailed namespace rules.

---

## Governance

ASC is governed through an open contribution and review process.

Key principles:

- Controls require evidence-based references.
- Schema modifications require review.
- Control identifiers are permanent.
- Contributions are tracked through GitHub.

See:

```text
GOVERNANCE.md
```

for full governance details.

---

## RFC Process

New controls are proposed through Requests for Comments (RFCs).

A control proposal should include:

- Purpose
- Risk Addressed
- References
- Validation Requirements
- Monitoring Requirements

See:

```text
RFC_PROCESS.md
```

for details.

---

## Validation

ASC controls are validated against the official JSON schema.

Validation tooling is located in:

```text
validation/harness.py
```

The validation process ensures:

- Required fields are present
- Control identifiers follow ASC format
- Metadata follows schema requirements
- Registry consistency is maintained

---

## Current Controls

| ID | Title | Status |
|------|------|------|
| ASC-001 | Prompt Injection Protection | Active |

---

## Roadmap

### Version 0.1

- ASC Namespace
- Governance Model
- RFC Process
- JSON Schema
- ASC-001
- Validation Harness

### Version 0.2

- ASC-002 Retrieval Data Isolation
- ASC-003 Model Access Control
- Schema Enforcement
- GitHub Actions Validation

### Version 1.0

- Core Control Library
- Framework Mappings
- Community Review Process
- Automated Validation Pipeline

---

## Contributing

Contributions are welcome.

Before submitting a control:

1. Review the namespace rules.
2. Review the schema requirements.
3. Provide references.
4. Define validation steps.
5. Define monitoring requirements.

---

## License

This project is released under the Apache 2.0 License.

---

## Status

**ASC Registry v0.1.0**

Building an open, testable, machine-readable standard for AI security controls.
