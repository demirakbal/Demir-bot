# CloudKit sync

Original roadmap item 013 guidance. Use for requested CloudKit design or a supplied sync problem. Reuse [architecture guidance](../../architecture-review/references/ios-architecture-patterns.md) for ownership, [SwiftData migrations](swiftdata-migrations.md) for schema history/recovery, [error handling](ios-error-handling.md) for uncertain outcomes and [privacy-review](../../privacy-review/SKILL.md) for sharing and retention. This concerns an app's CloudKit design; it does not resume Demir Bot cloud skill synchronisation or any deferred service.

## Establish the mechanism and scope

Inspect only supplied source, relevant model/configuration declarations, entitlements and redacted diagnostics. Identify deployment/toolchain evidence, intended container/environment, database scope (private, shared or public), participating targets and data ownership. Keep identifiers redacted where unnecessary. Declarations are not proof of authenticated access, effective provisioning, deployed schema or successful sync. Missing project or access evidence stays explicit; do not query accounts, consoles or records to fill it in.

Determine whether the app uses SwiftData automatic sync, Core Data mirroring, CKSyncEngine or direct CloudKit operations. Preserve that choice unless a change is requested and justified. Do not graft a second sync engine onto framework-managed records or assume the same conflict/retry hooks exist in every mechanism. Consult current official documentation for actual target availability and behavior before prescribing APIs.

## Ownership and account boundaries

Trace one relevant edit from its local owner through persistence, pending transmission, server handling and incoming updates. State which component owns the local durable data, pending changes, sync metadata and user-visible status. Assign stable identity and define the handling of edits, deletions and relationships across devices. Remote and local copies do not imply that one can always overwrite the other safely.

Define the intended account and sharing boundary separately from in-memory service lifetime. Private/shared/public scope and participant permissions need explicit project evidence; a record identifier does not grant access. Describe what happens to unsent edits and visible local data when an account becomes unavailable or changes. Never upload one account's pending data into another account, erase unsent changes automatically or treat an account transition as permission to delete local records.

For app-managed sync, identify how its supported state/metadata survives interruption without reusing it across unrelated containers, accounts or environments. For framework-managed sync, preserve framework ownership rather than inventing a parallel queue or resetting internal metadata. These are design questions, not authorisation to inspect or change existing stores.

## Offline behavior and truthful status

Distinguish saved locally, pending sync, failed transmission and remotely confirmed results only to the extent the chosen framework exposes evidence. Do not label a local save as synced everywhere or promise immediate cross-device delivery. Describe useful offline reads/edits, unavailable remote-only data, stale views and how reconnecting reconciles outstanding work.

Use the existing error guidance for bounded recovery, cancellation and unknown mutation completion. Inspect partial failures per affected operation/item where supported; do not resend successful writes indiscriminately. Respect provider throttling and the selected engine's own retry responsibilities rather than adding nested retry loops. Apple documents that [CKSyncEngine](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5) handles some transient retries while leaving application-specific errors and account-change handling to the app.

Notifications and scheduling are signals, not guarantees of timely delivery. Describe interruption, replay, duplicate delivery and stale-result behavior without enabling background tasks. Do not start sync merely to investigate why an offline state persists.

## Conflict and deletion policy

Choose resolution from the meaning of the data. Identify which fields can merge independently and which changes require an explicit user decision. Specify concurrent edit/edit and edit/delete outcomes; avoid blindly resurrecting deleted records, discarding drafts or selecting last-write-wins without explaining lost updates and ordering assumptions.

For direct CloudKit conflict handling, Apple's [serverRecordChanged documentation](https://developer.apple.com/documentation/cloudkit/ckerror/serverrecordchanged) describes server, client and ancestor records and merging into the server record with its current change tag. Use available values under the actual operation contract, preserve unrelated changes and bound any retry. Do not bypass conflict detection by changing save policy merely to silence the error.

For Core Data/SwiftData mirroring, inspect the framework's supported merge behavior and the application's invariants. Do not assume direct CKRecord callbacks are exposed by the persistence framework or manually rewrite its cloud records. Distinguish local context merge policy from an end-to-end business conflict policy. Where existing automatic behavior cannot satisfy a requirement, report that limitation before proposing a different architecture.

## Schema compatibility and environments

Review the local schema separately from the CloudKit schema and intended environment. Apple's [SwiftData sync guidance](https://developer.apple.com/documentation/swiftdata/syncing-model-data-across-a-persons-devices) describes compatibility restrictions, including unsupported unique constraints and required relationships. Check the actual target's documented rules instead of assuming every valid local model can sync. Preserve relationship meaning when adapting optionality; do not drop invariants merely to satisfy storage declarations.

Explicitly identify development versus production configuration from existing evidence. A working development setup does not prove the production schema is deployed. Apple's [deployment guidance](https://developer.apple.com/documentation/cloudkit/deploying-an-icloud-container-s-schema) describes additive development-schema changes merging into production. Treat production schema evolution as a compatibility commitment; plan for older clients and supported upgrade paths rather than assuming fields/types can be freely removed or redefined.

Keep local migrations, cloud schema deployment and data transfer separate. Do not imply that promoting a schema migrates all local stores or copies development records. Identify any required deployment/index/permission work as a pending operation; never initialise, reset or deploy a container while writing guidance. Existing entitlements can influence automatic configuration, so do not construct a container or launch an app/preview as a supposedly read-only probe.

## Recovery and acceptance

Reuse the persistence recovery assumptions: sync is not an independently verified rollback snapshot. Local restoration can interact with later remote edits/deletions; do not promise that restoring a file reverses cloud state. Preserve existing stores and pending changes when a zone, account or schema becomes unavailable. Do not delete and recreate containers, zones or local stores as a routine repair.

Illustrative acceptance examples, not executable checks:

- **Offline edit:** supplied source reports Synced immediately after local save. **Expected action:** distinguish local durability from available remote evidence and define honest pending/failure states; do not send data to observe completion.
- **Conflict:** two devices edit the same logical record. **Expected action:** identify the actual sync mechanism, define merge or user-resolution semantics and account for deletion/replay; do not assume one universal CloudKit merge hook.
- **Environment gap:** a feature exists only in the supplied development schema evidence. **Expected action:** state that production readiness is unverified and identify pending deployment requirements without opening the console or changing the container.
- **No-action case:** a local-only feature has no sync requirement. Preserve its configuration; do not add entitlements, background modes or cloud services.

Source basis: official Apple resources linked above, consulted 27 September 2026. This is original guidance, not an executed account, schema or sync assessment. For app-specific work, require the named project, settings, relevant schema/configuration and supplied evidence; do not invent access.

Report saved guidance separately from observed source and unverified runtime behavior. No account access, container changes, sync activation, real database opening/copying/mutation, migrations, checks/fixtures, tests, builds, evaluations, benchmarks, delegation, commits, package operations, installations, index refreshes, cache deletion or background activity follow from this reference. Leave private data, the installed plugin, cloud skill sync, university RAG and training unchanged.
