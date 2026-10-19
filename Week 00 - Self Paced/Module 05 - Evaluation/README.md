# Module 05 — Evaluation

The program map is [README.md](../../README.md). This module is part of [Week 00 — Self Paced](../README.md).

Measure the agent. A demo is not a measurement.

The practice set is already in this folder. The scorer runs `ask` on each case and records whether the tool, the document, the numbers, and the refusal match. `data/eval` is the instructor set. Leave it closed until you choose to print the instructor report. The practice check is enough to finish.

**Time.** About half a day.
**Who.** [target_audience.md](../../target_audience.md). Same case for the whole group.
**Your work.** Read the eight practice lines, run the scorer, and name a failure from the list in this module. Adding a line is optional.
**Done when.** `Practice evaluation passed.` You can point at a score row and say which field failed.
**Practice cases.** [practice_cases.jsonl](practice_cases.jsonl)
**Check.** `python -m course screening_eval.check` from `Week 00 - Self Paced`. No API key.

## Leave closed

`data/truth`, `data/eval`, and `problem_simulation/config.yaml`, until you deliberately run the instructor report.

## Sequence

| | Note | What you do |
|---|---|---|
| 1 | [Why measure](01-why-measure.md) | See why one good demo is not enough. |
| 2 | [The practice set](02-the-practice-set.md) | Read the fields in one case. |
| 3 | [What is recorded](03-what-is-recorded.md) | Tool, document, result, refusal, latency, model calls. |
| 4 | [Error types](04-error-types.md) | Name the failure instead of saying "it broke." |
| 5 | [Check](05-check.md) | Run the practice set. The instructor report is optional. |

Next: [Why measure](01-why-measure.md).
