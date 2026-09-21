# Documentation Officer consistency checks

Use for formal project/course documents and significant cross-document changes. Keep small edits local.

## Traceability

Follow requirement/story → design/component → code/interface → test assertion → actual run evidence. Preserve stable IDs and distinguish test IDs from run IDs. Check duplicate/orphaned IDs, broken references, inconsistent terminology, missing acceptance criteria and conflicting priority/scope. One test can cover several requirements only if relevant assertions exist; a filename is not proof.

A useful optional table:

`requirement | current criterion | design/code source | test/assertion | execution evidence/status | discrepancy/next action`

Do not infer the requirement from implementation convenience. Record conflicts, their versions and impact; resolve from authoritative current evidence or ask a targeted question only when genuinely blocked. Historical changelogs can reflect legitimate evolution. Distinguish immutable identity from display numbering, missing from malformed data, per-item from batch atomicity and local from global failure.

## Evidence and status

Separate planned, not implemented, not run, blocked, passed, failed, waived and excluded. Never turn an empty acceptance form, green scanner gate, screenshot or named test into proof of execution. Record actual environment/revision/date/actor when known; otherwise mark unknown. Keep failure and retest history, and distinguish functional success from usability complaints. Do not invent client sign-off.

Reconcile totals and denominators; excluded requirements are not passes. Distinguish code coverage, requirement coverage and stakeholder acceptance. Mocked database/export boundaries do not prove real persistence or actual workbook/image contents. Compare quality scans only with compatible rules, scope, exclusions and coverage imports. Missing coverage reports differ from measured zero coverage.

## Course-derived examples

These lessons come from Demir's reviewed software-engineering documents, not universal stack or grading rules:

Detailed course examples are private. When relevant, resolve the active profile and read course-evidence/documentation-and-adrs/references/consistency-and-evidence.md. Use actual supplied source files for exact quotations or new conclusions. Retain unique IDs, reconciled scope totals, explicit mocked boundaries and honest failure/retest history; never import unsupported pass claims.
