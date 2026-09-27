# Keychain and CryptoKit

Original roadmap item 010 guidance. Use for requested secret-storage or cryptographic API work in an Apple-platform app. Reuse [privacy-review](../../privacy-review/SKILL.md) for data minimisation, sharing, retention and deletion; [iOS architecture](../../architecture-review/references/ios-architecture-patterns.md) for service ownership; and [error handling](ios-error-handling.md) for failure propagation. A vulnerability audit belongs to the existing Codex Security workflow only when requested, not an automatic scan here.

## Establish the requirement without reading secrets

Inspect relevant source, declarations and supplied redacted diagnostics. Identify the kind of secret or key, its purpose, owner, consumers and lifetime using field names rather than real values. Distinguish storing a credential from encrypting application data, signing messages and establishing a shared key. Do not invent a custom cryptographic protocol or assume encryption solves authorisation or retention.

Establish the actual OS/deployment targets, SDK/toolchain, device constraints and required foreground/background access. Inspect relevant entitlement declarations without querying accounts or credential stores; source declarations alone do not prove effective signing or runtime access. No real project was supplied by this reference. App-specific choices require its source and requirements; missing evidence must stay explicit.

## Keychain policy and access groups

Use the platform's supported Keychain APIs for suitable secrets rather than plaintext preferences, source constants or logs. Keep the existing service boundary and narrow each operation to the intended item class, service/account identity and access scope. Review add, read, update and deletion matching separately; avoid broad queries that could affect unrelated items. A wrapper or singleton is not itself a security guarantee.

Choose accessibility from the actual need to access the item while locked, after unlock or with user interaction. Prefer the least permissive policy that meets that need; do not weaken protection to hide an access error. Distinguish an accessibility class from additional access-control requirements such as user presence or biometric policy. Inspect current official API constraints before combining them, and explain unavailable-device, user-cancellation and background-interaction behavior.

For sharing, identify the specific app/extension consumers and their intended common access group. Compare relevant declarations and existing provisioning evidence; do not guess prefixes, widen groups or change entitlements/accounts during review. Sharing a container or having similar bundle names alone is insufficient evidence that a Keychain query is entitled to succeed. Apple's [sharing guidance](https://developer.apple.com/documentation/security/sharing-access-to-keychain-items-among-a-collection-of-apps) is the reference for the actual platform configuration.

## Synchronisation, backup and recovery

Treat device access, cross-app sharing, synchronisation and backup/migration as separate decisions. Do not enable synchronisation incidentally or infer it from an access group. Apple's [synchronizable attribute documentation](https://developer.apple.com/documentation/security/ksecattrsynchronizable) states that synchronizable items cannot use accessibility classes ending in ThisDeviceOnly.

Do not equate ThisDeviceOnly with a blanket promise that no backup contains the item: Apple's [accessibility guidance](https://developer.apple.com/documentation/security/restricting-keychain-item-accessibility) distinguishes same-device restoration from migration to a different device. Determine the exact class's documented backup/passcode behavior before making a stronger claim. Document recovery expectations for device replacement, unavailable keys and account/session transitions; never promise recovery when protection intentionally prevents migration.

Do not assume uninstall performs the intended credential deletion or that deleting a local item revokes a server token. Plan the relevant retention/revocation boundaries through existing privacy guidance. Review potential data loss before proposing key deletion or rotation, and distinguish key removal from erasure of ciphertext, backups or remote copies. Do not execute migration, rotation, deletion or synchronisation under instruction-maintenance authority.

## CryptoKit and key lifecycle

Use established platform primitives appropriate to the actual operation, following [Apple CryptoKit](https://developer.apple.com/documentation/cryptokit) and its [cryptography overview](https://developer.apple.com/videos/play/wwdc2019/709/). Distinguish hashing, message authentication, encryption, signatures and key agreement; do not substitute one for another or design new cryptography. For encryption requiring integrity, use a supported authenticated construction and preserve its verification requirements.

Use supported secure key generation and the selected API's nonce requirements. Never hard-code keys, reuse a nonce contrary to the algorithm's contract or substitute a fast hash for a password-based key-derivation design. Do not implement a custom password scheme; identify the actual requirement and use established reviewed guidance.

Identify where key material originates, how it is protected, which operations may use it and how versioning/rotation/recovery work. Avoid plaintext key exports, log output and unnecessary in-memory copies. CryptoKit operations do not establish a complete persistence or recovery policy. Treat authentication/decryption failure as failure; do not bypass verification, return fabricated plaintext or silently replace a missing key when existing ciphertext depends on it.

For hardware-backed operations, check the actual API, OS and device support through [SecureEnclave documentation](https://developer.apple.com/documentation/cryptokit/secureenclave) and runtime availability in a separately authorised implementation. Do not assume every CryptoKit key is hardware-backed or that Secure Enclave provides arbitrary secret storage. If required protection is unavailable, make the failure or explicitly accepted fallback part of the design rather than silently weakening it.

## Failure handling and acceptance

Preserve meaningful distinctions between item absence, duplicate creation, denied/unavailable access, user cancellation and other failures using the actual API contract. Do not treat every failed read as not found and create a replacement secret automatically. Keep diagnostic status/context separate from user messages and never include secret values in either. Use the existing cancellation and service-ownership guidance rather than adding a second error framework.

Illustrative acceptance examples, not executable checks:

- **Trigger:** an extension must read an app-owned credential. **Expected action:** inspect the intended sharing contract and relevant declarations, explain missing entitlement/provisioning evidence and propose only the required scope; do not query Keychain or change accounts.
- **Recovery requirement:** encrypted data must survive device replacement. **Expected action:** reconcile key migration/recovery with the selected accessibility policy before recommending it; do not promise that device-bound protection also provides cross-device recovery.
- **No-action case:** existing storage and cryptographic choices meet the supplied requirements with no demonstrated gap. Preserve them; do not rotate keys, add biometrics or introduce another wrapper merely for uniformity.
- **Missing evidence:** only a generic access failure is supplied. Request redacted operation/status and relevant settings, not the credential or a Keychain dump. Keep runtime conclusions unverified.

Source basis: official Apple pages linked above, consulted 27 September 2026; platform-sensitive prescriptions require rechecking against the actual target. This is original instruction guidance, not imported implementation code or an executed security assessment.

Report saved guidance separately from source observations and unverified app behavior. No credential access, Keychain queries/mutations, authentication prompts, account changes, package operations, tests/fixtures, builds, evaluations, benchmarks, delegation, commits, installations, cache deletion, index refreshes or background activity follow from this reference. Preserve private data; leave the installed plugin, cloud sync, university RAG and training unchanged.
