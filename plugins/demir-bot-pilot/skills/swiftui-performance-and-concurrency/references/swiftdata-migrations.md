# SwiftData migrations

Original roadmap item 011 guidance. Use for requested SwiftData schema evolution or a supplied migration failure. Reuse [iOS architecture](../../architecture-review/references/ios-architecture-patterns.md) for data ownership, [error handling](ios-error-handling.md) for truthful failure states and [privacy-review](../../privacy-review/SKILL.md) for retention and recovery copies. Core Data-to-SwiftData conversion is a separate scope; do not substitute that workflow for versioning an existing SwiftData store.

## Establish the source history

Inspect relevant model declarations, historical schema definitions, migration plan and container/configuration construction as source text. Identify named shipped schema versions, supported upgrade origins, intended destination, deployment targets and actual SDK/toolchain evidence. Use supplied synthetic data descriptions and the recovery design; do not infer historical schemas from the latest model alone or manufacture fixtures when their creation is prohibited.

Apple's [VersionedSchema](https://developer.apple.com/documentation/swiftdata/versionedschema) describes a schema version and its models. Preserve the meaning of shipped versions rather than silently editing historical definitions to match the new model. Trace attributes, relationships, optionality, uniqueness and rename intent across the actual versions; version labels alone do not prove distinct or compatible schemas.

Absent project source, schema versions, synthetic examples or recovery requirements, reusable guidance can be saved but app-specific migration choices remain unresolved. Request missing declarations or synthetic descriptions, never a production database or private records.

## Choose and connect migration stages

