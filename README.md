# ASC Registry

**ASC (AI Security Controls) Registry** is an open standard for defining AI security controls as machine-readable, testable, and versioned artifacts.

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
│   ├── ASC-001.yaml
│   ├── ASC-002.yaml
│   ├── ASC-003.yaml
│   ├── ASC-004.yaml
│   └── ASC-005.yaml
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

- Controls require evidence-based references
- Schema modifications require review
- Control identifiers are permanent
- Contributions are tracked through GitHub

See:

```text
GOVERNANCE.md
```

for governance details.

---

## RFC Process

New controls are proposed through Requests for Comments (RFCs).

Each control proposal should include:

- Purpose
- Risk Addressed
- References
- Validation Requirements
- Monitoring Requirements

See:

```text
RFC_PROCESS.md
```

for the complete review process.

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

| ID | Title | Primary Risk Area | Status |
|----|---------|------------------|---------|
| ASC-001 | Prompt Injection Protection | Input Security | Active |
| ASC-002 | Retrieval Data Isolation | Data Security | Active |
| ASC-003 | Model Access Control | Identity & Access | Active |
| ASC-004 | Agent Permission Boundaries | Agent Security | Active |
| ASC-005 | Output Validation and Guardrails | Output Security | Active |

---

## ASC Initial Baseline

The ASC Initial Baseline establishes five foundational control domains for AI systems:

| Domain | Control |
|----------|----------|
| Input Security | ASC-001 |
| Data Security | ASC-002 |
| Identity & Access Security | ASC-003 |
| Agent Security | ASC-004 |
| Output Security | ASC-005 |

Together, these controls provide foundational coverage across the primary security layers of modern AI applications.

---

## Roadmap

### Version 0.1.0

- ASC Namespace
- Governance Model
- RFC Process
- JSON Schema
- Validation Harness
- ASC-001 Prompt Injection Protection
- ASC-002 Retrieval Data Isolation
- ASC-003 Model Access Control
- ASC-004 Agent Permission Boundaries
- ASC-005 Output Validation and Guardrails

### Version 0.2.0

- GitHub Actions Validation
- Automated Schema Enforcement
- Additional Control Categories
- Community RFC Reviews

### Version 1.0.0

- Comprehensive AI Security Control Library
- Framework Cross-Mappings
- Community Governance Model
- Automated Validation Pipeline
- Reference Implementations

---

## Contributing

Contributions are welcome.

Before submitting a control:

1. Review the namespace rules.
2. Review the schema requirements.
3. Provide references.
4. Define implementation guidance.
5. Define validation requirements.
6. Define monitoring requirements.

---

## License

This project is released under the Apache License 2.0.

---

## Status

**ASC Registry v0.1.0**

Building an open, testable, and machine-readable standard for AI Security Controls.
