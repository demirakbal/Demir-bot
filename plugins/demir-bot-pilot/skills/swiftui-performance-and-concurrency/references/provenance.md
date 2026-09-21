# Adaptation provenance

Adapted 2026-09-21 from the retained ECC review copy, inspected in full for this task. Previously discovered via Firecrawl. Hashes identify reviewed content; no latest-upstream claim. No upstream code examples, dependencies or scripts imported.

## swiftui-patterns
- Source: https://github.com/affaan-m/ECC/blob/main/skills/swiftui-patterns/SKILL.md
- Reviewed SHA-256: 79e3c8b5b7c38fa04778b1084cddc2f8db5f671e682b0e9c1d5bd2f95800f690

## swift-concurrency-6-2
- Source: https://github.com/affaan-m/ECC/blob/main/skills/swift-concurrency-6-2/SKILL.md
- Reviewed SHA-256: 00aed6a804ff7dc9b37d119cdb115d0869643dd84caf3c01d7f058398ab1955a

Borrowed: deliberate state ownership, localized view dependencies, stable identity, avoiding expensive body work and explicit concurrency/isolation design.
Adapted: deployment-target and per-target settings awareness; cooperative cancellation and stale-result protection; actor reentrancy and task ownership; measured performance distinguished from hypotheses.
Removed: blanket ObservableObject replacement, assumptions that Swift 6.2 universally changes default isolation, universal MainActor/@concurrent recipes, automatic migration/build/profiling/testing and unconditional rendering guarantees.
Preserved: actual project conventions, opt-in execution, no unsolicited documents, private-project disclosure restrictions, deferred cloud sync and university RAG.
Maintenance: compare relevant source changes against these fingerprints; consult official Apple/Swift documentation for version-sensitive implementation decisions.
