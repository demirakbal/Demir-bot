# Preserve zero: written before/after

Status: illustrative source, NOT RUN. Contract for this synthetic example: `amount` is a number or None; only None means missing. Zero and negative numbers are valid. No other accepted-input change is requested.

Request: “Fix display_amount so zero stays zero; keep the existing API. Don't write or run tests or builds.”

Starting source in start.py uses truthiness, so zero selects the fallback. The narrowly proposed correction is:

```python
def display_amount(amount, fallback=10):
    return fallback if amount is None else amount
```

Representative explanation: “Only None now uses the fallback. A supplied zero or negative amount is preserved. The function name, parameters and default stay the same. This was inspected as source; it was not executed.”

Expected values by reasoning: None with the default gives 10; 0 gives 0; -2 gives -2; a supplied fallback is used only for None. These are illustrative expectations, not test output. In a real project inspect the caller/input contract before applying this pattern; do not assume all false/empty values mean the same thing. Stop at the authorized source change and explanation, with no automatic test/commit/deployment.
