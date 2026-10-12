# ASC Registry

**ASC (AI Security Controls) Registry** is an open standard for defining AI security controls as machine-readable, testable, monitorable, and versioned artifacts.

Unlike traditional security frameworks that are published as static documents, ASC controls are designed to be implemented, validated, monitored, and integrated into engineering workflows, security operations, governance programs, and automation pipelines.

---

# Mission

The mission of ASC is to establish a common language for AI security controls that can be adopted by:

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

# Design Principles

Every ASC control must be:

## Implementable

Provide practical implementation guidance.

## Verifiable

Include validation requirements.

## Monitorable

Define monitoring requirements and security signals.

## Evidence-Based

Controls must include references to recognized standards, frameworks, or research.

## Machine-Readable

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

This enables organizations to align engineering controls with governance, compliance, risk, and audit requirements.

---

# Framework Alignment

ASC aligns with established security frameworks:

- OWASP LLM Top 10
- NIST AI RMF
- MITRE ATLAS

Framework mappings are maintained under:

```text
mappings/
```

---

# Repository Structure

```text
asc-registry
│
├── controls/
├── mappings/
├── tests/
├── use-cases/
├── schema/
├── validation/
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
├── mappings
│   ├── README.md
│   ├── owasp-llm-top10.yaml
│   └── nist-ai-rmf.yaml
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

---

## Control Domains

The initial ASC baseline establishes five foundational security domains for AI systems.

| Domain | Control |
|----------|----------|
| Input Security | ASC-001 |
| Data Security | ASC-002 |
| Identity & Access Security | ASC-003 |
| Agent Security | ASC-004 |
| Output Security | ASC-005 |

Together these controls provide foundational coverage across the primary security layers of modern AI applications.

---

## Current Framework Coverage

| ASC Control | OWASP LLM | NIST AI RMF | MITRE ATLAS |
|------------|------------|------------|------------|
| ASC-001 | LLM01 | MAP.2 | AML.T0051 |
| ASC-002 | LLM06 | MANAGE.2 | AML.T0015 |
| ASC-003 | LLM02 | GOVERN.3 | AML.T0028 |
| ASC-004 | Pending | Pending | Pending |
| ASC-005 | Pending | Pending | Pending |

---

## Namespace

---

# ASC Security Baseline

The ASC Security Baseline currently consists of fifteen foundational control domains.

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
| Continuous Monitoring | ASC-011 |
| Adversarial Testing | ASC-012 |
| Sensitive Data Protection | ASC-013 |
| Third-Party AI Risk Management | ASC-014 |
| Human Oversight & Governance | ASC-015 |

These controls provide foundational security coverage across AI applications, RAG deployments, AI agents, model-serving platforms, and enterprise AI environments.

Control identifiers are permanent and never reused.

# Security Tests

ASC includes a growing security validation library linked to controls.

| Test | Control |
|--------|--------|
| TEST-001 | ASC-001 |
| TEST-002 | ASC-002 |
| TEST-003 | ASC-003 |
| TEST-004 | ASC-004 |
| TEST-005 | ASC-005 |
| TEST-006 | ASC-006 |
| TEST-007 | ASC-007 |
| TEST-008 | ASC-008 |
| TEST-009 | ASC-009 |
| TEST-010 | ASC-010 |
| TEST-011 | ASC-011 |
| TEST-012 | ASC-012 |
| TEST-013 | ASC-013 |
| TEST-014 | ASC-014 |
| TEST-015 | ASC-015 |

---

# Security Use Cases

Current use cases include:

for namespace rules.

---

# Governance

ASC follows an open governance model.

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

---

# RFC Process

New controls are introduced through Requests for Comments (RFCs).

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

## Version 0.1.0

- Namespace Definition
- Governance Model
- RFC Process
- Validation Harness
- Initial Security Controls

## Version 0.2.0

- Framework Alignment Layer
- OWASP LLM Top 10 Mappings
- NIST AI RMF Mappings
- MITRE ATLAS References
- GitHub Actions Validation
- Automated Schema Enforcement
- Community RFC Reviews

## Version 1.0.0

- Comprehensive AI Security Control Library
- Expanded Framework Coverage
- Community Governance Model
- Automated Validation Pipeline
- Reference Implementations
- Security Testing Library
- Use Case Driven Control Profiles

---

# Contributing

Contributions are welcome.

Before submitting a new control:

1. Review the namespace rules.
2. Review the schema requirements.
3. Provide supporting references.
4. Define implementation guidance.
5. Define validation requirements.
6. Define monitoring requirements.

---

# License

Released under the Apache License 2.0.

---

# Status

**ASC Registry v0.2.0**

Current Capabilities:

- 15 AI Security Controls
- 15 Security Validation Tests
- OWASP LLM Top 10 Alignment
- NIST AI RMF Alignment
- MITRE ATLAS References
- GitHub Actions Validation
- Security Use Cases
- JSON Schema Validation

Building an open, testable, monitorable, and machine-readable standard for AI Security Controls.

**ASC Registry v0.2.0 (Foundation Phase)**

Building an open, testable, monitorable, and machine-readable standard for AI Security Controls.
