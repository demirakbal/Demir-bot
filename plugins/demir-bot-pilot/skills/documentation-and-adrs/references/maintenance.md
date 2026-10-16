# Scoped documentation maintenance

Use when an authorized source change affects a documented contract, setup step, ownership boundary, inventory or evidence claim. Identify the canonical owner and update the smallest affected passage. Link shared guidance instead of copying rules across the coordinator, specialist and README. Preserve historical records, labeling their artifact/date rather than silently treating them as current.

For Demir Bot, the Markdown roadmap owns scope and per-item state, RESOURCES.md owns navigable resource inventory, README.md owns first-use/support status, specialist references own procedures and the private profile owns machine paths/facts. Installed copies, indexes, exported PDFs and published sites are distinct versions with separate refresh authority. A source edit must not update their evidence claims as though deployment happened.

Inspect changed passages, link destinations/anchors and representative examples directly. Reconcile material counts and setup claims against actual source names; label a snapshot boundary when the batch is still evolving. Do not rerun historical tests, regenerate the PDF, build a doc site or claim current runtime proof from an old release. Keep unrelated drafts and local changes intact.

Acceptance example: a new bundled tool is linked from its owner and resource inventory, while the README says its installed copy has not yet been refreshed. No-action case: a variable rename that does not change the documented contract needs no new ADR or duplicate report. Return the concrete doc changes and material unresolved claims. Documentation consistency is source evidence, not behavioral acceptance.

## Translated documentation

Use only for a selected language and an identified source revision. The English installation, update/recovery, first-use, usage and troubleshooting owners must be stable enough for the requested translation. Ask for the actual target language rather than inferring it from a name, home directory or locale. Do not create empty language folders or claim multilingual support before translated content exists.

Keep one canonical source and an explicit source-version link for each translation. Preserve stable roadmap IDs, plugin selectors, paths, code/API identifiers, commands, evidence states and permission scope exactly where translation would change their meaning. Translate explanations naturally, including error/limitation wording; do not turn “not run” into “passed” or drafting into sending. Mark stale/unreviewed translations when the source changes rather than silently serving conflicting setup instructions. Actual linguistic review and example execution are distinct evidence.

Acceptance example: an approved target-language installation guide links its English source revision and preserves the real selector and unrun evidence limits. No-action case: maintaining one English paragraph does not translate every file or install a translation service. For the current legacy batch, the user selected English only on 16 October 2026. No translated guide is required, and no multilingual runtime claim is made. Revisit translation only if another language is later requested.
