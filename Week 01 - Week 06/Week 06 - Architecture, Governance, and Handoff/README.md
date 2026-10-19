# Week 06 — Architecture, governance, and handoff

The program map is [README.md](../../README.md). This week is part of [Week 01 — Week 06](../README.md).

Week 6 of the six-week engagement. A clinical director has agreed to be clinical safety owner, with conditions. The owners register is not updated. By Friday you can say why the pilot stays stopped, can show a design that denies what the rules deny, and can hand over a pack the authority can run and govern.

Hartland's people and counts are for practice. They are not a real health service, and they are not instructions for care.

**Time.** One week, you alone. You open the drop yourself.
**Who.** You, wearing every hat in [The week](01-the-week.md). Do every note, in order.
**Your work.** A findings file, three CSV files, a production contract, a Dockerfile, four decision records, two governance records, two pages, and a runbook.
**Done when.** `handoff_check` passes on your folder, including a rerun on a seed you build yourself, and you have marked the pages against the debrief.
**Order.** Top to bottom. Write when a note tells you to stop.
**Debrief.** The practice-seed answer key. Reading it early skips the week. Another seed changes the counts, the account ids, and the site names.

## Leave closed

`data/truth`, `data/eval`, `reference_handoff` in this folder, and `handoff_check.key`.

`data/truth` and `data/eval` are the hidden model and the answer key. `drops/week-6` is released by this week's second note. The reference solution and the key printer are for maintainers. Opening them skips the week.

## What you will produce

Keep the folder outside the repo, or under `work/week-06/`, which git ignores.

| Artifact | When | Note |
|---|---|---|
| Impact log | Day 1, before any rewrite | [02 — Open the drop](02-open-the-drop.md) |
| `conditions.md` | Days 1–2 | [03 — Five conditions](03-five-conditions.md) |
| `flows.csv`, `threats.csv` | Days 2–3 | [06](06-flows-across-zones.md), [07](07-the-threat-model.md) |
| Contract and Dockerfile | Days 3–4 | [09](09-from-prototype-to-production.md), [10](10-the-production-contract.md) |
| Four decision records | Days 3–4 | [11 — Decisions on the record](11-decisions-on-the-record.md) |
| Governance records, `hazard-log.csv` | Day 4 | [12](12-the-governance-pack.md), [13](13-the-hazard-log.md) |
| Two pages and a runbook | Day 5 | [14 — Write the handoff](14-write-the-handoff.md) |

The checker reads `findings.json`, `flows.csv`, `threats.csv`, `hazard-log.csv`, `contracts/production.yaml`, `deploy/Dockerfile`, `adr/ADR-01.md` through `adr/ADR-04.md`, `governance/transparency-record.yaml`, `governance/model-card.yaml`, `executive-page.md`, `clinical-page.md`, and `runbook.md`. Shapes are in [templates](templates/findings.example.json).

## Sequence

| | Note | Day | Hat | What you do |
|---|---|---|---|---|
| 1 | [The week](01-the-week.md) | 1 | You | The job, the hats, the contracts |
| 2 | [Open the drop](02-open-the-drop.md) | 1 | Be the product manager, then the consultant | The memo. Stop and write the impact log |
| 3 | [Five conditions](03-five-conditions.md) | 1–2 | Be the product manager, then the consultant, then the data scientist | Who acts, and who confirms |
| 4 | [The register stays blank](04-the-register-stays-blank.md) | 2 | Be the product manager | Risks, the blank rows, Gate 3 |
| 5 | [The estate as it runs](05-the-estate-as-it-runs.md) | 2 | Be the architect | Zones, tiers, and where the photographs sit |
| 6 | [Flows across zones](06-flows-across-zones.md) | 2–3 | Be the architect, then the data engineer | What is allowed, denied, and pending |
| 7 | [The threat model](07-the-threat-model.md) | 3 | Be the architect, then the software engineer | Four threats, and which ones are still live |
| 8 | [Service levels](08-service-levels.md) | 3 | Be the software engineer, then the architect | The hour the design has to meet |
| 9 | [From prototype to production](09-from-prototype-to-production.md) | 3–4 | Be the software engineer | The Week 00 - Self Paced container against the standards |
| 10 | [The production contract](10-the-production-contract.md) | 4 | Be the software engineer, then the data engineer | The contract and the Dockerfile |
| 11 | [Decisions on the record](11-decisions-on-the-record.md) | 3–4 | Be the architect | Four proposed decisions. Stop and write them |
| 12 | [The governance pack](12-the-governance-pack.md) | 4 | Be the ML specialist, then the architect, then the consultant | Two tiers, two records. Stop and write them |
| 13 | [The hazard log](13-the-hazard-log.md) | 4 | Be the ML specialist, then the data scientist | Causes from the files. The signature stays blank |
| 14 | [Write the handoff](14-write-the-handoff.md) | 5 | Be the consultant, then the product manager, then the software engineer | Two pages and a runbook, before the debrief |
| 15 | [Check](15-check.md) | 5 | You | Run `handoff_check`, then a second seed |
| 16 | [Debrief](16-debrief.md) | 5 | You | After the pages exist |

## Also on the desk

| | |
|---|---|
| What each file is | [data/README.md](../data/README.md) |
| Weeks 2 to 5 | [Week 02](../Week%2002%20-%20Enterprise%20Data/README.md), [Week 03](../Week%2003%20-%20Retrieval%20and%20ML%20Evidence/README.md), [Week 04](../Week%2004%20-%20Graph%20Retrieval%20and%20Integration/README.md), [Week 05](../Week%2005%20-%20The%20Agent%20and%20the%20Re-plan/README.md) |
| The Week 00 - Self Paced container and handoff | [Dockerfile](../../Week%2000%20-%20Self%20Paced/Dockerfile), [handoff](../../Week%2000%20-%20Self%20Paced/handoff/README.md) |
| The mock services and the published levels | [serve/README.md](../problem_simulation/serve/README.md) |
| How to run the check | [15 — Check](15-check.md) |

From `Week 01 - Week 06`, when the folder exists:

```text
python -m course handoff_check --work <your folder>
```

Next: [The week](01-the-week.md).
