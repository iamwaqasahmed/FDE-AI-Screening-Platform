# Screening handoff

Checks the pages left with Hartland. It does not call a model and it does not read `data/truth`.

The pack is in [handoff](../handoff): an executive page, a clinical page, a runbook, and an owner note. Both audience pages name Hill Counties Health Centre, Oakridge Primary Care, and North City Eye Clinic. The executive page keeps the 93% hospital slide off the primary-care pilot. The clinical page keeps the grader as signer and the 14-day pathway as a draft. The owner note leaves `clinical_safety_owner` unassigned and `pilot_starts` set to `no`.

The lesson is [Module 07](<../Module 07 - The handoff/README.md>).

From the repository root:

```text
python -m screening_handoff.check
```
