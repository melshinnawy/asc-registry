# ASC Registry

**ASC (AI Security Controls) Registry** is an open standard for defining AI security controls as machine-readable, testable, monitorable, and versioned artifacts.

Unlike traditional security frameworks that are published as static documents, ASC controls are designed to be implemented, validated, monitored, and integrated into engineering workflows, security operations, governance programs, and automation pipelines.

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

## Vision

ASC aims to become the operational security control layer for AI systems.

Rather than replacing existing frameworks, ASC translates security guidance into controls that can be:

- Implemented
- Tested
- Monitored
- Audited
- Automated

---

## The Problem

Organizations implementing AI systems face several challenges:

1. Security guidance is fragmented across multiple frameworks.
2. Controls are often descriptive but not testable.
3. Security requirements are difficult to automate.
4. Validation approaches vary across organizations.
5. Security teams lack a common control language for AI systems.

This often results in inconsistent implementations, duplicated effort, and difficult audits.

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

Controls must include references to recognized standards, frameworks, or research.

### Machine-Readable

Controls must conform to the published schema and support automation.

---

## Framework Alignment

ASC does not replace existing AI security frameworks.

Instead, ASC provides an operational security control layer that translates framework guidance into practical controls.

Current framework alignment includes:

- OWASP LLM Top 10
- NIST AI RMF
- MITRE ATLAS

Framework mappings are maintained within:

```text
mappings/
```

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
│   ├── ASC-005.yaml
│   ├── ASC-006.yaml
│   ├── ASC-007.yaml
│   ├── ASC-008.yaml
│   ├── ASC-009.yaml
│   └── ASC-010.yaml
│
├── mappings
│   ├── owasp-llm-top10.yaml
│   └── nist-ai-rmf.yaml
│
├── tests
│   ├── prompt_injection
│   ├── retrieval_security
│   ├── access_control
│   ├── agent_security
│   └── output_security
│
├── use-cases
│   ├── secure-rag.md
│   └── secure-agent.md
│
└── validation
    └── harness.py
```

---

## Current Controls

| ID | Title | Primary Risk Area | Status |
|------|------|------|------|
| ASC-001 | Prompt Injection Protection | Input Security | Active |
| ASC-002 | Retrieval Data Isolation | Data Security | Active |
| ASC-003 | Model Access Control | Identity & Access Security | Active |
| ASC-004 | Agent Permission Boundaries | Agent Security | Active |
| ASC-005 | Output Validation and Guardrails | Output Security | Active |
| ASC-006 | AI Supply Chain Security | Supply Chain Security | Active |
| ASC-007 | Training Data Integrity | Data Integrity | Active |
| ASC-008 | AI Logging and Telemetry | Monitoring & Detection | Active |
| ASC-009 | Secure Model Deployment | Deployment Security | Active |
| ASC-010 | AI Incident Response | Incident Response | Active |

---

## ASC Core Security Baseline

The ASC Core Security Baseline establishes ten foundational control domains for AI systems.

| Domain | Control |
|----------|----------|
| Input Security | ASC-001 |
| Data Security | ASC-002 |
| Identity & Access Security | ASC-003 |
| Agent Security | ASC-004 |
| Output Security | ASC-005 |
| Supply Chain Security | ASC-006 |
| Data Integrity | ASC-007 |
| Monitoring & Detection | ASC-008 |
| Deployment Security | ASC-009 |
| Incident Response | ASC-010 |

Together these controls provide foundational coverage across modern AI applications, RAG systems, AI agents, model serving platforms, and enterprise AI environments.

---

## Security Tests

ASC includes foundational security validation tests mapped to controls.

| Test | Control |
|--------|--------|
| TEST-001 | ASC-001 |
| TEST-002 | ASC-002 |
| TEST-003 | ASC-003 |
| TEST-004 | ASC-004 |
| TEST-005 | ASC-005 |

---

## Security Use Cases

ASC currently includes:

- Secure RAG
- Secure Agent

These use cases demonstrate how controls and security tests can be combined to secure real-world AI deployments.

---

## Namespace

ASC uses globally unique identifiers for controls.

Examples:

```text
ASC-001
ASC-002
ASC-003
```

Control identifiers are permanent and never reused.

See:

```text
docs/namespace.md
```

for namespace rules.

---

## Governance

ASC is governed through an open contribution and review process.

Core principles:

- Evidence-based controls
- Transparent review processes
- Permanent control identifiers
- Community-driven improvements
- Versioned evolution of the registry

See:

```text
GOVERNANCE.md
```

for governance details.

---

## RFC Process

New controls are proposed through Requests for Comments (RFCs).

Each proposal should include:

- Purpose
- Risk Addressed
- References
- Implementation Guidance
- Validation Requirements
- Monitoring Requirements

See:

```text
RFC_PROCESS.md
```

for the complete process.

---

## Validation

ASC controls are validated against the official JSON schema.

Validation tooling is located in:

```text
validation/harness.py
```

Validation ensures:

- Required fields are present
- Control identifiers follow ASC format
- Metadata complies with schema requirements
- Registry consistency is maintained

---

## Roadmap

### Version 0.1.0

- ASC Namespace
- Governance Model
- RFC Process
- JSON Schema
- Validation Harness

#### Core Security Controls

- ASC-001 Prompt Injection Protection
- ASC-002 Retrieval Data Isolation
- ASC-003 Model Access Control
- ASC-004 Agent Permission Boundaries
- ASC-005 Output Validation and Guardrails
- ASC-006 AI Supply Chain Security
- ASC-007 Training Data Integrity
- ASC-008 AI Logging and Telemetry
- ASC-009 Secure Model Deployment
- ASC-010 AI Incident Response

### Version 0.2.0

- Framework Alignment Layer
- OWASP LLM Top 10 Mappings
- NIST AI RMF Mappings
- MITRE ATLAS References
- GitHub Actions Validation
- Security Test Library
- Security Use Cases
- Automated Schema Enforcement
- Community RFC Reviews

### Version 1.0.0

- Comprehensive AI Security Control Library
- Expanded Framework Coverage
- Community Governance Model
- Automated Validation Pipeline
- Reference Implementations
- Security Testing Library
- Use Case Driven Control Profiles

---

## Contributing

Contributions are welcome.

Before submitting a control:

1. Review the namespace rules.
2. Review the schema requirements.
3. Provide supporting references.
4. Define implementation guidance.
5. Define validation requirements.
6. Define monitoring requirements.

---

## License

This project is released under the Apache License 2.0.

---

## Status

**ASC Registry v0.2.0**

Current Capabilities:

- 10 AI Security Controls
- OWASP LLM Top 10 Mappings
- NIST AI RMF Mappings
- MITRE ATLAS References
- GitHub Actions Validation
- Security Test Library
- Security Use Cases
- JSON Schema Validation

Building an open, testable, monitorable, and machine-readable standard for AI Security Controls.
