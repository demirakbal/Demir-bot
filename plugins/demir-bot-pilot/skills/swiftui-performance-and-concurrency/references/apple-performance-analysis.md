# Apple performance evidence

Original roadmap item 018 guidance. Use for a requested performance investigation, relevant source concern or interpretation of supplied traces. Reuse the parent skill for SwiftUI invalidation, ownership, isolation and task lifetime; [architecture](../../architecture-review/SKILL.md) for justified boundary changes; and [release guidance](../../release-readiness-and-observability/SKILL.md) for artifact/environment attribution. Do not create a profiling framework or automatically instrument an app.

## Establish a representative question

Name the user-visible operation and intended outcome: launch to a usable screen, scrolling, an edit/save, a large import or another supplied workload. Record available evidence of source revision, build configuration, optimisation/symbol availability, device versus simulator, OS/toolchain, data size, warm/cold state and relevant network/thermal/power conditions. Mark unknowns rather than inventing a baseline or performance target.

Distinguish elapsed latency, CPU time, throughput, memory footprint, allocation volume and I/O. A change can trade one for another. Define the operation boundary and units before comparing numbers; a faster helper is not necessarily a faster completed user task.

Without a named project or supplied evidence, save reusable guidance only. App-specific conclusions need actual source/workload context. Do not profile, benchmark, build, launch an app or create checks to fill gaps in an instruction-only task.

## Source investigation

Trace one affected path and its data size, repetitions, ownership and scheduling. Look for repeated decoding/sorting, synchronous file/database work, unbounded collections, redundant requests, expensive view computation and retained subscriptions/tasks. Tie each hypothesis to source locations and explain why that workload may expose it; do not call it a measured hotspot.

Reuse existing caching and isolation guidance. Specify invalidation, memory bounds and concurrency ownership before proposing caching. Moving work into Task does not establish background execution; moving it away from the main actor does not eliminate its CPU, memory or I/O cost. Prefer the smallest correction that preserves ordering, cancellation, errors and visible behavior. Do not remove needed work, weaken privacy or ignore failures to make a path appear faster.

## Read supplied traces with their limits

Use an existing supplied export, excerpt or image for the relevant interval. If the format needs unavailable tooling or an unapproved export/conversion, name the limitation and use available evidence; do not silently capture a replacement. Keep raw traces, memory graphs, paths and possible user data outside the plugin and external services. Quote only necessary redacted evidence.

- **CPU and responsiveness:** align the supplied symptom interval with the relevant thread/task and call tree. Distinguish self cost from inclusive cost and avoid summing overlapping parent/child samples. Sampling percentages depend on the selected interval and filters; they are not exact invocation counts. Apple's [main-thread analysis](https://developer.apple.com/tutorials/instruments/analyzing-main-thread-activity) and [execution-frequency guidance](https://developer.apple.com/tutorials/instruments/determining-execution-frequency) explain why a hot frame may need further causal analysis.
- **Waiting versus working:** a long elapsed operation may be blocked on I/O, synchronisation or another dependency rather than consuming CPU. Use only the available thread-state, timing or dependency evidence to distinguish them. Apple's [hang-analysis guidance](https://developer.apple.com/tutorials/instruments/getting-started-with-hang-analysis) discusses this distinction. Do not infer a lock owner or exact wait duration from CPU samples alone.
- **SwiftUI:** correlate supplied view-update or body-cost evidence with state dependencies and identity. Repeated body evaluation is not automatically a full render or a defect; determine whether its work contributes to the relevant interaction. Missing framework symbols or source attribution limits conclusions.
- **Memory:** distinguish transient peaks, surviving allocations, caches, retained objects and unreachable leaks. Use supplied generations/timelines and ownership paths where available. Apple's [memory-use guidance](https://developer.apple.com/documentation/xcode/gathering-information-about-memory-use) connects allocations with relevant intervals. A high footprint alone is not proof of a leak, and absence of a leak report does not prove acceptable retention.
- **I/O and throughput:** connect supplied file/database/network timing to bytes, operation count, concurrency and queueing where recorded. Distinguish app-side work from remote latency; do not infer disk or server saturation from elapsed time alone. Avoid claiming a universal concurrency setting or throughput capacity from one sample.

## Launch and lifetime depth

Define the launch boundary: process start, first frame and first useful interaction are different outcomes. Identify whether the supplied evidence represents cold/warm launch, debugger attachment and a representative build. Trace eager service creation, synchronous loading, decoding, migrations and dependencies needed for the first useful screen. Do not move critical work later without explaining the resulting loading/error state or simply shift the same delay to the first tap.

For memory growth, trace expected object lifetime against supplied retention paths or source ownership: closures, task handles, observers, subscriptions and caches. Reuse dependency-injection and cancellation guidance before prescribing weak captures. One retained instance can be intentional; repeated growth needs workload/time evidence. Do not assume breaking a reference is safe if it cancels necessary work or invalidates shared state.

## Comparison and any later profiling scope

Classify findings as source hypothesis, supplied measurement or observed operation with a locator. A measured interval can support a hotspot claim without proving its root cause. For a proposed fix, explain the mechanism and trade-offs; label benefit unmeasured until comparable evidence exists.

Compare before/after evidence only when workload, result correctness, build/device conditions and metric definitions are sufficiently comparable. State sample count and variability when supplied; do not turn a single run into a stable percentile, invent savings or generalise simulator/debug results to production devices. Missing comparability stays explicit.

If a profiling workflow is separately requested, define a finite workload, target artifact/device, suitable supported instrument, capture interval, permitted data and stop condition using current official tool documentation. Planning capture does not authorise running it. No instrumentation, signposts, benchmarks, fixtures, trace conversion, provider installation or repeated capture/fix loop follows from this reference.

## Acceptance and delivery

Illustrative acceptance examples, not executable checks:

- **Source only:** a view repeatedly sorts a growing collection. Explain the likely cost and a scoped alternative; report no measured frame-time gain.
- **Supplied trace:** the main thread is busy during a reported hang. Identify the filtered interval and expensive frames, then inspect their source; do not equate a high sample percentage with exact call count or sole root cause.
- **Memory:** a supplied graph retains a model through an owned task. Trace the expected completion/cancellation path before proposing a lifetime change; do not claim a confirmed leak from the graph alone.
- **No-action case:** a small unrelated edit has no performance requirement or evidence. Do not start profiling or add speculative optimisation.

Return the workload, evidence locator, finding/confidence, smallest proposed or saved change and unverified benefit concisely. Do not create an extra report or claim release readiness from one performance observation.

Source basis: official Apple resources linked above, consulted 27 September 2026; original guidance reusing existing specialists. No real app or trace was assessed by writing this reference.

Preserve all instruction-only restrictions: no profiling, benchmarks, builds, app/simulator launches, checks/fixtures, tests, scans, evaluations, delegation, commits, package operations, installations, index refreshes, cache deletion or background activity. No credential/account access, container changes, sync activation or real database access/copy/migration. Leave private data, installed plugin, cloud skill sync, university RAG and training unchanged.
