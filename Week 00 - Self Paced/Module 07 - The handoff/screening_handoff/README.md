# Screening handoff

Checker for the reference pack in [Module 07](../README.md). It reads the pages. It does not write them.

Checks the pages left with Hartland. It does not call a model and it does not read `data/truth`.

The pack is in [handoff](../../handoff): an executive page, a clinical page, a runbook, and an owner note. Both audience pages name Hill Counties Health Centre, Oakridge Primary Care, and North City Eye Clinic. The executive page keeps the 93% hospital slide off the primary-care pilot. The clinical page keeps the grader as signer and the 14-day pathway as a draft. The owner note leaves `clinical_safety_owner` unassigned and `pilot_starts` set to `no`.

The lesson is [Module 07](../README.md).

From `Week 00 - Self Paced`:

```text
python -m course screening_handoff.check
```
