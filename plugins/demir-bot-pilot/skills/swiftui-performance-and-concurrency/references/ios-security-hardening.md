# iOS security boundaries

Original roadmap item 017 guidance. Add platform-specific questions to the existing workflows, not another scanner, threat-model framework or security specialist. Trigger only for requested hardening or a source-backed concern in an authorised iOS change. A small unrelated edit does not trigger an audit.

## Reuse existing owners

Follow the coordinator's existing [security and privacy routes](../../demir-bot/references/routes.md#specialist-routes). Requested repository audits use codex-security:security-scan; requested change audits use codex-security:security-diff-scan. Existing findings use the relevant triage/fix/verification skill only within its authorised scope. Structural hardening proposals can use codex-security:propose-security-hardening when requested. Resolve actual availability and prerequisites before claiming any specialist workflow ran. Under a no-scan/no-test scope, retain bounded source guidance and report the limitation rather than executing those workflows.

Reuse [privacy-review](../../privacy-review/SKILL.md) for collection, sharing, retention and deletion. Reuse [Keychain/CryptoKit](keychain-cryptokit.md), [navigation](swiftui-navigation.md), [privacy manifests](../../privacy-review/references/privacy-manifests.md), [package management](spm-dependency-management.md) and [architecture](../../architecture-review/references/ios-architecture-patterns.md) for their established contracts. Do not duplicate cryptographic recipes, URL parsing, SDK declarations or severity systems here.

## Bound the evidence

Identify the named project, supported OS/SDK/toolchain, relevant target and requested security property. Inspect affected source/configuration and supplied redacted evidence only. Trace the entry point, caller-controlled input, trust boundary, sensitive operation and existing enforcement. Distinguish a confirmed source pattern, plausible exposure and demonstrated exploit; neither a filename nor an entitlement alone proves a vulnerability.

Missing app source or effective signing/runtime evidence stays explicit. Do not access credentials, Keychain contents, private databases, accounts or network services to manufacture proof. Select only the relevant dimensions below.

## Transport

Trace the actual networking API, endpoints, redirects and authentication-challenge handling. Prefer supported secure transport and platform trust evaluation; inspect custom delegates for indiscriminate acceptance of certificates or bypassed identity checks. Do not repair a connection error by disabling trust evaluation or broadening transport exceptions.

Apple's [ATS guidance](https://developer.apple.com/documentation/security/preventing-insecure-network-connections) distinguishes URL Loading System protection from lower-level networking and recommends narrowly scoped exceptions only when necessary. Inspect relevant Info.plist exceptions and affected call sites, including embedded web content where applicable. ATS configuration alone is not proof that every connection is protected. Do not run network probes or adopt documentation's diagnostic commands under this scope.

Keep credentials and sensitive fields out of URLs/logs and review whether redirects or cross-origin requests can disclose them. Use the existing privacy workflow for the concrete data flow. Do not add certificate pinning universally: any justified pinning design needs supported APIs, ownership, rotation/recovery and an explicit availability trade-off; it must not replace ordinary trust validation.

## Storage and data exposure

Use the Keychain reference for secrets and key lifecycle. For other sensitive data, inspect the intended file/store location, configured protection, access timing and copies created in caches, temporary files, exports, logs or backups. Check current official platform documentation for the actual file-protection APIs before prescribing a class. A sandbox, encrypted database or privacy manifest does not prove that derived copies are protected or retained appropriately.

Consider relevant screen snapshots, clipboard/export paths and diagnostic output only when the supplied flow exposes sensitive content. Preserve product requirements and accessibility; do not blanket-disable useful sharing or claim guaranteed erasure of memory/backups. Reuse persistence recovery guidance rather than opening stores or deleting files. Keep server authorisation separate from local UI locks and biometric presentation.

## Entitlements and effective authority

Map each implicated capability to its target and legitimate consumer. Inspect the existing configuration and supplied signing evidence for unnecessary breadth, especially shared containers, Keychain groups and associated domains. Apple's [App Groups entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.application-groups) documents shared-container and communication capabilities; the group name is not an application-level authorisation rule.

Distinguish requested source entitlements from the effective signed product and provisioning state. Do not claim a production entitlement is active from a source plist alone. Propose the smallest supported scope without changing teams, certificates, provisioning, account permissions or capabilities incidentally. Development/debug settings need release-context evidence before they become a release finding.

## Interprocess communication and extensions

Identify the mechanism actually present: app extensions, shared containers, incoming URLs, document/file handoffs, web-to-native bridges or supported IPC APIs. Do not prescribe macOS-specific mechanisms to an iOS target without checking platform support. Reuse navigation's link-validation rules for URL entry points.

Treat incoming messages, shared-file contents and extension inputs according to their trust boundary. Validate operation names, types, lengths, file references and allowable destinations before sensitive work. Avoid interpreting untrusted data as commands or executable content. A claimed sender identifier or a custom URL scheme is not authenticated caller identity; use supported identity/authorisation mechanisms where required and keep server permissions enforced independently.

For shared state, identify all writers, access scope and consistency/coordination requirements. Do not assume common group membership guarantees valid data or safe concurrent writes. Limit the receiving component's authority to its actual purpose; avoid exposing a broad privileged operation merely because an extension needs one narrow action. For a web bridge, inspect allowed origins/frames and message contracts rather than trusting arbitrary page content.

## Acceptance and reporting

Illustrative acceptance examples, not executable checks:

- **Transport:** source accepts every server-trust challenge. Identify the affected path and smallest platform-trust correction within authorised scope; do not probe a server or claim an intercepted session.
- **Entitlement/IPC:** an extension reads a shared file and performs an action from its contents without validation. Trace writer access, parsing and the sensitive action; distinguish the source concern from unverified exploitability and avoid changing group membership without scope.
- **Storage:** a supplied flow writes a sensitive export to a persistent cache. Reuse privacy/storage ownership to examine purpose, protection and retention; do not read or remove the actual export.
- **No-action case:** no relevant boundary changes or demonstrated gaps are present. Retain the existing design and specialist routes; do not create a new audit or universal hardening checklist for the app.

Report source evidence, rationale, saved guidance/code and unverified runtime claims separately. A scoped inspection is not a completed Codex Security scan, penetration test, compliance certification or proof of exploit prevention.

Source basis: official Apple resources linked above and existing bundled guidance, consulted 27 September 2026. No scanner, exploit, code sample or check suite imported.

Preserve instruction-only restrictions: no security scans, checks/fixtures, tests, builds, apps/simulators, network probes, evaluations, benchmarks, delegation, commits, installations, package operations, index refreshes, cache deletion or background activity. Do not access credentials/accounts, modify entitlements/containers, enable sync or open/copy/migrate real databases. Leave private data, installed plugin, cloud skill sync, university RAG and training unchanged.
