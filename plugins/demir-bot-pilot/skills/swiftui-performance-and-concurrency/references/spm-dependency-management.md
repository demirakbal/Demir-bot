# Swift package management

Original roadmap item 009 guidance. Use for a requested package change or a supplied dependency, resource or binary-target problem. Reuse [project navigation](ios-project-structure.md) to identify the consuming target/product and [Xcode diagnostic classification](xcodebuild-error-taxonomy.md) to distinguish compiler/linker symptoms from resolution failures. Do not add a package-management framework or perform a broad dependency audit.

## Establish the dependency context

Inspect the relevant Package.swift, project package references, available Package.resolved and existing configuration/documentation as text. Identify the workspace/project/package that owns each record rather than assuming all resolution files belong to the same operation. Use supplied toolchain, SDK, destination and deployment evidence; keep unavailable settings explicit.

Separate the manifest's tools-version requirement, language settings, deployment declarations and the actual compiler used. Consult current official Swift/Apple documentation before prescribing version-dependent manifest syntax or compatibility rules. Reading a manifest does not authorise evaluating it, invoking package plugins or running tools to obtain a dependency graph.

Trace only the affected chain: `declared dependency -> product -> target consumer -> available resolution/source evidence`. Package identity, product name and imported module name need not be interchangeable. Do not diagnose a fetch failure merely because a compiler cannot import a module.

## Versions and resolution

- Record the declared requirement type and value, such as a version range, exact version, branch, revision or local path, from actual source. Compare it with the relevant recorded version/revision without assuming that a declaration is the currently used dependency.
- Distinguish declared constraints, a saved resolution record, locally available content and a successfully built integration. None alone establishes all the others. A missing lockfile is an evidence gap, not permission to create one or resolve dependencies.
- For a supplied conflict, trace direct and relevant transitive constraints using available records/source. Identify which requirement is incompatible and what remains unknown. Do not relax ranges, upgrade everything, remove a pin or select an arbitrary older version as a default remedy.
- Preserve existing lockfiles, local path overrides and unrelated pins. If a future dependency edit is authorised, keep it scoped and explain any expected resolution work separately. Do not hand-edit a resolved revision to simulate a successful resolver outcome or delete the file to force a fresh graph. Explain reproducibility trade-offs for moving branches and local paths without claiming a pin proves trust or availability.
- Existing resolution failures may reflect authentication, network access, missing versions, manifest/toolchain incompatibility or conflicting requirements. Classify supplied evidence and name missing access rather than trying credentials, mirrors, account changes or downloads.

## Package resources

Locate the target's resource declarations, relevant files and consuming code. Distinguish source presence, declared inclusion and observed runtime loading. Review processing/copying intent, exclusions, localisation and bundle lookup against the actual supported tooling; do not assume the app's main bundle owns package resources.

Trace the resource through the package target and exposed product to its consumer. Keep ownership at the appropriate boundary and avoid copying the resource into the app as an unexplained workaround. Case/path differences, naming collisions and generated resources are hypotheses to investigate with source evidence. If generated outputs are unavailable, identify the producing step without running it. Do not claim resources are bundled or load successfully without operational evidence.

## Binary targets and compatibility

Inspect the declared local artifact path or remote artifact reference and any recorded integrity metadata. Use only already available, authorised metadata/source; do not download, unpack or execute an unknown artifact merely to complete this review. Identify the supplier and relevant provenance evidence, leaving unavailable contents unknown.

For an available binary, inspect relevant metadata for platform/device-versus-simulator coverage, architecture and declared compatibility. A matching CPU architecture alone does not establish the correct platform variant or Swift/toolchain compatibility. Do not promise compatibility from a filename, change excluded architectures as a blanket fix or substitute an unverified binary. Consult current official documentation for the actual artifact format and toolchain before recommending a concrete change.

Preserve recorded integrity checks. A checksum can establish correspondence with an expected artifact when actually verified; it does not prove that the supplier or code is safe. Never replace a checksum just to bypass a mismatch. Distinguish declared metadata from independently observed verification, signing or successful linkage.

## Provenance and scoped decisions

For the affected dependency, inspect available evidence of source location, publisher, revision, licence/provenance and any executable plugins or build steps. Distinguish first-party claims from verified facts. A package declaration or trusted hosting domain is not a full supply-chain assessment. Flag material unknowns without inventing vulnerabilities, redistribution rights or permission to run scans.

Reuse architecture-review for an actual boundary/design question and existing security/privacy/release specialists only for their relevant requested scope. Keep private repository addresses, tokens, signing information and private source out of public outputs and the plugin package.

## Acceptance and reporting

Illustrative acceptance examples, not executable checks:

- **Version conflict:** supplied manifests and resolution evidence show incompatible requirements. Identify the conflicting constraints and smallest supported change to consider; preserve the lockfile and do not run resolution.
- **Missing resource:** package code looks in the app bundle while the supplied declarations place the resource in a package target. Explain the ownership/lookup mismatch and deployment-dependent correction; do not claim runtime loading has succeeded.
- **Binary mismatch:** supplied metadata identifies a device variant while the failure concerns a simulator build. Distinguish the platform mismatch from a generic missing-package error; do not download a replacement or disable architecture checks.
- **No-action case:** dependency declarations and available records fit the requested task with no demonstrated gap. Retain versions and wiring; do not update packages just because newer versions may exist.
- **Missing evidence:** no app manifest, resolution record or diagnostic is supplied. State which inputs a concrete investigation needs; do not invent a graph or compatibility result.

Report saved guidance or authorised source edits separately from inspected declarations, unresolved dependencies and unverified build/runtime behavior. This instruction-only scope permits no fetching, resolution, updating, resetting, cache deletion, manifest execution, tests, fixtures, builds, evaluations, benchmarks, delegation, commits, installations, index refreshes or background activity. Leave the installed plugin, private data, cloud sync, university RAG and training unchanged.
