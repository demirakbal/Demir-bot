# Written-only installation lifecycle checks

Status: **NOT RUN**, 16 October 2026. Demir authorized writing checks only; no test/build execution, provider operation, installation/uninstallation or index refresh is authorized. The source suite `test_installation_lifecycle.py` uses synthetic temporary plugin trees and imports local doctor/fingerprint helpers only when explicitly executed later. It never invokes Codex, QMD, a subprocess, model or provider. Importing the test file is execution too; do not import it as a syntax check.

## Offline source/cache contracts

Fifteen written cases cover equal trees, source additions, changed content despite unchanged version, extra stale files, snapshot restoration, absent installed tree, missing optional providers, an external private sibling, symlink rejection, duplicate manifest keys, portable identity mismatch, supplied-index evidence limits and explicit upstream file selection. They exercise inventory/comparison boundaries, not a real host installer. Synthetic copies cannot prove registration, fresh-task discovery, account isolation or uninstall behavior. Temp fixtures contain no real profiles or credentials.

## Real host lifecycle scenarios — prepared, blocked pending isolated target

Use the actual supported host operations only after confirming an isolated target and the necessary run/install/remove/rollback authority. Do not invent a host-isolation flag or run against the user's active registration as a fixture. Preserve the actual source/marketplace pointer, prior installed version and private-profile state; record only sanitized locators/snapshots outside the package. Stop before any operation whose supported isolation is unclear.

| Scenario | Required observation on the selected host | Recovery/containment |
|---|---|---|
| Fresh install | Correct identity/version/path and new-session catalogue exposes the expected skills | Remove only the test registration/resources under explicit cleanup scope. |
| Upgrade | Same identity, intended changed files and fresh-session behavior; no duplicate registration | Preserve prior usable artifact/source and supported reinstall path. |
| Stale cache | Same version but source/cache differ; refresh updates only selected installation | Do not patch cache directly or assume restart repairs bytes. |
| Rollback | Selected prior artifact installs/discovers correctly while later unrelated work remains | Distinguish source, installed, profile and index rollback. |
| Uninstall | Exact test registration removed from the intended client; source/private profile retained as expected | No directory-wide deletion or cloud-definition removal. |
| Optional tools absent | Ordinary skill use gives a useful fallback and no implicit install/authentication | No provider calls or invented availability. |
| Profile isolation | Synthetic user A/B/no-profile tasks do not load another profile or export it | Use synthetic profiles only; never inspect actual private biography/credentials. |

Every real scenario remains NOT RUN. Evidence must name exact host/OS/CLI, source/artifact, operation, result, discovery state and retained resources; do not convert source equality into runtime acceptance. External effects and destructive cleanup remain separately scoped. A future bounded run should preserve failures and return results before any unrequested fix/rerun.
