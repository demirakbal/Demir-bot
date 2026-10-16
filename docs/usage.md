# Everyday use

Ask for the outcome in ordinary language. Give the actual source or project and any important limits; Demir Bot should select the smallest relevant existing skill/tool. You do not need to name every specialist. A clear request should lead to work, with questions only where a missing decision materially changes it. Use the [installation guide](installation.md) if the plugin is absent from the current task.

| You want | Example request | Expected boundary |
|---|---|---|
| Explain code | “Explain this function from its actual source, one call at a time. Don't edit.” | Source-grounded teaching, no refactor or run. |
| Change code | “Fix the stated behavior in this checkout. Preserve the existing architecture.” | Scoped source change and limitations; no automatic tests/builds/commit. |
| University work | “Use these assignment files to implement part 2; keep lecturer text and starter behavior.” | Use actual criteria and selected part; distinguish supplied versus new work. |
| Research | “Compare these sources for this question and explain the strongest counterevidence.” | Read supporting passages, cite claims, state access/coverage limits; no experiment or build. |
| Writing | “Revise this draft using only supplied facts. Return the draft; don't send.” | Relevant channel tone and approved facts, no account operation. |
| Project update | “Update this roadmap item and report what changed.” | Canonical Markdown/source record, no inferred completion or PDF/site publication. |
| Multi-item chain | “Do these selected items; after each, tell me elapsed time and changes, then continue.” | Continue independent authorized work; report precise blockers and unverified outcomes. |

The examples describe intended behavior, not recorded runtime results. A supplied file path must be accessible in the current environment; local Mac files are not automatically visible to a browser/cloud client. If a file/tool is unavailable, name the missing dependency and finish independent work without inventing its contents or claiming a mode switch.

## Tests and other operations

Be explicit about separate scopes: “write checks only,” “run these existing checks,” or “run these checks and fix relevant failures.” Writing never implies running, and a run request does not imply a repair loop. Builds, previews, device launches, benchmarks and model evaluations likewise need their actual scope. See the QA gate guidance for evidence limits; unrun work stays unverified.

For a real account operation, identify the service, account/resource, exact effect/content/destination and relevant audience or schedule. Installed tools do not guarantee authentication or permission. Drafting a message is separate from sending; queued/accepted is separate from completed delivery. Reuse applicable existing approval without repeated questions for the identical action, and reconcile uncertain outcomes before retrying. Do not put secrets into a chat prompt or committed source.

## Preferences, corrections and stopping

A one-time correction changes the current response. Ask explicitly to save a reusable preference when persistence is intended; the existing private owner keeps approved scope and facts outside the package. Ask to inspect, revise, forget or roll back the specific rule without resetting unrelated data. Missing profiles use supplied facts and provisional tone.

You can narrow, pause or stop a chain at any time. A blocked item should not stop independent assigned work, but an inactive session cannot keep working by instruction alone. No timers, recurring jobs, autonomous learning, cloud sync, RAG or training are started by ordinary requests. Source changes, installed updates, QMD indexing and public releases remain separate. See [update/recovery](update-and-recovery.md) for those lifecycle boundaries.
