---
name: privacy-review
description: Review personal-data handling in a requested feature, assistant workflow, integration or data flow. Use for privacy reviews and concrete decisions about collection, tool sharing, telemetry, retention, deletion, consent or reuse of personal information. Route vulnerability audits to existing Codex Security skills. Skip unrelated work and automatic audits after routine coding tasks.
---

Plugin pilot routing: select bundled siblings as `demir-bot-pilot:<skill-name>` from the active catalogue. Resolve file references relative to this skill directory; paths beginning with a bundled skill name are relative to the parent `skills/` directory. External provider skills remain optional and retain their own names. Do not fall back to a duplicate standalone copy silently.


# Privacy Review

Add the privacy questions not covered by a vulnerability scan. A system may prevent unauthorized access yet still collect, share or keep more personal data than its purpose requires. Work within the requested scope; do not turn every mention of a person into a privacy audit.

## Choose the right workflow

- For a repository vulnerability audit, use the available `codex-security:security-scan`; for a PR or patch use `codex-security:security-diff-scan`. Use their own instructions and actual prerequisites. Do not recreate their scanning, threat-modeling, severity or finding-validation pipelines here.
- For an existing finding, choose Codex Security triage, fix or verification only when that specific action is requested. An ordinary code fix does not authorize tests. If a specialist workflow requires unrequested execution or reports, provide a bounded source review or implementation within scope and explain the coverage limit; never silently claim the full scan completed.
- For privacy-only reviews, stay here. For combined reviews, reuse the existing security evidence and add only privacy gaps. An overlapping leak or access-control finding gets one explanation with both impacts, not duplicate findings.
- Connector permission inspection belongs to the available Plugin Management tools. A plugin being installed does not establish its account access, retention policy or allowed recipients.

## Inspect only the relevant data flow

1. Reuse the stated purpose, affected feature, known users and existing evidence. Ask only if missing information materially changes the decision: whose data, why it is needed, where it goes, or which jurisdiction applies to a legal question. Do not request raw personal records to clarify a schema.
2. Trace representative fields through collection, processing, recipients, storage and deletion using relevant code, settings or supplied documents. Include identifiers and combinations that can identify a person, free text, attachments and metadata when present. Use field names and synthetic examples; never echo credentials, private messages or complete personal records into findings.
3. Examine only applicable gaps:
   - **Collection and purpose:** Is each field needed for the requested feature? Can fewer fields, lower precision, aggregation or on-device processing achieve it? Note optional fields, defaults and unrelated reuse.
   - **Sharing and assistant tools:** Identify the actual destination and fields sent, including prompts, external model providers, plugins, exports, links and analytics. Inspect scope and onward sharing from evidence; do not upload private content to research or scanning services just to investigate it. Reading a document is not permission to publish its contents or send it to another provider.
   - **Logs and derived copies:** Look for personal content in logs, errors, URLs, telemetry, caches, exports, backups, embeddings and search indexes. Prefer redaction before emission and bounded access. Masking, encryption and pseudonymization do not by themselves establish anonymity; assess linkability and retained lookup information.
   - **Retention and deletion:** Identify the real purpose, retention trigger, deletion path and downstream copies. Do not invent a universal retention duration. Distinguish requested deletion, queued processing, backup expiry and confirmed deletion; account for documented holds or obligations without guessing them.
   - **People's controls:** Where relevant, inspect understandable notices, meaningful choices, withdrawal, correction, access and export. Do not assume consent is the only legal basis or that a generic cookie banner solves every privacy issue. Verify requester authority before exposing another person's records.
4. Separate observed behavior, plausible risks and unknowns. Describe the affected people, concrete consequence, evidence location, smallest relevant change and what remains unverified. Missing evidence is not proof a control is absent. Avoid arbitrary privacy scores and legal-compliance badges.
5. For a review, return findings and next actions in the conversation. Implement fixes only when requested or already authorized. If changing data flows, preserve the user's functional requirements and identify any meaningful utility trade-off before making it.

## Boundaries

Respect Demir's implementation-first preference: no unsolicited tests, scanners, browser checks, benchmarks, new reports, policy documents or security cleanup. Creating this skill does not authorize auditing an actual project. No new dependencies, accounts or background services are required by this workflow.

Do not delete records, revoke credentials, change account permissions, notify affected people or publish findings merely because a privacy risk was found. Follow existing task authorization and applicable tool requirements; do not invent an extra approval step for already-authorized routine work. Address concrete risk, not hypothetical warnings on every task.

For legal applicability, mandatory retention, breach deadlines or rights obligations, establish the jurisdiction and processing context, then verify current primary legal or regulator sources. Distinguish technical advice from unresolved legal questions; never certify compliance from a checklist. General privacy engineering can proceed without a legal-research detour when no legal conclusion is needed.

Use Demir Bot's visual feedback format when coordinating through it, preserving required work versus optional improvements and honest verification status. Read [sources-and-coverage.md](references/sources-and-coverage.md) only for the assessed overlap and adaptation rationale.
