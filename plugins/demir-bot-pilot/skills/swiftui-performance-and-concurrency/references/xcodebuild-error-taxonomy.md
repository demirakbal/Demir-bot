# Xcode diagnostic classification

Original roadmap item 007 guidance. Use when the user supplies an Xcode build failure or asks to interpret an existing diagnostic. Reuse [project navigation](ios-project-structure.md) for target, scheme, package and configuration evidence, and the parent skill for Swift isolation and language-mode questions. Reuse architecture-review only when source evidence reveals a real dependency-boundary problem; a failed build alone does not justify an architecture review or rewrite.

## Establish the evidence

Identify the supplied log or diagnostic location and available context: project/revision, target, scheme, action, configuration, destination/platform, toolchain and SDK. Keep unknown facts explicit. A screenshot, truncated excerpt or final exit status may be insufficient; name the missing diagnostic block rather than inventing it or launching another build.

Read the failing task's surrounding diagnostic and referenced source/configuration before proposing a cause. Separate errors, warnings, explanatory notes and the final command summary. Build tasks can run concurrently, so the first line containing error is not necessarily the root cause. Group repeated failures by their target/task and trace a causal chain where evidence supports one; allow multiple independent failures.

Record the emitting phase separately from the suspected cause. A compiler reporting a missing module may reflect a package or target-configuration issue. A failed signing step may reflect configuration, credentials or environment. Generic nonzero-exit messages do not establish any one cause.

## Classification guide

These are investigation directions, not exact-message matching rules or claims about a particular Xcode release. Consult current official Apple/Swift documentation when interpreting version-sensitive diagnostics or proposing toolchain-specific changes.

| Category | Evidence to inspect | Avoid assuming |
|---|---|---|
| Compiler/type checking | Source location, full diagnostic and notes, involved declarations, imports, target membership, language mode, deployment and isolation settings | That suppressing the diagnostic, adding unsafe concurrency annotations or changing language mode is the correct fix. |
| Linker | Referenced symbols, emitting target, linked products, relevant definitions, object/library inputs and platform compatibility in supplied output/configuration | That every undefined symbol is a missing package, or that excluding an architecture is a universal remedy. |
| Dependency resolution or availability | Manifest requirements, recorded resolved versions, product references, local package paths and supplied fetch/resolution failure | That a missing module proves a network failure, or that deleting resolution records/upgrading packages will fix it. |
| Signing/provisioning | Failing target and configuration, bundle/entitlement requirements and the specific supplied signing diagnostic | That renewing certificates, changing teams, enabling automatic signing or accessing an account is authorised or necessary. |
| Environment/toolchain/destination | Supplied tool/SDK selection, supported destination evidence, referenced paths, permissions and resource errors | That a different local Xcode version, missing simulator or cache corruption caused the failure without supporting evidence. |
| Resource, generated-file or build-script phase | Named phase, earlier script output, declared inputs/outputs, resource membership and generator configuration | That a generic script failure is a Swift compiler defect, or that it permits executing the script to investigate. |

Retain unclassified or mixed causes when the evidence does not support a narrower conclusion. An emitting phase can be confirmed while its root cause remains only a hypothesis.

## Investigate and propose a narrow correction

