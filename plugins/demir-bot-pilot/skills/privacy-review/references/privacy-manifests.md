# Apple privacy manifests

Original roadmap item 016 guidance. Use for a requested privacy-manifest review or preparation for an Apple app/SDK. Reuse the parent privacy-review workflow for data flows, recipients and retention; [project navigation](../../swiftui-performance-and-concurrency/references/ios-project-structure.md) and [package guidance](../../swiftui-performance-and-concurrency/references/spm-dependency-management.md) for target, bundle and dependency ownership. Do not turn this into an automatic vulnerability audit, legal certification or submission workflow.

## Establish evidence before declarations

Identify the named app/SDK, relevant targets/platforms, toolchain, dependency versions and requested release scope from supplied source/configuration. Inspect existing PrivacyInfo.xcprivacy files, relevant call sites, SDK manifests/documentation and available redacted diagnostics. Trace actual configuration-dependent behavior, not just dependency names or marketing claims. Unavailable SDK internals or server-side behavior remain unknown; do not query private services or inspect personal records to fill gaps.

Use current official Apple requirements for the actual release date and platform. Start with [privacy manifest files](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files), [adding a manifest](https://developer.apple.com/documentation/bundleresources/adding-a-privacy-manifest-to-your-app-or-third-party-sdk) and [third-party SDK requirements](https://developer.apple.com/support/third-party-SDK-requirements/). Record the applicable source/date when making a project-specific recommendation. Do not freeze an SDK list or reason-code catalogue into this skill.

Apple specifies PrivacyInfo.xcprivacy as a property-list resource. Identify the owning app/SDK target and expected packaging using current platform guidance. A file present in source is not proof it reaches the built product. Do not create a manifest for this instruction plugin merely because the reference describes one.

## Map behavior to the appropriate declaration

For each relevant entry, retain a compact source-backed relationship: `owner/version -> behavior/call site -> purpose/recipient -> Apple category or approved reason -> uncertainty`. Keep this conversational unless a persistent deliverable is requested. Do not copy private payloads or credentials into evidence.

### Required reason APIs

Compare actual app and SDK API use with Apple's current [required reason API guidance](https://developer.apple.com/documentation/bundleresources/describing-use-of-required-reason-api). Inspect wrapper calls and available transitive dependencies where implicated; a text search alone is not comprehensive binary/runtime coverage. Distinguish a possible API match from a confirmed use in the relevant target.

Select an approved reason only when its complete conditions match the real use. Do not choose a common code just to remove a warning or declare a purpose the implementation does not satisfy. If none fits, state the mismatch and the need for an authorised behavior change or the applicable Apple process rather than inventing a reason. Apple requires SDKs to account for their own required reason API use; do not assume an app manifest substitutes for the SDK's declaration.

### Data collection and tracking

Use Apple's current [data-use definitions](https://developer.apple.com/documentation/bundleresources/describing-data-use-in-privacy-manifests) to assess data types, collection purposes, linkage and tracking. Trace relevant data from the app through SDKs and recipients. Distinguish local processing, transmission, collection and tracking under those definitions; do not equate every network request with tracking or every locally held field with reportable collection.

Where applicable, map evidence to NSPrivacyCollectedDataTypes, NSPrivacyTracking and NSPrivacyTrackingDomains using Apple's [tracking guidance](https://developer.apple.com/documentation/technotes/tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest). Do not populate tracking domains with every API host or mark all booleans false by default. Missing telemetry evidence is not proof of no collection. Clarify unresolved behavior before preparing definitive declarations; do not use invalid placeholder values in a purportedly ready manifest.

## SDK and packaging responsibilities

Compare the actual SDK/version/distribution format with Apple's current listed-SDK requirements, including repackaged dependencies. Distinguish source dependencies from binary distributions and the applicable signature obligations. Do not claim a signature was verified from a manifest, publisher name or package pin.

Preserve third-party manifests and their ownership. If an SDK file is missing, invalid or inconsistent with available behavior evidence, identify that dependency and the smallest supported remedy. Do not patch a generated cache, replace the vendor's declaration with fabricated values, update packages or contact the vendor without applicable authority. Existing app declarations do not establish that every embedded SDK obligation is met.

Inspect resource inclusion/configuration as source only. An existing archive or privacy report can be evidence when supplied and authorised, but do not build, archive, run a validator or generate a report under this scope. Syntax validity, source inclusion, final bundle inclusion, observed data behavior and App Store acceptance are separate evidence states.

## Preserve related privacy controls

A privacy manifest does not replace permission purpose strings, App Tracking Transparency requirements where applicable, App Store privacy answers, a privacy policy or legal obligations. Check current Apple guidance for the implicated control rather than assuming one declaration satisfies another. Do not change account settings, consent flows, permissions or public disclosures incidentally. Legal conclusions require their own factual and jurisdictional scope.

When authorised to prepare a real manifest, preserve unrelated valid entries and use only supported keys/value types grounded in inspected evidence. Keep unresolved facts explicit in the response instead of certifying the file as complete. If configuration changes collection behavior, revisit the affected entry; neither an empty template nor a previously accepted submission proves present compliance.

## Acceptance and delivery

Illustrative acceptance examples, not executable checks:

- **API reason:** source calls a required reason API. Identify its actual purpose and owning app/SDK, compare it with the current approved conditions and state any mismatch; do not copy a popular reason code blindly.
- **SDK gap:** an embedded SDK is covered by current requirements but its supplied package lacks the relevant manifest evidence. Identify the missing SDK/version evidence or vendor remedy; do not fabricate the vendor's data-use claims or fetch an update.
- **No-action case:** an unrelated UI copy change affects no inspected data/API behavior or packaging. Do not rewrite privacy declarations or launch a new global audit.
- **Missing evidence:** only an empty template is supplied. State the app/SDK source, versions and data-flow facts needed; do not report no collection or compliance from the template.

Report saved guidance or authorised declaration edits separately from observed source and unverified behavior, packaging, signature validity and submission acceptance. No compliance certification follows from this review.

Source basis: official Apple resources linked above, consulted 27 September 2026. Original instructions, not copied manifests or an executed assessment. App-specific declarations require actual app/SDK evidence.

Preserve the instruction-only restrictions: no apps, simulators, checks/fixtures, tests, builds, evaluations, benchmarks, delegation, commits, package operations, installations, index refreshes, cache deletion or background activity. Do not access accounts, publish, contact vendors, change containers, enable sync or open/copy/migrate real databases. Leave private data, installed plugin, cloud skill sync, university RAG and training unchanged.
