# 06 — The pages

Open the five finished pages and put them beside yours. A blank section makes one check name the miss. The other checks do not read that page.

## Benchmark

An empty benchmark makes the eval check say the report misses a planted failure, and the report misses the second run.

[benchmark.md](work/benchmark.md) names `log-night` with hallucination, `log-circular` with retrieval, `log-friday` with reasoning, and `log-approval` with workflow. It also says the second run moves the retrieval citation. The other three failures stay open. That is expected. The four names are the Lesson 4 failures. Only the retrieval line moved.

## Improvement

A page that does not name the label cost makes the eval check say the improvement plan misses the label cost. The message does not print a price.

[improvement.md](work/improvement.md) prices the fix with `cost.label`. The count of labels is the number of citations the repair changed. GPU hours are not the cost of this fix. Read the sar for `cost.label` in [prices.csv](sources/release/finance/prices.csv). Do not copy that amount onto the page.

## Rehearsal brief

A page that copies the sponsor sentence makes the rcp check say the requirements restate the sponsor sentence, the requirements leave triage in scope, and the requirements miss the rehearsal brief. Putting triage in scope, or leaving `p-triage` out of Non-goals, makes the rcp check say the requirements leave triage in scope. Dropping `not the value model` makes the rcp check say the requirements follow the dot-vote. A page that misses the brief's facts makes the rcp check say the requirements miss the rehearsal brief. The message does not name the missing fact.

[rcp/requirements.md](work/rcp/requirements.md) keeps the headings. Scope cites the in-force document and keeps patient data off `ext-large`. It does not contain the sponsor sentence. Priorities say the ranking is not the value model. Non-goals name `p-triage`, `vendor-bot`, and a clinician who owns urgency. Systems map `req-cite` to `dms`. Gates put that requirement on the risk tier named in [stage-gate.md](sources/release/gates/stage-gate.md). That file does not name `req-cite`. Evidence names `dpo`, the seats, and the citation the second run moved. [role-cards.md](sources/release/workshop/role-cards.md) holds the sponsor sentence on the CDO card. The brief does not copy it.

## Readout

[readout.md](work/readout.md) answers the second run, names `p-triage` as a non-goal, leaves urgency with a clinician, keeps patient data off `ext-large`, names the backlog, prices the fix with `cost.label`, names `dms`, and cites `slices/before.jsonl` and `gates/stage-gate.md`. Asks is not empty. `dpo` holds the ruling. A miss on one of those facts fails only the readout check. The message does not print a price.

## Retro

[retro.md](work/retro.md) has Keep, Drop, and Open, each with a sentence. An empty heading makes the readout check say the retro note is missing a heading. The message does not name the heading. Drop is a requirements list that copies the sponsor sentence. Open is the three failures the second run did not move.

Next: [07 — Knowledge](07-knowledge.md).
