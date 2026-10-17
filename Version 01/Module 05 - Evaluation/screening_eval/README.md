# Screening eval

Reference scorer for [Module 05](../README.md). The practice set is the set you need to finish. The instructor file is optional.

Scores the agent on labeled questions. A demo is not a measurement. Each case is sent through [screening_agent](<../../Module 04 - The agent/screening_agent>) `ask`, and the reply is compared with the expected tool, document, numbers, and refusal.

The practice set is [practice_cases.jsonl](../practice_cases.jsonl). Participants read it. Adding a line is optional. [data/eval/cases.jsonl](../../data/eval/cases.jsonl) is the instructor set. The scorer maps older tool names there onto the catalog where it can. A clinic due-count or one person's wait is `unsupported`, not an agent failure.

| Field | Meaning |
|---|---|
| `tool_ok` | The expected tool was called |
| `document_ok` | `document_id` matches |
| `result_ok` | The expected numbers or status are in the tool result |
| `refusal_ok` | A required refusal happened, or a normal answer was not refused |
| `latency_ms` | Wall time around `ask` |
| `model_calls` | How many times the model was asked to continue |
| `error_type` | Why a case failed. Empty when it passed |

| `error_type` | When it is used |
|---|---|
| `wrong_join` | A count, a letter code, or the tool does not match |
| `draft_treated_as_policy` | The 14-day draft is treated as in force |
| `silent_model_treated_as_healthy` | An empty vendor label is described as healthy or as no disease |
| `letter_invents_diagnosis` | A letter answer adds a diagnosis |
| `missed_refusal` | A diagnosis or an unsigned referral was answered |
| `unsupported` | The instructor case asks for a figure the catalog does not return |

The lesson is [Module 05](../README.md).

From the repository root, with no API key:

```text
python -m course screening_eval.check
```

That runs the practice set with a scripted model and fails if any practice case fails. It does not need `data/eval` to be present.

```text
python -m course screening_eval.check --instructor
```

That also prints the instructor report. The practice set must still pass.
