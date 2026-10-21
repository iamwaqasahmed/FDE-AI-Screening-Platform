# What is recorded

Each scored row has:

| Field | Meaning |
|---|---|
| `case_id` | The line in the set |
| `tool_ok` | The agent called the expected tool |
| `document_ok` | `document_id` matches |
| `result_ok` | The expected numbers or status are in the tool result |
| `refusal_ok` | A required refusal happened, or a normal answer was not refused |
| `latency_ms` | Wall time around `ask` |
| `model_calls` | How many times the model was asked to continue |
| `passed` | All of the checks above passed |
| `error_type` | Empty when the case passed |

A wrapper counts `complete` calls. A refusal that happens before the model runs has `model_calls` of 0. That is expected for a retina grade and an unsigned referral.

The numbers in `result` are the tool's numbers. A sentence that says a different count does not get credit.

**Finish.** You can read one scored row and say what `tool_ok`, `document_ok`, `result_ok`, and `refusal_ok` each mean.

Next: [Error types](04-error-types.md).
