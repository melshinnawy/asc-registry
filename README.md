# ASC Registry

ASC (AI Security Controls) Registry is an open standard for defining AI security controls as machine-readable, testable, monitorable, and versioned artifacts.

Unlike traditional security guidance published as static documentation, ASC controls are designed to support implementation, validation, monitoring, governance, and automation.

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

# Vision

ASC aims to become the operational security control layer for modern AI systems.

Rather than replacing existing frameworks, ASC transforms security guidance into controls that can be:

- Implemented
- Tested
- Monitored
- Audited
- Automated

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

Reference recognized frameworks, research, and standards.

## Machine-Readable

Support automation through structured formats and validation schemas.

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
└── LICENSE
```

---

# Current Controls

| ID | Title | Domain |
|------|------|------|
| ASC-001 | Prompt Injection Protection | Input Security |
| ASC-002 | Retrieval Data Isolation | Data Security |
| ASC-003 | Model Access Control | Identity & Access Security |
| ASC-004 | Agent Permission Boundaries | Agent Security |
| ASC-005 | Output Validation and Guardrails | Output Security |
| ASC-006 | AI Supply Chain Security | Supply Chain Security |
| ASC-007 | Training Data Integrity | Data Integrity |
| ASC-008 | AI Logging and Telemetry | Monitoring & Detection |
| ASC-009 | Secure Model Deployment | Deployment Security |
| ASC-010 | AI Incident Response | Incident Response |
| ASC-011 | Model Monitoring Security | Continuous Monitoring |
| ASC-012 | AI Red Teaming | Adversarial Testing |
| ASC-013 | Sensitive Data Protection | Data Protection |
| ASC-014 | Third-Party AI Risk Management | Vendor Risk Management |
| ASC-015 | Human Oversight and Approval | Governance & Oversight |

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

---

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

- Secure RAG
- Secure Agent

Future use cases may include:

- Secure Copilot Deployment
- Secure Model Serving
- Multi-Agent Security
- Enterprise AI Governance

---

# Governance

ASC follows an open governance model.

Core principles:

- Evidence-based controls
- Transparent review process
- Permanent control identifiers
- Community contribution model
- Versioned evolution of controls

See:

```text
GOVERNANCE.md
```

---

# RFC Process

New controls are introduced through Requests for Comments (RFCs).

Each RFC should include:

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

---

# Validation

ASC controls are validated against the official schema.

Validation capabilities include:

- Required field validation
- Control identifier validation
- Schema compliance checks
- Repository consistency verification

Automation is implemented through:

- JSON Schema
- Validation Harness
- GitHub Actions

---

# Roadmap

## Version 0.1.0

- Namespace Definition
- Governance Model
- RFC Process
- Validation Harness
- Initial Security Controls

## Version 0.2.0

- Framework Alignment
- OWASP Mappings
- NIST AI RMF Mappings
- MITRE ATLAS References
- GitHub Actions Validation
- Security Tests
- Security Use Cases

## Version 1.0.0

- Expanded Control Library
- Reference Architectures
- Community Governance
- Automated Validation Pipeline
- Additional Framework Coverage
- Security Control Profiles

---

# Contributing

Contributions are welcome.

Before submitting a new control:

1. Review the namespace requirements.
2. Review schema requirements.
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

Current governance is maintained by a single project maintainer.

Future versions may introduce additional maintainers, advisory reviewers, and community governance processes.