Use [SchemaMigrationPlan](https://developer.apple.com/documentation/swiftdata/schemamigrationplan) to describe the relevant schemas and stages, following current documentation for the project's SDK. Compare every supported origin with the destination, including users who skip releases. Do not assume an adjacent-version path automatically covers all shipped stores or invent reverse migration support.

[MigrationStage](https://developer.apple.com/documentation/swiftdata/migrationstage) provides lightweight and custom stages. Select lightweight migration only when the actual change is supported by the target platform and preserves required meaning. For a custom transformation, identify the affected data, invariants, ordering and failure behavior. Check which schema/models are available in each migration callback for the actual API; do not assume old and new model types can both be fetched in either callback.

Review these decisions only where the change requires them:

- Renames must preserve intended identity rather than accidentally removing and recreating data. Use supported schema metadata only after checking its availability and semantics.
- Required fields need a justified value for existing records. Do not invent user data or use an empty default merely to avoid a migration failure.
- New uniqueness or relationship constraints need an explicit policy for existing duplicates, missing references and conflicting values. Preserve relationships and explain any authorised loss or merge; never silently discard records.
- Transformations involving types, split/merged entities or encoded values need clear mappings and treatment of unconvertible input. Preserve stable identifiers where required by references, navigation or external systems.
- A migration must not depend incidentally on network access, live credentials or a background service. Identify external prerequisites separately rather than introducing new side effects into store opening.

Trace the selected plan to the actual container and configuration used by each relevant app/extension entry point. A declared but unused plan does not establish migration coverage. Preserve store ownership, shared-container boundaries and existing sync configuration; do not enable CloudKit or alter production schemas to make a local migration appear complete.

## Opening a container can perform work

Apple documents that [ModelContainer](https://developer.apple.com/documentation/swiftdata/modelcontainer) performs migrations as schemas evolve. Treat creating a container against a real store, launching an app or running a preview that reaches that store as potentially mutating. Source review does not authorise any of those operations. Do not probe a live store to discover its version, inspect its rows, copy it into this repository or assume a preview uses synthetic storage.

## Recovery assumptions and failure behavior

Before proposing execution, define the exact source/destination versions, store owner, supported recovery method and authority to operate on that store. Identify what must remain recoverable and who decides whether a failed transition can be retried. Treat atomicity, interruption recovery, partial writes and repeatability as properties requiring evidence, not guarantees implied by a custom stage.

Do not equate reverting app code with reverting persisted data. An older app may not understand an upgraded store. Any backup/restore design must account for a consistent store snapshot, related files or external resources, access protection and compatibility of the restoring app. Do not copy only a guessed database file or promise rollback without a supported recovery procedure. Actual backup creation, restoration and deletion require their own applicable authority.

On migration or container-initialisation failure, preserve the error and existing data. Do not delete the store, silently create a new empty one, fall back to an in-memory store as apparent success or repeatedly retry a destructive path. Describe an honest unavailable/recovery state using existing error handling. Where synchronisation is already used, distinguish local recovery from remote state and avoid claiming a local rollback reverses remote changes.

## Core Data-to-SwiftData transitions

Roadmap item 012 extends this reference. Trigger: an explicit adoption request or a demonstrated persistence requirement involving an existing Core Data app. Reuse the schema-history and recovery guidance above; framework adoption is distinct from migration between existing SwiftData schema versions. Do not migrate solely for newer syntax.

### Establish compatibility from source

Inspect the relevant Core Data model versions and mapping declarations, store descriptions/configurations, managed-object subclasses and persistence consumers as source. Compare these with proposed SwiftData models and the actual supported SDK/deployment targets. Identify app/extension consumers and any existing sync integration. Model generation, app launch and container construction are execution, not read-only inspection; do not invoke them under this scope.

Build a compact correspondence for the affected entities: source entity/attribute -> destination model/property -> conversion or compatibility assumption -> unresolved evidence. Include persisted names, types, optionality, defaults, uniqueness, identifiers, transformable values and relevant model features. Preserve historical definitions. A Swift class rename is not necessarily a persisted entity rename; do not infer storage identity from class names alone.

Map relationships explicitly: destination entity, cardinality, optionality, inverse, delete rule and ordering where used. Identify how existing identifiers and cross-record references remain meaningful. Do not assume a Core Data object identifier is an interchangeable SwiftData identifier. Surface unsupported features or unclear conversions rather than dropping them or replacing values with defaults.

Apple's [adoption sample](https://developer.apple.com/documentation/coredata/adopting-swiftdata-for-a-core-data-app) illustrates complete adoption and coexistence with matching models. It is evidence for those demonstrated arrangements, not proof that an arbitrary Core Data model is compatible. Use current official guidance for the actual schema/toolchain, and leave compatibility unverified without authorised operational evidence.

### Select a transition strategy

- **Retain Core Data:** appropriate when it meets the requirement or compatibility/recovery evidence is insufficient. Keep existing stores and consumers working; do not invent a migration obligation.
- **Compatible adoption or coexistence:** identify the precise shared store location, compatible model definitions, configuration and participating consumers. Apple's sample explicitly configures both stacks for the same store and enables persistent history tracking for its Core Data stack. Determine the applicable history/change-observation and conflict behavior for this project; do not assume sharing a path alone coordinates contexts or writers. Follow [Apple's migration presentation](https://developer.apple.com/videos/play/wwdc2023/10189/) for the demonstrated compatibility considerations, while checking current target support.
- **Explicit conversion to a separate store:** consider only if the requirements and available APIs support it. Specify identity mapping, relationship reconstruction, conversion failures, interruption/retry behavior and the authority for eventual cutover. This is a proposed design, not permission to export or copy real records. Do not describe an ad hoc row copy as an established migration mechanism.

Keep one defined source of truth during each phase. State who can write, when other consumers must stop or change over, and how updates are reconciled. Avoid unplanned dual writes. Trace the chosen configuration through real construction sites; defaults or app-group changes can affect location, so do not assume the old store will automatically be selected. Do not add app groups, entitlements or cloud capabilities incidentally.

### Cutover and rollback assumptions

Define the supported starting versions, destination and cutover condition before replacing a persistence stack. Keep old model/mapping assets required for supported upgrade paths; do not remove them merely because a sample's complete-conversion variant does so. Preserve app behavior such as fetch semantics, save timing and relationship deletion rules unless a change is explicitly requested.

Reuse the recovery section above for consistent snapshots, related resources and protected copies. A preserved old store may cease to be a current rollback point once writes reach the new store. Identify how post-cutover changes would be retained or reconciled; do not promise lossless reversal by switching the old code back on. Shared-store coexistence is not an independent backup, and local rollback does not undo remote synchronisation.

On conversion or initialisation failure, preserve the original store and report the failure. Do not overwrite it, retry destructively, substitute an empty store as success or delete migration evidence. Actual backup creation, export, copy, cutover, restore and retirement remain separately scoped operations. This task authorises none of them.

Acceptance examples — illustrative, not executable checks:

- **Trigger:** a supplied app model has an ordered relationship and a transformable attribute. **Expected action:** compare their intended SwiftData representations and supported semantics, name unresolved compatibility and preserve the Core Data store; do not assume generated models settle the issue.
- **Coexistence:** a widget will use SwiftData while the host retains Core Data. **Expected action:** identify shared-store/model/configuration requirements, change visibility and writer ownership from source; do not launch either process or open the store to prove compatibility.
- **No-action case:** an unrelated UI change needs no persistence transition. Keep Core Data and existing migration assets unchanged.
- **Missing dependency:** source model history or the supported toolchain is absent. State which declarations/settings are needed; never request a live database as a substitute.

Source basis for this section: the two official Apple resources linked here, consulted 27 September 2026. No sample code was imported and no store was inspected or migrated.

## Acceptance and delivery

Illustrative acceptance examples, not executable checks:

- **Trigger:** supplied schema versions add uniqueness to a field whose synthetic examples contain duplicates. **Expected action:** identify the conflict policy and relationship preservation needed before selecting a stage; do not mark the transition safely lightweight or discard duplicates by default.
- **Skipped release:** the app supports upgrades from two shipped versions. **Expected action:** describe how both origins reach the destination and name unsupported paths without constructing containers or running migrations.
- **Failure:** supplied code catches container failure and deletes the store. **Expected action:** identify that data-loss fallback and propose preservation/recovery behavior within authorised implementation scope; do not open or delete the store.
- **No-action case:** a view-only change leaves the schema and persistence behavior unchanged. Do not introduce a new schema version or migration plan.

For a concrete design, report the version path, source locators, selected stage rationale, required invariants, recovery assumptions and missing evidence concisely. Do not create an additional report or check suite by default. Saved instructions or source edits do not prove preservation, successful migration, restore safety or runtime compatibility.

Source basis: official Apple documentation linked above, consulted 27 September 2026. Recheck version-sensitive APIs for the actual target. This is original guidance, not copied migration code or an executed assessment.

Preserve instruction-only scope: no real database access, copying, modification or migration; no fixtures/checks, tests, builds, previews, evaluations, benchmarks, delegation, commits, package operations, installations, cache deletion, index refreshes or background activity. Leave the installed plugin, private data, cloud sync, university RAG and training unchanged.
