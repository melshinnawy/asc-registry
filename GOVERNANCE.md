# Governance

## Purpose

The ASC Registry is an open standard for defining AI Security Controls as machine-readable, testable, and versioned artifacts.

This document defines how the registry is maintained and how changes are approved.

---

## Maintainers

Repository maintainers are responsible for:

- Reviewing control submissions
- Reviewing schema modifications
- Preserving namespace integrity
- Maintaining documentation
- Managing releases

---

## Control Submission Requirements

Each proposed ASC control MUST include:

- A control identifier
- A title
- A description
- Implementation guidance
- Validation requirements
- Monitoring requirements
- References to supporting sources

Controls that do not satisfy schema requirements will not be accepted.

---

## Schema Changes

Schema modifications require maintainer approval.

Changes must:

- Be documented
- Include justification
- Preserve backward compatibility whenever possible

Breaking changes should only be introduced in major releases.

---

## Namespace Governance

ASC identifiers are permanent.

Rules:

- IDs are never reused
- IDs are assigned sequentially
- Deprecated controls retain their original identifier
- Existing control IDs cannot be reassigned

Examples:

```text
ASC-001
ASC-002
ASC-003
```

---

## Review Process

All contributions are reviewed through GitHub pull requests.

Maintainers may request:

- Additional references
- Additional validation guidance
- Clarification of implementation requirements

Approval is based on technical quality, evidence, and consistency with ASC objectives.

---

## Future Governance

As community participation grows, governance may evolve to include:

- Multiple maintainers
- Advisory contributors
- Formal RFC reviews
- Community voting mechanisms

---

## Version

Governance Version: 0.1.0
