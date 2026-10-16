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

## Project context, Space and Page ownership

Keep one canonical owner for each information type. Retrieve only the relevant source explicitly; a Project, conversation, Space or Page mention does not make its content accessible to every task. Review current version/access before relying on a mirror. This ownership map is a procedure, not an instruction to create projects/spaces or migrate their content.

| Area | Canonical source and retrieval | Optional reusable surface and freshness |
| --- | --- | --- |
| Demir Bot | User-selected development checkout; roadmap Markdown and source/configuration; resolve machine locators through the active private setup | A Page may summarize the roadmap with source/revision and known gaps. Update the repository owner first; never run two independent completion queues. |
| University | Actual current assignment/rubric/starter files and relevant course/project material | Project groups task context; a selected Page may hold a checklist or notes. Reconcile lecturer clarifications and current scope; preserve starter/user authorship and submission constraints. |
| Grynd or another code project | Actual repository files and accepted project decisions | A deliberately selected Page may summarize requirements/architecture; inspect implicated source before editing or asserting shipped status. |
| Career | Active private approved facts plus relevant supplied/authorized opportunity, CV and correspondence | A user-selected tracker/Page can hold agreed application state. Confirm time-sensitive role/status facts; do not copy private correspondence into shared content by implication. |
| LinkedIn | Approved private facts and linkedin-tone calibration; actual project/publication evidence | User-selected draft/content Page may hold approved material. Reconcile project changes and approvals; Page presence does not authorize publication. |
| Research | Original papers/data, dated source notes and the current research question | A Page can hold a source-linked synthesis, not replace the original paper or flatten uncertainty. Refresh affected claims when sources/versions change. |

Private preferences, facts and channel tones remain in their existing profile files; generic procedures remain in skills. Do not create a second global memory store. A Page summary records the canonical source, revision/date, coverage and outstanding differences. A cloud Page does not automatically sync to local files or grant private-profile access. Space and Project are distinct organizing surfaces; use actual supported tools and permissions rather than claiming an automatic project-to-space binding.

Before a permitted Page create/edit/share or data move, inspect destination audience and relevant existing material, resolve conflicts, and honor the user's exact action scope. Linked sources retain their access rules; copied or summarized content is exposed to the destination audience. Without authority/access, work from supplied sources and give the precise missing dependency; do not create a replacement mirror or upload private data. University RAG, account linking and cloud skill synchronization remain separately gated.

Use the same source-reuse compact handoff for continuity, carrying only relevant locators and decisions. Stale/unavailable content is a retrieval limitation, not proof that a requirement disappeared. This guidance creates no Page, Space, connector or synchronization mechanism.

## Course-derived examples

These lessons come from Demir's reviewed software-engineering documents, not universal stack or grading rules:

Detailed course examples are private. When relevant, resolve the active profile and read course-evidence/documentation-and-adrs/references/consistency-and-evidence.md. Use actual supplied source files for exact quotations or new conclusions. Retain unique IDs, reconciled scope totals, explicit mocked boundaries and honest failure/retest history; never import unsupported pass claims.
