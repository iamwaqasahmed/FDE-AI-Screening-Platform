# Week 02 — Enterprise data

The program map is [README.md](../../README.md). This week is part of [Week 01 — Week 06](../README.md).

Week 2 of the six-week engagement. The ministry published a new registry extract this morning. Your Week 1 code still runs on the old file. By Friday the team has one cluster per person, counts it will stand behind, contracts that fail loudly, a warehouse model, and a release plan that survives the freeze.

Hartland's people and counts are for practice. They are not a real health service, and they are not instructions for care.

**Time.** One week, a team of five or six. No facilitator. You open the drop yourselves.
**Who.** Mixed. Each role has a hard problem in the drop. The split is in [The week](01-the-week.md).
**Your work.** A findings file, `clusters.csv`, `pathway_rules.csv`, eleven feed contracts, a model, and a data note.
**Done when.** `enterprise_check` passes on your folder, including a rerun on a seed you build yourselves, and you have marked the note against the debrief.
**Order.** Top to bottom. Write when a note tells you to stop.
**Debrief.** The practice-seed answer key. Reading it early skips the week. Another seed changes the counts, the dates, and the site names.

## Leave closed

`data/truth`, `data/eval`, `drops/week-3` through `drops/week-6`, `reference_enterprise` in this folder, and `enterprise_check.key`.

`data/truth` and `data/eval` are the hidden model and the answer key. `drops/week-2` is released by this week's first note. Later drops stay closed until their own week. The reference solution and the key printer are for maintainers. Opening them skips the week.

## What you will produce

Keep the folder outside the repo, or under `work/<team>/week-02/`, which git ignores.

| Artifact | When | Note |
|---|---|---|
| Drop log | Day 1, before any fix | [02 — Open the drop](02-open-the-drop.md) |
| Eleven contracts | Days 1–2, before loaders | [03 — Contracts first](03-contracts-first.md) |
| `clusters.csv` | End of Day 3 | [06 — Resolve identity](06-resolve-identity.md) |
| Pathway rules, cohorts | Days 3–4 | [08](08-pathway-by-site-and-date.md), [09](09-cohorts.md) |
| Model, release plan, data note | Day 5 | [10](10-the-warehouse-model.md), [11](11-release-and-the-freeze.md), [12](12-write-the-data-note.md) |

The checker reads `findings.json`, `clusters.csv`, `pathway_rules.csv`, `contracts/*.yaml`, `model.md`, and `data-note.md`. Shapes are in [templates](templates/findings.example.json).

## Sequence

| | Note | Day | Lead | What you do |
|---|---|---|---|---|
| 1 | [The week](01-the-week.md) | 1 | Everyone | The job, the roles, the two contracts |
| 2 | [Open the drop](02-open-the-drop.md) | 1 | Data engineer | Diff version 3. Stop and write the drop log |
| 3 | [Contracts first](03-contracts-first.md) | 1–2 | Architect | Eleven feeds. A silent drop is a failure |
| 4 | [The APIs](04-the-apis.md) | 2 | Software engineer | Version 3 of the API is not version 3 of the file |
| 5 | [Keys over time](05-keys-over-time.md) | 2 | Data engineer | Who owns each key, and when it was valid |
| 6 | [Resolve identity](06-resolve-identity.md) | 2–3 | Data engineer | One cluster per person. Publish it by Day 3 |
| 7 | [Count people](07-count-people.md) | 3 | Data engineer | Eligible people, and coverage the warehouse missed |
| 8 | [Pathway by site and date](08-pathway-by-site-and-date.md) | 3–4 | Data scientist | The rule that applied, not the register's status |
| 9 | [Cohorts](09-cohorts.md) | 4 | Data scientist, ML | Rows, then people, then an upper bound |
| 10 | [The warehouse model](10-the-warehouse-model.md) | 4–5 | Architect | A person key, validity dates, rules that cite clauses |
| 11 | [Release and the freeze](11-release-and-the-freeze.md) | 4–5 | Product manager | The window you missed, and the one you can use |
| 12 | [Write the data note](12-write-the-data-note.md) | 5 | Consultant | Two pages, before the debrief |
| 13 | [Check](13-check.md) | 5 | Everyone | Run `enterprise_check`, then a second seed |
| 14 | [Debrief](14-debrief.md) | 5 | Everyone | After the note exists |

## Also on the desk

| | |
|---|---|
| What each file is | [data/README.md](../data/README.md) |
| Week 1, and the code you are about to rerun | [Week 01](../Week%2001%20-%20Problem%20Discovery/README.md) |
| How to run the check | [13 — Check](13-check.md) |

From `Week 01 - Week 06`, when the folder exists:

```text
python -m course enterprise_check --work <your folder>
```

Next: [The week](01-the-week.md).
