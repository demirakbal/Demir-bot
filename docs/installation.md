# Local Codex installation and first discovery

This guide describes the current local Codex path. It does not install another browser/cloud plugin or authorize an installation by being read. See [support matrix](support-matrix.md) for optional tools and unverified client/runtime boundaries. The plugin needs no provider account for ordinary instruction use; actual provider operations have separate access requirements.

1. Open the authorized development checkout and inspect its AGENTS.md. Confirm `plugins/demir-bot-pilot/` is the intended source and both manifests identify `demir-bot-pilot`. Keep private profile/credentials outside the checkout. Cloning the repository alone does not register a marketplace.
2. Inspect the current host's plugin/marketplace help and configured sources. Confirm the selected marketplace entry points to this source rather than an older archive/cloud copy. This repository has no bundled marketplace definition in the inspected source; a new environment needs an actual supported marketplace source/entry before a selector can work. Do not invent that entry or treat another user's `personal` selector as universal.
3. For this already configured local environment, the observed supported selector is `demir-bot-pilot@personal`. Only when installation/refresh is authorized, the documented operation is:

   ```sh
   codex plugin add demir-bot-pilot@personal --json
   ```

   Other environments must use the actual selected marketplace. The locally inspected CLI accepts either `PLUGIN@MARKETPLACE` or `PLUGIN --marketplace MARKETPLACE`. Its marketplace-add operation accepts an actual local/Git marketplace source, not an arbitrary assertion that a plugin folder is one. Source registration can fetch/write configuration; it requires its own appropriate setup scope.
4. Inspect the installation response's identity, version and path. Compare the selected installed source with the canonical source when that inspection is requested; an install response alone does not prove byte equality. Use the optional installation doctor only under run authority; its saved source has not been run in this batch.
5. Start a fresh task or use the host's supported reload/discovery flow. Inspect the actual catalogue before claiming new instructions are loaded. Use the bundled namespaced coordinator and a simple supplied-content task only if runtime invocation is authorized; do not turn setup into an unrequested behavioral test campaign.

For missing discovery, distinguish absent registration, wrong source pointer, stale installed bytes, old active session and unsupported client. Preserve original errors with secrets redacted. Do not patch caches, install standalone duplicates, disable host protections or repeat a failing mutation unchanged. See the troubleshooting guide when available; the coordinator's plugin-routes and agent-profiles references own detailed fallback.

Private-profile setup is optional and separately authorized through the existing profile loader/onboarding reference. QMD/RTK, external providers and native project profile definitions are not installed by this command. Four `.codex/agents` definitions belong to the checkout, not the plugin package; all four profiles were exposed in the local Codex session; no worker was dispatched. Cloud sync/RAG/training/background services remain deferred.

Evidence: local CLI help for plugin/add/marketplace/marketplace-add was inspected on 16 October 2026; help completed while reporting it could not create PATH aliases under the current permissions. No aliases or permissions were repaired. A later authorized refresh installed version 0.1.1 with all 220 package files matching canonical source. The existing QMD collection was refreshed to 162 files with no pending embeddings. These are installation/indexing observations; a fresh session must load the latest instructions, and runtime invocation remains unverified.
