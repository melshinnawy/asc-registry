# Framework Mapping Review

All mappings in `controls/*.yaml` are **provisional** until each ID below is checked against the official source. Mapping files in `mappings/` are generated from the controls, so fix mappings in the control YAML only.

## To verify

1. **OWASP LLM Top 10 edition.** Most controls appear to use the 2023 (v1.1) numbering; a prior mapping file declared 2025. Pick one edition, record it, and re-map every control. Numbering differs between editions (for example supply chain and sensitive information disclosure).
2. **MITRE ATLAS technique IDs** (atlas.mitre.org). Check that each technique actually fits the control. Reused or doubtful: `AML.T0043` (ASC-004, 010, 015), `AML.T0000` (ASC-006), `AML.T0040` (ASC-012), `AML.T0015` (ASC-002, 013).
3. **NIST AI RMF subcategories.** Confirm each cited item (for example `MAP.2`, `MANAGE.4`) matches the control's intent, ideally at subcategory level (such as `MANAGE.4.1`; extend the schema pattern if so).
4. **ASC-002** was repaired using the values the previous README published (LLM06, MANAGE.2, AML.T0015). Treat them as unverified.

Once verified, remove the `status: provisional` note from `validation/generate.py`.
