# Design-system handoff

Roadmap item 031. Use for requested design-system guidance or a concrete token/component consistency problem. The existing frontend skill already owns semantics, forms, responsive states and accessibility; Figma owns its design tooling. This reference fills the handoff between design intent and project implementation, not a new design provider or coordinator.

## Establish evidence and ownership

For project work, identify the named project, actual framework/component-library versions, relevant design source, affected components and operation-specific access. Inspect only relevant tokens, styles and variants. Distinguish approved design intent, implemented conventions and a proposed change. Name which source owns token values and how code/design correspondence is maintained; do not silently treat either an old screenshot or the newest local CSS as authoritative.

Use available Figma skills for an actual Figma request or supplied reference. For library/tokens/components work, reuse `figma:figma-generate-library` and its required tool prerequisites when acting in Figma. Design-to-code work uses the relevant Figma route and prerequisites. Provider installation does not prove file access or permission to create, update or publish a library. Instruction maintenance does not activate those operational workflows.

## Reuse tokens and components

Selectively adapt ECC's design-system categories: inspect relevant color, type, spacing, shape, shadow and breakpoint conventions; assess component consistency and applicable themes/states. Preserve the project's scale instead of imposing arbitrary values. Avoid subjective numeric scores or aesthetic bans as acceptance criteria. Do not generate a new design document, token export or preview automatically.

Map existing semantic tokens to their current foundations and theme values before adding literals or aliases. Identify the affected consumers and ownership of a proposed token change. Preserve identifiers and public component interfaces where required; renaming/removing a token needs a consumer migration plan rather than silent replacement. A visual resemblance does not prove two values have the same semantic purpose.

Prefer an existing component or supported variant when it meets the actual requirement. Explain a new variant by its user purpose and behavior; avoid duplicating a component for a one-off styling difference or generalizing a single example into a universal abstraction. Keep token and variant decisions in the project's existing documentation system when documentation is requested.

## Preserve behavior across relevant states

For the affected component, identify required default, focus, hover, pressed, selected, disabled, loading and error states as applicable, not as a compulsory matrix for every element. Reuse the parent skill's keyboard, focus, form feedback and motion rules. A disabled-looking style does not implement disabled behavior, and a Figma variant is not a runtime interaction.

Specify responsive behavior from the actual content and supported layout: wrapping, overflow, alignment, reachability and state changes at existing breakpoints. Consider long/localized text, enlarged text and supported themes where relevant. Keep intentional exceptions explicit rather than forcing every screen into identical density or structure. Do not infer contrast compliance, reflow, keyboard usability or rendering quality from token names or a static screenshot.

Use a concrete observed inconsistency or requirement to propose polish. Separate visual intent from behavioral correctness and measured accessibility. Do not launch browsers, generate screenshots, audit the whole repository, install a UI library or publish a Figma library/site merely to demonstrate the proposal. Relevant Superpowers methodology does not replace design approval, framework expertise or access.

## Acceptance examples and limits

Prose examples only, not checks or fixtures:

- Trigger: supplied source shows two equivalent actions using inconsistent semantic tokens. Expected action: identify the authoritative token/component and affected consumers, then propose or implement only the authorised scoped correction. No-action case: design ownership is unresolved; do not overwrite shared foundations or invent approval.
- Trigger: an approved responsive component specification includes an error state missing from supplied code. Expected action: map the intended state to the existing component and preserve accessible feedback. No-action case: no project or source is supplied; do not claim the component is implemented or tested.
- Trigger: instruction-only roadmap maintenance. Expected action: save this handoff and retain existing Figma/frontend routes. No-action case: do not create a design file, tokens, components, preview or test suite.

Report saved guidance separately from observed source/design evidence and unverified project behavior. No named UI project, stack versions, design file or operation-specific access was supplied here; project tokens, components and responsive behavior remain unverified. Keep coordinator routes unchanged and preserve unrelated work/private data. No tests, checks, fixtures, builds, evaluations, benchmarks, delegation, commits/push, installations, publication, spending or account changes. Keep installed caches/QMD indexes unchanged and cloud synchronization, university RAG, training and background automation inactive.

## Source basis

See [adaptation provenance](provenance.md#item-031-design-system-handoff) for the selectively consulted ECC source and unavailable interface-polish material. Existing Figma skill scope was inspected; no Figma operation or runtime validation was performed.
