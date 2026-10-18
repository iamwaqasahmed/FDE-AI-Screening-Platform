# Week 03 — Retrieval and ML evidence

Week 3 of the six-week engagement. The data protection officer restricted the vendor pathway this morning. Your Week 2 cohort still includes the captures that may no longer leave the authority. By Friday the team has an index that cites the document in force, a vendor extract the memo allows, and a number for the vendor model that survives the proposals.

Hartland's people and counts are for practice. They are not a real health service, and they are not instructions for care.

**Time.** One week, a team of five or six. No facilitator. You open the drop yourselves.
**Who.** Mixed. Each role has a hard problem in the drop. The split is in [The week](01-the-week.md).
**Your work.** A findings file, `answers.jsonl`, `redactions.csv`, `vendor_extract.csv`, one contract, a retrieval card, and an evidence note.
**Done when.** `evidence_check` passes on your folder, including a rerun on a seed you build yourselves, and you have marked the note against the debrief.
**Order.** Top to bottom. Write when a note tells you to stop.
**Debrief.** The practice-seed answer key. Reading it early skips the week. Another seed changes the counts, the dates, and the site names.

## Leave closed

`data/truth`, `data/eval`, `drops/week-4` through `drops/week-6`, `reference_evidence` in this folder, and `evidence_check.key`.

`data/truth` and `data/eval` are the hidden model and the answer key. `drops/week-3` is released by this week's second note. Later drops stay closed until their own week. The reference solution and the key printer are for maintainers. Opening them skips the week.

## What you will produce

Keep the folder outside the repo, or under `work/<team>/week-03/`, which git ignores.

| Artifact | When | Note |
|---|---|---|
| Impact log | Day 1, before any rerun | [02 — Open the drop](02-open-the-drop.md) |
| Retrieval card | Days 1–3 | [03](03-the-baselines.md) through [08](08-answer-the-questions.md) |
| `answers.jsonl`, `redactions.csv` | End of Day 3 | [06](06-cite-refuse-and-resist.md), [07](07-personal-data-and-the-register.md), [08](08-answer-the-questions.md) |
| Contract, then `vendor_extract.csv` | Day 3 | [07](07-personal-data-and-the-register.md), [09](09-restrict-the-cohorts.md) |
| Operating points, claims, the leak | Day 4 | [10](10-labels-you-can-trust.md) through [13](13-the-leak.md) |
| Evidence note | Day 5 | [14 — Write the evidence note](14-write-the-evidence-note.md) |

The checker reads `findings.json`, `answers.jsonl`, `redactions.csv`, `vendor_extract.csv`, `contracts/vendor_extract.yaml`, `retrieval-card.md`, and `evidence-note.md`. Shapes are in [templates](templates/findings.example.json).

## Sequence

| | Note | Day | Lead | What you do |
|---|---|---|---|---|
| 1 | [The week](01-the-week.md) | 1 | Everyone | The job, the roles, the four contracts |
| 2 | [Open the drop](02-open-the-drop.md) | 1 | Product manager, architect | The memo. Stop and write the impact log |
| 3 | [The baselines](03-the-baselines.md) | 1 | Software engineer | Print the questions. Run keyword and TF-IDF. Read ten losses |
| 4 | [Index with status and dates](04-index-with-status-and-dates.md) | 1–2 | Data engineer | A draft never binds. A cited document is not in force because it is cited |
| 5 | [Originals, scans, and duplicates](05-originals-scans-and-duplicates.md) | 2 | Data engineer | PDF, DOCX, XLSX, the scan, and the forwarded copy |
| 6 | [Cite, refuse, and resist](06-cite-refuse-and-resist.md) | 2–3 | Software engineer | The answer file. Four texts that try to instruct you |
| 7 | [Personal data and the register](07-personal-data-and-the-register.md) | 2–3 | Architect, software engineer | Which model may see which text. The contract, before the extract |
| 8 | [Answer the questions](08-answer-the-questions.md) | 3 | Software engineer, data engineer | Beat the baselines on the slices they lost. Write the card |
| 9 | [Restrict the cohorts](09-restrict-the-cohorts.md) | 3 | ML specialist, data scientist | The captures that may still cross. Publish the extract |
| 10 | [Labels you can trust](10-labels-you-can-trust.md) | 3–4 | Data scientist, ML specialist | Routine grade, adjudication, and what is not in the drop |
| 11 | [Operating points and drift](11-operating-points-and-drift.md) | 4 | ML specialist | The model card, by subgroup, and the firmware that moved the scores |
| 12 | [Check the claims](12-check-the-claims.md) | 4 | Consultant, product manager, ML specialist | Three proposals. One number is a subgroup. One deployment did not succeed |
| 13 | [The leak](13-the-leak.md) | 4 | Data scientist | The column written after the outcome, and the honest split |
| 14 | [Write the evidence note](14-write-the-evidence-note.md) | 5 | Consultant, product manager | Two pages, before the debrief |
| 15 | [Check](15-check.md) | 5 | Everyone | Run `evidence_check`, then a second seed |
| 16 | [Debrief](16-debrief.md) | 5 | Everyone | After the note exists |

## Also on the desk

| | |
|---|---|
| What each file is | [data/README.md](../data/README.md) |
| Week 2, and the clusters you are about to reuse | [Week 02](../Week%2002%20-%20Enterprise%20Data/README.md) |
| How to run the check | [15 — Check](15-check.md) |

From `Version 02`, when the folder exists:

```text
python -m course evidence_check --work <your folder>
```

Next: [The week](01-the-week.md).
