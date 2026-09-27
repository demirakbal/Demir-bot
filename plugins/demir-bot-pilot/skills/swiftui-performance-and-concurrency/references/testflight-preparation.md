# TestFlight preparation

Roadmap item 039. Use for instruction maintenance or an explicitly requested TestFlight workflow. Reuse item 037 [signing diagnostics](xcodebuild-error-taxonomy.md#code-signing-and-provisioning), item 038 [submission constraints](app-store-review-compliance.md), item 025 [Xcode CLI integration](xcode-cli-integration.md) and item 036 [connector contracts](../../architecture-review/references/backend-api-contracts.md#typed-connector-operation-contract). Their saved guidance is not evidence that a real project's signing, access or tooling works. Reuse [release readiness](../../release-readiness-and-observability/SKILL.md) rather than creating another release coordinator.

## Establish the workflow boundary

Name the app/project, platform, source revision, scheme/configuration, toolchain, bundle/app identity, intended version/build and existing artifact when available. Identify the requested endpoint: preparation, archive/export, upload, processing observation, beta review or distribution to a specific group. Reuse existing project automation and supported tools; do not introduce a runner, CI service or signing framework by default.

Consult Apple's current [TestFlight overview](https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview/) and relevant operation documentation for the actual platform. Distinguish internal and external testing, review requirements and eligibility from supplied facts; do not freeze current limits or expiry durations into a permanent recipe. No account access is implied by tool availability. Use only non-secret supplied evidence to establish project-specific prerequisites under instruction-only scope.

Preparation, code/configuration changes, build/archive/export, upload, submission, distribution and notifications are separate effects. Honour existing exact-action authority without repeatedly asking, but do not infer authority for later stages from an earlier stage. This roadmap request permits guidance only; do not write an executable workflow, invoke tools, create checks or start automation.

## Versioning, artifact and signing evidence

Follow the project's existing version/build-number source and sequencing policy. Keep marketing version, build identifier, source revision and artifact identity distinct. Identify how parallel or retried workflow runs avoid ambiguous artifact/version selection; do not invent a next build number or edit versions without project evidence and authority. Verify applicable Apple requirements before prescribing a numbering rule.

Tie any later proposed upload to one existing or explicitly authorised produced artifact and its known provenance. Preserve evidence of target, configuration and signing assumptions, including embedded targets where relevant. A filename or successful archive does not alone establish the intended bundle identity, valid distribution signing or TestFlight eligibility. Do not create an archive, inspect Keychain, renew profiles or change signing modes to fill gaps under this scope.

Separate build provenance, export/signing evidence and remote processing evidence. Existing artifact checks or project gates may be requirements, but absent authority leaves them unperformed; do not disable gates or present source inspection as a successful build/validation.

## Release notes and reviewer information

Prepare notes only from supplied changes and known limitations for the identified build. Distinguish beta testing instructions from public release claims. State what changed, useful areas to exercise and known issues without claiming tests passed or bugs were fixed when evidence is absent. Preserve requested locale and approved terminology. Do not include secrets, private issue text, personal tester data or unsupported marketing claims.

Use Apple's current [test-information guidance](https://developer.apple.com/help/app-store-connect/test-a-beta-version/provide-test-information) for applicable fields. Identify missing feedback contacts or reviewer-access requirements without inventing them or creating accounts. Draft notes remain local proposals until metadata editing is authorised; do not post them, send invitations or provide real credentials in the plugin.

## Upload, processing and distribution evidence

For a later authorised operation, use the exact supported tool/API contract from items 025/036. Record target app/build, artifact identity, operation status and safe evidence locator. Keep credentials and raw private logs outside the package. Distinguish transport acknowledgement, upload acceptance, processing completion, eligibility/review status, assignment to a group and tester availability. Do not claim distribution from a successful upload alone.

If an outcome is uncertain, preserve the delivery/build identifier and last observed state. Do not automatically increment the build, upload again or switch tools; first identify whether separately authorised status inspection can resolve the uncertainty. Bound any authorised polling and stop at its limit. A pending job is not a completed release, and local cancellation does not prove remote cancellation.

Before any distribution, identify the exact authorised build and audience and the effects of existing group automation or notification settings. Uploading can interact with already-configured distribution behavior; do not assume it is isolated from testers. Do not create groups, enable public links, add testers, change automatic distribution, submit beta review or notify anyone without applicable scope. If the effects cannot be established, report that dependency before acting.

A recovery proposal may preserve an older usable build or stop further distribution only where supported and authorised. Do not promise that replacing or expiring a build reverses installed-app data changes or external side effects. Keep tester feedback and account information private; this guidance does not authorise retrieving them.

## Acceptance examples and reporting

Prose examples, not executable cases or fixtures:

- Trigger: preparation is requested for a named build with supplied signing and change evidence. Expected action: describe version/artifact identity, notes and the remaining supported-operation dependencies. No-action case: upload authority is absent; leave the artifact local and do not invoke distribution.
- Trigger: supplied upload output reports acceptance but no completed processing state. Expected action: report upload acceptance only and identify the missing status evidence. No-action case: no account/status-read authority exists; do not poll, retry or claim tester availability.
- Trigger: a workflow targets an existing tester group whose automatic distribution behavior is unknown. Expected action: identify the uncertain audience/notification effect. No-action case: do not assume upload-only scope permits notifications or change group settings.

Report guidance saved, project preparation actually completed, artifact/signing evidence, upload state and distribution state separately. No named app, actual versions, artifact, release-note facts or supported account access was supplied for this roadmap change. No real workflow was authored or executed; signing, upload and distribution behavior remain unverified.

Preserve unrelated work/private data and keep the coordinator unchanged. No tests, checks, fixtures, builds, evaluations, benchmarks, delegation, commits/push, installation, publication, spending or account changes. Installed caches and QMD indexes remain unchanged; cloud synchronization, university RAG, training and background automation stay inactive.

Source basis: original synthesis from roadmap item 039, its existing prerequisite references and linked Apple TestFlight documentation consulted on 27 September 2026. No app/account operation was performed.
