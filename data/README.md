# Participant packs

The practice packs are stored in git so the day notes can link to them. Running a build again rewrites the same files for that release.

| Release | What it is |
|---|---|
| [rel-m01-l01/](rel-m01-l01/README.md) | Module 1, Lesson 1. Kickoff |
| [rel-m01-l02/](rel-m01-l02/README.md) | Module 1, Lesson 2. Extracts and samples |
| [rel-m01-l03/](rel-m01-l03/README.md) | Module 1, Lesson 3. Events, calendar, and criteria |
| [rel-m01-l04/](rel-m01-l04/README.md) | Module 1, Lesson 4. Approval rules, scenarios, and tools |
| [rel-m01-l05/](rel-m01-l05/README.md) | Module 1, Lesson 5. Steering questions and failure scenarios |
| [rel-m02-l01/](rel-m02-l01/README.md) | Module 2, Lesson 1. FHIR v2 notice, sign-in, and one status scenario |
| [rel-m02-l02/](rel-m02-l02/README.md) | Module 2, Lesson 2. Webhooks, cancellation events, and the wait-time extract |
| [rel-m02-l03/](rel-m02-l03/README.md) | Module 2, Lesson 3. Receipt timing, access clauses, and usability scripts |
| [rel-m02-l04/](rel-m02-l04/README.md) | Module 2, Lesson 4. Deployment standard, credentials, and the inference endpoint |
| [rel-m02-l05/](rel-m02-l05/README.md) | Module 2, Lesson 5. Change request for Ain and the nightly schedule file |
| [rel-m03-l01/](rel-m03-l01/README.md) | Module 3, Lesson 1. Approved history, annotation guideline, and fidelity card |
| [rel-m03-l02/](rel-m03-l02/README.md) | Module 3, Lesson 2. Signed ruling, GPU quota, and the model register |
| [rel-m03-l03/](rel-m03-l03/README.md) | Module 3, Lesson 3. Criteria v4, the change feed, and the document store |
| [rel-m03-l04/](rel-m03-l04/README.md) | Module 3, Lesson 4. Hidden-test protocol, judge calibration, and the eye-screening campaign |
| [rel-m03-l05/](rel-m03-l05/README.md) | Module 3, Lesson 5. Rehearsal brief, price sheet, and steering questions |
| [rel-m04-l01/](rel-m04-l01/README.md) | Module 4, Lesson 1. Attack window, PHI-in-logs notice, and the first data-subject requests |
| [rel-m04-l02/](rel-m04-l02/README.md) | Module 4, Lesson 2. Incident replay, Ramadan-hours circular, and shadow-extract |
| [rel-m04-l03/](rel-m04-l03/README.md) | Module 4, Lesson 3. Surge forecast, external-token price change, and the referral batch |
| [rel-m04-l04/](rel-m04-l04/README.md) | Module 4, Lesson 4. Site-a failover drill, insure outage, and the rent-versus-buy note |
| [rel-m04-l05/](rel-m04-l05/README.md) | Module 4, Lesson 5. Contact-center handoff, warehouse feed, HR leave, and the rehearsal proposal |

From `problem_simulation`:

```text
python -m alwaha.build --profile practice --release rel-m01-l01
python -m alwaha.build --profile practice --release rel-m01-l02
python -m alwaha.build --profile practice --release rel-m01-l03
python -m alwaha.build --profile practice --release rel-m01-l04
python -m alwaha.build --profile practice --release rel-m01-l05
python -m alwaha.build --profile practice --release rel-m02-l01
python -m alwaha.build --profile practice --release rel-m02-l02
python -m alwaha.build --profile practice --release rel-m02-l03
python -m alwaha.build --profile practice --release rel-m02-l04
python -m alwaha.build --profile practice --release rel-m02-l05
python -m alwaha.build --profile practice --release rel-m03-l01
python -m alwaha.build --profile practice --release rel-m03-l02
python -m alwaha.build --profile practice --release rel-m03-l03
python -m alwaha.build --profile practice --release rel-m03-l04
python -m alwaha.build --profile practice --release rel-m03-l05
python -m alwaha.build --profile practice --release rel-m04-l01
python -m alwaha.build --profile practice --release rel-m04-l02
python -m alwaha.build --profile practice --release rel-m04-l03
python -m alwaha.build --profile practice --release rel-m04-l04
python -m alwaha.build --profile practice --release rel-m04-l05
```

`problem_simulation/build/` holds the facilitator truth for the same seed. That folder stays out of git. Leave it closed.
