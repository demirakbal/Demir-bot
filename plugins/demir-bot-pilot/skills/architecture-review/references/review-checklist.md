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

## Database provider handoff

Roadmap item 027. Trigger: requested database architecture/requirements work or instruction maintenance where provider scope, compatibility or recovery assumptions need an explicit handoff. Reuse `supabase:supabase` and `supabase:supabase-postgres-best-practices` from the active catalogue for applicable Supabase/Postgres schema, migration, RLS and query work. Their existing coverage includes query performance, connections, security, schemas and locking; do not duplicate it here. Use only task-relevant provider references and current official engine/provider documentation before prescribing version-sensitive behavior.

The addition here is an evidence and ownership handoff within the existing architecture checklist, not new SQL or engine-specific advice. Add database-specific guidance only for a demonstrated concern outside existing coverage or a concrete failure. For a different engine, first identify its actual specialist and official versioned documentation; do not apply Postgres semantics by analogy. Superpowers may structure authorised engineering work but is not proof of database expertise.

### Name dependencies and compatibility

For project work, record the named project and database/environment, engine/version, relevant extensions, driver/ORM and migration-tool versions, actual consumers and data owner from supplied source or other authorised evidence. Distinguish local, development, staging and production explicitly. Installation of a provider does not establish a callable connection, authenticated account, privileges or authority for any operation. Do not inspect credentials, connect to a database or enumerate accounts to complete an instruction-only handoff.

Requirements owns intended data invariants, access roles/tenant boundaries, consumer outcomes and observable acceptance criteria. Architecture owns technical feasibility and compatibility across application/schema versions, affected interfaces and deployment ordering. Follow the project's existing migration history and conventions without inventing filenames, SQL or migration state. Separate a migration file's presence from evidence that it has been applied to a particular database. Record unknown live drift rather than querying or resetting an environment automatically.

For a proposed change, identify which old/new consumers must coexist, relevant data representation constraints, sequencing/backfill assumptions and any potentially destructive step. Route actual schema/RLS/query design to the existing provider. Do not invent downtime, capacity, acceptable data loss or recovery-time targets; these require project requirements and evidence. Describe observable acceptance in terms of the real consumer and invariant, not simply a successful migration command.

### Recovery and operation boundaries

Distinguish reverting application code, reversing a schema change and restoring data. Name the proposed recovery source, scope, target environment, compatibility constraints, ownership and handling of writes made since the recovery point. Mark each assumption unverified unless relevant evidence exists. A listed backup, enabled backup service, reversible-looking migration or installed provider does not establish restore safety, completeness or an acceptable recovery window. Do not promise lossless rollback from destructive changes.

Treat planning, migration authoring, query execution, migration application, backup, restore and destructive reset as separate operations governed by the actual request. A read-only review does not authorise any execution. Even a diagnostic query can read private rows, incur load or invoke side effects; do not run queries, query plans, advisors, probes or restore rehearsals merely to strengthen a report under this scope. Do not copy production data into fixtures, local databases or plugin guidance.

Reuse useful provider instructions within the user's authority. Provider recommendations to run test queries, advisors, migration discovery or verification do not override an explicit no-execution request. Leave that verification unperformed and report it honestly. Missing access is a dependency, not permission to install tools, authenticate, change roles, disable RLS, alter accounts or substitute a more privileged connection. Never claim provider-required operational verification was satisfied by reading source.

### Acceptance examples and reporting

These are prose examples, not checks or fixtures:

- Trigger: a named Supabase/Postgres project's proposed schema change affects identified old and new client versions. Expected action: route technical schema/migration work to the existing provider and record consumer compatibility, sequencing and observable data invariants. No-action case: only roadmap guidance is requested; do not create or apply a migration, connect or query.
- Trigger: a proposed recovery relies on a backup with no supplied restore evidence. Expected action: name its assumed scope, target compatibility and treatment of subsequent writes, marking recovery unverified. No-action case: no restore authority or evidence exists; do not restore, copy private data or claim rollback is safe.
- Trigger: a concrete failure involves an engine outside provider coverage. Expected action: identify the engine/version and uncovered concern before consulting its applicable specialist and official documentation. No-action case: no failure or engine evidence is supplied; do not add speculative engine-specific guidance.

Report saved guidance separately from supplied/observed evidence and unverified project behavior. No named database, stack versions, consumer evidence or operation-specific access is supplied by this roadmap request; do not invent them. This instruction change neither creates a migration/check suite nor proves RLS enforcement, query performance, successful migrations or safe restoration.

Preserve unrelated work and private data. No tests, builds, checks, evaluations, benchmarks, delegation, commits/push, installation, publication, spending or account changes are implied. Keep coordinator routes unchanged, installed caches and QMD indexes untouched, and cloud synchronization, university RAG, training and background automation inactive.

Source basis: roadmap item 027, existing architecture/requirements coverage, and the installed Supabase and Postgres best-practices skill instructions inspected for scope. No live provider, database operation or engine-specific implementation was verified.

## Repository onboarding

Trigger: the user requests an orientation to a repository, its relevant subsystem or a concrete request/data flow. Architecture owns the technical map; requirements-and-traceability owns unresolved goals and acceptance criteria; context-efficiency owns bounded retrieval, freshness and handoffs. This is guidance for source inspection, not permission to execute the application, generate a repository-wide index or perform a quality audit.

