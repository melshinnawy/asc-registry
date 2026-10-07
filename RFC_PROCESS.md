# RFC Process

## Purpose

The ASC Registry evolves through an open Request for Comments (RFC) process.

RFCs allow contributors to propose:

- New controls
- Schema enhancements
- Validation improvements
- Governance updates
- Framework mappings

All proposals are reviewed before being accepted into the ASC Registry.

---

## Proposal Submission

RFCs are submitted through GitHub Issues or Pull Requests.

Each RFC should clearly define:

- Purpose
- Security risk addressed
- Proposed solution
- References
- Validation requirements
- Monitoring requirements
- Potential impact on existing controls

---

## Control Proposal Requirements

Every proposed ASC control MUST include:

### Control Metadata

- Control Identifier (if assigned)
- Title
- Description
- Status

### Security Context

- Risk Addressed
- Threat Scenario
- Expected Security Outcome

### Operational Guidance

- Implementation Requirements
- Validation Requirements
- Monitoring Requirements

### Evidence

- References
- Industry Standards
- Research Publications
- Vendor Documentation
- Public Security Guidance

---

## Review Process

RFCs are evaluated against:

- Technical accuracy
- Evidence quality
- Practical applicability
- Consistency with ASC objectives
- Compatibility with the ASC schema

Maintainers may request revisions before approval.

---

## Approval Criteria

An RFC may be approved when:

- Required information is provided
- References are sufficient
- Validation requirements are defined
- Monitoring requirements are defined
- No conflicts exist with existing ASC controls

Approved proposals become part of the ASC Registry.

---

## Rejected Proposals

RFCs may be rejected if:

- Evidence is insufficient
- The proposal duplicates an existing control
- The proposal conflicts with registry objectives
- Validation requirements are missing

Rejected proposals may be revised and resubmitted.

---

## Versioning

Approved controls follow the ASC namespace and versioning standards.

Examples:

```text
ASC-001
ASC-002
ASC-003
```

Control identifiers are permanent once assigned.

---

## Future Evolution

As the registry grows, the RFC process may evolve to include:

- Advisory review boards
- Community voting
- Formal review periods
- Multiple maintainers

---

## Version

RFC Process Version: 0.1.0
