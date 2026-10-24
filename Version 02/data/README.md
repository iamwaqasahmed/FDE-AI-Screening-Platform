# Participant packs

The practice packs are stored in git so the day notes can link to them. Running a build again rewrites the same files for that release.

| Release | What it is |
|---|---|
| [rel-w1d1/](rel-w1d1/README.md) | Week 1, Day 1 kickoff |
| [rel-w1d2/](rel-w1d2/README.md) | Week 1, Day 2 extracts and samples |
| [rel-w1d3/](rel-w1d3/README.md) | Week 1, Day 3 events, calendar, and criteria |
| [rel-w1d4/](rel-w1d4/README.md) | Week 1, Day 4 approval rules, scenarios, and tools |
| [rel-w1d5/](rel-w1d5/README.md) | Week 1, Day 5 steering questions and failure scenarios |
| [rel-w2d1/](rel-w2d1/README.md) | Week 2, Day 1 FHIR v2 notice, sign-in, and one status scenario |
| [rel-w2d2/](rel-w2d2/README.md) | Week 2, Day 2 webhooks, cancellation events, and the wait-time extract |
| [rel-w2d3/](rel-w2d3/README.md) | Week 2, Day 3 receipt timing, access clauses, and usability scripts |
| [rel-w2d4/](rel-w2d4/README.md) | Week 2, Day 4 deployment standard, credentials, and the inference endpoint |
| [rel-w2d5/](rel-w2d5/README.md) | Week 2, Day 5 change request for Ain and the nightly schedule file |
| [rel-w3d1/](rel-w3d1/README.md) | Week 3, Day 1 approved history, annotation guideline, and fidelity card |
| [rel-w3d2/](rel-w3d2/README.md) | Week 3, Day 2 signed ruling, GPU quota, and the model register |
| [rel-w3d3/](rel-w3d3/README.md) | Week 3, Day 3 criteria v4, the change feed, and the document store |
| [rel-w3d4/](rel-w3d4/README.md) | Week 3, Day 4 hidden-test protocol, judge calibration, and the eye-screening campaign |
| [rel-w3d5/](rel-w3d5/README.md) | Week 3, Day 5 rehearsal brief, price sheet, and steering questions |
| [rel-w4d1/](rel-w4d1/README.md) | Week 4, Day 1 attack window, PHI-in-logs notice, and the first data-subject requests |
| [rel-w4d2/](rel-w4d2/README.md) | Week 4, Day 2 incident replay, Ramadan-hours circular, and shadow-extract |

From `problem_simulation`:

```text
python -m alwaha.build --profile practice --release rel-w1d1
python -m alwaha.build --profile practice --release rel-w1d2
python -m alwaha.build --profile practice --release rel-w1d3
python -m alwaha.build --profile practice --release rel-w1d4
python -m alwaha.build --profile practice --release rel-w1d5
python -m alwaha.build --profile practice --release rel-w2d1
python -m alwaha.build --profile practice --release rel-w2d2
python -m alwaha.build --profile practice --release rel-w2d3
python -m alwaha.build --profile practice --release rel-w2d4
python -m alwaha.build --profile practice --release rel-w2d5
python -m alwaha.build --profile practice --release rel-w3d1
python -m alwaha.build --profile practice --release rel-w3d2
python -m alwaha.build --profile practice --release rel-w3d3
python -m alwaha.build --profile practice --release rel-w3d4
python -m alwaha.build --profile practice --release rel-w3d5
python -m alwaha.build --profile practice --release rel-w4d1
python -m alwaha.build --profile practice --release rel-w4d2
```

`problem_simulation/build/` holds the facilitator truth for the same seed. That folder stays out of git. Leave it closed.
