---
name: git-and-github-workflow
description: Inspect and perform scoped Git and GitHub repository work, including branches, focused commits, synchronization, pull requests and recovery from conflicts or failed operations. Use for requested version-control work or a concrete Git blocker; ordinary code edits do not imply committing, pushing or merging.
---

# Git and GitHub workflow

Select this bundled skill as `demir-bot-pilot:git-and-github-workflow`. Use existing Git, GitHub CLI or available connector capabilities; this is guidance, not a new runtime or proof of account access. Follow repository AGENTS.md, the current request and existing session authorization. Do not run application tests, linters, builds, scanners or evaluations unless explicitly requested. Git state/diff inspection is distinct from application testing.

## Scope and authorization

Establish the requested operation, repository, branch/base, destination and relevant authorization from current context. Do not ask again for clearly granted permission. A material change of destination, content or effect needs a new decision; a retry of the same authorized operation does not, once its outcome and cause are understood.

| Operation | Boundary |
|---|---|
| Local status, history and diff reads | Inspect only relevant state; redact credentials and private content before output. A review does not authorize fixing it. |
| Fetch or remote/PR reads | Within requested remote inspection/synchronization using available access. Fetch downloads objects and updates local tracking refs; it does not integrate the working branch or grant push permission. Do not fetch merely because ordinary editing began. |
| Local branch creation, edits and focused staging | Within requested implementation/workflow scope, preserving unrelated edits and index state. A request to implement guidance only does not authorize practicing the operations. |
| Commit, merge, rebase or pull | Require applicable task scope for recording/integrating history. Ordinary implementation is not an instruction to commit. Explicitly requested integration can authorize its routine local steps, but shared-history rewriting remains separate. |
| Push, PR creation/update, comments/reviews, GitHub merge | Remote writes need authorization for the repository, destination and intended changes. A PR request can include necessary branch publication when the destination is clear; it does not authorize merging, publishing a release or arbitrary comments. A commit request alone does not authorize pushing. |
| Discard, reset, branch/worktree deletion, amend/rebase of shared commits, force push | Require explicit applicable authorization for the affected work/history and effect, with a concrete recovery point. A generic “fix the push” is insufficient. Prepare the scoped result/options before asking; reuse prior exact authorization. |

Respect branch protection, required reviews, merge queues and release gates. Do not bypass hooks, signing, secret protection or required CI; inspect known hooks/workflows before a requested mutation when they can trigger forbidden tests or deployment. If a required side effect conflicts with scope, report the specific gate and stop that operation. Never silently disable it. Remote branch cleanup, auto-merge, reviewer requests, releases, permissions and deployment are separate effects, not default completion steps.

## Inspect before changing state

Use the smallest useful subset, with raw/porcelain output where exact state matters:

```sh
git rev-parse --show-toplevel --git-dir --git-common-dir
git rev-parse --show-superproject-working-tree
git status --short --branch
git branch --show-current
git branch -vv
git worktree list --porcelain
git diff --no-ext-diff --no-textconv --stat
git diff --cached --no-ext-diff --no-textconv --stat
git ls-files --others --exclude-standard
```

Inspect relevant full working-tree and staged diffs, not just statistics. Record pre-existing staged/unstaged/untracked work and current HEAD. Handle an unborn branch (no commit yet) separately from detached HEAD (a commit but no branch). Read `git status` for an interrupted operation before starting another. Git metadata may be outside `.git/` in linked worktrees; use `git rev-parse --git-path <name>` for operation metadata rather than assuming a directory layout.

Inspect configured fetch AND push destinations and relevant upstream/push settings locally; avoid emitting credential-bearing URLs or broad config dumps. Verify the host, repository owner, push URLs/refspecs and upstream rather than assuming `origin`, `main`, or that the upstream is the intended PR base. Multiple push URLs can send data to multiple destinations. Resolve fork head versus base explicitly. Missing upstream is a state to resolve, not permission to set it arbitrarily. Tracking refs describe the last fetch, not necessarily current remote state.

## Preserve work and choose a branch

Use project branch conventions; otherwise prefer `codex/<focused-name>` for new work. Select the intended starting commit before `git switch -c <branch> <start>`. Inspect dirty state and worktree ownership before switching. Do not force-switch or recreate an existing branch with `-C` to bypass a collision. Reuse an already suitable worktree; use the supported native worktree capability when isolation is useful and authorized. Do not install dependencies, run baseline tests or delete worktrees as incidental setup/cleanup.

Keep unrelated files and hunks in place. For operations requiring a clean state, prefer isolation or a scoped private backup over silently stashing someone else's work. See [recovery.md](references/recovery.md) before stashing, aborting or rewriting. A branch pointer preserves commits only; it does not back up uncommitted or untracked files. Keep rollback copies outside the public repository and indexed skill collection, with restricted permissions.

## Focused staging and commits

