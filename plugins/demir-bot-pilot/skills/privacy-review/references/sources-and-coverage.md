# Sources and coverage

Inspected on 2026-09-21. This is skill provenance and routing guidance, not an audit of Demir's projects or a claim of exhaustive plugin coverage.

## Existing Codex Security coverage

Read installed Codex Security 0.1.24 entrypoints for security-scan, security-diff-scan, threat-model and fix-finding, plus the sensitive-data section in references/threat-model.md. Standard and diff workflows cover source-backed vulnerability discovery and validation; the threat model includes trust boundaries, sensitive-data handling, privacy guarantees and auditability. A targeted search of the skill entrypoints and shared references did not reveal a dedicated purpose/minimization/retention/individual-control workflow. Some privacy-relevant security issues are already covered; route those to the existing specialists.

## Public skills assessed

- [Data Privacy Compliance](https://github.com/davila7/claude-code-templates/blob/main/cli-tool/components/skills/enterprise-communication/data-privacy-compliance/SKILL.md): inspected the actual instructions, including purpose limitation, minimization, retention, rights and consent. Useful conceptual coverage, but unsuitable for wholesale import: broad legal-compliance framing, fixed example retention periods and deadlines, automated-deletion examples and extra reporting would expand Demir's scope. The inspected instruction file did not require a runnable dependency install; its example application code references functions and libraries not supplied in that file.
- [Implementing Data Minimization Architecture](https://github.com/mukul975/privacy-data-protection-skills/blob/main/plugins/privacy-by-design-skills/skills/implementing-data-minimization-architecture/SKILL.md): inspected collection, processing, storage and access guidance. Useful lifecycle organization; not imported as a package. Excluded its company-specific assumptions, numerical approval scores, universal parameter examples, fixed infrastructure choices and claims about reversible HMAC pseudonyms. Its metadata declares Apache-2.0; we did not execute or install its repository scripts or dependencies.
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework): primary reference describing voluntary privacy-risk management. Use the current framework and primary sources for deeper assessment when needed; it is not a legal-compliance certificate.

The local instructions are newly worded and conceptually adapted from these inspected workflows; no upstream code, legal templates, illustrative company claims or numerical scorecards were copied. No third-party runtime package was installed. Candidate popularity was not used as evidence of quality. The specialist references available Codex Security and Plugin Management capabilities conditionally, without claiming authentication or adding hard connector dependencies.
