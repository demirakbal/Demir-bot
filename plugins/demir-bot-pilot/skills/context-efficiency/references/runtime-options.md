# Match optimization to the runtime

## ChatGPT / Work Mode

Guide source selection, progressive loading, scoped search, output filtering and concise handoffs. Do not claim guaranteed invocation, deletion of earlier messages, control of hidden prompts, forced compaction, changed account limits or durable scratch storage.

With programmatic tools, retain full responses in a supported execution store or file, parse once, and emit selected fields and relevant excerpts. Preserve source identifiers, status, errors, coverage and recovery pointers. Stores may be session-only. Filter before emitting: later summaries cannot remove output already in the conversation.

Avoid arbitrary prefix truncation for substantive evidence. Select by structure or query and inspect omitted sections when needed. Empty search results do not establish absence.

For commands preserve actual exit status and failure context. A successful truncator in a pipeline must not mask a failed command. Prefer supported machine-readable test reports, keep raw logs recoverable, and include passed/failed/skipped counts and material warnings. Inspect raw output when uncertain.

## Local Codex / terminal tools

Resolve host-specific installation evidence and commands through the active private profile (demir-bot/references/profile-loading.md), local-setup.md and runtime-options.md. Without that profile, discover only the relevant executable and existing collection configuration; never assume a host, home directory, runtime, downloaded model or authenticated connection. Use direct reads for known files and scoped native search when optional tools are absent.

RTK is an optional CLI output filter, not an installed ChatGPT plugin. Inspect installation instructions and host compatibility before changing hooks. Headline savings concern selected command outputs; byte-based estimates are not measured whole-session tokens. Preserve failure semantics and a raw-output escape path.

QMD is optional local search for large recurring document collections. It needs setup, resources, scoping and index freshness; semantic search/reranking add costs. Use existing search or rg first when sufficient. ChatGPT needs an available connection to use a local index.

Repository maps help locate relevant symbols and dependencies. Reuse existing maps and update affected parts; do not build an AST index for tiny tasks. Maps do not replace implementation reads before edits.

Do not install binaries, global hooks, dependencies or servers merely because these options are listed.

## API applications under our control

Consult current provider documentation. Keep stable prefixes and tool definitions stable where useful, append changing task data, and measure actual cache-read/write usage. Support, retention, billing and routing vary by model/provider. Caching can reduce processing cost and latency while the input still occupies context; it does not change ChatGPT subscription allowance.

Implement observation masking or compaction only in runtimes we control. Retain originals and constraints; evaluate quality, retries, latency and total cost. Do not assume this host's existing history can be rewritten.

## Measurement

Compare equivalent tasks and quality criteria. Include input/output usage, summarizer calls, indexing/setup, rereads and failed retries when measurable. Otherwise label observed characters or source reload counts precisely, without presenting them as token billing.

Use simple filtering where appropriate. Summaries cost tokens and may omit critical details; use structured handoffs at meaningful boundaries. No universal percentage, fixed context threshold or “same intelligence” guarantee is justified.
