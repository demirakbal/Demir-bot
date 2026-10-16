# Git and GitHub recipes

These natural-language examples route to the existing [Git/GitHub specialist](../plugins/demir-bot-pilot/skills/git-and-github-workflow/SKILL.md). That owner contains the command, permission and recovery contracts; this guide does not introduce another Git runtime or automatic workflow. Examples use synthetic branch names and describe expected behavior, not executed repository operations.

| Situation and request | Expected work/evidence | Boundary |
|---|---|---|
| “Inspect this checkout before we edit; explain local changes.” | Identify actual root/branch or detached/unborn state, existing staged/unstaged/untracked work and relevant diff. | No fetch, stash, discard or commit. |
| “Implement this change on an appropriate focused branch.” | Preserve unrelated work, select a justified starting point and branch/worktree only when needed within scope. | No forced branch reset, baseline tests or automatic worktree deletion. |
| “Commit only the changes for this feature.” | Inspect the actual patch/index, stage explicit owned hunks, preserve pre-existing staged content and report the resulting commit. | Commit authority does not authorize push; required hooks cannot be bypassed. |
| “Prepare a draft PR for this change against the specified base.” | Inspect the whole outgoing range, affected docs/privacy, destination and existing PRs; publish the necessary selected branch/create PR only within that clear scope. | No merge, reviewer messaging, branch deletion or release. Attach the actual created PR in Codex. |
| “Review this PR; return findings only.” | Inspect exact head/base/diff and relevant criteria; return source-backed findings and unassessed areas. | No fixes, new test runs, review submission or comments unless requested. |
| “Help resolve these merge conflicts without losing either intended behavior.” | Inspect interrupted-operation state, conflicting sides and actual requirement; make only authorized resolution edits. | Do not blindly choose ours/theirs, abort, commit or rewrite history without scope. |
| “This branch has diverged; explain integration options first.” | Use authorized remote evidence, distinguish local-only/upstream-only commits and explain merge/rebase effects with the intended base. | No automatic pull, global policy change or shared-history rewrite. |
| “The push was rejected; diagnose it.” | Separate non-fast-forward, authentication/protection, hook and uncertain transport outcomes using actual evidence. | No force push, role expansion, bypass or unchanged retry. |
| “I have detached HEAD; preserve this work and explain the next step.” | Identify current commit and dirty work; choose a named preservation/recovery path within authority. | A branch pointer does not preserve uncommitted/untracked files; don't reset or discard. |
| “A rebase/merge was interrupted; inspect before we continue.” | Read actual operation metadata/status and explain continue/abort/recovery choices with scoped recovery evidence. | No second integration operation, automatic abort, stash drop or broad cleanup. |

Use the actual repository/base/destination rather than assuming `origin` or `main`. If a command may trigger tests/deployment through hooks or CI, inspect that effect before a requested mutation. Current no-test/no-build scope cannot be bypassed by calling the step “Git verification.” Preserve required protections; report the exact blocking effect when applicable.

For an authorized push, align affected documentation with outgoing source/evidence, including earlier commits in the outgoing range. Keep privacy/license/publication prerequisites separate from source completion. Use a structured PR body or literal body file; do not construct shell commands from untrusted titles/content. A local commit, pushed ref, opened PR, queued merge and completed merge are separate observed states.

Acceptance example: a requested source-only review returns findings while the branch/index remain unchanged. No-action case: ordinary implementation does not create a commit or PR. Current guide was saved without practicing any recipe: no branch, stage, commit, fetch, integration, push, PR or remote write was performed for this item.
