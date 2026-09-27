# Xcode CLI integration

Original roadmap item 025 guidance. Use for instruction maintenance or a requested, scoped Xcode command-line integration. Reuse [project navigation](ios-project-structure.md), [architecture review](../../architecture-review/SKILL.md), [diagnostic classification](xcodebuild-error-taxonomy.md) and [device management](simulator-device-management.md). Use existing [release guidance](../../release-readiness-and-observability/SKILL.md) for release evidence and authority; do not add a separate CLI specialist or duplicate those workflows.

## Establish installed support without assuming it

For project implementation, identify the named project, requested operation, actual host/Xcode/SDK/tool versions, relevant artifact and operation-specific access. Distinguish installed tools from the active developer toolchain and any task-local override. A tool on PATH, an Xcode application directory or a Command Line Tools installation alone does not prove the needed executable, SDK or subcommand is available for the intended operation.

Start with supplied version/path/help output and relevant project integration definitions. For separately authorised discovery, use only supported, narrowly scoped read-only lookup/version/help facilities for the relevant tools. Establish the executable's resolved location, selected developer directory, version and supported subcommand/options. Treat wrappers as code with possible side effects, not transparent aliases. Do not run builds or project-evaluating commands merely to infer settings; package resolution, scripts or network work may be implicit.

Do not switch the global developer directory, install/update Xcode or runtimes, accept licence agreements, download components, change environment persistently or repair accounts as discovery. If tool discovery would require first-launch setup or another state change, stop that operation and name the dependency. Do not dump the full environment or credential stores. Instruction-only maintenance performs no installed-tool discovery commands and makes no claim about this host's support.

## Define the exact operation contract

Before any separately authorised invocation, establish:

- Identity and scope: executable/version, working directory, project/workspace/package, scheme/configuration and exact device, artifact or destination as relevant.
- Inputs: supported flags/subcommands, input format, quoting, required existing files, version-sensitive options and configuration precedence, with official documentation and installed help evidence.
- Effects: read/write paths, replacement behavior, processes, network/account use, package resolution, signing and any implicit scripts or uploads. A command named validate or export is not necessarily local or non-mutating.
- Outputs and completion: exit status, documented output format, artifact location, asynchronous job/delivery identifier and the evidence that establishes completion. Do not treat progress text or a submitted request as a finished operation.
- Failure/recovery: how diagnostics are retained safely, whether partial artifacts or remote submissions can exist, and the narrow next step. Do not retry an uncertain upload blindly or delete caches/data to repair a tool failure.

Separate discovery, planning, script creation and execution. An integration request does not authorise every available subcommand. Use existing project conventions and the minimum necessary operation; no generated wrapper, check suite, hook, CI workflow or automation is required by this roadmap item. Avoid interpolating untrusted paths or metadata into shell syntax. Keep credentials out of command examples, shell history, logs and saved plugin files.

## Verify upload tooling for the actual service

Use current official Apple documentation plus evidence from the installed tool before proposing an upload command. Identify whether the task concerns an App Store Connect build, asset pack, notarization or another service; support for one operation does not establish support for another. Distinguish Xcode, Transporter application/CLI, altool and API operations by the specific documented contract rather than treating them as interchangeable.

On 27 September 2026, Apple's [Upload builds](https://developer.apple.com/help/app-store-connect/manage-builds/upload-builds) page lists altool and Transporter among upload options. This supports neither blanket removal of altool nor reuse of historical examples without verification. Recheck supported versions, platform/artifact requirements, authentication methods and the exact operation at the time of project work. Do not copy credentials or flags from a historical tutorial. If current official pages or installed help disagree, document the discrepancy and leave the disputed command unexecuted until resolved.

Establish the intended app/team/destination and available operation-specific authority from supplied non-secret evidence. Do not access Keychain, create API keys, log in, change roles/accounts, alter signing or fetch credentials to complete a plan. Missing access is a named blocker, not permission to change accounts. Use the project's approved secret-handling mechanism only within separately authorised execution; never embed authentication material in a reusable example.

Distinguish local preparation/validation, upload acceptance, server processing, TestFlight distribution, review submission and release. Evidence for one stage does not prove another. A successful upload does not establish publication or release readiness. Uploading itself transfers an artifact externally and requires applicable authority even if publication is not requested. This roadmap scope authorises neither uploads nor remote validation.

## Acceptance examples and boundaries

These are prose examples, not executable checks, fixtures or scripts:

- Trigger: a supplied recipe assumes an old altool invocation works. Expected action: identify its service and compare current official documentation with installed-version/help evidence before recommending the exact operation. No-action case: the installed contract or access is unknown; do not run the recipe, install tooling or claim upload support verified.
- Trigger: a requested tool resolves under a different developer toolchain than expected. Expected action: explain the mismatch and scoped configuration choices using supplied evidence. No-action case: switching toolchains or installing components is not authorised; preserve the existing host configuration.
- Trigger: an upload attempt's supplied output only reports receipt. Expected action: distinguish receipt from processing/distribution, retaining the delivery identity without exposing secrets. No-action case: account access is absent or prohibited; do not poll remotely, retry the upload or claim release success.
- Trigger: instruction-only roadmap work. Expected action: save this reference and the existing SwiftUI route. No-action case: do not discover live tools, author checks, run builds, invoke validation or upload artifacts.

Report saved guidance separately from observed operations and unverified project behavior. Name which documentation, supplied output or local evidence supports a conclusion; web documentation is not proof of installed availability. No named iOS project, actual tool versions, artifact or operation-specific access was supplied for this guidance change, so command compatibility and operational outcomes remain unverified.

Preserve unrelated work and private data. No tests, checks, builds, evaluations, benchmarks, delegation, commits/push, installation, publication, spending or account changes. Keep installed caches and QMD indexes unchanged, and cloud synchronization, university RAG, training and background automation inactive.

## Source basis

Original synthesis from roadmap item 025 and existing SwiftUI, architecture and release references. Apple's upload-builds documentation was consulted on 27 September 2026. No Xcode CLI, account, upload or runtime operation was performed to produce this guidance.
