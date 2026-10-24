# The failures

The four names are hallucination, retrieval failure, reasoning gap, and workflow issue. The examples are in [slices/failures.jsonl](../../data/rel-w3d4/slices/failures.jsonl). The type is not on the row. `classify` names the row.

The shell names every row a pass. The copy names each planted failure.

Copy [templates/benchmark.md](templates/benchmark.md) to `work/benchmark.md`. Tie each name to its log id. Record extraction, citation, and journey against the budgets.

Copy [templates/workshop.md](templates/workshop.md) to `work/workshop.md`. The seats are `cdo`, `access-mgr`, `phc-lead`, and `dpo`. The dot-vote in [workshop/dot-vote.json](../../data/rel-w3d4/workshop/dot-vote.json) ranks triage first. That ranking is not the value model.

The shell judge marks a fluent citation correct. The copy checks the calibration subset in [slices/calibration.jsonl](../../data/rel-w3d4/slices/calibration.jsonl). A fluent wrong citation is not a pass.

`intervals.py` is the district slice, with a confidence interval. `experiment.py` reports only the pre-registered metric on [experiment/ab-status.json](../../data/rel-w3d4/experiment/ab-status.json). The contained count is not that metric. Those two are the advanced path. The checks do not require them.

`gate.py` is the regression. A fluent wrong citation is not accepted. The shell CI leaves `evaluation-gate` commented. The copy uncomments the job and runs `tests.test_gate`.

The architect notes which failure is a design bug. The workflow failure is a design bug.
