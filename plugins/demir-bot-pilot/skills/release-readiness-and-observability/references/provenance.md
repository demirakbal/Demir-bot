# Adaptation provenance

Adapted 2026-09-21 from retained ECC instructions previously discovered with Firecrawl and inspected in full for this task. Reviewed hashes identify the actual source text; no claim of current upstream freshness. No upstream scripts, configuration examples or dependencies imported.

## production-audit
- Source: https://github.com/affaan-m/ECC/blob/main/skills/production-audit/SKILL.md
- Reviewed SHA-256: 3ab3dd8a364ee17566e9361f0ebed2aec3b3146ede44e1db0a72c5ceae1ca0a4

## deployment-patterns
- Source: https://github.com/affaan-m/ECC/blob/main/skills/deployment-patterns/SKILL.md
- Reviewed SHA-256: b864abd1954570c4a469b7e1deb897e57858d25db2fd98d035ff7bca4a15b9b6

Borrowed: local-evidence review, actual production boundaries, configuration validation, deployment alternatives, migration compatibility, health signals and rollback/recovery planning.
Adapted: independent evidence states and operation-specific claims; project-specific observability, privacy-aware logs and actionable alerts; application rollback separated from data restore and migration bookkeeping.
Removed: numerical readiness scores/caps, automatic post-merge review, automatic browser/HTTP checks, blanket testing/security scans, CI auto-deploy templates, pinned example versions as recommendations, fabricated health latency and unconditional instant-rollback claims.
Preserved: opt-in tests/builds/runs, explicit action scope, no unsolicited reports, no third-party uploads or recurring monitoring, deferred cloud synchronization.
Maintenance: compare relevant upstream changes with these reviewed fingerprints and preserve local adaptations; consult current official provider docs for commands only when the actual task needs them.
