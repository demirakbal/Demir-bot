# iOS localisation

Original roadmap item 015 guidance. Use for requested localisation work or a demonstrated issue with translated text, plural selection, locale formatting or right-to-left layout. Reuse [project navigation](ios-project-structure.md) and [Swift package management](spm-dependency-management.md) for resource ownership, [iOS accessibility](ios-accessibility-audit.md) for reflow and meaningful labels, and [error handling](ios-error-handling.md) for user messages. Do not create a translation service or audit unrelated screens.

## Establish the localisation contract

Inspect relevant source, localisation resources and project settings as text. Identify source language, approved target languages/regions, supported toolchain/deployment targets, owning target/bundle and existing key/table conventions. Distinguish display language from region, calendar, time zone, currency and measurement preferences; one language does not imply one regional format.

Use supplied approved translations and terminology. If absent, implement authorised localisation structure without presenting invented translations as approved. Any requested translation draft stays labelled for review. Do not silently replace reviewed wording, mark drafts approved or send strings/private content to external translation providers. Missing source, target settings or approved wording remains explicit rather than blocking unrelated reusable guidance.

## String catalogs and text ownership

Follow the project's existing resource format. Apple's [plural localisation guidance](https://developer.apple.com/documentation/xcode/localizing-strings-that-contain-plurals) recommends string catalogs for Xcode 15 and later and describes strings/stringsdict for earlier tooling. Distinguish authoring-tool support from availability of the runtime APIs used by the app. Do not automatically migrate legacy resources or prescribe newly introduced generated symbols without checking compatibility.

Trace each affected string from its source call to the correct table/catalog and bundle. A literal, runtime String, key and verbatim user content can take different paths through localisation APIs; inspect the actual initializer rather than assuming all visible text is extracted. Preserve user-entered content and technical identifiers as data unless translation is expressly intended.

Keep complete localisable phrases with contextual comments and meaningful interpolation, instead of concatenating translated fragments in an English word order. Preserve placeholder identity, type, formatting intent and translator ability to reorder content. Separate keys when identical source words have different meanings. Include affected accessibility labels, hints and error messages without duplicating unnecessarily the native control's spoken semantics.

Preserve unrelated entries, developer comments, review state and existing translations. A stale/unreferenced marker alone does not authorise deletion. Missing language variants need an explicit fallback/pending status, not a claim of complete translation. Apple's [string catalog guidance](https://developer.apple.com/documentation/xcode/localizing-and-varying-text-with-a-string-catalog) describes extraction and variants; its build instructions do not authorise building, exporting or regenerating catalogs in this task.

## Plurals and variable content

Use the selected resource system's language-specific plural variants for count-bearing messages. Do not implement pluralisation as count equals one versus everything else for all languages. Preserve the numeric input needed for plural selection instead of supplying only a preformatted string.

Review the required categories and placeholders for each approved language, including messages with more than one count. Do not fabricate grammatical forms or treat copying the source language into every category as approved localisation. Optional variants should reflect the actual message contract; preserve meaningful empty/zero states without assuming every language uses the same grammatical category.

## Dates, numbers, currencies and units

Use supported Foundation format styles/formatters for user-facing dates, numbers, percentages, currencies, lists and measurements, following [Apple's formatting guidance](https://developer.apple.com/documentation/xcode/preparing-dates-numbers-with-formatters/). Keep underlying values typed; do not build display formats with manual separator substitution or parse a localised display string as a stable storage/wire format.

Preserve the operation's semantic currency, unit, calendar and time-zone requirements separately from presentation preferences. Locale formatting does not convert money between currencies or determine the event's intended time zone. Do not change amounts, precision or business rounding rules as an incidental localisation fix. Distinguish numeric-input parsing from display formatting and report unsupported/ambiguous input through existing error handling.

Trace explicit locale overrides and any cached formatting state only where relevant. Do not force one locale globally to repair a single fixed-format protocol field. Keep storage/network representations governed by their own contracts. Current source can establish selected formatting APIs; actual rendered output remains unverified without authorised observations.

## Right-to-left layout and text expansion

Use semantic leading/trailing alignment and platform layout conventions where appropriate. Apple's [LayoutDirection documentation](https://developer.apple.com/documentation/swiftui/layoutdirection) describes SwiftUI's direction support; inspect custom coordinates, offsets and gestures instead of blindly reversing arrays or applying a whole-screen transform.

Distinguish directional navigation artwork from logos, media, charts and content whose direction carries another meaning. Do not mirror every image. Review mixed-direction text such as names alongside numbers or identifiers using platform-supported text behavior, without altering the stored user content or inserting arbitrary direction characters as a blanket fix.

Account for longer translated phrases, wrapping and Dynamic Type while preserving reachable actions and logical reading order. Inspect truncation and fixed-size constraints; do not solve expansion by globally reducing font size or removing accessibility support. Language, locale and layout-direction settings are related but distinct; a changed locale in a preview declaration is not proof of a functioning RTL layout. Do not run previews or change device settings under this scope.

## Acceptance and delivery

Illustrative acceptance examples, not executable checks:

- **Plural:** source concatenates a count with an English noun. Replace that approach within authorised code scope with the existing resource system's complete message and approved plural variants; leave missing translations explicitly pending.
- **Formatting:** an amount uses a hard-coded separator and currency symbol. Identify the actual currency and numeric contract, then propose compatible locale-aware display without changing its value.
- **RTL:** a custom row hard-codes left/right spacing and a directional arrow. Review semantic alignment and the arrow's purpose; do not mirror unrelated artwork or claim visual success from source alone.
- **No-action case:** an internal machine identifier is deliberately nonlocalised and no user-facing change is requested. Preserve it; do not translate protocol keys or migrate catalogs for novelty.

Report source edits/saved guidance, approved versus pending language content and unverified linguistic/rendered behavior separately. A source review is not native-language approval or device-tested localisation. No additional report, catalog export or check suite is implied.

Source basis: official Apple resources linked above, consulted 27 September 2026. Original guidance; no translations or implementation code imported. App-specific work requires actual source/settings and approved translations.

Preserve instruction-only restrictions: no apps, simulators, previews, settings changes, checks/fixtures, tests, builds, evaluations, benchmarks, delegation, commits, installations, package operations, index refreshes, cache deletion or background activity. Do not access accounts, alter containers, enable sync or open/copy/migrate real databases. Leave private data, installed plugin, cloud skill sync, university RAG and training unchanged.