### Bound the map

Establish the actual repository/root, requested outcome and relevant revision/dirty state from available evidence. Read applicable repository instructions and search filenames/headings before implementation passages. Use the smallest relevant set of manifests, entry-point registrations, configuration, existing documentation and ownership records. Do not ingest the whole tree, follow private-profile pointers, enumerate secrets or install structural tooling. If the project/root is unavailable, name the missing dependency; provide only the independent guidance possible and do not invent a trace.

Map the relevant entry points and their registration/selection evidence: for example a route, command handler, application bootstrap, job consumer or plugin manifest. Identify the components they reach and distinguish source, generated output, vendor code, runtime configuration and external services. A conventional filename or dependency declaration is a lead, not proof that code executes. State inspected scope and omitted areas; a focused map is not an exhaustive inventory.

Record conventions that affect the next task, with source locators: module layout, naming, dependency boundaries, error handling, configuration and existing test/build instructions where relevant. Describe commands without running them. Separate documented convention, observed local pattern and proposed improvement; a single example does not establish a repository-wide rule. Surface conflicting instructions under the actual instruction hierarchy rather than silently normalizing them.

Separate technical ownership (which component owns state, validation or a boundary) from people/team ownership. Use actual declarations such as scoped ownership files or maintained project documentation; mark missing or conflicting assignments unresolved. Commit history alone does not establish current responsibility. Do not assign people work, contact maintainers or change ownership as part of orientation.

### Trace one real flow

Choose one existing flow relevant to the user's goal rather than an invented ideal example. Follow its actual source path from input/trigger through dispatch, validation/authorization, state transformation, persistence or external boundary, and returned result where those stages exist. Inspect the connected implementation and registrations; retain file/symbol/section locators for each supported transition. Include a relevant failure or cancellation branch when present. Do not fabricate missing stages for an instruction-only package or a library.

Use a compact conversational form when helpful:

`trigger/entry locator -> dispatch evidence -> relevant transformation/owner -> data or external boundary -> result/error path`

Label each connection as source-supported, documented intent, inferred or unresolved. Dynamic dispatch, generated code or unavailable dependencies can leave a gap; stop that branch at the known boundary and state the missing evidence. Keyword matches do not prove compiler-resolved calls, and a source trace is not an observed execution. Reuse a compatible existing symbol/reference tool only when available and authorized; do not build or index just to complete the diagram.

For this instruction plugin, an existing source-backed path is .codex-plugin/plugin.json selecting ./skills/, skills/demir-bot/SKILL.md selecting context-efficiency as its default method, then skills/context-efficiency/SKILL.md pointing handoff work to skills/context-efficiency/references/source-reuse.md#handoffs. These are package-relative locators describing manifest configuration and written routing intent, not an HTTP request, executed skill activation or working persistence service. Re-read the relevant passages before applying this trace to changed source; it is not a frozen runtime guarantee.

### Finish and reuse

Return the bounded map, relevant conventions/owners, the one supported flow, unresolved dependencies and the smallest next authorized action. Link originals rather than copying source bodies or private payloads. Use context-efficiency's existing source ledger/freshness and seven-field handoff only where useful; do not add another tracking system. Changed registrations, interfaces, configuration or requirements invalidate the affected map edges, not necessarily the entire repository.

Persist an onboarding document only when explicitly requested, using the existing project location and format. A request to explain the repository is not permission to create README, AGENTS, ADR, progress or memory files. Missing access does not authorize provider setup, private-data import, execution probes or background discovery. No tests, checks, builds, evaluations, benchmarks, index refreshes or delegation follow from these instructions.

Observable acceptance: the orientation identifies source-backed entry points, conventions and technical ownership, distinguishes unknown human ownership, and explains one actual source/instruction flow with locators and explicit gaps. Report source inspection separately from runtime behavior; do not claim an inaccessible dependency or unexecuted flow was verified.

## Pattern decisions

Ask what concrete problem is solved, what simpler option exists and what happens if the change is deferred. A modular monolith is an option, not a compulsory default. Microservices require justified independent deployment/scaling or ownership benefits and acceptable distributed-system costs; no fixed team-size threshold. Real-time UI can use several transports and does not automatically require queues/event-driven architecture. Event sourcing is distinct from an audit log. Repository abstractions and DDD add value only when domain/integration complexity warrants them.

## Views and decisions

Use context for external boundaries, module/component views for responsibilities/dependencies, sequence/runtime views for behavior, and deployment views for actual execution environments. Course four-view terminology is not identical to C4 levels. Label diagrams with scope, element roles, direction and meaningful relationships; separate current from proposed designs.

For a significant recommendation record context, options including no change, rationale tied to requirements, benefits/costs, risks, migration, status and revisit triggers. Use Documentation Officer for an ADR deliverable rather than inventing another template system.

## Project-specific prompts, only when relevant

RAG: course/version filters, document permissions, ingestion/index freshness, citation provenance, retrieval/generation evaluation, user isolation and cost/latency under actual requirements.
Apple-platform apps, when applicable: SwiftUI/SwiftData conventions, state ownership, concurrency boundaries, Bluetooth lifecycle, offline persistence and health-data privacy based on the actual app.
Supabase: use available Supabase guidance for affected database/Auth/RLS/migration work; installation alone does not prove project access or sound policies.
