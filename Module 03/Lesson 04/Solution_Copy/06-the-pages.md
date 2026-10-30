# 06 — The pages

Open the three finished pages and put them beside yours. The eval check reads the benchmark and the workshop. It does not read the experiment page. A miss on that page does not fail a check. The page is still here.

## Benchmark

The blank template is a heading and two empty sections. If the four pairs are missing, the eval check says the report misses a planted failure. If extraction, citation, journey, or budget is missing, it says the report misses a metric against its budget.

The finished page in [benchmark.md](work/benchmark.md) is the one to teach:

- log-night is a hallucination. The reply cites a clause that is not on file.
- log-circular is a retrieval failure. The reply uses a document that is not in force.
- log-friday is a reasoning gap. The offer uses Friday.
- log-approval is a workflow issue. The booking has no approval.

The workflow failure is a design bug.

[failures.jsonl](sources/release/slices/failures.jsonl) does not contain those four names. [metrics.json](sources/release/budget/metrics.json) holds the floors.

## Workshop

The blank template is a heading. If a seat id is missing, the eval check says the workshop notes miss a seat. If the phrase `not the value model` is missing, it says the workshop notes treat the dot-vote as the value model. If the notes put triage in scope, or if they contain a banned sentence, it says the workshop notes put triage in scope.

The finished page in [workshop.md](work/workshop.md) is the one to teach. The seats are `cdo`, `access-mgr`, `phc-lead`, and `dpo`. The dot-vote ranks `p-triage` first, then the vendor bot. That ranking is not the value model.

[seats.md](sources/release/workshop/seats.md) names the four ids. [dot-vote.json](sources/release/workshop/dot-vote.json) is the ranking. The notes do not say triage is in scope, triage is already approved, the assistant may set clinical urgency, the assistant sets clinical urgency, or the external model may receive identified patient data.

## Experiment page

The finished page in [experiment.md](work/experiment.md) says the pre-registered metric is `honest_pending`, the contained count is not the metric, and the comparison uses `honest_pending` only. It does not name a winning arm. [ab-status.md](sources/release/notices/ab-status.md) says the effect is not stated.

Next: [07 — Knowledge](07-knowledge.md).
