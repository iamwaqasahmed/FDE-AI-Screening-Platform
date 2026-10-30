# Idea — Module 02 Lesson 05 — The Ain change

Research packet for `rel-m02-l05` / change request `cr-ain`. No course file was edited. The student copy, the solution copy, the slides, `course_design/module-02.md`, the curriculum map, and `problem_simulation` stay as they are. This folder is a proposal for a later rewrite.

## Thesis

A nightly file is the interface, and for many enterprises it stays the interface. Module 2 Lesson 5 currently teaches a queue that returns `queued`, a function that keeps yesterday when tonight's file is missing, and a pasted sentence that Stage 2 monitoring arrives later. An FDE who can only do that will fail the engagement the moment the file is short, repeated, or locally coded.

The day should teach five practices around that file:

1. Reconciliation of queued intents against an applied file.
2. Control totals that reject a file before it replaces yesterday.
3. Idempotent reprocessing of the same file.
4. A narrow dual-run in which the legacy file remains the slot master.
5. Change enablement: risk, authority, schedule, and backout, distinct from a six-line change card and from a standing CAB.

The trap stays. Ain does not get a live slot.

## How to read this packet

| File | Job |
| --- | --- |
| [01-existing-lesson-evaluation.md](01-existing-lesson-evaluation.md) | What `rel-m02-l05` actually grades, labeled keep / tighten / replace / delete |
| [02-industry-research.md](02-industry-research.md) | Primary sources: strangler fig, anti-corruption layer, file controls, ITIL 4 change enablement, hospital cutovers, smoke versus synthetic monitoring |
| [03-redesign-architecture-and-simulation.md](03-redesign-architecture-and-simulation.md) | Target simulation and four labeled alternatives |
| [04-exercises-assessment-instruction.md](04-exercises-assessment-instruction.md) | One-day sequence, exercises, and checks |
| [05-tradeoffs-recommendations-sources.md](05-tradeoffs-recommendations-sources.md) | Recommendation, deletions, and the source list |

Labels used in every file: **KEEP**, **TIGHTEN**, **REPLACE**, **DELETE**, **ADD**.

## What this lesson is today

Classroom name: The Ain change. Release `rel-m02-l05`. Steering asks to include `h-ain`. The student sequences smoke, then the change, then the readout, then the retro; pastes `queue.py`, `file_ain.py`, `notify.py`, and `contract.py`; updates `deployment.md`; pastes `readout.md` and `retro.md`; answers why Ain cannot confirm a slot and what Stage 2 adds to monitoring. Checks: `chk-deploy`, `chk-journey`, `chk-readout`, `chk-individual-m02`. The trap is promising a live slot at Ain.

Foundation in `course_design/module-02.md`: a smoke test and a sequenced change. Advanced: a queued booking that waits for the nightly file. Traceability (`problem_simulation/design/traceability/module-02-trace.md`) calls the advanced piece `cr-ain` and `sched-ain`'s nightly file, plus a compensating notify, and says the proof is "ready for Stage 2 optimization." Monitoring at this stage is request rate, error rate, and model latency. The full operations stack is deferred.

## Recommendation in one paragraph

Adopt Alternative A in document 03. Keep the live-slot trap, the zone split, the missed night, and the rule that a failed notice does not confirm a slot. Replace the paste-and-token day with a small file protocol: control record, poison quarantine, idempotent file id, a shadow reconcile that does not book, and a change record whose authority is delegated. The smoke test gains one synthetic booking that must stay queued. The monitoring answer names the signals Stage 2 still lacks. Alternatives B and C donate the strangler seam and the change record. Alternative D, rewriting only the monitoring paragraph, is rejected.

## Boundaries

- Fictional client: Al-Waha Health Cluster. No real patient data.
- Clinic codes stay out of check messages, as they do today.
- This packet does not implement the new checks.
- "CAB theater" is a teaching label for a failure mode. It is not an Axelos term. The official public purpose of the practice is on PeopleCert. The CAB-delegation argument is paraphrased from the paid ITIL 4 Change Enablement practice guide and flagged as such in document 02.
