# Week 04 — Graph retrieval and integration

The program map is [README.md](../../README.md). This week is part of [Week 01 — Week 06](../README.md).

Week 4 of the six-week engagement. The letter bureau says a queue failure last week duplicated some letters and lost none. The request file and the dispatch file do not agree. By Friday you can say who was not reached, what must not be sent again, and can answer a question that needs more than one record.

Hartland's people and counts are for practice. They are not a real health service, and they are not instructions for care.

**Time.** One week, you alone. You open the drop yourself.
**Who.** You, wearing every hat in [The week](01-the-week.md). Do every note, in order.
**Your work.** A findings file, `reconciliation.csv`, `resend.csv`, one contract, `answers.jsonl`, a graph card, and an incident note.
**Done when.** `graph_check` passes on your folder, including a rerun on a seed you build yourself, and you have marked the note against the debrief.
**Order.** Top to bottom. Write when a note tells you to stop.
**Debrief.** The practice-seed answer key. Reading it early skips the week. Another seed changes the counts, the dates, and the site names.

## Leave closed

`data/truth`, `data/eval`, `drops/week-5`, `drops/week-6`, `reference_graph` in this folder, and `graph_check.key`.

`data/truth` and `data/eval` are the hidden model and the answer key. `drops/week-4` is released by this week's second note. Later drops stay closed until their own week. The reference solution and the key printer are for maintainers. Opening them skips the week.

## What you will produce

Keep the folder outside the repo, or under `work/week-04/`, which git ignores.

| Artifact | When | Note |
|---|---|---|
| Impact log | Day 1, before any rerun | [02 — Open the drop](02-open-the-drop.md) |
| `reconciliation.csv` | Day 1 | [03 — Keys that mean a letter](03-keys-that-mean-a-letter.md) |
| Cohort notes, C-07 | Days 2–3 | [05](05-the-chase-list.md), [06](06-who-was-not-reached.md) |
| Contract, then `resend.csv` | Days 2–3 | [07](07-the-contract-and-the-agreement.md), [08](08-resend-without-harm.md) |
| `answers.jsonl`, graph card | Days 3–4 | [09](09-the-baselines.md) through [11](11-answer-with-the-path.md) |
| Incident note | Day 5 | [14 — Write the incident note](14-write-the-incident-note.md) |

The checker reads `findings.json`, `answers.jsonl`, `reconciliation.csv`, `resend.csv`, `contracts/bureau_dispatch.yaml`, `graph-card.md`, and `incident-note.md`. Shapes are in [templates](templates/findings.example.json).

## Sequence

| | Note | Day | Hat | What you do |
|---|---|---|---|---|
| 1 | [The week](01-the-week.md) | 1 | You | The job, the hats, the four contracts |
| 2 | [Open the drop](02-open-the-drop.md) | 1 | Be the product manager, then the software engineer | The notice. Stop and write the impact log |
| 3 | [Keys that mean a letter](03-keys-that-mean-a-letter.md) | 1 | Be the software engineer, then the data engineer | A row is not a letter. Publish the reconciliation |
| 4 | [The precedent](04-the-precedent.md) | 1–2 | Be the product manager, then the data engineer, then the consultant | The same failure, a year and a half ago |
| 5 | [The chase list](05-the-chase-list.md) | 2 | Be the data scientist, then the data engineer | The programme's list is not the overdue cohort |
| 6 | [Who was not reached](06-who-was-not-reached.md) | 2–3 | Be the data scientist, then the ML specialist | C-07, in people, and the clock at the clinic |
| 7 | [The contract and the agreement](07-the-contract-and-the-agreement.md) | 2–3 | Be the architect, then the consultant | What the bureau may hold, and for how long |
| 8 | [Re-send without harm](08-resend-without-harm.md) | 3 | Be the software engineer, then the product manager | Hold the people a second letter would hurt |
| 9 | [The baselines](09-the-baselines.md) | 3 | Be the software engineer | Where one document is not enough |
| 10 | [Build the graph](10-build-the-graph.md) | 3–4 | Be the data engineer, then the architect | Edges with a source and a date |
| 11 | [Answer with the path](11-answer-with-the-path.md) | 4 | Be the software engineer, then the data engineer | Cite the records the answer walked |
| 12 | [What the calls say](12-what-the-calls-say.md) | 3–4 | Be the ML specialist, then the data scientist | Half the "letter never arrived" calls are uncoded |
| 13 | [Cost and owners](13-cost-and-owners.md) | 4 | Be the consultant, then the product manager | Pounds, and the decisions a person still owns |
| 14 | [Write the incident note](14-write-the-incident-note.md) | 5 | Be the consultant, then the product manager | Two pages, before the debrief |
| 15 | [Check](15-check.md) | 5 | You | Run `graph_check`, then a second seed |
| 16 | [Debrief](16-debrief.md) | 5 | You | After the note exists |

## Also on the desk

| | |
|---|---|
| What each file is | [data/README.md](../data/README.md) |
| Week 2 clusters, and Week 3's pilot scope | [Week 02](../Week%2002%20-%20Enterprise%20Data/README.md), [Week 03](../Week%2003%20-%20Retrieval%20and%20ML%20Evidence/README.md) |
| How to run the check | [15 — Check](15-check.md) |

From `Week 01 - Week 06`, when the folder exists:

```text
python -m course graph_check --work <your folder>
```

Next: [The week](01-the-week.md).
