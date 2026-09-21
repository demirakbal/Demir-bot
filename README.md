# Demir Bot

Demir Bot is an instruction-based personal assistant workflow for Codex. It selects relevant skills and available tools for coding, university work, research, writing and LinkedIn. The plugin bundles the coordinator and 20 specialist skills in one package.

It is not an always-running service, a trained model, or an account-access mechanism. Installing it does not install Gmail, Firecrawl, Higgsfield or other external plugins, authenticate accounts, or grant permission to send or publish.

## Repository layout

```text
plugins/demir-bot-pilot/
  .codex-plugin/plugin.json     Plugin manifest
  skills/
    demir-bot/                 Coordinator
    <skill-name>/
      SKILL.md                 Skill instructions (the skill's source)
      references/              Supporting guidance and provenance, where present
      agents/openai.yaml       Client metadata, where present
      LICENSE*                 Retained upstream notices, where present
AGENTS.md                      Instructions for working on this repository
RESOURCES.md                   Linked inventory of bundled reference resources
```

Most of the source is Markdown and YAML, not executable application code. The existing local publishing runtime, credentials and user records are deliberately not bundled. The `plugins/` directory can hold additional first-party plugins later; unrelated third-party packages should remain external dependencies.

## Included skills

| Skill | When to use it |
|---|---|
| [demir-bot](plugins/demir-bot-pilot/skills/demir-bot/SKILL.md) | Coordinate tasks, select specialists and preserve scope and user preferences. |
| [context-efficiency](plugins/demir-bot-pilot/skills/context-efficiency/SKILL.md) | Reuse evidence, read selectively and keep tool output focused. |
| [clarify-and-execute](plugins/demir-bot-pilot/skills/clarify-and-execute/SKILL.md) | Resolve material ambiguity through useful choices, then execute. |
| [requirements-and-traceability](plugins/demir-bot-pilot/skills/requirements-and-traceability/SKILL.md) | Define requirements, acceptance criteria and evidence links. |
| [architecture-review](plugins/demir-bot-pilot/skills/architecture-review/SKILL.md) | Examine boundaries, dependencies and architectural trade-offs. |
| [code-refactoring-refactor-clean](plugins/demir-bot-pilot/skills/code-refactoring-refactor-clean/SKILL.md) | Perform requested or concretely justified behavior-preserving refactoring. |
| [documentation-and-adrs](plugins/demir-bot-pilot/skills/documentation-and-adrs/SKILL.md) | Maintain requested documentation and architectural decisions. |
| [qa-and-test-evidence](plugins/demir-bot-pilot/skills/qa-and-test-evidence/SKILL.md) | Plan, write or run tests only within the explicitly requested scope. |
| [privacy-review](plugins/demir-bot-pilot/skills/privacy-review/SKILL.md) | Review collection, sharing, retention and reuse of personal information. |
| [demir-linkedin](plugins/demir-bot-pilot/skills/demir-linkedin/SKILL.md) | Research and draft posts, improve positioning and prepare networking actions. |
| [personal-writing](plugins/demir-bot-pilot/skills/personal-writing/SKILL.md) | Route writing to the relevant channel tone and approved facts. |
| [linkedin-tone](plugins/demir-bot-pilot/skills/linkedin-tone/SKILL.md) | Apply the user's privately stored LinkedIn calibration. |
| [email-tone](plugins/demir-bot-pilot/skills/email-tone/SKILL.md) | Apply audience-specific email language and approved signatures. |
| [deep-research-and-idea-validation](plugins/demir-bot-pilot/skills/deep-research-and-idea-validation/SKILL.md) | Compare evidence, alternatives, feasibility and demand. |
| [frontend-quality-and-accessibility](plugins/demir-bot-pilot/skills/frontend-quality-and-accessibility/SKILL.md) | Implement semantic, keyboard-accessible and responsive interfaces. |
| [release-readiness-and-observability](plugins/demir-bot-pilot/skills/release-readiness-and-observability/SKILL.md) | Assess deployment prerequisites, rollback, health signals and recovery. |
| [swiftui-performance-and-concurrency](plugins/demir-bot-pilot/skills/swiftui-performance-and-concurrency/SKILL.md) | Handle SwiftUI state, identity, task lifecycle and actor isolation. |
| [jurisdiction-specific-legal-feasibility](plugins/demir-bot-pilot/skills/jurisdiction-specific-legal-feasibility/SKILL.md) | Research a defined activity, jurisdiction and date using official sources. |
| [agent-configuration-review](plugins/demir-bot-pilot/skills/agent-configuration-review/SKILL.md) | Review agent, skill, hook and MCP configuration within requested scope. |
| [ml-training-specialist](plugins/demir-bot-pilot/skills/ml-training-specialist/SKILL.md) | Assess or implement project-specific ML workflows; distinguish retrieval from training. |
| [youtube-learning](plugins/demir-bot-pilot/skills/youtube-learning/SKILL.md) | Learn from timestamped transcript and visual evidence without conflating them. |

