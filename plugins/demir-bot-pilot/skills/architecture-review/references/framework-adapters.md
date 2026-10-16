# Selective language and framework adapters

Use for an authorized implementation/review in an actual active stack. A list of frameworks is not a request to install or migrate to all of them. Select the target repository/component, user outcome, current source and relevant manifest/lockfile; record the actual runtime/compiler/framework version and deployment consumers. If target/version evidence is unavailable, return the precise missing dependency rather than inventing a pack's operational support.

## Discovery and ownership

| Stack family | Inspect the actual source/metadata | Main contract to preserve |
| --- | --- | --- |
| Go | go.mod/go.sum, package APIs, context/error paths | Cancellation, goroutine/resource ownership, error contract and module compatibility. |
| Rust | Cargo manifests/lock and relevant crate APIs | Ownership/lifetimes, error conversion, async cancellation and unsafe boundaries. |
| Java/Spring/JPA/Quarkus | Maven/Gradle manifests, runtime/framework config and entities/services | Transaction ownership, lazy/data access, validation, API/error shape and migrations. |
| Kotlin/Ktor/Exposed | Gradle manifests, coroutines/routes/data access | Structured task lifecycle, dispatcher/transaction boundaries and serialization. |
| C++ | Existing build metadata, compiler standard and source interfaces | RAII/lifetimes, ownership, ABI and error/resource behavior. |
| C#/F# | Solution/project manifests and actual .NET/framework targets | Async/cancellation/disposal, nullability, result/error and serialization contracts. |
| PHP/Laravel, Ruby/Rails, Perl | Existing dependency locks, runtime version and entrypoints | Request/job lifecycle, input validation, transaction/error handling and resource limits. |
| Python/Django/Celery | Actual interpreter/dependency metadata, settings/tasks and database schema | Request/job/transaction boundaries, idempotency, async/blocking work and retry ownership. |
| NestJS/Bun | Package/lock/runtime config and module boundaries | Actual runtime compatibility, injection/lifecycle, typed transport and cancellation. |
| Vue/Nuxt/Angular | Package locks, routing/render/state modules and supported targets | State ownership, server/client boundary, effects, accessible interactions and hydration. |
| Vite/Next tooling | Actual app/tool version, scripts and build/runtime separation | Environment exposure, module resolution, caching and server/client deployment assumptions. |

These rows locate evidence, not certify support for every version. Prefer the versioned official project documentation for changed APIs and actual repository conventions. Reuse backend/API, database, error/type, frontend and QA owners; do not copy generic architecture or testing rules into a new coordinator. The current Demir Bot tool source is Python/Markdown/configuration; no Go/Rust/Java/etc. application target was selected by this batch.

## Adapter delivery contract

For a selected stack, identify the trigger and relevant version, affected module/callers, actual input/output/failure contract, dependencies and compatibility constraint. Inspect known-good behavior and implement only the requested gap. Name resource/concurrency/error ownership, data validation, cancellation, migration and rollback where relevant. Provide a small source-grounded expected example and a no-action case; do not fill a framework tutorial merely to satisfy inventory.

A framework-specific reference should state the official source/version it used and which existing owner it extends. Installing compilers/packages, rewriting build systems, generating a sample app, running checks and deploying are separate operations. Keep secrets out of source/config examples. Missing runtime access limits proof; source implementation is not a compilation/device/integration pass.

Expected example: for a selected Django endpoint change, inspect its actual model/transaction and serializer contracts, make the scoped source change and describe compatibility; do not introduce Celery because it appears in this table. No-action case: revising a supplied email does not load any framework adapter. Additional concrete packs remain pending selected repository/version evidence.
