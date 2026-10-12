# Changelog

All notable changes to ASC Registry will be documented in this file.

---

## v0.2.1

### Fixed

- Restored the truncated `schema/control.schema.json` (it was invalid JSON)
- Repaired `ASC-011.yaml`, `ASC-002.yaml` (missing `references`, `version`, valid mappings), `TEST-003.json`, `TEST-013.json`
- Removed stray characters from docs and the README

### Changed

- Validation harness now validates against the schemas, collects all errors, and exits non-zero on failure
- CI now installs dependencies and runs the harness on pushes and pull requests
- All 15 tests now use one schema (`schema/test.schema.json`); TEST-001 to TEST-005 gained real steps and criteria
- Framework mappings are generated from the control files, removing contradictions; marked provisional pending verification
- README rewritten and its control table generated
- SECURITY.md now uses private reporting; added CODEOWNERS and a Code of Conduct reporting channel

## v0.2.0

### Added

- ASC-001 through ASC-015
- OWASP LLM Top 10 mappings
- NIST AI RMF mappings
- MITRE ATLAS references
- Security test library
- GitHub Actions validation
- Secure RAG use case
- Secure Agent use case

### Improved

- Repository structure
- Control consistency
- Validation workflows

---

## v0.1.0

### Initial Release

- Governance framework
- RFC process
- Control schema
- Validation harness
- Initial registry structure
