# Week 01 — Problem discovery

Week 1 of the six-week engagement. The Chief Digital Officer wants the vendor model live. Your team has the base drop and five days to find which problems are real, how big they are, and what has to come first.

Hartland's people and counts are for practice. They are not a real health service, and they are not instructions for care.

**Time.** One week, a team of five or six.
**Who.** Mixed. Each role has a hard problem in the drop. The split is in [The engagement](01-the-engagement.md).
**Your work.** An ask log, a findings file, twelve interview scripts, a note per persona, and a brief.
**Done when.** `discovery_check` passes on your folder, and you have marked the brief against the debrief.
**Order.** Top to bottom. Write when a note tells you to stop.
**Debrief.** The practice-seed answer key. Reading it early skips the week. Another seed changes the counts and the dates. Code that only works on the practice names will fail that rerun.

## Leave closed

`data/truth`, `data/eval`, `drops/week-3` through `drops/week-6`, and `reference_discovery` in this folder. Open `drops/week-2` at the start of Week 2, and each later drop at the start of its own week.

`data/truth` and `data/eval` are the hidden model and the answer key. The reference solution is for maintainers.

## What you will produce

Keep the folder outside the repo, or under `work/`, which git ignores.

| Artifact | When | Note |
|---|---|---|
| Ask log | Day 1, before the extracts | [02 — The ask](02-the-ask.md) |
| Systems table and profile | Days 1–2 | [03](03-systems-of-record.md), [04](04-profile-before-you-trust.md) |
| Timeline | Day 3 | [05 — The timeline](05-the-timeline.md) |
| Interview scripts and notes | Days 3–4 | [06 — Interviews](06-interviews.md) |
| Sizing and ranking | Days 4–5 | [08](08-size-the-problems.md), [09](09-rank-the-opportunities.md) |
| `findings.json`, notes, brief | Day 5 | [10 — Write the brief](10-write-the-brief.md) |

The checker reads `findings.json`, `interviews/<persona>.txt`, `notes/<persona>.md`, and `brief.md`. Shapes are in [templates](templates/findings.example.json).

## Sequence

| | Note | Day | What you do |
|---|---|---|---|
| 1 | [The engagement](01-the-engagement.md) | 1 | The team, the roles, the limit |
| 2 | [The ask](02-the-ask.md) | 1 | Read the board paper. Stop and write the ask log |
| 3 | [Systems of record](03-systems-of-record.md) | 1 | Nineteen notes, one owner that is blank |
| 4 | [Profile before you trust](04-profile-before-you-trust.md) | 2 | Schemas, dates, duplicates, units. Keep the code |
| 5 | [The timeline](05-the-timeline.md) | 3 | Tickets, notices, and the months the calls move |
| 6 | [Interviews](06-interviews.md) | 3–4 | Twelve questions each. Write down what they did not say first |
| 7 | [Walk one person](07-walk-one-person.md) | 4 | Seven keys, and where the link breaks |
| 8 | [Size the problems](08-size-the-problems.md) | 4 | People, waits, reminders, money |
| 9 | [Rank the opportunities](09-rank-the-opportunities.md) | 5 | Eight opportunities, blockers, and what must come first |
| 10 | [Write the brief](10-write-the-brief.md) | 5 | Two pages. Same facts, two readers |
| 11 | [Check](11-check.md) | 5 | Run `discovery_check` |
| 12 | [Debrief](12-debrief.md) | 5 | After the brief exists |

## Also on the desk

| | |
|---|---|
| What each file is | [data/README.md](../data/README.md) |
| Words for the pathway | [Health language](../../health_language.md) |
| How to run the check | [11 — Check](11-check.md) |

From `Week 01 - Week 06`, when the brief and the findings exist:

```text
python -m course discovery_check --work <your folder>
```

Next: [The engagement](01-the-engagement.md).
