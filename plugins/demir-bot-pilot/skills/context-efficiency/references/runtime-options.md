# Match optimization to the runtime

## ChatGPT / Work Mode

Guide source selection, progressive loading, scoped search, output filtering and concise handoffs. Do not claim guaranteed invocation, deletion of earlier messages, control of hidden prompts, forced compaction, changed account limits or durable scratch storage.

With programmatic tools, retain full responses in a supported execution store or file, parse once, and emit selected fields and relevant excerpts. Preserve source identifiers, status, errors, coverage and recovery pointers. Stores may be session-only. Filter before emitting: later summaries cannot remove output already in the conversation.

Avoid arbitrary prefix truncation for substantive evidence. Select by structure or query and inspect omitted sections when needed. Empty search results do not establish absence.

For commands preserve actual exit status and failure context. A successful truncator in a pipeline must not mask a failed command. Prefer supported machine-readable test reports, keep raw logs recoverable, and include passed/failed/skipped counts and material warnings. Inspect raw output when uncertain.

## Local Codex / terminal tools

Resolve host-specific installation evidence and commands through the active private profile (demir-bot/references/profile-loading.md), local-setup.md and runtime-options.md. Without that profile, discover only the relevant executable and existing collection configuration; never assume a host, home directory, runtime, downloaded model or authenticated connection. Use direct reads for known files and scoped native search when optional tools are absent.

RTK is an optional CLI output filter, not an installed ChatGPT plugin. Reuse known local setup instructions when available; select it only for supported verbose commands where filtering serves the task. Do not blindly prefix shell syntax or every command, change hooks or install tooling from this guidance. When exact output matters, use the original command or the documented `rtk proxy <command>` escape path within existing execution authorization. A proxy invocation is not recovery of a previous run. Headline savings concern selected command outputs; byte-based estimates are not measured whole-session tokens. Follow the recovery contract below; do not assume RTK retained the complete raw stream or preserved the producer status without evidence.

QMD is optional local search for large recurring document collections. It needs setup, resources, scoping and index freshness; semantic search/reranking add costs. Use existing search or rg first when sufficient. ChatGPT needs an available connection to use a local index.

Repository maps help locate relevant symbols and dependencies. Reuse existing maps and update affected parts; do not build an AST index for tiny tasks. Maps do not replace implementation reads before edits.