## Working principles

- Implement the requested work; ask questions only when answers materially change the result.
- Testing is opt-in. Writing code does not automatically authorize tests, linting, builds, browser checks or repeated fix loops.
- Keep facts, inference, proposals and executed evidence separate.
- Require approval of the exact external action, content and destination before publishing or sending.
- Preserve rollback and private-data boundaries. No autonomous learning, background automation or cloud synchronization is implied.

## Private personalization

The [profile loader](plugins/demir-bot-pilot/skills/demir-bot/references/profile-loading.md) resolves an explicit profile directory, then `DEMIR_BOT_PROFILE_DIR`, then `demir-bot-private` under `CODEX_HOME` (default `~/.codex`). Personal facts, tone examples, account history and local commands remain there, outside this repository.

Without a profile, use supplied facts and provisional tone; do not assume Demir's identity or accomplishments. Do not commit the private profile, correspondence, CVs, credentials, publishing queue, course documents, index databases or backups. `.gitignore` is a convenience, not a privacy guarantee: inspect staged changes before pushing.

## Optional external capabilities

Demir Bot can select available Firecrawl, Gmail, GitHub, Figma, Sites, Higgsfield, Visualize, document/PDF tools, Codex Security and other relevant providers. See [provider routes](plugins/demir-bot-pilot/skills/demir-bot/references/plugin-routes.md). Install and authenticate providers separately, only when needed. Availability and permissions differ by client and account.

RTK and QMD are optional local helpers. Neither is included. The plugin contains publishing approval guidance but does not include a Buffer connection or executable publisher. University RAG is a deferred project, not an implemented service in this repository.

## Development workflow

1. Clone this repository and open that checkout as the Codex project. Use its `AGENTS.md` instructions.
2. Pull current changes before starting; preserve unrelated local edits. Use a focused branch for substantial work.
3. Edit `plugins/demir-bot-pilot/skills/<name>/` and relevant references. Keep the plugin ID stable to preserve existing skill names.
4. Inspect the diff and staged files. Run tests or evaluations only when explicitly requested. Retain upstream notices and provenance.
5. Commit and push the intended change; use a pull request when appropriate. Merging and publishing follow the task's authorization.
6. Updating repository files does not automatically update an installed plugin cache. Use the current supported plugin installation/update workflow to point the local marketplace at this checkout, then reinstall the local plugin and verify the client catalogue. Do not edit cache files directly or reinstall standalone duplicates.

The existing installation initially points to an older local source directory. After cloning, connect the checkout through the supported local-plugin setup workflow; do not assume that cloning alone changes that pointer. Keep private profile paths outside the checkout and preserve rollback during that transition. QMD collection paths, if used, need an explicit scoped update; do not index private data or Git history.

## Current status and limitations

The private pilot's 21 namespaced skills have been exposed in the client catalogue without standalone duplicates. Core saved instructions were compared with the previous skill setup, and private course evidence was retained separately. This is not proof of full runtime parity or every provider operation.

Default-icon overrides were removed, but actual icon appearance remains unverified. The standalone manifest validator previously could not run because PyYAML was absent. Public redistribution and licensing compatibility have not been fully reviewed. No CI, automated test campaign, model training, deployment or cloud synchronization is configured by this repository.

## Sources and licensing

See [RESOURCES.md](RESOURCES.md) for the bundled references and notices, and [upstream adaptations](plugins/demir-bot-pilot/skills/demir-bot/references/upstream-adaptations.md) for source URLs, reviewed versions where recorded, borrowed guidance and intentional omissions.

Existing upstream licence files are preserved in their skill directories. This repository does not assign a blanket licence to material with differing or unassessed provenance. Public distribution requires checking the applicable permissions and attribution; a private repository is not a licence grant.
