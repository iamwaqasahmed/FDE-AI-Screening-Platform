# 01 — Existing lesson evaluation

`course_design/module-03.md` and the slides ask for one person-level waitlist, labels under `ann-v2`, and a synthetic sample that passes the fidelity card. Named ideas: identity versus row count, Hijri dates, guideline versions, the clinic-code change, fidelity, a canary scan before sharing. Traps: merging a mother and a newborn, or training on clerk labels after the guideline changed. Checks: `chk-m03-l01-identity`, `chk-m03-l01-labels`, `chk-m03-l01-synthetic`.

## What is graded

Identity loads `dates.py`, `codes.py`, and `cluster.py`. A missed Hijri conversion is reported as a month boundary off by a day. The solution is tabular arithmetic, not an Umm al-Qura table. A kept catalog code is the stale-code miss. At `h-wadi` on or after `2024-06-01`, endocrinology codes become `ENDO-CLN`. Groups must match gold. Separate messages fire for a merged mother and newborn, merged twins, a linked reused MRN, or a patient count equal to the row count. The reference links equal national ids, skips `newborn` and `twin`, and follows `replaces`. Phone and MRN do not link. `patients.md` and a sequenced `sprint.md` are required.

Labels require `ann-v2`, photo rather than scan when the text says phone or photo, and a sub-specialty when the text names retina or pediatric. Synthetic scores `sample()` against the fixture card only: size 4–8, specialty shares 0.4–0.6, "kindly" 0.2–0.6, rare label present and between 0.3 and 0.7. Those bands are the course card, not an external score. The solution invents four rows and drops the clerk file. The shell copies a real letter and fails the card, the watermark, and the national-id test. `scan.accept` must reject `CANARY-` and any history national id. A copied `clerk.jsonl` fails all three checks without the token being printed. Problem text must not echo an id, a converted date, or a rate. `pit.py` and `budget.py` are optional: deleting them still passes. The demo shows two MRNs, one shared national id, and the line that they stay two people.

## What holds

Each trap has its own message: shared national id (mother and newborn), shared phone (twins), reused MRN, and row count. A failed check digit stays a person. `death-late` and `seen-elsewhere` propose removal and leave the person in the cluster file. `ann-v2` changes the target. One engineer holds all five roles. Corpus phone photos are page images, so the label `photo` is a source type, not a clinical picture.

## Gaps

The linker emits no probability or clerical band. `design/11-eval-and-hardness.md` says identity is precision and recall against point-in-time gold. The code is an exact group match, and point-in-time features are optional `pit.py`. That row also says synthetic includes train-on-synthetic test-on-real. The code checks bands, the marker, ids, and the scanner. It does not train a model, name attribute disclosure, or set a privacy parameter. Labels are a function to `ann-v2`, not a versioned adjudication record. The words page never names Umm al-Qura, and a correct civil conversion can fail because gold follows `dates.py`. PDPL is absent. The fictional export rule is a course rule, not the statute.
