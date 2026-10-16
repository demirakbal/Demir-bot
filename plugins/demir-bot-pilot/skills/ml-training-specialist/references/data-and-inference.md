# Data quality, lineage and inference delivery

Use for a concrete data/ML pipeline or inference feature; skip unrelated code and simple fixed-data explanations. This reusable contract extends the existing ML specialist; it does not create a dataset, training run, model registry or serving endpoint.

## Establish the actual data contract

Read the supplied schema, pipeline and task/version before implementation. Name record identity, unit of prediction, target availability time, valid units/ranges, missing-value semantics, duplicates, label source and split policy. Distinguish rejected records, repaired records and true zero/empty values. Preserve a minimal dataset/version locator, licensed origin and transformation lineage rather than copying private rows into a report. Model artifacts point to their exact training-data/preprocessing/configuration versions when available; unknown lineage remains unknown.

Define split invariants before fitting: entity/time leakage, near duplicates, future-derived features and label-conditioned filtering. Fit learned preprocessing on training data only, preserve a genuinely held-out evaluation boundary and compare against a meaningful simple baseline on the same population and metric. Reusing a saved split is not proof its construction was sound. A metric improvement is not a fair comparison if preprocessing, sample population, hardware or data access changed.

## Implement inference consistently

Use the project's existing framework/version and endpoint/batch path. Preserve feature order, shapes/dtypes, normalization, vocabulary/tokenization, missing/unknown handling and label mapping from the trained artifact. Validate user-controlled size/shape/resource bounds at the relevant boundary; do not load arbitrary serialized code or downloaded weights incidentally. Distinguish a malformed request, unavailable model, resource exhaustion and uncertain partial batch outcome. Avoid returning raw private input or internal secrets in errors.

Name the supported execution device and actual model version, warm/cold behavior, batching limits, cancellation and response schema. Keep service auth, rate/concurrency policy, model replacement and rollback with the existing project owner. A fallback must be disclosed and fit the same task; never silently substitute a model or present a heuristic as model output. Deployment, downloads, training and paid compute remain separate actions.

## Performance and acceptance

For an authorized measurement, record workload/input sizes, model/preprocessing version, device/runtime, cold versus warm state, batch/concurrency, sample count, latency distribution, throughput, memory/error behavior and quality trade-off. Throughput and individual response latency answer different questions. Do not benchmark, profile, sweep parameters or claim speedups from this guidance alone.

Expected example, not a run: a requested publication classifier uses the supplied labeled split, fits its vocabulary on training records, persists that vocabulary with the model, and applies the same transformation to inference; a held-out score stays separate from training metrics. No-action example: editing a plot label does not trigger a data audit, model training or serving migration.

Return the scoped source change, actual input/output contract and supported failure/rollback behavior. Mark data quality, leakage, reproducibility and inference/runtime throughput unverified when not examined or executed. Required missing project/data/model/access remains a blocker rather than a fabricated demonstration.
