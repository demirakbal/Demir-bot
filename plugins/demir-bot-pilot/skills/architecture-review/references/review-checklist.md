# Architecture review checks

Select applicable dimensions; record unassessed areas instead of implying comprehensive assurance.

| Dimension | Questions and evidence |
|---|---|
| Responsibilities | Are modules cohesive with explicit contracts? Does a change require touching unrelated concerns? Look at actual call sites and data ownership, not folder names alone. |
| Dependencies | Identify concrete imports/calls, cycles, shared mutable state and boundary leaks. Distinguish source dependencies from runtime and deployment dependencies. Cycles need diagnosis, not automatic merging or splitting. |
| Domain and interfaces | Are invariants, identity, validation, errors and compatibility clear? Avoid inheritance solely for reuse and unnecessary interfaces. Data access in a controller is contextual, not automatically a defect. |
| Data and transactions | Who owns records and migrations? Check atomicity, consistency, ordering, duplicates, retry/idempotency, concurrency, caching and cross-service failure boundaries. |
| Security/privacy | Trace trust boundaries, server authorization, tenant/course isolation, secrets, sensitive logs and data retention. UI hiding is not authorization; a diagram does not enforce controls. |
| Reliability | Analyze timeouts, retries, cancellation, backpressure, degraded modes, resource cleanup and recovery. Retry can duplicate side effects. |
| Performance/scalability | Look for measured bottlenecks, N+1 queries, unbounded data/work, memory and contention. State representative workload and assumptions; no fabricated capacity claims. |
| Operability | Observe configuration, deployment topology, logs/metrics, migrations, rollback, restore and ownership. Do not prescribe new infrastructure without need. |
| Testability | Are pure logic and external boundaries accessible to meaningful tests? Mocks do not prove real integrations; test tooling alone does not justify exposing private APIs. |
| Evolution | Consider migration sequencing, old/new compatibility, rollback and complexity cost. Prefer reversible incremental improvements when they meet requirements. |

## Pattern decisions

Ask what concrete problem is solved, what simpler option exists and what happens if the change is deferred. A modular monolith is an option, not a compulsory default. Microservices require justified independent deployment/scaling or ownership benefits and acceptable distributed-system costs; no fixed team-size threshold. Real-time UI can use several transports and does not automatically require queues/event-driven architecture. Event sourcing is distinct from an audit log. Repository abstractions and DDD add value only when domain/integration complexity warrants them.

## Views and decisions

Use context for external boundaries, module/component views for responsibilities/dependencies, sequence/runtime views for behavior, and deployment views for actual execution environments. Course four-view terminology is not identical to C4 levels. Label diagrams with scope, element roles, direction and meaningful relationships; separate current from proposed designs.

For a significant recommendation record context, options including no change, rationale tied to requirements, benefits/costs, risks, migration, status and revisit triggers. Use Documentation Officer for an ADR deliverable rather than inventing another template system.

## Project-specific prompts, only when relevant

RAG: course/version filters, document permissions, ingestion/index freshness, citation provenance, retrieval/generation evaluation, user isolation and cost/latency under actual requirements.
Apple-platform apps, when applicable: SwiftUI/SwiftData conventions, state ownership, concurrency boundaries, Bluetooth lifecycle, offline persistence and health-data privacy based on the actual app.
Supabase: use available Supabase guidance for affected database/Auth/RLS/migration work; installation alone does not prove project access or sound policies.
