# Traceability and change impact

Maintain links both ways: source/goal → requirement → design/interface → implementation → verification assertion → run evidence. Define link direction explicitly: artifact implements requirement; test verifies requirement; child refines parent. Do not infer satisfaction merely from an 'implements' link.

Suggested matrix:

`requirement ID/revision | source | design/code reference | test/assertion | real/mocked boundary | evidence/run | status | gap`

Distinguish planned, not implemented, not run, blocked, passed, failed, waived and excluded; retain failed runs/retests. A test can cover multiple requirements only with corresponding assertions. Manual inspection, analysis and stakeholder validation can be valid verification methods where appropriate; do not force everything into unit tests. System validation of user needs differs from verification against specified requirements.

Check duplicate IDs, broken links, missing parents, requirements lacking implementation/verification, and artifacts with no requirement rationale. Flag exceptions contextually: infrastructure/enabling work may have a legitimate technical rationale. Do not delete an artifact merely because a link is missing.

Coverage measures must state revision, eligible scope, numerator and denominator. Separate mapped requirements, assertion coverage, executed verification and accepted outcomes. If 12 total requirements include 2 excluded, eligible count is 10; do not count exclusions as passed. Zero eligible means N/A, not 100%. Partial assertion coverage remains partial. Uploaded reports remain reported results unless verified. Mocked downloads/databases do not prove actual artifacts/persistence.

For a change record old/new criteria, reason/source, revision/status, affected dependencies, design/code, tests, docs/ADRs, migration/compatibility and unresolved decisions. Identify upstream/downstream impacts through actual links; label inferred impacts. Mark previous evidence stale when the changed criterion invalidates it; retain historical evidence. Do not automatically invalidate unrelated evidence or renumber every requirement.

Prioritize conflicts by user/operational impact. Preserve authoritative baseline and draft replacement until a relevant decision is resolved. Existing user approval can authorize routine updates; never manufacture approval records. Formal regulated traceability is beyond this lightweight workflow without applicable project controls.