1. Connect the actionable diagnostic to the relevant source or configuration using actual locators. Inspect only the implicated declarations and dependency path; do not load the whole repository or unrelated machine/account configuration.
2. State what supports the leading explanation, plausible alternatives and the smallest missing evidence that would distinguish them. Do not treat a familiar error string as proof.
3. Separate a source/configuration correction from environment recovery or external access. If fixing code is authorised, change only what the evidence supports and preserve unrelated settings. A request to classify a failure alone authorises explanation, not remediation.
4. Preserve lockfiles, working caches, signing assets and private data. Cache trouble is a hypothesis requiring evidence, not a default diagnosis. Do not delete DerivedData, reset packages, reinstall tools, change certificates/accounts or disable safeguards as a routine first response. Use [DerivedData hygiene](#deriveddata-hygiene-and-scoped-recovery) for a scoped recovery decision; this does not authorise executing it.
5. Read back any authorised edit and describe why it addresses the diagnostic. Without a separately authorised build, report the correction as saved and compilation unverified. Never interpret disappearance from an edited log, a warning-only excerpt or a proposed command as a successful build.

Do not invoke build tools even for version/settings discovery under this instruction-only scope. Use existing supplied output and project files; list unknown effective settings. Do not fetch packages, run scripts, launch devices, inspect credential stores or upload private logs. Quote only necessary redacted diagnostic excerpts; retain useful source locators without exposing signing identifiers, tokens or personal paths unnecessarily.

## Code-signing and provisioning

Roadmap item 037 extends the signing category above. Trigger: a requested diagnosis for a named target with supplied signing/configuration evidence, or instruction maintenance. Reuse project navigation for target/configuration ownership, [architecture guidance](../../architecture-review/SKILL.md) for genuine app/extension capability boundaries and [release guidance](../../release-readiness-and-observability/SKILL.md) for distribution evidence. Do not create another signing specialist or infer an architectural defect from a signing failure.

### Establish the target and evidence chain

Identify the project/revision, exact target (including implicated extensions or embedded products), scheme/configuration, action, destination/platform, Xcode/SDK versions and intended development/distribution method. Distinguish project declarations from effective settings shown in supplied output and from evidence about an existing signed artifact. Simulator results do not establish physical-device or distribution signing success. A generic signing failure does not establish an expired certificate.

Trace only the relevant configuration sources and overrides, bundle identifier, signing mode/team declaration, entitlement source and profile/identity selection evidence. Use sanitised supplied excerpts where possible. Do not enumerate Keychain identities, decode private profiles, inspect account settings or invoke build/signing tools under instruction-only scope. Missing effective settings, artifact entitlements or profile metadata remain explicit gaps; do not fabricate matches from filenames or display names.

Compare the relevant relationships rather than applying a universal signing recipe:

- Identity evidence: whether the intended signing identity is actually available and usable for this operation, including private-key access when evidenced. A certificate's presence alone does not prove access to its corresponding key or successful signing. Do not export keys or change trust/access controls to investigate.
- App identity: the named target's bundle identifier and provider app-identifier/team relationships as shown by supplied evidence. Do not assume every entitlement prefix equals a guessed team identifier or that changing a bundle ID is harmless; it can affect app identity, stores and service relationships.
- Entitlements: distinguish requested source entitlements, capability configuration, profile authorization and the signed artifact's effective entitlements. Compare the relevant capability using current Apple documentation for the actual platform/toolchain. Do not remove an entitlement merely to silence a diagnostic or enable unrelated capabilities as a repair.
- Provisioning: when applicable to the actual platform and distribution method, inspect supplied evidence of profile identity, validity, app/capability compatibility, permitted signing identities and device eligibility where required. Do not assume every distribution method uses the same profile/device requirements or that a profile file's presence means it was selected.
- Embedded targets: diagnose each implicated product's configuration and relationship to the containing app. Do not propagate the app's identifier, entitlements or profile indiscriminately to extensions/frameworks.

These are diagnostic questions, not claims about a supplied project or version-specific rules. Consult current official Apple documentation before prescribing identity/profile requirements, capability changes or signing commands. Reuse [Keychain guidance](keychain-cryptokit.md) for a relevant access-group boundary, without accessing secret material, and [Xcode CLI guidance](xcode-cli-integration.md) for any later authorised tool operation.

### Narrow diagnosis and recovery boundaries

Connect the exact diagnostic to supported evidence: configuration mismatch, unavailable identity/key access, capability/profile mismatch, eligibility/validity issue or an unresolved environment cause. Preserve alternatives when the evidence is incomplete. Authentication/account access, source configuration and signing-asset state are different causes and require different authority.

Describe the smallest correction or missing non-secret fact before any action. Automatic signing is a configuration choice, not a harmless diagnostic shortcut: enabling it or allowing provisioning updates can entail external account/asset effects. Do not toggle signing modes, register devices, renew/revoke/import certificates, create/download profiles, alter entitlements/bundle IDs, change teams/accounts or disable signing without applicable authority. Current roadmap restrictions prohibit such operations. Do not use cache deletion or broad profile removal as routine recovery.

If a later request authorises a source correction, preserve unrelated targets/settings and explain its identity/capability implications. Source edits alone do not verify profile compatibility, compilation, signing, installation, upload or store acceptance. Those are separate outcomes requiring their own evidence and scope. A request to diagnose is not permission to build or launch the app to confirm the theory.

### Acceptance examples and reporting

Prose examples, not checks or fixtures: supplied diagnostics identify a capability mismatch for an extension; trace that extension's entitlements and profile evidence rather than replacing every target's signing settings. A supplied certificate listing without key-access evidence supports only the listing, not a conclusion that signing works. A final signing exit code without its detailed message calls for the missing diagnostic, not certificate renewal or a Keychain search.

Report the named target/action, observed configuration or supplied evidence, suspected cause/confidence, smallest correction/dependency and unverified outcomes separately. No named iOS project, actual tool versions, signing diagnostics or operation-specific access is supplied for this instruction change. Saved guidance does not establish a diagnosed project failure or usable signing identity.

No checks, tests, fixtures, builds, evaluations, benchmarks, delegation, commits/push, installations, publication, spending, account changes or signing/private-data modifications are authorised here. Keep unrelated work and coordinator routes intact, installed caches and QMD indexes unchanged, and cloud synchronization, university RAG, training and background automation inactive.

## DerivedData hygiene and scoped recovery


Roadmap item 008 extends this diagnostic reference. Use when supplied evidence suggests stale generated artifacts, a cache compatibility problem or a build-state inconsistency. A generic build failure, old directory timestamp or recent Xcode update alone is insufficient. Reuse the classification above before attributing a failure to cached state.

### Diagnose before choosing recovery

Compare the implicated artifact and diagnostic with available evidence of source revision, target, configuration, platform, SDK/toolchain and relevant generator inputs. Identify alternative explanations such as wrong target membership, incompatible dependencies, missing generated inputs, permissions or insufficient storage. Keep cache corruption a hypothesis unless the evidence supports it; do not call an artifact corrupt merely because rebuilding might replace it.

Determine the actual output/cache location from supplied build settings, logs or project configuration. Do not assume the default DerivedData location, infer ownership from a similar directory name or enumerate unrelated projects' caches. Distinguish generated build products and intermediates from package checkouts, shared caches, source files, archives and retained diagnostic results. Availability and layout can depend on the toolchain; consult current official documentation before proposing version-specific recovery commands.

Identify whether other targets, projects or active operations use the implicated location. If ownership, current use or recoverability is unknown, state the missing evidence and leave it untouched. Do not interrupt processes or inspect account/private data to manufacture that evidence.

### Choose the narrowest supported option

| Evidence | Proposed next step, within applicable authority |
|---|---|
| Source, target or configuration explains the failure | Address that specific cause if authorised; retain working caches. |
| Evidence is incomplete or only a final failure summary exists | Request the relevant diagnostic/settings excerpt; do not propose a broad reset as a substitute. |
| A particular generated artifact is implicated | Identify its producer, exact scope, required inputs and supported regeneration method before proposing recovery. |
| A cache-specific hypothesis needs comparison | A separately authorised build using a distinct output location may preserve the original evidence; disclose that package/shared state may still be reused, so this is not automatically a fully isolated comparison. |
| A specific recoverable output location is supported as the cause | Propose only that scoped recovery, with ownership, impact and preservation requirements explicit; do not expand to all DerivedData or shared package state. |

Never treat clean builds, package resets, relocation or quarantine as read-only actions. A move can disrupt ongoing work just as deletion can. No wildcard deletion, automatic cleanup hook, scheduled cache purge or repeated clean/build loop follows from this guidance. A clean operation also needs its scope understood; its name does not guarantee that it affects only the suspected artifact.

Before any later authorised recovery, define the exact path and owner, reason for selection, affected work, regeneration prerequisites and what evidence must be retained. Preserve diagnostic records through existing authorised storage; do not copy private logs into the plugin. Explain rebuild time, possible dependency downloads or unavailable offline inputs where applicable. A rollback/preservation plan must describe what can actually be restored; do not promise reversal after deletion or automatically create backups without authority.

Keep recovery and verification distinct. With builds prohibited, provide the supported recommendation and leave the cause and outcome unverified. If a later scoped operation is authorised, record what changed and its observed result without claiming that a successful rebuild proves cache corruption; changed inputs or environment may explain the result. A failed recovery does not authorise a broader purge or retry loop.

### Acceptance examples — illustrative, not executed checks

- **Trigger:** supplied diagnostics name a generated module artifact inconsistent with the documented toolchain/configuration. **Expected action:** locate its producer and owned output from existing evidence, consider configuration/dependency alternatives, and describe the smallest supported recovery or missing input. Do not delete it or run a build under instruction-only authority.
- **No-action case:** the log shows an ordinary source type mismatch. Follow compiler diagnosis and leave DerivedData unchanged.
- **Missing dependency:** the project uses an unknown custom output path or the directory's ownership cannot be established. State that the relevant settings/path evidence is needed; do not guess a folder to remove.

## Output and acceptance

A concise response should identify: `failed task/target -> diagnostic evidence -> category and confidence -> likely cause/alternatives -> smallest correction or missing input -> execution status`. Use ordinary prose for one failure; a small table helps only for independent failures. Do not create a standalone report by default.

Illustrative acceptance examples, not executable checks:

- **Compiler:** a supplied isolation diagnostic includes its source and target settings. Apply the parent's isolation guidance to those declarations and explain the supported correction; do not add blanket unsafe annotations or claim compilation success.
- **Mixed category:** a compiler cannot import a product, but the supplied project declarations show it is not linked to the affected target. Describe the observed configuration gap and compiler symptom separately; do not infer a package-fetch outage.
- **Insufficient evidence:** only the final nonzero exit message is supplied. State that the failing task's detailed diagnostic is needed; do not guess signing or prescribe a cache reset.
- **No-action case:** the user requests an explanation only. Classify the supplied evidence and suggest the smallest next step without editing files or rerunning the operation.

This is saved diagnostic guidance. No actual build has been diagnosed merely by adding it. Project conclusions require the actual logs/source/settings; build success remains unverified until observed within authorised scope. Preserve the user's restrictions on tests, fixtures, builds, evaluations, benchmarks, delegation, commits, installations, index/cache refreshes, publication and background activity. Keep cloud sync, university RAG and training inactive.
