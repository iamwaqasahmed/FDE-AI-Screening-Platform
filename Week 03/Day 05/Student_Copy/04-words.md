# 04 — Words

[Chapter 03](03-the-brief.md) opened the files. This chapter names the words those files use, before a later chapter asks you to use them. You do not paste a file on this page. If you are lost on this page, scroll to the line that starts with Next. That line is the end of the reading.

## The brief and the sprint

| Word | Meaning |
| --- | --- |
| Rehearsal brief | The client requirements in [rehearsal.md](packet/release/notices/rehearsal.md). The file you write is `rcp/requirements.md` |
| Sponsor sentence | The first line under `cdo` in [role-cards.md](packet/release/workshop/role-cards.md). A list that copies it is not a brief |
| `steer-w3` | The five questions in [steer-w3.md](packet/release/steering/steer-w3.md). The readout answers them |
| Fix, then second, then spec | The order of [the sprint](05-the-sprint.md). The fix is first. The second measurement is next. The spec is last |
| Lead presents | The last line of the sprint. You present. No part is handed to someone else |

## The second run

| Word | Meaning |
| --- | --- |
| In-force document | A citation the asker is allowed to see. Week 3 Day 3 left that rule |
| Unauthorized citation | A citation that is not in force. It is not a citation you keep |
| `slices/before.jsonl` | The public slice. Each row is an output. The file has no label field. Labels stay on the grading service |
| Repair | Replace a citation that is not in force. Leave an in-force citation as it is |
| Second run | Score that slice, then score it again after the repair. The after rate is higher. That is the moved retrieval failure |
| Retrieval | The failure on `log-circular`. The reply used a document that is not in force. The second run cites the in-force document |
| Hallucination | The failure on `log-night`. The reply cites a clause that is not on file. It stays open |
| Reasoning | The failure on `log-friday`. The offer uses Friday. It stays open |
| Workflow | The failure on `log-approval`. The booking has no approval. It stays open |

## The cost

| Word | Meaning |
| --- | --- |
| `cost.label` | The row in [prices.csv](packet/release/finance/prices.csv) that prices one label. Read the sar from that file. Do not copy it onto a page |
| Annotation budget | The two keys in [labels.json](packet/release/budget/labels.json). The fix is priced only when the label spend fits |
| GPU hours | A row on the price sheet. GPU hours are not the cost of this fix |
| Label count | The number of citations the repair changed. The improvement page names that count as labels |

## The spec

| Word | Meaning |
| --- | --- |
| `p-triage` | A story in [seed.json](packet/release/backlog/seed.json). It is a non-goal. A clinician owns urgency |
| `vendor-bot` | A story in the same file. It is a non-goal |
| `req-cite` | The in-scope story. Cite the in-force document. It is not named in the stage-gate file |
| Dot-vote | A ranking you already saw on Day 4. It can put `p-triage` first. That ranking is not the value model |
| `dms` | The system `req-cite` maps to |
| Risk tier | The gate [stage-gate.md](packet/release/gates/stage-gate.md) names. The citation requirement sits on that tier. The stage-gate file does not name `req-cite` |
| `ext-large` | The external model. Patient data stays off it |
| Clinician | The person who owns urgency. The assistant does not assign it |

## The personal lab

| Word | Meaning |
| --- | --- |
| `asker` | Who is asking, on a citation row in [personal.jsonl](packet/release/slices/personal.jsonl) |
| `audience` | Who the document is for. A staff document is not served to a patient |
| `version` | The version on the citation. A kept citation still carries it |
| Floor | The `floor` on a metric row. The value has to clear that floor |
| Keep | Not a field in `personal.jsonl`. Do not add one |

## The pages and the gate

| Word | Meaning |
| --- | --- |
| Benchmark | The four planted failures, with evidence, and the line that the second run moves the retrieval citation |
| Improvement plan | The change, and the cost in labels |
| Readout | Remeasure, Spec, Systems, Backlog, Cost, and Asks. It cites a release file |
| Retro | Keep, Drop, and Open. Each heading has a body |
| Improvement gate | The job in the work workflow. The packet copy is commented. Chapter 07 replaces the work copy |
| Shell | The starter app. The same tests fail beside it |
| Watermark | A mark on a sample. A file that carries it, copied into `work/`, fails a check. The message does not print the mark |

## Seats

| Id | Who |
| --- | --- |
| `cdo` | Layla Al-Harbi, on the role card |
| `access-mgr` | Noura Al-Qahtani, on the role card |
| `phc-lead` | Dr. Hassan Al-Dosari, on the role card |
| `dpo` | Sara Al-Mutairi, on the role card. The readout names this seat for the ruling |
| `med-dir`, `ciso`, `finance` | The other seats on the steering committee, in [steer-w3.md](packet/release/steering/steer-w3.md) |

## What the check will see

| Check | What it reads |
| --- | --- |
| Eval | `repair.py`, `remeasure.py`, `cost.py`, `sprint.md`, `benchmark.md`, `improvement.md`, `knowledge.md`, and the work workflow |
| Rcp | `rcp/requirements.md`, `backlog.py`, and `gates.py` |
| Readout | `readout.md` and `retro.md` |
| Individual | `personal.py` |

A miss on a page fails only the check in that row. You do not run a check until [chapter 10](10-finish.md).

This page is done when you have scanned the tables.

The [concept index](../../../learning/concept-index.md) lists words from the whole course and points back to the page that introduced each one. It is a lookup. It is not the next chapter.

Next: [05 — The sprint](05-the-sprint.md).
