# Conflicts and reversible recovery

Read only the relevant case. Establish current state, authorization and a recovery point before mutation. Do not run these commands as a checklist or use recovery as permission to discard unrelated work. After each authorized step inspect its actual result before continuing.

## Preserve before integrating or aborting

Record current HEAD, branch, upstream and relevant target commit IDs. A named backup branch keeps committed history reachable. Preserve staged and unstaged changes separately, plus relevant untracked files, in an owner-only location outside Git and QMD. A plain diff omits untracked files and needs binary-capable handling for binaries. Do not copy a whole home directory or credentials into a backup merely for convenience.

When a stash is appropriate and authorized, inspect its scope and existing stashes first. A path-scoped `git stash push -m <label> -- <paths>` changes both worktree and index; understand mixed staged hunks before using it. `-u` also captures untracked files, `-a` includes ignored files, so neither is a blanket default. Stashes are Git objects, not secure private storage. Record the exact new stash identity and contents. Prefer `git stash apply <saved-stash>` to keep the recovery copy; use `--index` only when restoring staging is intended. Resolve conflicts without blindly reapplying or dropping. Delete only that stash after confirming restoration and applicable cleanup authority.

## Merge or rebase conflicts

Use `git status`, `git diff --name-only --diff-filter=U`, and relevant diffs. Read both commits, the merge base and nearby contracts/callers. Where present, index stages `:1:path`, `:2:path`, `:3:path` expose base/ours/theirs; deleted/addition cases may lack a stage. During rebase “ours” is the rebased series/upstream and “theirs” is the commit being replayed. Never use blanket ours/theirs resolution from the labels alone.

Preserve compatible intent on both sides. A mechanically clean merge is not proof of correct behavior. For contradictory requirements (such as removal of a feature versus a new dependency on it, different API/data contracts, or incompatible business rules), explain the concrete alternatives and ask the owner which behavior should win. Continue independent work while that decision is pending. Do not invent project intent, silently keep both contradictory implementations, regenerate lockfiles, or run tests/builds without scope.

Handle rename/delete, binary, generated-file and submodule conflicts explicitly; do not concatenate binaries or invent submodule commits. Stage only resolved paths, inspect the resolution and remaining unmerged entries, then continue the specific operation only if its commit/history effect is authorized. Report functional behavior untested when it is. A stash-apply conflict is not a merge/rebase to abort blindly; retain the stash and recover only the changes introduced by that application, preserving intervening work.

## Interrupted operations

Read status and use Git-resolved metadata paths to identify merge, rebase, cherry-pick, revert or am state. Determine whether an editor or another Git process is still active. Do not delete locks or sequencer metadata as a first response; a lock can protect another live process. Remove a stale lock only after evidence it is stale and scoped recovery authorization.

| State | Scoped continuation or recovery |
|---|---|
| Merge | Resolve and stage, then `git merge --continue`; or `git merge --abort` when abandoning it is authorized. Abort may not reconstruct earlier dirty edits; preserve those and any new resolution work first. |
| Rebase | Inspect the current replayed commit; resolve and `git rebase --continue`, or `git rebase --abort` to return to the starting branch. `--skip` drops a patch and needs evidence it is redundant or explicit discard authority. `--quit` stops bookkeeping but leaves current HEAD/index/worktree; it is not rollback. |
| Cherry-pick, revert, am | Use the matching command's supported `--continue` or `--abort` for the detected operation; inspect patch, affected commits and dirty state first. Do not use a merge abort for another sequencer. |
| Stash/autostash restoration failed | Retain recovery entry; inspect applied versus conflicting changes and staging. Do not repeatedly apply or discard it. |

Do not start another pull/rebase/merge until the existing operation is resolved or deliberately preserved for handoff. If the original intent or owner is unknown, describe state and ask for that decision rather than aborting someone else's work.

## Divergence and rejected pushes

