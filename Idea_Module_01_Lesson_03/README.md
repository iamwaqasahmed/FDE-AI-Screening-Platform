# Idea packet — Module 01 Lesson 03, intake workflow

Research only. This folder does not change `Module 01/Lesson 03`, the checks, or the release. It is a curriculum argument for a later editor.

The lesson id is `rel-m01-l03`. The workflow is `wf-intake`. It runs from `referral.submitted` to a held approval. It does not accept, return, or book. Ain (`h-ain`) has no slot API in this release. A person still has to decide.

## Thesis

A small Python worker under-teaches production workflow. The day already teaches the referral rules that matter: a Sunday–Thursday SLA calendar, sequence against file order, idempotency of one `event_id`, in-force criteria against a higher draft, a duplicate that stays held, a hold that is released, and a poison event that is not applied. Those rules are the right lab.

What the day does not teach is how those rules survive a crash, a second process, or a second system. The correct worker keeps a `seen` set in memory, fabricates `apr-{referral_id}`, and exits when it has written `approval.held`. The intake note says an in-flight referral keeps its criteria version. Chapter 07 says the pasted worker does not store that version. The syllabus line in `course_design/module-01.md` promises orchestration frameworks, LLMs, APIs, and databases. The student paste calls none of those.

Referral operations need four production ideas the lab only names, or misses:

1. Durable execution, so a restart resumes a referral instead of folding the file again.
2. A transactional outbox, so the state change and the outgoing message commit together, with consumers that tolerate a repeated delivery.
3. A saga compensation for the hold, recorded as a step, with the referral left in a human state.
4. Clinical-policy versioning that pins the in-force document at start, including after a later document becomes active.

Temporal, Restate, DBOS, and plain transactional messaging are four ways to get there. For this self-paced forward-deployed lesson, only the last one belongs in the student's hands. The other three belong on a comparison card, with their own limits stated in the vendor's words.

## Decision

Keep the graded scenarios. Replace the full-file paste with smaller edits so the student changes the functions that own the Friday trap, the sequence, the criteria status, the duplicate flag, the hold release, and the dead letter. Add one crash in the same Python harness: the process dies after `hold` and before the referral row is committed, and a second run must not open a second hold. Pin criteria with one extra scenario so the in-flight sentence in `intake.md` is true of the log. Leave Temporal, Restate, and DBOS as names, with one paragraph each on idempotency and on what "exactly once" does and does not cover. Do not install a workflow server. Do not book. Do not give Ain a slot API. Do not let the worker accept or return.

Lesson 4 already waits on an approval id before `slots.book` and `referral.return`. This lesson's job is to leave a durable `approval.held` state that the next lesson can gate. A boolean `approved` is the wrong object. Lesson 4's tool catalog uses `approval: true` to mean "this tool requires an approval id." That flag is a gate on a tool. It is a different object from the referral's state. The intake note should say so, so the next morning does not collapse them.

## How to read this packet

| File | Question it answers |
| --- | --- |
| [01-existing-lesson-evaluation.md](01-existing-lesson-evaluation.md) | What the student, the solution, the checks, and the facilitator page actually do, and what to delete |
| [02-industry-research.md](02-industry-research.md) | Durable execution, messaging patterns, referral standards, Saudi calendars, and human approval, with sources |
| [03-redesign-architecture-and-simulation.md](03-redesign-architecture-and-simulation.md) | The replacement lab: modules, data, failures, and four runtime choices |
| [04-exercises-assessment-instruction.md](04-exercises-assessment-instruction.md) | Prerequisites, exercises, the rubric, and how a chapter should teach without pasting the solution |
| [05-tradeoffs-recommendations-sources.md](05-tradeoffs-recommendations-sources.md) | What is in the lesson, what is name-only, later lessons, and the source list |

## Maturity labels used throughout

- **Proven.** A practice with a stable description and a long production record. Idempotent receivers, dead-letter channels, transactional outbox, saga compensation, and a business calendar supplied as data are in this class. HL7 v2 referral messages are in this class. The civil-service week Sunday–Thursday is in this class.
- **Emerging.** A practice that is real and documented, with a narrower record or a standard that is still maturing. Temporal as an industry runtime is close to proven; requiring it in this lesson would still be an emerging teaching choice. Restate and DBOS are emerging. FHIR `Task` status is Trial Use, maturity level 3, in the FHIR v5.0.0 value set.
- **Experimental.** A practice this course should not grade. Blanket exactly-once claims across a hospital API, an LLM as the system of record for facility and criteria, computing Eid dates inside the worker, and treating a tool-catalog boolean as the approval workflow.

