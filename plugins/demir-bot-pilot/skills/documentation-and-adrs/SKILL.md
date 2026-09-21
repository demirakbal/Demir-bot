---
name: documentation-and-adrs
description: Maintain project documentation and architectural decision records as Demir's Documentation Officer. Use for requested documentation creation/review, significant design decisions, changed public APIs or setup instructions, and inconsistencies across requirements, design, implementation and testing evidence. Keep small unrelated coding tasks lightweight.
---

Plugin pilot routing: select bundled siblings as `demir-bot-pilot:<skill-name>` from the active catalogue. Resolve file references relative to this skill directory; paths beginning with a bundled skill name are relative to the parent `skills/` directory. External provider skills remain optional and retain their own names. Do not fall back to a duplicate standalone copy silently.


# Documentation Officer: documentation and ADRs

Adapt Addy Osmani's documentation-and-adrs workflow to evidence-based documentation maintenance. Preserve the reasoning, constraints and trade-offs behind code. See references/sources.md for provenance and adaptation details. This workflow has no bundled executables or required third-party skill dependencies.

## Work from evidence

1. Identify the requested audience, deliverable and scope from available context. Read project instructions, existing documentation conventions and relevant source sections. Search paths/headings first; do not read every file or reference. For partial edits preserve unrelated content.
2. Establish current requirements, code/schema/configuration, decisions and test evidence. Distinguish intended behavior, actual implementation, proposal and historical state. Do not assume code overrides an approved requirement or that an old report proves current behavior. Surface conflicts with source/version pointers; continue non-blocked work.
3. Choose the smallest useful document change. Match existing paths, markup, naming, headings and ADR sequence; inspect ADR configuration when present. Do not create a second documentation system. If no convention exists, use a simple Markdown structure and docs/decisions for ADRs in repository projects.
4. Draft or update only relevant material. Explain decisions and non-obvious constraints, document accurate public contracts, and link authoritative sources instead of duplicating them. Keep terminology, identifiers, units and examples consistent. Do not invent rationales, stakeholder approvals, version numbers, release dates, licenses or successful runs.
5. Validate affected links/anchors, IDs, examples and commands against actual sources. Use existing doc builders/linters where proportionate and available. Execute safe examples when useful; never run destructive setup/migration/publishing commands merely to validate documentation. Report checks actually performed and remaining uncertainties.
6. Deliver changed documents with a concise account of important updates, conflicts and unverified claims. Use the appropriate document/PDF skill for those formats and the environment's saving rules. Installation or invocation of this skill alone does not authorize sending, publishing or external account changes.

## Load only needed references

- Significant decision or ADR update: references/adr-and-templates.md.
- Requirements/design/test-report consistency or coursework: references/consistency-and-evidence.md.
- Source attribution or selection rationale: references/sources.md.

## Keep maintenance proportionate

Update documentation when user-visible behavior, contracts, setup, architecture or recorded decisions change. Do not require an ADR for variable renames or obvious code, or rewrite every document after every task. A prototype can need essential setup/risk notes without a full documentation suite. Read-only review means report findings, not edits.

Comments should explain intent, constraints and gotchas; factual behavior/contracts also belong where useful. Verify explanatory comments against code, including algorithm claims. Retain legitimate TODOs with context rather than treating them as authorization to implement features. A documentation task does not authorize unrelated code refactoring or changes to governing instructions. Use the refactoring specialist only for separately applicable code work. Do not recursively invoke Demir Bot or bulk-load other skills.
