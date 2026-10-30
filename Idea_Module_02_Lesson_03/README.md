# Module 02 Lesson 03 — research proposal

Independent curriculum proposal for `rel-m02-l03`, Tests and the receipt. Course files were read and left unchanged. Write scope is this folder only.

**Thesis.** Fixture tests of a deterministic mock are necessary and insufficient. An FDE with no QA department can still automate contract tests, property-based tests, time control, a recorded-versus-live model gate, a seeded mutation, and a usability rubric for low-literacy and caregiver users.

Read `01` through `05` in order: evaluation, sources, architecture, exercises, tradeoffs.

## Labels

`[KEEP]` stays. `[DELETE]` leaves the student path. `[REPLACE]` keeps the target and changes the mechanism. `[ADD]` is new automation. `[GATE]` blocks the day. `[NIGHTLY]` stays off the student laptop. `[TRAP]` is a failure the check must catch. `[DO NOT SNAPSHOT]` must not be an exact expected string.

## Boundary that stays

The student still replaces `calendar_count.py`, `schema.py`, `receipt.py`, and the four tests (`test_calendar.py`, `test_schema.py`, `test_receipt.py`, `test_journey.py`). Checks remain `chk-tests` and `chk-ux`. Foundation scripts remain `status-short` and `caregiver`. `[TRAP]` A receipt test that sleeps for the old delay. `phone-only` / `pop-literacy` stays off the foundation table.
