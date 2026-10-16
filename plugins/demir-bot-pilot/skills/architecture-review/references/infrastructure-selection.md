# Workload-specific infrastructure selection

Use for a concrete project bottleneck or an explicitly requested infrastructure decision. Resolve the actual workload, consistency/latency/availability needs, current schema/API consumers, operational owner, environment and cost envelope from evidence. Compare the existing service and a simpler configuration first. A database/product list is not permission to provision systems or copy data.

| Candidate | Concrete reason to consider it | Contracts that need explicit ownership |
| --- | --- | --- |
| Redis/cache/coordination | A measured/requested cache, short-lived state or coordination need | Authoritative source, TTL/invalidation, eviction, durable fallback, atomicity, retries and failure behavior. A cache is not automatically a durable database or permission store. |
| MySQL/relational alternatives | Actual transactional/schema/compatibility requirement | Transaction/isolation behavior, indexes/query consumers, migrations, backup/restore and driver/runtime compatibility; reuse existing database handoff guidance. |
| ClickHouse/analytical stores | Actual analytical workload/data shape and ingestion/query needs | Ingest/idempotency, ordering/updates/deletion semantics, retention, schema evolution and result freshness; no assumption of relational transactional parity. |
| Kubernetes/orchestration | A justified deployment/operations need beyond current hosting | Workload/namespace identities, least-privilege access, configuration/secrets, resource/cost bounds, health signals, rollout/rollback and on-call ownership. |
| Hosting/environment tooling | A named application/runtime and actual unsupported requirement | Build versus runtime configuration, region/data destination, secrets, network/access, deploy identity, logs, backup and shutdown/rollback. |

Use official documentation for the actual product/version and preserve provider-specific semantics. Record a source-backed keep/adapt/add decision, real dependencies and what would change it; do not claim performance or availability from vendor promises. Benchmarking, load generation, credentials, data migration, cloud provisioning and spend remain separately authorized. A setup request must identify the actual project/account/region and allowed operations before writes.

For implementation in a selected project, use the existing backend/data/release owners for request/error contracts, secret handling, migration and recovery. A timeout may leave an operation uncertain; reconcile rather than blindly retrying destructive or chargeable actions. Do not import a second deployment framework by default or assume backup existence means recoverability.

Expected example, not an executed migration: a named repeated-read bottleneck may justify a bounded cache with an explicit invalidation source and uncached fallback; losing Redis does not lose the authoritative record. No-action case: a Markdown-only skill update does not provision a cluster or add a database. Current item has no selected workload/account target; reusable decision and delivery guidance is saved, actual infrastructure remains pending that evidence and authority.
