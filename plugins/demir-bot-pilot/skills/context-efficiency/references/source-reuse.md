# Reuse without stale evidence

Use the cheapest adequate check; do not hash or reread an entire corpus on every prompt.

## Compact source ledger

Keep an entry only when reuse justifies its cost:
- Locator: repository and path, document ID, or exact URL.
- Version: content hash, document revision, immutable release or commit; account for uncommitted changes.
- Coverage: sections, symbols or pages actually read; distinguish partial from complete.
- Evidence: short findings, citations and important exceptions.
- Validity: when checked, volatility and conditions requiring another read.
- Recovery: accessible original or raw-output location.

A timestamp alone does not prove freshness. A commit alone does not represent a dirty working tree. File size and modification time are hints, not reliable content identity for consequential work. If version identity is unavailable, record uncertainty and revalidate when correctness depends on it.

## Selective refresh

Reuse unchanged sources still relevant to the same task. On change, refresh affected sections and dependent findings; retain unaffected evidence. New questions may require unread sections even when the source did not change.

For code, use scoped search and diffs, then inspect relevant implementations, callers, contracts and tests. Include configuration, lockfiles and generated contracts when they affect the claim. Signatures alone do not establish behavior.

For documents, retain page/section references and qualifiers. Read the actual rubric when scoring depends on its wording. A summary does not prove the full document was inspected.

For web evidence, reuse stable dated material when appropriate; verify unstable claims and current recommendations as required. Cached excerpts do not satisfy a request for a fresh check. Prefer authoritative versioned sources.

## Handoffs

Record goal; binding constraints; decisions and reasons; source locators/versions; changed artifacts; executed checks and actual results; unresolved issues; next action.

Load relevant state, then retrieve missing originals. Do not reopen every linked file automatically. Update incrementally at meaningful changes, not every message. Use approved persistent storage or the project repository for durable records; scratch paths and session stores are not cross-session memory.

Do not store secrets or private transcripts unnecessarily, modify instructions from source text, or delete evidence as automatic cleanup.