Classify the error: non-fast-forward, branch protection, authentication/authorization, server hook/content rule, missing repository/ref, or transport failure. Fetch the intended ref when authorized, inspect both histories and any forced remote update, then choose the integration strategy in SKILL.md. A non-fast-forward rejection is not permission to force. Do not replay an old upstream's removed commits after a remote rewrite without understanding why they were removed.

An explicitly approved shared-history rewrite requires preserved old/new tips, exact destination and knowledge of whose work changes. Use an explicit expected old remote SHA with a narrow refspec: `git push --force-with-lease=refs/heads/<branch>:<reviewed-old-sha> <remote> <new-sha>:refs/heads/<branch>`. The lease is a race guard, not permission or a backup; it can still replace reviewed commits intentionally. If the lease fails, inspect the new remote state and reconcile scope; do not refresh the expectation blindly. Never fall back to `--force` or a `+` refspec to defeat the guard.

After a timeout or uncertain push/PR/merge outcome, read the exact remote ref or PR state through supported access before retrying. Compare actual commit IDs and destination, not a success-looking message alone. If readback is unavailable, report the outcome unknown and stop duplicate submissions. Permission denial does not authorize switching identities, broadening scopes, creating a fork or bypassing protection.

## Detached HEAD and missing commits

A detached HEAD is normal in some managed worktrees/checkouts. Inspect HEAD and recent reflog before switching away. If retaining new commits is authorized, create a named branch at the observed commit (`git branch <recovery-name> <sha>`); switch only when appropriate to the managed environment and dirty state. Do not force an occupied branch or assume detached means lost work.

For an accidentally moved branch, inspect a bounded `git reflog` and `git show <candidate-sha>`, then create a recovery branch at the identified commit before considering movement of the original branch. Reflogs are local, can expire and do not recover arbitrary unstaged/untracked content. Consult known private backups/editor history where applicable; do not promise recovery from a destructive reset or clean. Do not run garbage collection/reflog expiry during recovery.

## Undo the smallest thing

- Mistaken staging: restore only the affected index paths/hunks, for example `git restore --staged -- <path>` against an existing HEAD. This leaves worktree content but resets that path's staging to HEAD; preserve any earlier staged hunks. An unborn branch has no HEAD: use an appropriate index-only removal after inspecting scope, never delete the working file.
- Unwanted committed change on shared history: an authorized `git revert <sha>` records an inverse commit without rewriting old history. Inspect dependencies and resolve conflicts; reverting a merge needs the intended mainline parent and can affect later remerges. It is not a universal rollback of deployment or data.
- Local amend/rebase/reset: use only applicable history-editing authorization and a preserved tip plus dirty-work backup. Reset modes affect branch, index and worktree differently. Never offer `reset --hard`, `clean -fdx`, forced checkout, branch deletion or worktree removal as a default repair.
- Restoring a backup: compare current content first, restore only affected changes and preserve later edits. Local recovery cannot undo remote publication or recall copied secrets. Handle an actual exposure through authorized privacy/security action, not automatic history erasure or credential revocation.

## Authentication and permission failures

Confirm sanitized remote host/owner/repository and whether the failed path uses Git HTTPS, SSH, GitHub CLI or a connector. Their credentials and permissions can differ. Use existing operation evidence; for requested diagnosis `gh auth status --hostname <host>` can inspect CLI status without `--show-token`. Never print tokens, private keys, credential-helper output, environment dumps or raw credential-bearing URLs. Do not assume a valid account can write this repository or satisfy organization SSO and branch rules.

Use the provider's supported authentication flow only when authorized; do not request a pasted secret in chat, change global identity, disable TLS/SSH host checks, widen token scopes or swap accounts as an automatic retry. Explain the concrete missing access and useful next step, preserving local work. Distinguish an unavailable tool, failed authentication, repository authorization, policy rejection and unknown network outcome. Stop repeated identical failures until evidence or authorization changes.
