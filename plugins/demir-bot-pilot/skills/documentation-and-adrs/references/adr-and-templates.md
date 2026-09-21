# ADRs and document structures

Reuse the project's existing templates, numbering, extensions and headings. These are fallback outlines, not mandatory sections for every task. Replace example values with evidence; omit irrelevant fields rather than inventing them.

## ADR

Use for significant or costly-to-reverse decisions: architecture, data models, important dependencies, authentication or deployment choices. Record:

- Unique next ID and specific title.
- Status: proposed, accepted, superseded or deprecated according to evidence. A draft defaults to proposed; do not invent acceptance.
- Actual date when known; otherwise mark unknown or omit according to convention.
- Context: requirements, constraints, decision drivers and uncertainties.
- Decision or proposal and scope.
- Alternatives genuinely considered, benefits, costs and reason for selection. Mark newly suggested alternatives as suggestions, not historical deliberations.
- Consequences: trade-offs, risks, migration/compatibility and follow-up where applicable.
- Links to requirements, related decisions and evidence.

Preserve old ADRs. When a decision changes, create a successor and cross-link the superseded record rather than rewriting history. Do not make general database/framework claims from sample ADRs; evaluate the actual workload and constraints.

## README / onboarding

Purpose and maturity; prerequisites and versions from configuration; minimal verified setup/run commands; configuration names/defaults with secret placeholders; test/build commands; architecture/docs links; troubleshooting; contribution/license information only where applicable and verified. Do not assume npm, a particular OS, an MIT project license or a five-minute setup.

## API reference

Document observed/intended contract with discrepancies explicit: operation, authentication/authorization, parameters/types/units/defaults, body, response/status codes, errors, pagination, idempotency and compatibility where relevant. Use actual schema and implementation; examples need realistic sanitized data. Generated docs have a source of truth: update source inputs rather than editing generated outputs by default.

## Architecture and release notes

State current versus proposed architecture, scope and boundaries; diagrams need titles, element roles, labeled relationships and a legend when useful. Include only views answering the reader's question. Significant decisions link to ADRs.

Separate unreleased work from released changes. Derive release/version/date claims from evidence. Describe user impact, breaking changes and migration requirements. Avoid copying every commit into a changelog.

Match reader purpose: learning tutorial, task how-to, factual reference or conceptual explanation. A navigable source map helps future sessions, but is not a guarantee of persistent memory or automatic token reduction.