Inspect the actual patch and privacy boundary before staging. Use explicit paths (`git add -- <paths>`) or selected hunks (`git add -p -- <paths>`). Never default to `git add .`, `git add -A`, `git commit -a`, or force-adding ignored files. For mixed ownership within one file, stage only task hunks. Preserve pre-existing staged content; if a commit would include it, use suitable isolation or a carefully preserved index plan rather than silently unstaging or committing it.

Before an authorized commit inspect the entire staged patch and file list. Exclude credentials, private profiles, correspondence, course evidence, runtime queues, local config, indexes and backups. Ignore rules do not protect files already tracked. Check identity/signing settings without inventing an author or changing global configuration. Use a message explaining the concrete change and why, following project conventions. Inspect the resulting commit and remaining status; report its actual hash. Do not claim tests passed when only the patch was read. A failed hook/signing step is a blocker to diagnose, not permission to bypass controls or automatically fix unrelated code.

## Fetch and integration strategy

For authorized synchronization, fetch the confirmed remote/branch first, inspect the result and unexpected forced updates, then compare the intended refs. Do not automatically prune, fetch all remotes, or change persistent pull policy. Where the confirmed upstream exists, `git rev-list --left-right --count HEAD...@{upstream}` reports local-only then upstream-only commits; a bounded `git log --left-right --graph --oneline HEAD...@{upstream}` explains them. No upstream or common ancestor requires resolving the intended relationship before integration.

| State | Decision |
|---|---|
| Equal | No integration needed. |
| Behind only | If updating is authorized and edits are protected, fast-forward to the inspected target: `git merge --ff-only <target>`. An explicitly chosen `git pull --ff-only <remote> <branch>` fetches again and may see newer content. |
| Ahead only | Inspect outgoing commits; push only within remote-write scope. |
| Diverged | Explain the commits on both sides and use project policy: merge preserves the existing graph; rebase rewrites local commits onto the target. Choose only an authorized strategy; do not guess when shared-history or project intent is unclear. |

Never use a bare automatic pull as a repair recipe. Use explicit per-command strategy instead of changing global settings. Before merge/rebase preserve relevant refs and dirty work. Merges may create a commit; `--no-commit` alone does not stop a fast-forward. If review before any integration commit is required, select appropriate `--no-ff --no-commit` behavior deliberately. Rebase unpublished local work only within authorized history-editing scope; published/shared commits require explicit rewrite approval and coordination. Do not paper over unrelated histories with `--allow-unrelated-histories`.

## Pushes, pull requests and merges

Before a push confirm destination visibility, exact outgoing refs/commits and authorized content. Review the whole outgoing range, not only the latest diff: deleted secrets can remain in history. Stop if private material would be published; reuse privacy guidance for relevant handling. Prefer an explicit branch refspec such as `git push <remote> HEAD:refs/heads/<branch>`; add upstream tracking only intentionally. Avoid `--all`, `--mirror`, tags, deletion or force options as defaults. For rejection or uncertain network outcome use [recovery.md](references/recovery.md).

For an authorized PR, inspect existing PRs for the same head/base to avoid duplicates, repository templates and the final range. Prepare an accurate title/body with problem, change, actual evidence and remaining limitations. Specify repo/base/head explicitly with the available connector or `gh pr create --repo <owner/repo> --base <base> --head <head> --title <title> --body-file <file>`; add `--draft` when requested or appropriate to unfinished work. GitHub CLI can otherwise offer to push/fork; do not let that create unapproved remote effects. Even `gh pr create --dry-run` may push, so it is not a read-only preview. Keep body files outside Git when private and use safe literal text handling. Read back the created PR's URL, head/base and state; attach it through the Codex artifact tool when available. Creating a PR does not merge it.

For a requested merge, inspect the current PR head SHA, base, diff, review state, protection and existing required checks without triggering new runs. Respect the project's allowed merge/squash/rebase method. Use a supported head-match guard (for example `gh pr merge --match-head-commit <sha>`) to avoid merging an unreviewed revision; re-review if it changed. Do not use admin bypass. Queueing or enabling auto-merge is deferred execution and needs that scope; report queued versus merged accurately. Read back final state and merge SHA before claiming completion. Do not delete branches/worktrees automatically. Route deployment/release implications to the existing release specialist only when relevant and requested.

## Finish with evidence

Report saved changes, local commits, remote refs and PR state separately, only where actually observed. Identify preserved unrelated work, pending operations, blockers and unverified behavior. Stop after the requested result; no automatic tests, cleanups, reports, background watchers, cloud sync or new services. For source maintenance use the coordinator's existing [maintenance](../demir-bot/references/capability-maintenance.md) and [sync](../demir-bot/references/skill-sync.md) guidance. Consult [provenance.md](references/provenance.md) for assessed alternatives and official sources, and check current official docs/local supported options when version-specific details affect an operation.
