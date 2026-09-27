# Free local evaluation runner

This standard-library Python runner makes **zero model/API calls** and needs no key, extra service, installation or paid API. Responses can be produced manually using an existing subscription, subject to its limits and available models. It is not an automatic subscription API or a verified tool-disabled model host. A prompt asking for no tools does not enforce isolation.

## Workflow

Run `python free_runner.py --help` from this directory. Choose an output directory outside the plugin and the exact model already selected by the user; do not substitute one.

1. `python free_runner.py prepare /absolute/path/to/new-run --model SELECTED_MODEL` freezes the 26 core and 39 A2 cases, owner/reference source excerpts and hashes. It creates separate `subject`, `responses` and `grades` directories plus a reviewer-only oracle. No model runs occur.
2. `python free_runner.py packet /absolute/path/to/new-run CORE-001` prints only that subject packet. Give it to a fresh subscription chat with tools unavailable where supported. Do not supply the oracle, other cases, this reviewer guide or previous responses. If tool disabling cannot be established, label the session manual text-only with isolation unverified; it does **not** satisfy the approved tool-disabled campaign. Obtain authority for that changed evaluation mode before collecting subject responses.
3. Save the original response as a local UTF-8 text file outside the plugin. Import with `python free_runner.py record /absolute/path/to/new-run CORE-001 /absolute/path/to/response.txt --model SELECTED_MODEL --tools none-observed`. Other tool observations are `attempted` and `unknown`. These are operator reports, not machine-verified isolation. Stop the campaign on attempted tools; no repair turns or replacement responses. One recorded response per case is enforced; the runner cannot prevent extra chats outside it. Preserve setup failures in the operator record rather than silently retrying.
4. Review against the separate `reviewer.json` without sending it to the subject. Use `python free_runner.py grade /absolute/path/to/new-run CORE-001 --outcome met --evidence 'Specific response evidence for the required and forbidden outcomes'`. Outcomes are `met`, `violated` or `inconclusive`; a response is never automatically graded. Each grade is saved once. Unknown/attempted tools cannot receive `met`.
5. `python free_runner.py report /absolute/path/to/new-run` shows not-run, ungraded and reviewed totals. It always leaves full functionality false and tool isolation unverified. Text quality is different from native plugin routing and real operations.

Repeat only for the authorised case IDs, with one fresh response per case and no retries. Keep the user's model fixed. Candidate excerpt scope is explicit; linked documents are not automatically loaded. Unavailable supporting context should be reported rather than fetched by the subject. One case per item is representative coverage, not an exhaustive domain test.

## Boundaries and evidence

The runner does not launch a browser, shell subprocess, CLI model, worker or network client. It neither reads credentials nor loads private profiles. It writes only the selected run directory; choose a trusted local path, and keep response files free of private data. Hashes catch accidental packet/response changes; they are not signatures or protection against a malicious operator editing records and hashes together. Explicit user-selected input/output paths remain trusted local operator inputs.

Preparation can run now. The previously approved 65-case tool-disabled evaluation remains blocked until enforced isolation is available; creating this runner does not silently downgrade that requirement. No new campaign is started automatically. No promise of extra subscription allowance or zero underlying subscription cost is made.

Local tests: from `../checks`, run `PYTHONDONTWRITEBYTECODE=1 python -m unittest test_free_runner` only within authorised local-test scope. Tests use synthetic temporary files and no model calls.
