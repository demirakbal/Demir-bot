# Working on Demir Bot

This checkout is the development source for the Demir Bot plugin. Edit `plugins/demir-bot-pilot/`, not installed plugin caches or archived standalone skill packages. Resolve the canonical parent project root, this Git checkout and the roadmap directory from the active private profile's local-setup.md through the coordinator's profile-loading.md; keep absolute local paths in that existing configuration. Roadmap work uses the configured master Markdown source and its PDF companion. Read only the relevant skill and references. Preserve the plugin identity and its namespaced routes.

Implement requested work without automatically running or writing tests, linters, builds, browser checks or evaluation loops. Explicit testing requests remain scoped. Do not create unrelated reports or expand a small change into a refactor.

The coordinator's `plugins/demir-bot-pilot/skills/demir-bot/references/execution-scope.md` owns the detailed execution and handoff contract. Apply its relevant scope to supported Work/Codex/worker handoffs; repository instructions do not automatically propagate to another host. Complete an explicitly assigned implementation chain without routine reconfirmation, preserve item-level progress reporting, and stop when the selected scope is finished or cannot progress. A handoff/profile does not itself authorize spawning workers, tests or external actions.

Keep the private user profile, credentials, account history, messages, course source documents, runtime queues, host-specific private configuration, QMD databases and rollback backups outside Git. The generic project-scoped `.codex/agents/*.toml` role definitions are development source, not private host configuration; they contain no personal profile, credentials or account locators. Never copy files into this checkout merely because a reference points to them. Inspect staged changes before committing or pushing.

Preserve upstream licence notices and adaptation provenance. Do not claim public redistribution rights or execution verification without evidence.

Use focused commits/branches and preserve other work. Do not force-push or merge without applicable authorization. Skill changes do not automatically update the installed cache: use the supported local-plugin update flow when requested and report whether the installed version was refreshed.

Cloud skill synchronization, background automation, university RAG and model training remain inactive unless explicitly authorized for the current scope. External providers need their own available tools, authentication and action approval.
