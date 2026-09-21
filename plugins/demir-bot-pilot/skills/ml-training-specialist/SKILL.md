---
name: ml-training-specialist
description: Implement or review ML data pipelines, training and fine-tuning workflows in the actual project stack, or assess whether training would improve Demir Bot. Use for concrete ML work and assistant-improvement research; do not start training or autonomous self-modification merely by invoking the skill.
---

Plugin pilot routing: select bundled siblings as `demir-bot-pilot:<skill-name>` from the active catalogue. Resolve file references relative to this skill directory; paths beginning with a bundled skill name are relative to the parent `skills/` directory. External provider skills remain optional and retain their own names. Do not fall back to a duplicate standalone copy silently.


# ML training and assistant improvement

Establish the objective, available data and rights, target metric, framework/version, compute/device, budget and intended output from project evidence. No current project is assumed. A reusable skill can be installed before a project exists; do not invent a dataset, model, framework or training run. Ask only for decisions that materially affect implementation.

## Choose an intervention

Compare a simple heuristic or baseline, better instructions, retrieval, tool reliability and actual model training. Reuse deep-research-and-idea-validation for substantial current comparisons and primary-source evidence; do not impose research for routine code. Use privacy-review for concrete data, telemetry, retention or sharing decisions. Never send private skill files, CVs, conversations or publishing drafts to a training/research service without applicable authorization.

Demir Bot is an instruction coordinator, not its underlying model. Editing skills, adding QMD retrieval and fine-tuning a separately supported model are different operations. A local skill cannot retrain ChatGPT or increase its hidden context/allowance. Demir wants future improvement from approved feedback; that interest does not create an always-running learner or grant blanket self-editing, data collection, training spend or release permission.

For assistant improvement, identify a demonstrated error and an approved, minimal example. Prefer a scoped instruction/retrieval correction where suitable. Keep raw personal conversations out of training corpora by default; record purpose, consent/authority, provenance, exclusions and deletion propagation for approved data. A future autonomous loop needs explicitly bounded triggers, allowed files/actions, budget, evaluation authorization, rollback and stop conditions. Never let it alter approval, privacy or testing boundaries to reward itself. Evaluation design may be discussed; executing evaluations remains opt-in. Use existing QA evaluation guidance when requested.

## Implement in the actual stack

- Inspect dependencies, versions and existing pipeline first. Keep preprocessing and inference consistent; avoid introducing PyTorch, a remote tracking service, model registry or a new serving API merely because an example uses one.
- Define input/target shapes and dtypes, missing-data behavior, provenance and label availability. Split by entity/time where needed, deduplicate across splits, fit preprocessing only on training data, and keep held-out data out of feature/model selection. Do not silently inspect or tune on a test set.
- Match the loss and metrics to the task, imbalance and decision cost. Preserve a meaningful baseline and uncertainty. Average metrics with the correct sample/token weighting; batch averages are not necessarily dataset averages. Distinguish training loss from generalization evidence.
- Make device/precision explicit from actual CPU, Apple MPS or CUDA support. Do not assume CUDA on this Mac. Inspect framework-version support for AMP, compile and distributed features. Choose batching/workers/pinning and clipping for the workload, not copied defaults.
- In PyTorch, separate train/eval modes and gradient tracking, retain tensors needed for backward, zero gradients at the intended accumulation boundaries, handle partial accumulation and scheduler/scaler steps correctly. Avoid retaining graphs in metrics and silently skipping nonfinite losses. Prefer small, clear loops over speculative distributed machinery.
- Record seeds and environment where relevant without promising exact reproducibility across devices/releases. Resume checkpoints need appropriate model, optimizer, scheduler/scaler, step and RNG/sampler state; do not claim weights alone resume an interrupted run. Use atomic checkpoint replacement and explicit retention within the requested project. Treat downloaded weights and serialized objects as untrusted; inspect loaders and avoid arbitrary pickle/code execution.
- Performance changes need a concrete bottleneck or supplied evidence. No automatic profiling, benchmarks, hyperparameter sweeps or claims of speedups. Compare alternatives in reasoning when execution is not authorized.

## Execution and delivery

Writing training code does not authorize running it. Explicit training requests permit the agreed training run and its normal training-validation steps only within the established dataset/compute/budget scope; they do not authorize unrelated tests, benchmark campaigns, paid resources, uploads or deployment. When the run's scope is unclear, clarify before launching it. Stop on budget exhaustion or meaningful failures rather than silently relaunching.

No mandatory tests, reports, model cards, CI jobs, delegation or background monitoring. Provide requested code and concise feedback distinguishing implementation, executed training, evaluation evidence and unverified claims. Preserve cloud sync and university RAG deferrals. Read references/provenance.md for adaptation history.