## Explicit deletions

These are recommendations for a later edit of the lesson, not edits made here.

1. Delete the full replacement of `worker.py` and `calendar_count.py` as a paste of the finished program. Keep the starter bugs visible and have the student replace named functions.
2. Delete the grading rule that any two numbered lines in `knowledge.md` pass. Grade the clock and the second-delivery sentence, still without printing a hidden due date.
3. Delete the claim, in the facilitator syllabus, that this day integrates an LLM and an orchestration framework, unless the day grows those pieces. The student pages are already more accurate than that syllabus line.
4. Delete the in-flight criteria sentence as a word search with no log row behind it. Either pin `criteria_id` in the worker or stop telling the student the note has implemented the rule.
5. Delete local invention of `apr-{referral_id}` as if `eref` had returned it. The mock should return the held id. The worker should store that id.
6. Delete the idea that an in-memory `seen` set is the definition of idempotency. Keep the `event_id` rule. Persist the key, or label the set as single-pass.
7. Do not add booking, a live Ain API, auto-accept, auto-return, a second agent, a Hijri calculator, or a required Temporal, Restate, or DBOS install.

## What stays

The Friday trap stays. The holiday list stays data. The out-of-order pair stays. Replay of one `event_id` stays. `crit-endo-v3` in force and `crit-endo-v4` draft stay. The duplicate stays flagged and unbooked. Compensate releases the hold and leaves `approval.held`. The retry budget ends in a dead letter that opens nothing. The watermark stays out of `work/` and out of the check's message. `chk-events` keeps refusing to print the due date, the clause, and the fitting state. Ain stays unheld and unbooked. The workflow still stops for a coordinator.

## Time budget

The curriculum map pairs this release with Lesson 4 on one classroom day, and the self-paced path gives it a full lesson. The redesign fits the self-paced lesson. It does not add a server, a new language, or a second day. The comparison card is reading. The new graded behavior is one crash and one criteria pin, checked the same way the nine scenarios are checked now.

## What the current day already gets right

The graded world is nine scenarios in one JSONL file, plus a Monday–Friday starter that ignores the pack calendar. File order is not scenario order. The order pair arrives as sequence 2 (Wadi) and then sequence 1 (Ain) on the same calendar day, so only the facility reveals which letter won. The replay id arrives twice. Friday's referral is dated Thursday 14 January 2027, and the hidden gold lands the two-day count on Sunday 17 January 2027. The holiday row starts 9 March 2027 and must skip the three listed dates. v3 is in force and v4 is a draft with a higher version. The duplicate stays held. Compensate releases the hold and stays at `approval.held`. The retry budget writes a dead letter that opens nothing. Ain is unheld and unbooked. The check names the miss and withholds the due date, the clause, and the watermark. That assessment design should survive any rewrite of the chapter.

The gap is durability and honesty about what the paste implements. The correct worker's `seen` set dies with the process. The approval id is a string the worker formats, while `eref.yaml` describes a held decision the mock never returns. Chapter 07 says the in-flight criteria rule is not in the worker, and the check accepts the sentence anyway. The facilitator syllabus promises an orchestration framework and an LLM. The chapters deliver a batch script and a substring match, which is the right extraction for this day and the wrong label.

## How the four runtimes were judged

Plain transactional messaging can live in the given SQLite module: one transaction for the referral, the event id, and the outbox row, plus a mock that treats the referral id as a hold key. A deterministic crash after `hold` and before commit is a new scenario. Students see the boundary.

Temporal documents the boundary the slogan skips. An activity whose retries are on is observed completed once and may execute more than once. The approval pattern is the right picture of a person: the workflow waits on a signal, and the timer survives a worker restart. That picture is a paragraph. The server is a second course.

Restate journals steps and dedupes an `Idempotency-Key` for 24 hours by default. The lesson's event-id rule does not expire. The number belongs on the card so nobody treats the default as the policy.

DBOS records a datasource transaction in the same database commit and, on replay, returns the stored result instead of running the function again. A hold that leaves that database is outside the guarantee. The card quotes the tutorial's scope. The lab uses visible SQL so the commit is printable.

## Sources in one place

Full citations are in [05-tradeoffs-recommendations-sources.md](05-tradeoffs-recommendations-sources.md). The five pages that most change the design are Temporal's activity definition (exactly-once observation versus repeated execution), Temporal's approval pattern (a waited human state), Chris Richardson's transactional outbox (and the duplicate publish), Hohpe and Woolf's dead letter channel, and the FHIR task-status value set (twelve statuses, and a waiting task is one of them).
