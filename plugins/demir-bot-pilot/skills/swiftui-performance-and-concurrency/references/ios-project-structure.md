# Focused iOS project navigation

Original roadmap item 002 guidance. Reuse architecture-review's [repository onboarding](../../architecture-review/references/review-checklist.md#repository-onboarding) for general scope, source evidence and flow tracing. This reference adds iOS-specific navigation, not another architecture workflow or executable mapper.

## Trigger and boundaries

Use when the user asks how a named iOS project is organised or a requested change requires identifying its target, scheme, package, resource ownership or configuration. Start from the supplied project root and task. If no app source is available, state that a concrete map needs the project path or supplied project files; do not substitute this plugin's layout or search unrelated projects.

Inspect existing files only within the authorised scope. Do not invoke Xcode, resolve packages, evaluate manifests, run build scripts, regenerate projects, launch devices or create indexes merely to discover structure. No account access is required for local source orientation; unavailable dependencies or generated settings remain explicit gaps.

## Build the smallest useful map

1. **Project entry:** locate the relevant workspace/project or package manifest and existing project documentation. If configuration is generated, identify the maintained source and its relationship to generated files; do not edit generated output by default.
2. **Targets and schemes:** inspect relevant project declarations and available scheme files to connect the requested feature to its app, extension, framework or test target. Record the applicable scheme action and configuration when declared. Do not assume a scheme name identifies one target or that absent shared scheme files prove no scheme exists; local/generated schemes may be unavailable.
3. **Source ownership:** follow the target's source membership and app entry point to the affected view, model or service. Use declarations and applicable membership rules, not folder names alone. Treat missing generated sources or ambiguous membership as unresolved rather than guessing.
4. **Packages:** inspect relevant package declarations, product references and available resolution records. Distinguish a declared version range, a recorded resolved version and source actually available for inspection. Trace only products used by the affected target; do not fetch dependencies or load their entire source trees.
5. **Resources:** locate relevant asset catalogs, localisation files, data models and other resources. Identify the owning target/package and inclusion evidence where available. Distinguish a file's presence from inclusion in the intended bundle; retain uncertainty when generated rules or unavailable configuration control it.
6. **Configuration:** follow relevant project/target settings, configuration selections and xcconfig references. Locate Info.plist and entitlement configuration only as needed. Record declared deployment and Swift settings separately from the actual installed toolchain and effective build settings, which may be unknown. Do not print signing identifiers, secret values, private endpoints or local environment contents into the map.
7. **Useful flow:** connect the selected target to one task-relevant entry point and its source/resource/configuration dependencies. Stop at unsupported links. Reuse architecture-review for substantive boundary decisions; mapping alone does not authorise restructuring.

## Compact navigation reference and reuse

Keep the result in the conversation unless a persistent project reference was requested. Prefer an existing suitable map over creating another document. Include only rows needed for the user's next action:

| Concern | Relevant name/path and source locator | Relationship or next location | Evidence gap |
|---|---|---|---|
| Project, target and scheme | Actual inspected declarations | Selected task context | Unknown selection or generated settings |
| Source and package | Actual entry point/product | Affected view, model or service | Unavailable dependency or ambiguous membership |
| Resource and configuration | Actual resource owner/settings source | Inclusion or configuration relationship | Effective value or bundle inclusion unconfirmed |

These are output fields, not example project facts; omit irrelevant rows and use real locators. State inspected scope and important unknowns. A source map does not prove successful compilation, resource loading, signing or runtime execution.

Reuse the map during the task. Re-read only affected entries when project declarations, schemes, manifests, resolution records, resource membership or relevant configuration change, or when the requested scope moves elsewhere. Do not load the complete repository map every turn. Missing freshness evidence means a focused source re-read, not an automatic rebuild or indexing operation.

## Acceptance examples — illustrative, not executed checks

- **Trigger:** a user supplies an iOS repository and asks where to change a widget's shared image. **Expected action:** inspect the relevant app/extension declarations and resource configuration, then return source-backed locations for the affected target, image and any shared package, with unresolved inclusion clearly marked. Do not infer sharing from a similarly named folder.
- **No-action case:** a small edit already has a current, source-backed target and file location. Reuse that context and inspect the affected file; do not produce a new repository inventory.
- **Missing dependency:** the user requests a map without app source. State which project files are needed; do not fabricate target names, schemes, tool versions or a successful build.

This reference is saved instruction guidance. Application to a real project and its effectiveness remain unverified until observed within authorised scope.
