---
name: agent-configuration-review
description: Review a requested agent, skill, hook or MCP configuration for permission, secret-handling, trust-boundary and supply-chain risks using scoped evidence. Use for explicit assistant-environment reviews; not automatic scans or application vulnerability audits.
---

Plugin pilot routing: select bundled siblings as `demir-bot-pilot:<skill-name>` from the active catalogue. Resolve file references relative to this skill directory; paths beginning with a bundled skill name are relative to the parent `skills/` directory. External provider skills remain optional and retain their own names. Do not fall back to a duplicate standalone copy silently.


# Agent configuration review

Reuse Demir Bot's capability register and inspect only the authorized configuration surface. Identify the actual host, active configuration and scope; distinguish runtime settings from templates, plugin caches and example files. A saved instruction is not proof of runtime enforcement or authentication.

Read relevant tool permissions, sandbox/approval settings, hook entrypoints and MCP transport/dependency configuration. Assess consequential write/network access, trust boundaries between retrieved data and instructions, credential handling, package pinning/update paths, automatic script execution and unexpected persistence. Never print secret values or invoke credential helpers just to inspect them. Read limited needed fields; no sweeping home-directory, keychain or account scan.

Describe each finding with location, observed behavior/configuration, plausible effect, confidence and smallest relevant mitigation. A powerful tool or remote endpoint is not inherently malicious; assess authorization and controls. Missing hooks, absent deny lists or an unavailable scanner do not alone prove insecurity. Preserve applicable host-enforced restrictions; no bypasses or weakening safeguards for convenience.

AgentShield is an optional scanner, not required. A pinned local installation is recorded in references/local-scanner.md; read it before use. Before any requested install/run, inspect its current supported adapter, version, dependencies, data destinations and command scope using official source. No unpinned npx execution, --fix, external model analysis, paid calls, CI installation or generated reports by default. Scan output is evidence to triage, not a security certification or trustworthy numeric score. This instruction workflow can complete a source review without installing AgentShield.

Route actual application vulnerability reviews to Codex Security and data-handling questions to privacy-review only when relevant. Do not duplicate findings or launch those workflows automatically. Review is read-only; implement only requested fixes. Do not run scanners/tests, modify permissions, rotate credentials, contact providers or install monitors merely to obtain verification. State what remains unexamined and whether runtime enforcement was tested. Follow deferred cloud sync. Read references/provenance.md for reviewed source and limitations.
