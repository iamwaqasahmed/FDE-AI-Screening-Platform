# How the processes fit

`append_all` writes one of three tables in `var/log.sqlite` inside a single transaction. A command names its authority. Update and delete abort. There is no foreign key from one log to another. A shared clock command is rejected.

`project` reads one log at a time and writes `var/proj/hospital.sqlite`, `channel.sqlite`, and `payer.sqlite`. The hospital mart stores a wait figure beside the booking date. A nightly file keeps `trailer_ok` when the hospital sent it. A payer timeout is stored with a null window.

`serve` reads every JSON file in `student_pack/extracts`. `GET /extracts` returns the bundle. `GET /extracts/<name>` returns one file. `GET /ref/<ref>` returns the rows whose ref matches, using `round2.query.by_ref`. The view does not import `sealed.py`, `sealed_release.py`, or `sealed_holdouts.py`.

`check --release` reads `prediction.txt`, then grades the artifact. INV-01 and the permit half of INV-09 read a binding. INV-02 through INV-08 load a function from the student's file and call it. INV-09 also reads `handoff.json`. A miss names the broken relationship. Holdout inputs live in `sealed_holdouts.py` and are not copied into the pack.

`init` and `reset` delete generated state and write it again from `history()`. Seed `20270110`. The history includes the two-year population, the round-2 cohort, documents, faults, organization, threads, the legacy desk, integration faults, the audit, curriculum evidence, operations, lesson feeds, the cross-system link, the deeper case, timelines, locale examples, then the opening references. `python -m access scenario --name <name>` rebuilds that history plus one overlay. Names: `partner-outage`, `hours-served-stale`, `replay-storm`, `partial-write`. `reset` drops the overlay. `python -m access workload --count 400` writes `var/workload.jsonl` and does not change the student pack.

The student's package `repair` is not in this tree.
