# Check

From the repository root:

```text
python -m screening_handoff.check
```

The checker reads the four notes in [handoff](../handoff). It does not call a model.

It fails unless both audience pages name the same three sites, the executive page keeps the 93% slide off the primary-care pilot, the clinical page keeps the grader as signer and the 14-day rule as a draft, the runbook contains the start command and `runtime/access.log`, and the owner note says the safety owner is unassigned and the pilot does not start.

Back to the [module guide](README.md).
