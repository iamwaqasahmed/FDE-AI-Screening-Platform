# The check

From `problem_simulation`, with your work directory filled in:

```text
python -m alwaha.check eval --release rel-w3d5 --work "..\Week 03\Day 05\work"
python -m alwaha.check rcp --release rel-w3d5 --work "..\Week 03\Day 05\work"
python -m alwaha.check readout --release rel-w3d5 --work "..\Week 03\Day 05\work"
python -m alwaha.check individual --release rel-w3d5 --work "..\Week 03\Day 05\work"
```

`chk-w3-eval` scores the second run. It checks the repair, the before and after citation rates, and the label cost. It also reads the sprint, the benchmark, the improvement plan, the knowledge file, and the improvement gate. A miss says the repair leaves the unauthorized citation, the second run does not move the retrieval failure, the second run misses the held-out slice, the improvement cost misses the price sheet, the report misses a planted failure, or the report misses the second run. It does not print a price, a count, or a doc id. The Day 4 draft on `rel-w3d4` is unchanged.

`chk-w3-rcp` reads `rcp/requirements.md`, the backlog, and the stage gate. A miss says the requirements restate the sponsor sentence, the requirements leave triage in scope, the requirements follow the dot-vote, the requirements miss the rehearsal brief, the backlog keeps a non-goal, or the stage gate skips the risk tier.

`chk-readout` reads `readout.md` and `retro.md` against `steer-w3`. A miss says the readout does not answer the second run, does not name the non-goal, does not leave urgency with a clinician, or does not keep patient data off the external model.

`chk-individual-w3` is the personal lab. `cite` keeps version and audience, and refuses a staff document for a patient. `meets_budget` accepts a metric only at or above its floor. The rows are [slices/personal.jsonl](../../data/rel-w3d5/slices/personal.jsonl). A miss says the citation drops the version or the audience, the citation serves a staff document to a patient, or the metric read ignores its budget.

A watermarked file copied into `work/` fails the check. The message does not print the watermark.

On `practice`, the instructor can play the disagreement:

```text
python -m alwaha.demo.brief --profile practice
```

The lines are that the sponsor asks for triage in the front desk, and that the DPO keeps patient data off `ext-large`. They do not name a non-goal or a price.

Then write `work/knowledge.md` from [templates/knowledge.md](templates/knowledge.md), with two short answers:

1. What did the second run change?
2. Which requirement is out of scope, and why?

The day is done when all four checks print `passed` and the knowledge file has both answers.
