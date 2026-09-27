# App Store review guidance

Roadmap item 038. Use for instruction maintenance or a requested review of a named app against applicable official submission requirements. Reuse the parent SwiftUI skill, [release readiness](../../release-readiness-and-observability/SKILL.md), [privacy manifests](../../privacy-review/references/privacy-manifests.md) and [signing diagnostics](xcodebuild-error-taxonomy.md#code-signing-and-provisioning). Use architecture-review only for relevant feature/data boundaries. Do not create a compliance specialist, blanket audit or submission automation.

## Establish the app and applicable rules

For project review, identify the named app, platform, version/build/source revision, actual toolchain/SDK, intended storefronts/distribution path, feature/business model and supplied metadata or review correspondence. Separate the proposed release from an older accepted build. Missing source, build evidence, requirements or supported access remains explicit; do not open accounts or run the app to manufacture it.

Consult current [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) and relevant official submission documentation at review time. Record retrieval date and the precise applicable section alongside each finding. Verify exceptions, platform/region conditions and effective dates before applying a rule; do not freeze remembered purchase, privacy or submission rules into a universal checklist. A guideline interpretation is not Apple's decision or legal certification.

Use the app's actual features to select deeper review: account/data handling, purchases/subscriptions, user content, sensitive capabilities or other relevant categories. Do not assume every app needs every category. Determine applicability from evidence and current official rules before claiming a violation. For material legal questions, use the relevant legal route and jurisdiction rather than treating App Store guidance as complete legal advice.

## Tie requirements to evidence

For each relevant concern, record the rule/source/date, applicability rationale, app/build evidence, assessment and smallest correction or missing fact. Distinguish supported concern, unresolved interpretation, missing evidence and no issue found within the inspected scope. Do not infer failure merely from absent evidence or mark an unreviewed requirement satisfied.

Compare supplied metadata and feature descriptions with the intended build and available behavior evidence. Use Apple's [required-property reference](https://developer.apple.com/help/app-store-connect/reference/app-information/required-localizable-and-editable-properties) for applicable submission fields rather than inventing a permanent field list. Check the relevant locale/version relationship; a completed template is not proof that its claims are accurate.

Apple's pre-submission guidance addresses app completeness, accurate metadata, reviewer access and explanations of non-obvious features. Assess supplied evidence for these areas, preserving the distinction between documented intent and tested behavior. Do not create reviewer accounts, expose real credentials, activate backend services or execute tests under this roadmap scope. If reviewer access is required but unavailable, report that dependency without copying secrets into the plugin or report.

Reuse privacy guidance to reconcile actual app/SDK data behavior with declarations; a manifest, policy URL or previous acceptance does not prove present compliance. Do not prepare affirmative privacy answers from guesses. Keep signing/build compatibility evidence separate from review-policy assessment and release readiness. Review permission does not authorise code, declaration or store-metadata changes.

## Submission and uncertainty boundaries

Apple's [submission workflow](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-app) distinguishes preparing an app version for review from actually submitting it. Reuse [connector operation boundaries](../../architecture-review/references/backend-api-contracts.md#typed-connector-operation-contract) for any later authorised App Store Connect operation. Reads, edits, uploads, submission, distribution and release remain distinct effects.

For supplied rejection correspondence, tie the stated concern to the exact app version and cited rule. Separate Apple's stated reason from hypotheses; propose the smallest evidence-backed response or correction. Do not hide behavior from reviewers, fabricate supporting evidence, contact Apple, submit an appeal or resubmit automatically. Drafting review notes or an explanation, when requested, does not authorise sending it.

Conclude with findings and unassessed areas, not an acceptance probability, guarantee or certification. A source review, passing tests, successful upload or historical approval cannot guarantee the next decision. No issue found in limited evidence is narrower than full compliance. Preserve uncertainty when official requirements or applicability are ambiguous rather than inventing a definitive answer.

## Acceptance examples and reporting

Prose examples, not checks or fixtures:

- Trigger: supplied metadata describes a feature absent from the named build's source/evidence. Expected action: identify the discrepancy and applicable current metadata requirement, then propose a scoped correction. No-action case: only an idea is supplied; do not claim the build fails review or edit store metadata.
- Trigger: a named app's account-dependent flow lacks supplied reviewer-access information. Expected action: identify the review-access dependency and safe preparation needed. No-action case: no account authority exists; do not create credentials, log in or enable services.
- Trigger: a rejection cites a rule whose regional applicability is uncertain. Expected action: consult the current official section and state the unresolved facts. No-action case: do not promise acceptance after a guessed fix or submit an appeal.

Report saved guidance separately from inspected official sources/app evidence, actual operations and unverified behavior. No named app, actual tool versions, submission materials or operation-specific access was supplied for this instruction change. No app compliance determination, review submission or acceptance is established.

Preserve unrelated work and private data. No tests, checks, fixtures, builds, evaluations, benchmarks, delegation, commits/push, provider installation, publication, spending or account changes. Keep coordinator routes minimal, installed caches/QMD indexes unchanged, and cloud synchronization, university RAG, training and background automation inactive.

## Source basis

Original roadmap guidance informed by the official Apple pages linked above, consulted on 27 September 2026. Recheck their current requirements for a real app review. No private app/account access, execution or submission occurred.
