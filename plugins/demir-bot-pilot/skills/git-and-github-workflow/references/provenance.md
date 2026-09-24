# Sources and adaptation decisions

Reviewed 2026-09-21 for the user-requested scoped Git/GitHub skill. The privately supplied “Demir Bot - Project context and remaining work” supplied roadmap context (especially Git scope and the next LinkedIn fact-approval item). It is not bundled, indexed or treated as independent action authorization. The current user request and repository AGENTS.md control scope.

## Existing capabilities assessed

Reused the pilot's coordinator, capability-maintenance, skill-sync, context-efficiency, privacy-review and release-readiness-and-observability guidance. These remain the owners of maintenance, data handling and release decisions; this skill adds version-control decisions rather than duplicating those workflows. Git/GitHub CLI/connectors remain optional existing tools, not newly installed dependencies.

Inspected installed Superpowers 6.4.1 candidates and its root MIT license (Copyright (c) 2025 Jesse Vincent):

| Candidate | Reviewed SHA-256 | Decision |
|---|---|---|
| [using-git-worktrees](https://github.com/obra/superpowers/blob/main/skills/using-git-worktrees/SKILL.md) | `8cfb86f121269e8f7f12361e6795c4f6738828340e28964c9229d365666c9edd` | Adapt existing-worktree/submodule awareness, supported native worktree preference and preservation of dirty work. Do not import automatic setup/tests or an incidental ignore-file commit. |
| [finishing-a-development-branch](https://github.com/obra/superpowers/blob/main/skills/finishing-a-development-branch/SKILL.md) | `8db5a922b242dd4e1bf824cb91c13b3e8d8e8a86d6ceaf7f0774eb9cce909d65` | Adapt distinct local integration, PR and retained-work outcomes. Do not import mandatory test gate, fixed approval menu, bare pull or automatic cleanup. Worktree ownership is not inferred solely from directory names. |

The URLs identify upstream sources; hashes identify the installed text actually reviewed, not a claim that upstream main was checked. Retained the complete root MIT notice as `../LICENSE.upstream` (source SHA-256 `a37e0e9697144819e1d965176ac4ae5bc3fa02d11e7812036bbcadf6dafe2400`). No upstream scripts/hooks or runtime dependencies copied. Original task-specific wording combines these limited ideas with official command semantics. The MIT notice covers the adapted upstream material; it is not a blanket license or public-distribution certification for the whole pilot.

## Current official documentation inspected

Read the live official pages on the review date via the available web tool; Firecrawl CLI was unavailable on this host. Pages are mutable, so this records an access date and URL, not an immutable document version. Git pages showed versioned manual histories (including 2.55.0 on pull); do not assume that version is installed on a future host. Consult installed command help/current official docs for consequential version differences.

| Official source | Guidance used |
|---|---|
| [git-status](https://git-scm.com/docs/git-status), [git-switch](https://git-scm.com/docs/git-switch), [git-restore](https://git-scm.com/docs/git-restore) | Working/index state, branch creation versus forced reset, and index-only restoration. |
| [git-pull](https://git-scm.com/docs/git-pull) | Fetch plus integration; explicit fast-forward, merge and rebase strategies rather than relying on changing defaults. |
| [git-push](https://git-scm.com/docs/git-push) | Explicit refspecs, non-fast-forward protection and expected-SHA force-with-lease race guard. |
| [git-merge](https://git-scm.com/docs/git-merge) | Integration/continue/abort semantics, dirty-work limitations and no-commit versus fast-forward distinction. |
| [git-rebase](https://git-scm.com/docs/git-rebase) | Commit replay, continue/abort/skip/quit and reversed ours/theirs meaning. |
| [git-stash](https://git-scm.com/docs/git-stash), [git-reflog](https://git-scm.com/docs/git-reflog) | Scoped stash preservation/apply, optional index restoration, local expiring recovery history. |
| [GitHub conflict resolution](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/resolving-a-merge-conflict-using-the-command-line) | Competing edits and removed-file conflicts; choosing intended content. |
| [GitHub rejected pushes](https://docs.github.com/en/get-started/using-git/dealing-with-non-fast-forward-errors) | Inspect/fetch/integrate instead of overwriting remote history. |
| [GitHub SSH permission failures](https://docs.github.com/en/authentication/troubleshooting-ssh/error-permission-denied-publickey), [gh auth status](https://cli.github.com/manual/gh_auth_status) | Diagnose the actual credential path/host; separate authentication from repository permissions; no token display. |
| [gh pr create](https://cli.github.com/manual/gh_pr_create) | Explicit head/base/body, implicit push/fork behavior and non-read-only dry-run caveat. |
| [gh pr merge](https://cli.github.com/manual/gh_pr_merge) | Head-match guard, merge strategy, queue/auto-merge behavior and avoiding admin bypass/automatic deletion. |

Official documentation was consulted for semantics, not copied wholesale or relicensed. Authorization, no-repeat-permission behavior, project-intent clarification, no automatic tests and private rollback boundaries are the user's local adaptations. No commands in the workflow were exercised as behavioral scenarios. Saving and inspecting this skill, refreshing QMD and reinstalling the plugin establish only those particular maintenance outcomes; they do not establish Git/GitHub authentication, conflict-resolution correctness, retrieval quality or runtime reliability. Cloud synchronization remains deferred.
