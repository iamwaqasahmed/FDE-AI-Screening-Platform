# Module 03 — Retrieval

The program map is [README.md](../../README.md). This module is part of [Week 00 — Self Paced](../README.md).

Teach the agent where a rule comes from. The corpus holds an issued procedure and a stricter draft. Both can look relevant. A search that returns only the closest paragraph will treat the draft as policy.

The Module 02 tools still do the counting. Retrieval does not replace them.

**Time.** About half a day.
**Who.** [target_audience.md](../../target_audience.md). Same case for the whole group.
**Your work.** Read the notes, then `retrieve` in [screening_retrieval](screening_retrieval). The package is the reference.
**Done when.** The checker passes, and you can quote a passage with its status still `draft` when the document is a draft.
**Code.** The reference retriever is in [screening_retrieval](screening_retrieval).
**Check.** `python -m course screening_retrieval.check` from `Week 00 - Self Paced`.

## Leave closed

`data/truth`, `data/eval`, and `problem_simulation/config.yaml`. Retrieval reads [data/corpus](../data/corpus) only.

## Sequence

| | Note | What you do |
|---|---|---|
| 1 | [Why retrieval is not search](01-why-retrieval.md) | See why the closest paragraph can be the wrong rule. |
| 2 | [The corpus](02-the-corpus.md) | Learn the seven files and the status column. |
| 3 | [Chunks](03-chunks.md) | Split each file into sections. |
| 4 | [The status rule](04-status-rule.md) | Keep a draft from becoming current policy. |
| 5 | [Five questions](05-five-questions.md) | Ask the questions the service actually gets. |
| 6 | [Check](06-check.md) | Run the checker. |

Next: [Why retrieval is not search](01-why-retrieval.md).
