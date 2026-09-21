---
name: frontend-quality-and-accessibility
description: Implement usable, accessible web UI in the actual project stack, covering semantics, keyboard and focus behavior, forms, responsive layouts, interface states and reduced motion. Use for relevant frontend implementation or explicitly requested UI/accessibility reviews; do not trigger automatic audits or tests.
---

Plugin pilot routing: select bundled siblings as `demir-bot-pilot:<skill-name>` from the active catalogue. Resolve file references relative to this skill directory; paths beginning with a bundled skill name are relative to the parent `skills/` directory. External provider skills remain optional and retain their own names. Do not fall back to a duplicate standalone copy silently.


# Frontend quality and accessibility

## Apply within the requested change

Read relevant components, styles, design tokens, package metadata and repository instructions before deciding how to implement. Reuse the actual framework, routing conventions and existing component library; do not assume React/Next.js, install another design system or rewrite unrelated UI. Preserve the requested visual direction and user flow. Ask only when an unresolved product choice materially changes the result.

Apply the relevant principles while implementing the requested component. Do not turn every UI change into a repository-wide accessibility audit. Review requests are read-only unless fixes are authorized. Native apps require their platform-specific guidance rather than mechanically translating HTML/ARIA.

## Semantics and perceivable content

- Use native buttons for actions, anchors with destinations for navigation, and appropriate form elements, lists, tables, landmarks and logically structured headings. Styling should not erase meaning. Give non-submit buttons their explicit type where needed.
- Give controls clear accessible names, preferably from visible labels; preserve the visible wording in the accessible name. Use stable unique IDs and valid relationships. Add ARIA only for semantics/state not already supplied by native elements; never use it to conceal interactive content or claim unsupported behavior.
- Provide meaningful image alternatives and text equivalents for important chart information; decorative media should not clutter announcements. Name icon-only actions by purpose. Do not convey errors, selection or status only through color or motion.
- Use project color tokens and readable typography; preserve sufficient contrast, visible focus and meaningful states across supported themes. Avoid claiming contrast ratios from visual judgment or WCAG compliance from source inspection.

## Keyboard and focus

- Preserve logical DOM/tab order; avoid positive tabindex. All functionality must have a keyboard route. Follow the established interaction pattern for native controls and composite widgets rather than assigning arrow keys universally.
- Prefer existing accessible primitives for dialogs, menus, tabs, disclosures and comboboxes. If a custom widget is genuinely needed, consult the current official WAI-ARIA Authoring Practices for its precise roles, state and keyboard model; partial code examples are not complete implementations.
- Keep focus visible and unobscured. Do not remove outlines without an effective replacement. When content changes, manage focus deliberately without stealing it for routine background updates.
- A modal needs an accessible name, meaningful initial focus, background interaction suppression, contained keyboard focus, an operable close path and appropriate focus restoration. aria-modal alone implements none of these behaviors. Restore to the trigger if still valid, otherwise a logical surviving destination; handle nested overlays through the existing library.
- Preserve usable focus after deletion, navigation, validation and asynchronous updates. Avoid focusable hidden elements, accidental keyboard traps and hover-only access to essential content.

## Forms and feedback

- Provide persistent labels, relevant input types/autocomplete, instructions and programmatically associated help/errors. Placeholders are not labels. Group related choices with appropriate semantics and show requiredness in understandable text and native attributes where applicable.
- Preserve entered data after recoverable errors. Explain what failed and how to fix it, with field-level errors and a summary when useful. Set invalid state when invalidity is established; do not aggressively announce an error on every keystroke.
- Use native validation or the existing project's validation system intentionally; disabling native validation requires equivalent accessible feedback. Keep submission, pending and retry states understandable; prevent accidental duplicate submissions without leaving the user stuck.
- Use polite status announcements for meaningful asynchronous outcomes and assertive alerts sparingly for urgent information. Do not put every dynamic element in a live region or add duplicate announcements.

## Responsive layout and interface states

- Build layouts that reflow with available space and enlarged text; avoid fixed heights that clip content. Let labels wrap, keep actions reachable and make overflow deliberate for genuinely two-dimensional content such as data tables.
- Support touch as well as pointer/keyboard use, adequate target spacing and alternatives to drag-only interactions. Do not make essential information depend on hover. Respect project breakpoints while considering narrow widths, long/localized text and zoom in implementation reasoning.
- Distinguish initial loading, background refresh, success, empty data, no search results, error, permission restriction and offline states when relevant. Do not fabricate data or imply a successful save before confirmation.
- Preserve stable layout where practical. Explain the next useful action in empty/error states; offer a safe retry when appropriate. Do not expose internal implementation detail in product copy unless it helps the user decide.
- Respect prefers-reduced-motion for nonessential animation; favor CSS support where suitable and avoid an initial unnecessary animation before a client-side preference check. Keep information available when motion is removed. Avoid forced autoplay, flashing or animation as the sole status cue; provide relevant pause/stop controls.

## Reuse available providers appropriately

For an actual Figma design task or supplied Figma reference, use the relevant available Figma skill and its prerequisites; for complete site creation use Sites when appropriate to the user's chosen environment. Neither provider is required for a local component fix. Do not migrate a project, create a Figma file, publish a site or connect an account merely because the capability exists. Keep previews/deployments within explicit authorization. A design screenshot alone does not establish interactive accessibility.

For a standards-specific request, verify the applicable current W3C criteria and conformance level, including exceptions, using official sources. Avoid copying upstream criterion numbers or simplified target/contrast rules without checking them. Start with https://www.w3.org/TR/WCAG22/ and https://www.w3.org/WAI/ARIA/apg/ when needed. A pattern is guidance, not certification.

## Verification and completion boundaries

Inspect relevant source and reason about the requested behavior. Do not automatically run browsers, screenshots, accessibility scanners, audits, linters, type checks, builds, tests or build/test/fix loops. A requested preview/build/run permits that scoped action, not a testing campaign. If tests are requested, distinguish writing, running and fixing them; follow qa-and-test-evidence only within scope. Automated scans cannot establish full accessibility.

Report what changed and why, known remaining work and what was not executed or assessed. Never claim keyboard, screen-reader, zoom or responsive behavior was verified without the corresponding evidence. Do not produce extra reports/docs or repeat requests for testing. Keep cloud sync deferred under Demir Bot's rules. Read references/provenance.md only for maintenance or source history.
