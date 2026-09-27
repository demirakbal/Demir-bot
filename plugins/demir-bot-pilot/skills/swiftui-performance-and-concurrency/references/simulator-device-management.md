# Simulator and device management

Original roadmap item 024 guidance. Use for instruction maintenance or explicitly requested simulator/device selection, app launching or screenshot work. Reuse [project navigation](ios-project-structure.md) for project targets/configuration, [architecture review](../../architecture-review/SKILL.md) for app boundaries and side effects, and [UI test patterns](../../qa-and-test-evidence/references/ui-test-patterns.md) for observable screen state and isolation. Do not add a separate device-management specialist or assume a provider is installed.

## Identify the exact target and operation

For project operations, establish the named project, actual Xcode/tool/SDK versions, deployment compatibility, app target and bundle identifier, simulator versus physical device, OS/runtime version and stable device identifier. Distinguish a build target or scheme from a runtime device. Use a user-selected target or available scoped evidence; display names and a generic booted-device alias are insufficient when more than one destination could match.

Identify the requested operation separately: inspect/select, boot, install an existing artifact, launch an installed app, interact or capture a screenshot. Determine which necessary steps the current request actually authorises; do not ask again for already-authorised steps. A request for reusable guidance authorises none of these operations. Missing project, artifact, target or access is a dependency to report, not permission to invent one or launch something else.

Before an authorised operation, use supported tooling available for the actual host and toolchain. Consult its official version-appropriate documentation before selecting commands or flags. Distinguish simulator tooling from physical-device support; do not assume identical commands, permissions or behavior. Do not install tooling, download runtimes, change the active developer directory, pair/trust devices, enable developer settings, alter signing/provisioning or change accounts merely to make a request work.

Where selection evidence is insufficient, obtain only the inventory needed for the authorised task using available read-only facilities. Do not enumerate unrelated devices, installed apps or private containers for general discovery. If several matching targets remain and context cannot resolve them, request the exact choice before a dependent operation. Never silently substitute another device or OS when the intended target is unavailable.

## Preserve device state and data

Record relevant supplied/observed pre-operation state and ownership, including whether the target was already running and whether the requested app/artifact is present. An idle-looking simulator is not necessarily disposable. Do not boot, shut down, terminate or erase all devices as a convenience. Avoid affecting an unrelated active session.

Use the exact selected identifier for each supported operation and confirm subsequent evidence refers to that target. Do not create, clone, reset, erase or delete devices, clear caches, reset privacy permissions, uninstall apps or replace data as routine recovery. An installation or launch may affect persistent state; establish the requested app and known startup effects before acting. Preserve stores, Keychain data, account state and user content; do not open or copy containers to investigate this roadmap capability.

Launch can trigger app startup work such as network access, synchronization or migrations. Where prohibited effects cannot be excluded using supplied evidence or an existing authorised isolated mode, state the dependency and leave the launch unperformed. Do not invent a bypass or change production behavior to obtain a screenshot. Reuse existing architecture/privacy boundaries rather than assuming a simulator contains no private data.

## Scoped launches and screenshots

For an authorised launch, identify the installed app or explicitly authorised existing artifact and supported launch configuration. Do not build an absent artifact, install a different app, or resolve dependencies automatically. Booting a simulator, launching the Simulator interface and launching an app are distinct outcomes; report what actually occurred. Tool success alone does not establish that the intended screen loaded or the app works correctly.

For an authorised screenshot, establish the exact target, requested screen/state and permitted output destination. Capture only within that scope. A screenshot request does not automatically authorise unrelated navigation, login, permission acceptance or user-data changes. Follow applicable privacy guidance when visible personal data is involved; do not capture private content merely to improve evidence or upload an image to an external service without authority.

Reuse observable-state guidance rather than fixed sleeps to judge readiness when interaction is authorised. Confirm that the resulting artifact exists and inspect it only within the permitted scope before claiming it depicts the intended screen. Record device/OS, app/source identity when known, and relevant appearance, locale or orientation. Do not claim an image is current or from the requested device without evidence. For visual regression comparisons, reuse [snapshot-testing guidance](../../qa-and-test-evidence/references/snapshot-testing.md); capture alone does not approve a baseline.

Do not leave new background loops or monitoring active. End only task-owned processes when that cleanup is within scope and preserves user work; do not shut down a pre-existing device session. If restoring prior state would require destructive or unauthorised work, report remaining state instead of forcing restoration.

## Failure handling and acceptance examples

Classify supplied or observed failures as target ambiguity/unavailability, unsupported tool/runtime, missing artifact/app, access/pairing/signing dependency, launch failure or capture failure. Keep the original diagnostic and identify the smallest next action. Do not recover by deleting data, repeatedly relaunching, changing accounts or switching destinations silently. Reuse [Xcode diagnostic guidance](xcodebuild-error-taxonomy.md) for relevant supplied diagnostics without invoking builds.

These are instruction examples, not executable checks or fixtures:

- Trigger: two destinations share a display name. Expected action: distinguish stable identifiers and OS/runtime evidence, selecting only the authorised target. No-action case: the request does not disambiguate and context cannot resolve it; do not boot or launch either.
- Trigger: a screenshot of an already-running, explicitly identified synthetic app screen is requested. Expected action: use available supported capture tooling for that exact device and permitted destination, preserving unrelated sessions. No-action case: required access or safe screen evidence is missing; report the dependency rather than accessing accounts or changing data.
- Trigger: the requested app is absent. Expected action: report the missing artifact/installation dependency and distinguish it from device selection. No-action case: builds or installation are outside scope; do not perform them or substitute another app.
- Trigger: roadmap instruction maintenance. Expected action: save guidance and its existing SwiftUI route. No-action case: do not inspect live devices, launch apps, capture images or create checks.

## Reporting and boundaries

Report saved instructions separately from observed operations and unverified project behavior. Name actual target/action/artifact only when evidenced; do not claim launch success, screenshot accuracy, compatibility or preservation verified by runtime observation when only source guidance was reviewed.

This roadmap request supplies no named iOS project, actual tool versions, device identity or operation-specific access. It saves guidance only: no tests, fixtures, checks, builds, app launches, evaluations, benchmarks or device operations. Keep unrelated work and private data intact, coordinator routing minimal, installed caches and QMD indexes unchanged. No delegation, commits/push, provider installation, publication, spending or account changes. Cloud synchronization, university RAG, training and background automation remain inactive.

Original synthesis from roadmap item 024 and existing project-navigation, architecture and QA guidance. No command syntax, host tooling, device compatibility or runtime behavior was verified by this instruction change.
