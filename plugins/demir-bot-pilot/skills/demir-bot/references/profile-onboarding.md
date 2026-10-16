# Minimal private-profile onboarding

Use only when the user requests profile setup or a specific persistent preference change. Follow [profile-loading.md](profile-loading.md) for directory resolution, precedence, selected-file loading and missing-profile fallback. Setup is optional: supplied task facts and provisional tone work without any profile. Do not create a profile, copy another user's facts or change a personal record merely because this template exists.

## Prepare the user's exact scope

Confirm the intended private directory from the existing loader convention or explicit user destination. Keep it outside the plugin, repository, QMD collection and cloud exports. Use owner-only directory/file permissions on the supported local filesystem; do not promise encryption or isolation from the host/account. Inspect an existing target before writing and merge only approved fields; never replace a profile with this template. Ordinary source installation is separate from private-profile creation.

Start with only the requested `preferences.md`; create other files only when actual approved information needs an owner. Do not require a name, employer, contact address, biography, API key or complete task history. The synthetic formats below are examples, not approved facts or defaults for another user.

```markdown
# Preferences
- Approved preference: <exact requested behavior>
- Scope: <project/channel/personal and relevant exceptions>
- Decision: <date or non-sensitive approval reference>
```

For explicitly requested project-location setup, keep the parent root and Git checkout distinct in `local-setup.md`:

```markdown
# Local setup
- Project root: <approved absolute parent directory>
- Git checkout: <approved absolute repository directory>
- Plugin development source: <approved plugin source directory>
- Roadmap source: <approved canonical roadmap directory/file>
- Deferred operations: <only the user's actual deferrals>
```

Do not fill placeholders from a guessed home directory, another user's installation or a filename. A directory's existence does not establish it is the canonical source; use the actual user's decision and inspect the selected path when relevant. Personal claims belong in `facts.md` only when approved for reuse; channel examples belong in the relevant tone file. Projects/capabilities remain selected scoped pointers/evidence, not a duplicate transcript or secret store.

## Correct, withdraw and recover

Reuse capability-maintenance.md's canonical inspect/revise/forget/rollback contract. Preserve a private scoped pre-edit version for authorized ordinary changes where permitted, without copying unrelated facts. A request to erase a rule must not create a new backup containing it by default. Keep backup locators/retention in their existing private owner. Source rollback, installed-cache refresh, index removal and cloud deletion are different operations with separate evidence.

Acceptance example: a user approves one project-specific brevity preference; save that rule at its private owner without inventing a biography or overwriting email tone. Missing/inaccessible profiles fall back to current supplied facts and report material gaps. No-action case: plugin installation or a one-time response correction does not silently create a persistent profile. This item saves synthetic onboarding guidance only; no private directory, personal preference, backup, account or environment setting was changed.
