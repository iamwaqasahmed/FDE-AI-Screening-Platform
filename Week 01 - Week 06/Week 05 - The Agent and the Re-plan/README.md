# Week 05 — The agent and the re-plan

Week 5 of the six-week engagement. The Chief Digital Officer wants the pilot at a hospital clinic, and sooner. The press office wants a public line by Friday. By the end of the week the team can say no with a plan, can publish two paragraphs that survive the files, and has an agent that stops when a rule forbids the action.

Hartland's people and counts are for practice. They are not a real health service, and they are not instructions for care.

**Time.** One week, a team of five or six. No facilitator. You open the drop yourselves.
**Who.** Mixed. Each role has a hard problem in the drop. The split is in [The week](01-the-week.md).
**Your work.** A findings file, `backlog.csv`, `sweep.csv`, one contract, `answers.jsonl`, an agent card, a reply, and a public line.
**Done when.** `agent_check` passes on your folder, including a rerun on a seed you build yourselves, and you have marked the reply against the debrief.
**Order.** Top to bottom. Write when a note tells you to stop.
**Debrief.** The practice-seed answer key. Reading it early skips the week. Another seed changes the counts, the pace, and the site names.

## Leave closed

`data/truth`, `data/eval`, `drops/week-6`, `reference_agent` in this folder, and `agent_check.key`.

`data/truth` and `data/eval` are the hidden model and the answer key. `drops/week-5` is released by this week's second note. `drops/week-6` stays closed until its own week. The reference solution and the key printer are for maintainers. Opening them skips the week.

## What you will produce

Keep the folder outside the repo, or under `work/<team>/week-05/`, which git ignores.

| Artifact | When | Note |
|---|---|---|
| Impact log | Day 1, before any rerun | [02 — Open the drop](02-open-the-drop.md) |
| `backlog.csv` | Day 2 | [04 — The backlog](04-the-backlog.md) |
| Re-plan | Day 2 | [05 — The critical path](05-the-critical-path.md) |
| `press-line.md` | Days 2–3 | [07 — The public line](07-the-public-line.md) |
| Contract, then the agent | Days 2–4 | [08](08-what-the-agent-may-do.md) through [12](12-checkpoints-and-a-person.md) |
| `answers.jsonl`, `sweep.csv`, agent card | Day 4 | [09](09-the-baselines.md) through [13](13-score-the-trajectory.md) |
| `cdo-reply.md` | Day 5 | [14 — Write the reply](14-write-the-reply.md) |

The checker reads `findings.json`, `answers.jsonl`, `backlog.csv`, `sweep.csv`, `contracts/agent_trajectory.yaml`, `agent-card.md`, `cdo-reply.md`, and `press-line.md`. Shapes are in [templates](templates/findings.example.json).

## Sequence

| | Note | Day | Lead | What you do |
|---|---|---|---|---|
| 1 | [The week](01-the-week.md) | 1 | Everyone | The job, the roles, the contracts |
| 2 | [Open the drop](02-open-the-drop.md) | 1 | Product manager, consultant | The memo and the query. Stop and write the impact log |
| 3 | [Three asks](03-three-asks.md) | 1–2 | Product manager, architect, consultant | The date, the site, and the variation |
| 4 | [The backlog](04-the-backlog.md) | 2 | Data engineer, product manager | Duplicates without a column, and Heron's pace |
| 5 | [The critical path](05-the-critical-path.md) | 2 | Product manager, consultant | A range, and the constraint that binds |
| 6 | [The gate before the date](06-the-gate-before-the-date.md) | 2–3 | Consultant, product manager | Gate 2, the double count, the closed risk |
| 7 | [The public line](07-the-public-line.md) | 2–3 | Consultant, product manager | Two paragraphs. Stop and write them |
| 8 | [What the agent may do](08-what-the-agent-may-do.md) | 2–3 | Architect, consultant | The tier, the rules, the account, the models |
| 9 | [The baselines](09-the-baselines.md) | 3 | Software engineer | Where one retrieval is not an agent |
| 10 | [State, tools, and the trajectory](10-state-tools-and-the-trajectory.md) | 3 | Software engineer, data engineer | The contract, before the first run |
| 11 | [The veto](11-the-veto.md) | 3–4 | Software engineer, architect | A stop in code, on the action |
| 12 | [Checkpoints and a person](12-checkpoints-and-a-person.md) | 4 | Software engineer, data engineer | Resume, and the sweep |
| 13 | [Score the trajectory](13-score-the-trajectory.md) | 4 | ML specialist, data scientist | Stop and write the card |
| 14 | [Write the reply](14-write-the-reply.md) | 5 | Consultant, product manager | One page, before the debrief |
| 15 | [Check](15-check.md) | 5 | Everyone | Run `agent_check`, then a second seed |
| 16 | [Debrief](16-debrief.md) | 5 | Everyone | After the reply exists |

## Also on the desk

| | |
|---|---|
| What each file is | [data/README.md](../data/README.md) |
| Weeks 2 to 4, which the agent calls | [Week 02](../Week%2002%20-%20Enterprise%20Data/README.md), [Week 03](../Week%2003%20-%20Retrieval%20and%20ML%20Evidence/README.md), [Week 04](../Week%2004%20-%20Graph%20Retrieval%20and%20Integration/README.md) |
| The mock services | [serve/README.md](../problem_simulation/serve/README.md) |
| How to run the check | [15 — Check](15-check.md) |

From `Week 01 - Week 06`, when the folder exists:

```text
python -m course agent_check --work <your folder>
```

Next: [The week](01-the-week.md).