For cache/index selection, invalidation, bounded storage and structural-versus-prose retrieval, use [cache and retrieval records](source-reuse.md#cache-and-retrieval-records). Preserve existing build/dependency caches and scoped indexes; refresh operations require applicable authorization. Installation alone proves neither a connected retrieval tool nor project compatibility.

Do not install binaries, global hooks, dependencies or servers merely because these options are listed.

## Bounded output and recovery

Master item 004 (original ID 99) supplies an on-demand output-selection contract, not an executable wrapper, check suite or global interceptor. Use only for operations already authorized by the task. References to test reports apply only when those tests were separately authorized; filtering never grants permission to run them. Reuse item 002's observable-loading distinctions and item 003's opt-in routing records without starting telemetry collection.

### Select before emission

1. Define the question the output must answer, the source scope and a bounded selection before calling a tool: relevant structured fields, file/line ranges, headings, result/page limits or targeted search passages with enough surrounding context. Use supported parameters, not invented flags. Small exact results can remain unfiltered.
2. Decide how the evidence can be recovered before a lossy transformation. Prefer a supported execution store holding the returned object, a recoverable source with revision and locator, or an authorized private raw capture. For non-repeatable, expensive or state-changing operations, retain the original result from that same run before filtering; do not plan to rerun them for recovery. Provider-side projections/pagination may omit data before receipt: distinguish the full received response from the full source dataset.
3. Where the runtime permits, parse/select inside the tool orchestration before emitting to the model. Preserve the producer's status, decisive errors and evidence needed to interpret the result. Do not print a whole registry or payload merely to summarize it afterwards. If the host automatically exposes raw output first, state that pre-emission filtering was unavailable; a later summary cannot remove it.
4. Emit the compact result contract below. Bound routine rows/passages, not truthfulness: if decisive diagnostics exceed the chosen budget, disclose that and expand the relevant evidence or provide recoverable diagnostic sections. Do not silently clip the first/last lines, erase warnings, drop failed items or present a limited sample as exhaustive.

### Compact result contract

| Element | Required meaning |
|---|---|
| Source and operation | Safe source/run locator, requested scope and version when available; enough to distinguish runs without exposing secrets. |
| Producer outcome | Original command exit code or tool/API success, error, pending or cancelled state. Include decisive stderr/errors and partial-result warnings. Unknown status remains unknown. |
| Filter outcome | Selection/parsing succeeded, failed or incomplete, independent of producer success. A successful formatter cannot turn a failed command into success. |
| Selected evidence | Requested fields or relevant passages, with locators and essential surrounding context; summarize repeated diagnostics only when their distinct causes remain represented. |
| Coverage | Selection rule and bound; returned/omitted counts if exposed, otherwise unknown; pages/ranges inspected, pagination/cursors and upstream or local truncation. Zero matches in a limited search do not establish absence. |
| Recovery | Actual raw-result/source locator, what it retains, access/lifetime limits and the scoped retrieval method. Mark unavailable originals explicitly; never invent a log path or claim full capture from a truncated response. |

Keep producer and filter statuses separately when using pipelines; the final formatter's exit code is not the producer's exit code. Do not treat stderr presence alone as failure or empty stderr as success. If parsing fails, report that failure and recover the necessary raw excerpt instead of returning empty results or silently defaulting to success. A timeout, cancellation or yielded session is not a completed operation; retain its handle and known partial coverage when available.

### Intended bounded path (design only)

For an already-authorized source inspection, request one relevant section or result page; retain the received response and status in an available session store before emission. Return its status, source revision, selected passages and coverage, plus that store's actual handle. Recover missing context by selecting the needed field/range from the retained response. If the data was never returned, fetch the specific missing page/range only within the existing read scope and identify any version change. Do not claim a consistent snapshot across changing pages without evidence.

For an already-authorized command with potentially large output, choose a supported capture that preserves stdout, stderr and the original exit status, then select relevant records and diagnostic context for emission. The intended display is `producer status; filter status; selected evidence; coverage/omissions; recovery locator`. Recovery reads a bounded part of the captured output from the same run, not a replay of the command. These are interface designs, not executed examples or promised facilities in every host.

If using RTK would discard required original evidence or hide the producer status and no supported capture supplies it, choose an unfiltered/captured operation instead. Do not run both filtered and original commands just to compare them. An existing source file can be a recovery source for read-only inspection when its identity remains known; it is not a substitute for capturing a transient command result. If neither capture nor source recovery is available, avoid lossy filtering for decisive evidence and report the limitation.

### Evidence boundaries

Keep sensitive raw captures outside Git, plugin packages, shared exports and indexes, in an authorized private location or supported session store. Do not create persistent logs by default, upload payloads, retain credentials or broaden data collection for recoverability. If safe retention is unavailable, use scoped reads/redacted evidence and state any resulting loss of exact recovery. A redacted record is not an untouched original. Session stores and temporary files can expire; never promise durable recovery, access or deletion without evidence.

Saving this contract does not establish that a host or RTK path follows it. Report the intended selection and recovery mechanism separately from observed execution. Link any later savings claim to item 001's [measurement contract](#measurement), including recovery reads, filtering overhead, retries and comparable completed-task quality. Until a separately authorized comparison exists: **Behavior and session savings unverified.** No evaluation loop or background collector is enabled.

## API applications under our control

Consult current provider documentation. Keep stable prefixes and tool definitions stable where useful, append changing task data, and measure actual cache-read/write usage. Support, retention, billing and routing vary by model/provider. Caching can reduce processing cost and latency while the input still occupies context; it does not change ChatGPT subscription allowance.

Implement observation masking or compaction only in runtimes we control. Retain originals and constraints; evaluate quality, retries, latency and total cost. Do not assume this host's existing history can be rewritten.

## Cost-benefit decision rule

Master item 009 (original ID 95) is a lightweight instruction for choosing a workflow, not a scoring engine, benchmark or mandatory preflight. **Trigger:** there is a material choice between plausible ways to complete the requested outcome, or the user explicitly asks which workflow is appropriate. **Expected action:** choose the smallest adequate authorized option using available evidence about result quality, total usage, elapsed time and risk. **No-action case:** when a routine path already meets the requirements, proceed without a comparison table, extra discovery, baseline run, approval round or new record.

### Adequacy before optimization

Treat user requirements, required source freshness, privacy/access boundaries, mandatory specialist instructions and actual operation permissions as constraints. Exclude options that cannot meet them; less output or fewer tools cannot compensate for an incomplete answer, lost evidence or an unauthorized action. Apply item 005's instruction hierarchy when a workflow conflicts with the current scope. “Smallest” means least unnecessary machinery sufficient for the outcome, not shortest response, lowest apparent token count or guaranteed cheapest execution.

Consider the direct/reuse path and only realistic alternatives that add a needed capability. Do not enumerate every provider or build a new framework to decide. Use these dimensions qualitatively unless scoped measurements already exist:

| Dimension | Decision evidence |
|---|---|
| Expected task quality | Coverage of acceptance criteria, precision/freshness of evidence, missing inputs and known failure modes. Separate a reasoned expectation from observed success; do not assign an invented overall score. |
| Total usage | Reads, output, tool calls, setup/indexing, reference loading, summaries, likely recovery/rework and any authorized coordination. Include overhead in the comparison; unavailable token/cost data stays unknown. Do not convert bytes or account percentages to billed task tokens. |
| Latency | Expected end-to-end waiting, serial dependencies, setup and recovery. Explain concrete causes of delay rather than inventing timings; parallel durations cannot simply be added or treated as free. |
| Risk | Consequences of stale/missing evidence, incorrect edits, privacy exposure, irreversible effects and dependency failure; consider reversibility and recovery within existing authority. Greater consequences may justify more evidence or a relevant specialist, not unauthorized checks. |

Prefer the simpler option when available evidence supports comparable adequacy and it avoids unnecessary setup, loading or coordination. Choose added effort when it addresses a specific quality or risk gap. If trade-offs remain uncertain, say what is unknown and use a conservative adequate option; do not manufacture a numeric ranking, probability, savings percentage or ROI. Respect explicit user priorities within the binding constraints. Ask only when missing information or a user preference would materially change the choice, and continue independent authorized work.

### Named dependencies and stopping boundary

This rule depends on the current task's outcome/constraints, relevant source evidence and the actually available skills/tools needed for the chosen operation. Existing instruction owners are [routing and composition](../../demir-bot/references/routes.md), [provider fallback](../../demir-bot/references/plugin-routes.md#missing-provider-and-access-fallback) and [capability evidence](../../demir-bot/references/capability-maintenance.md#evidence-model). Reuse item 007's [freshness rules](source-reuse.md#cache-and-retrieval-records), item 008's [handoff format](source-reuse.md#handoffs) only when needed, and item 004's [bounded output contract](#bounded-output-and-recovery). These pointers are not instructions to load all references for each decision.

For an actual choice, name only material dependencies: for example, the target file and current contract for a direct edit, an already available compatible symbol index for structural navigation, or an authorized connected provider for account-specific data. State missing project access, compatibility, authority or telemetry explicitly. No new provider, paid resource, agent, index, report or approval ceremony is required by this rule. A written workflow does not establish that its dependencies are installed, connected or verified.

If the selected approach encounters a missing dependency or no longer meets the outcome, reassess only the affected choice using already authorized evidence. Use an eligible fallback or report the blocker; do not repeatedly retry unchanged failures, bypass a denial, expand scope or run an evaluation to settle uncertainty. Stop choosing once an adequate path is selected and execute only the authorized task. Revisit only when material evidence, scope or constraints change.

### Illustrative acceptance example (not an executed check)

For a requested one-function correction with tests explicitly excluded, the known paths are a scoped source edit or introducing a repository index and several reviewers. The target file, relevant callers/contract, current dirty state and write authority are the material dependencies. If those sources suffice, choose the scoped read/edit: it covers the requested behavior without new indexing or coordination. Preserve other accepted inputs and report execution as unverified. Do not quote a numerical saving. If the contract is missing and affects correctness, retrieve that specific source within scope or state the blocker rather than guessing or launching tests. This illustrates acceptance of the rule: adequate outcome, named dependency, bounded action and honest limitations.

For a stable question already answered by supplied evidence, the no-action case is a direct response: no workflow comparison or persisted cost record. Conversely, a consequential decision needing current primary evidence cannot use stale context merely because it is shorter; choose the necessary authorized retrieval or disclose the access limitation. These illustrations define intended behavior, not tested results.

### Reporting

Explain the choice briefly only when it helps the user assess a material trade-off; omit routine internal routing narration and unsolicited decision reports. Distinguish **rule saved**, **workflow actually chosen/used**, and **benefit unverified or measured**. Use item 003 only for separately requested routing observations and item 006's existing rule ownership rather than adding a duplicate catalogue. Any efficiency claim must satisfy item 001's [measurement contract](#measurement), including comparable completed-task quality and all retries/coordination. Saving this rule runs no comparisons and proves no improvement: **operational behavior and benefit remain unverified** until observed within authorized scope.

## User-set budgets, stop and resume

Master item 010 (original IDs 104, 105, 166, 167, 97) applies when the user supplies a task budget or asks to stop/resume budgeted work. It is instruction-level guidance, not a budget controller or account service. Without an explicit budget, follow the ordinary authorized task and item 009; do not invent task/session/day caps, seek approval for routine estimates or activate usage monitoring.

### Establish the actual limit

Reuse the user's amount, unit, scope and stop condition: tokens, elapsed time, monetary spend, calls or another explicitly named resource are not interchangeable. Determine whether the limit covers total task usage or additional usage from this point, using existing context. Ask only when an ambiguity materially affects compliance; never silently reset consumed usage or reinterpret a hard maximum as a preference. “Keep it brief/cheap” is a qualitative preference, not a numeric cap. A budget does not itself authorize spending, providers, delegation, tests or other otherwise excluded operations.

Use an existing task/budget record when useful. Preserve the requested limit and unit, task boundary, mechanism and its actual scope, last exposed usage with observation time/source, unknown attribution, and any remaining amount that can validly be derived. These fit item 008's Constraints/Evidence fields; do not create another ledger or persistent file by default.

### Supported mechanisms, with honest scope

| Mechanism | What it can support | What it does not establish |
|---|---|---|
| Exposed host task/goal budget | An accepted host control for the documented resource and task boundary; reuse an existing applicable goal/budget rather than creating duplicates | Coverage of tools, child agents, hidden usage or external charges unless the host explicitly includes them; accepted configuration alone is not observed cutoff behavior |
| Per-call output limit or timeout | A bound on the particular output/operation when supported | A total-task token/spend cap; a response timeout does not necessarily cancel remote work or stop billing |
| Task-specific usage readings | Consumed/remaining usage for the reported unit and scope; label estimates as estimates | Missing child/tool usage or undocumented enforcement; a reading is observation, not a controller |
| Account allowance windows | Account-level remaining percentage and reset information when exposed | Task-attributed token/cost usage or a task budget; concurrent tasks and other account activity confound attribution |
| Advisory estimate | A best-effort planning boundary using known usage and uncertainty | Guaranteed maximum, billing accuracy or hard enforcement |

Consult the actual available tool contract before configuring a mechanism; never invent a budget field, cancellation API or enforcement capability. Reuse host controls only when their activation is authorized and applicable. For a host goal API such as `create_goal`, comply with its explicit-goal requirement: a request to edit budget guidance is not a request to create a goal, and an ordinary task budget must not be treated as an explicit goal request when the API requires one. Set a token budget only when explicitly requested; inspect/reuse existing goal state when relevant. Status updates must follow the host's own conditions; do not misuse `complete`, `paused` or `blocked` to simulate a budget cutoff or resume a goal through an unsupported operation.

If no control enforces the user's resource and scope, state that limitation. Offer a conservative advisory approach or smaller scope without claiming a hard cap. Where a strict maximum is a prerequisite and the next operation's maximum consumption is unknown/unbounded, do not launch it on a guess; stop at that dependency or ask the one necessary choice. Do not install a controller, change account settings, redeem reset credits, purchase usage or move work to another account to satisfy the budget.

### Sparse observations and stopping

Use readings already available. When supported and within scope, take a snapshot at the start or a material work boundary, then only when new information could change whether work should continue, such as before a substantial next operation or near the known limit. Do not poll every tool call, set a timer/watcher, run trial tasks to estimate cost or promise automatic notification. Snapshot and coordination overhead also consume resources where applicable.

Apply item 001's unit and attribution rules: account percentages are not tokens; cached tokens may overlap input totals; retries, failed attempts, recovery, summaries and authorized coordination belong in the task boundary. A remaining amount is meaningful only for matching units/scopes with adequate coverage. Keep unknown usage unknown and do not subtract incomparable or incomplete readings to claim precise remaining budget.

Before substantial additional work, consider whether it can fit while preserving the required quality and leaving room for a concise checkpoint where feasible. Use available evidence and a task-specific margin rather than an arbitrary default reserve or invented forecast. If the limit is reached, the user says stop, or the next necessary action cannot reasonably fit, stop starting new substantive work. Preserve partial results and report what remains; do not quietly lower acceptance criteria, mark incomplete work complete or increase the budget. A host may interrupt before a checkpoint can be produced, so do not guarantee graceful completion under every cutoff.

For in-flight work, use a supported cancellation only within authority and report its actual result. Do not equate closing a UI, timing out or ending a turn with successful remote cancellation. If cancellation cannot be confirmed, state that the operation may remain pending and its usage is unknown; avoid duplicate submission, destructive cleanup or unsupported retries. Respect higher-priority host stop/budget controls.

### Checkpoint and graceful resume

Use the existing [seven-field handoff](source-reuse.md#handoffs), not a separate budget report: name the stop reason, original limit, observed usage and attribution gaps, saved artifacts, unverified/partial work, pending operations and the smallest next action. Keep the checkpoint conversational unless persistence is authorized. Saving incomplete work is not proof that the goal was achieved; do not run checks to manufacture a completion claim.

Resume only on applicable user authorization or the host's explicit continuation mechanism, not an account reset, elapsed time or background schedule. Reuse prior authorization for unchanged actions, but keep an exhausted explicit cap binding until it is changed. “Continue within the remaining budget” does not grant a fresh full budget; an ambiguous continuation after exhaustion needs only the necessary budget/scope clarification. Do not restart a host goal to erase usage or bypass its limit. User-specified additional budget and replacement total budget must remain distinct.

Before resuming, apply item 007's targeted freshness rules and item 008's handoff reconciliation. Account for completed work, prior consumption where the budget is cumulative, and pending operation status; do not replay completed or uncertain external actions. Report any unsupported host-side budget adjustment or missing usage access instead of inventing a reset. No recurring automation, account change, cloud sync, RAG or training is implied.

### Reporting boundary

Report **guidance saved**, **control configured/accepted** only when actually done, **enforcement observed or unverified**, and **work complete/partial/blocked** separately. Name the unit and scope of any observed control. This implementation activates no budget mechanism and makes no usage/account calls. Runtime enforcement, stopping/resumption behavior and efficiency benefit remain **unverified** until evidenced within separately authorized scope.

## Cost-aware model delegation

Master item 011 (original IDs 102, 160) applies to explicitly authorized delegation or its requested design. Designing this policy authorizes no workers, model calls or comparison runs. Default to a single agent unless a bounded independent subtask and current delegation authority justify another worker; do not create work merely to use concurrency. Apply item 009's adequacy rule and item 010's explicit budgets without adding default quotas.

### Eligible work and exclusions

Potentially eligible tasks have a clear input boundary, concrete acceptance criteria and a result the parent can review without repeating the whole task. Examples include extracting specified fields from an already authorized source, examining a separate module's stated contract, or drafting one independent section from approved facts. Use existing tools/direct work when they are already sufficient. A second agent is not required just because a task is eligible.

Keep tightly coupled work with the parent: unresolved requirements that control all later decisions, simultaneous edits to the same files/contracts, steps requiring each other's unfinished outputs, trivial work whose handoff/review would dominate, or tasks requiring private context the worker is not authorized to receive. Do not delegate unsupported external actions, account decisions or permissions to make them appear authorized. A high-consequence judgment is not an automatic candidate for a cheaper model; identify a separately bounded support task if useful and retain the consequential decision with an appropriate authorized reviewer.

Before dispatch, name the independent deliverable, allowed inputs/files, dependencies and why another worker adds value. If needed, assign non-overlapping edit ownership; in a shared workspace, preserve concurrent changes and reconcile results before integration. Unresolved shared state or a missing prerequisite makes the work dependent, not parallel. Do not recursively delegate or create user-visible tasks unless that scope is explicitly authorized and the actual tool contract permits it.

### Supported model choice

Resolve models, reasoning settings, inheritance and override restrictions from the current host's exposed tool contract or already available authoritative configuration. Do not hard-code a model catalogue, invent a cheaper tier or infer price from a model name. Record the requested choice and the effective model/settings only when exposed; otherwise mark the effective choice unknown. Host capability is not permission to override: respect user model choices and all applicable restrictions. For example, when a full-history fork must inherit its parent's model/settings, do not attach unsupported overrides or silently change the fork mode to evade that contract.

For a bounded task, consider a supported lower-priced model only when task capability, context/tool access and quality criteria remain adequate, and current pricing evidence supports that description. A documented rate difference is a price comparison, not proof of lower completed-task cost. In subscription/opaque-billing environments, a lighter model's actual task cost may be unknown. If pricing, compatibility or capability evidence is missing, say so; use an authorized known-adequate choice or keep the work with the parent, without claiming savings. No live model probes, purchases, account changes or provider installation are authorized by this selection rule.

Dependencies are the actual delegation tool and permitted concurrency, a supported model/settings combination, access to the bounded inputs, any explicitly required budget control, and a parent able to review/integrate the result. Report missing dependencies as scoped blockers and continue independent parent work. Do not route around denied access through a different worker or provider.

### Bounded handoff and parent responsibility

Reuse item 008's [seven-field format](source-reuse.md#handoffs), not a second delegation ledger. Put the task and acceptance criteria under Goal; allowed actions/files, model/settings, privacy, budget and stop boundaries under Constraints; source/version locators under Evidence; and the requested output plus return/escalation condition under Next action. Share only the necessary approved context. Explicitly carry exclusions such as no tests, external writes or further delegation; do not assume the worker sees the whole conversation.

Choose a suitable supported context mode without discarding binding instructions. A smaller handoff may reduce copied material but can omit critical facts; preserve relevant contracts and original-evidence pointers. Define an output boundary appropriate to the subtask, including omissions, failures and recoverable evidence under item 004. Do not fabricate a universal token allotment or promise that worker limits cover parent review or external charges.

The parent remains responsible for integration and acceptance. Inspect the returned artifact and its source evidence against the stated criteria; reconcile conflicting edits and unsupported claims. Distinguish a worker's completion assertion from evidence of completion. Source review does not authorize tests or establish execution success. Count this review, any corrective work and the final integration as part of the task, not free overhead. Do not trust a result simply because more agents agreed.

### Escalation and stopping

Classify the obstacle using item 005's existing routing/knowledge/tool/permission/model distinctions. Missing facts call for the specific authorized source; missing access or permissions call for reporting the dependency, not a stronger model. For complexity or capability limits supported by the returned evidence, narrow the task, have the parent complete it, or use an appropriate supported model within current authority and budget. If a needed override, additional work or budget is not authorized, ask only for that material decision. Do not default to the most expensive model or repeated worker calls.

Stop dispatching when the deliverable is accepted, the user/host stops work, the explicit budget is reached, a necessary dependency is unavailable, or another attempt would repeat the same failure without new evidence. Any retry needs an identified change in inputs, method or task boundary; it remains inside the authorized scope, not an automatic escalation loop. Use item 010 for cancellation uncertainty, pending operations and truthful partial-work checkpoints. Do not claim worker cancellation or refund from an ended parent turn.

### Comparison and reporting

Before recommending delegation as the default for a task class, require an authorized comparison against a single-agent workflow with comparable completed outcomes and quality criteria under item 001. Include parent planning, source preparation, model/worker calls, handoffs, coordination, waits, parent review, integration, failures, retries and escalation. Avoid double counting overlapping usage; wall-clock latency differs from summed worker durations. Missing child/tool usage remains an attribution gap. Count failed and abandoned attempts, and report sample size, variability and quality regressions rather than selecting only favorable runs.

Lower model unit price, fewer parent tokens, shorter worker output or more parallel agents alone establishes no whole-task saving. Without the comparison, any proposed benefit is **unverified**, and single-agent work remains the default. Do not run comparisons or collect ongoing telemetry from this guidance.

Report **delegation policy saved**, **workers actually dispatched and results reviewed** only when observed in authorized work, and **measured benefit or unverified benefit** separately. This source change starts no agents, changes no active model and proves no operational delegation behavior. Keep private handoffs and usage records outside Git/plugin packages and persist only within the existing authorization.

## Measurement

This is the baseline and cost-attribution contract for master item 001 (original IDs 165, 52, 96). Reuse the existing task record or a concise response when baseline work is requested or an efficiency claim is contemplated; do not create a telemetry service or mandatory per-task ledger. Use evidence already exposed by authorized work. Missing telemetry is a limitation, not permission to install providers, inspect accounts or execute trial tasks.

### Baseline record

Use the following fields for each baseline and candidate run. Record `unavailable` with the reason for missing values, `not applicable` only when justified, and zero only when observed. Keep private run records, account history and raw messages outside the plugin and Git; retain only minimal authorized evidence locators.

| Field | Required content |
|---|---|
| Task and scope | Task/run identifier, date, representative outcome, inputs/source versions, constraints and intended completion boundary. Account for dirty source changes; do not treat a commit as their full identity. |
| Result and quality | Completed, partial, failed or blocked; delivered artifact/evidence; acceptance criteria satisfied, missed or unexamined. Identify who or what assessed quality and whether the assessment was source inspection, user acceptance or an authorized evaluation. No invented aggregate quality score; saving instructions does not establish behavior. |
| Model and settings | Exposed provider/model/version, reasoning settings and other relevant exposed configuration; skill/tool versions, runtime and cache conditions where known. Mark hidden or unavailable settings explicitly. |
| Routing and failures | Intended versus observed specialist/tool route; unnecessary or failed routing, errors, rereads, retries and recovery. Distinguish no observed failure from unexamined routing. |
| Available metrics | Value, unit, source, observation interval and measured/estimated status for each metric below. Report the actual exposed subset, not an invented total. |
| Full overhead | All attempts, failed/abandoned work, setup/indexing, retrieval, summaries, review/gates, tool calls, agents and coordination associated with the task; record component coverage and overlaps. |
| Missing attribution | Missing telemetry, inaccessible child/tool usage, shared setup, unknown caching or pricing, concurrent account tasks/activity and any unmatched observation windows. State which conclusions these gaps prevent. |
| Comparison status | Baseline/candidate relationship, applicable evaluation authorization or `not authorized`, comparable outcome evidence, sample size, variability and limitations. Until an authorized comparison exists: `Improvement unverified`. |

Keep these metrics separate:

- **Tokens:** exposed input and output counts, with cached reads/writes separately identified under the provider's definitions. State whether cached counts are included in input totals; never add overlapping counters. Characters, bytes, local tokenizer estimates and filtered-output statistics are proxies, not measured whole-task tokens.
- **API cost:** distinguish observed billed charges from estimates. An estimate needs its currency, dated pricing source, applicable model/rates and covered usage categories, including cache and tool charges where applicable. Without these, cost is unavailable. Do not infer subscription billing from API rates.
- **Subscription allowance:** record an exposed account percentage/delta and window only when already available through authorized work. It is an account-level observation, not a token count or task bill. Concurrent activity or unknown accounting prevents task-specific attribution; no promise of extra allowance.
- **Elapsed time:** state start/end boundary and distinguish wall-clock latency from summed agent/tool durations. Parallel durations overlap; do not add them to claim end-to-end latency. Include waiting, retries and coordination in the task boundary.

Count every attempt once, including coordination and unsuccessful runs. For shared setup show the full setup cost and any explicit allocation assumption separately; do not silently amortize it away. If component usage is unavailable, retain the gap and report only the observed subtotal. Lower output volume alone cannot establish lower total task cost.

### Bounded comparison design, execution separately authorized

For a proposed optimization, design a finite comparison using this contract; a design is not a runnable check suite. Reuse [the existing evaluation reference](../../qa-and-test-evidence/references/demir-bot-evaluation.md) only for separately requested evaluation work. Do not write cases/checks, launch model runs, benchmarks, gates or repeated evaluation loops merely to fill baseline fields.

1. Name the baseline and candidate versions, hypothesis, representative task outcomes, fixed input scope and quality criteria before comparison. Change one relevant factor when practical; disclose changes in models, settings, tools, cache conditions or task difficulty that confound attribution.
2. Specify a finite case set/sample size, repetition count, ordering, task completion boundary and stop conditions in the proposed design. Do not invent a universal run count, spending budget or authority to execute. Stop at missing project/access/evidence dependencies rather than fabricating them.
3. Plan paired records for comparable completed outcomes using the fields above, plus all failed, incomplete and abandoned attempts. Apply the same quality criteria to both conditions. Report completion and routing failures across all attempts; do not select only the cheapest successful run.
4. For authorized reviews/gates (master item 034), record failures caught, failures missed and false alarms against an independently supported expected outcome. If missed failures cannot be established, mark them unknown. For skill improvements (031), pair versioned outcomes; for context loading (002), separate observable loading/output reductions from whole-task effects. This contract supports those items without implementing their evaluations.
5. If execution is later authorized, report actual sample size, per-run evidence and repeated-run variability with a stated summary such as range and median where supported. A single run cannot establish variability; absent repetitions mean variability unavailable. Model outputs are variable even with matching settings. Report confounders and uncertainty rather than claiming deterministic reproducibility.

### Claim boundary

A savings claim must identify the metric, comparable completed-task quality evidence, authorization and both observation scopes, including all retries and coordination. For comparable totals in the same unit, absolute savings are baseline minus candidate; a percentage uses the positive baseline as denominator. A zero/missing baseline makes that percentage undefined. Report regressions and quality trade-offs, not just favorable deltas.

Missing cost attribution prevents a whole-task cost claim; it need not erase a narrower, directly supported observation. For example, an observed byte reduction remains a byte reduction, with total token/cost improvement unverified. Keep estimates labeled throughout and never generalize one comparison to all tasks. Without an authorized, comparable completed-task comparison, use: **Improvement unverified; no supported savings claim.** Saving these instructions alone does not establish improved behavior or efficiency.
