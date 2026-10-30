# 03 — Redesign, architecture, and simulation

The redesigned lesson is still one self-paced morning. The student still replaces the calendar counter and the policy functions in the worker. The harness still grades a scenario log and still refuses to print hidden answers. Two behaviors are added because the current program cannot show them: a crash between a hold and a commit, and a criteria pin. Four runtimes are compared. One of them is the lab.

## Problem the redesign keeps

`wf-intake` starts at `referral.submitted` and stops at `approval.held`. It extracts specialty and facility from the letter with visible string rules. It selects the criteria document that is in force at the referral's start and stores that id. It flags a duplicate and still waits. It suggests a clinic from the catalog. It may hold a slot at a facility that has a slot API. It releases that hold if the next step fails. It does not book. Ain has no slot API, so the hold stays `none` and a queued reply is not a booking. A repeated `event_id` changes nothing. Events that share a referral are ordered by sequence. The higher sequence supplies the letter. The earliest sequence supplies the SLA date. The calendar file supplies the weekend and the holidays. The policy supplies the working-day count and the retry count. After the retry count, the event is a dead letter and is not applied. A coordinator is the next actor. The worker does not accept or return.

That list is the current gold, plus the pin and the crash. Lesson 4 continues to own patient booking, the approval decision, and the rule that a return cannot leave without a coordinator.

## Target architecture

Keep the process small and split the file the student reads. The current `worker.py` is one path from pack to rows. A later editor can split it without a framework.

| Module | Owns | Who edits it |
| --- | --- | --- |
| `calendar_count.py` | `add_working_days` from the calendar dict | Student |
| `select.py` | Sequence order, letter versus clock, in-force document, pin | Student |
| `effects.py` | Hold, release, retry budget, dead-letter row, Ain branch | Student |
| `store.py` | Referral row, seen `event_id`, outbox row, dead-letter record | Given |
| `tools.py` | Pack loader and hospital mock, including call counts | Given, still not edited |
| `worker.py` | Load, call the modules, commit, write the log | Given shell with the student functions called by name |

The store is a single SQLite file in `work/`, created by the given module. One transaction writes three things or none of them: the referral row, the seen `event_id`, and an outbox row whose payload is `approval.held` or `dead-letter`. The mock hold is called with the referral id as the idempotency key. The mock records the first hold id and, on a second call with the same key, returns the same id and increments a duplicate counter. The check fails the scenario if the duplicate counter is non-zero after the crash case, or if a hold remains open on the compensate case, or if the dead letter has an outbox row that says the event was applied.

This is plain transactional messaging, scaled to one file. The "broker" is the outbox table. The check is the consumer. There is no network relay, because a relay that can crash after publish is the story on the comparison card, and the replay scenario already shows a second delivery. Adding a real broker would spend the day on operations.

The approval id comes from `tools.hold_approval(referral_id)`, which returns `apr-{referral_id}` and status `held`. The worker stores that pair. It does not format the id itself. The function is still a mock. It exists so the system of record is the mock, which is the lesson's stand-in for `eref`. `decideReferral` in the OpenAPI file stays the document the architect reads. The worker does not gain an HTTP client.

`approval.held` is a row, not a boolean. Fields are the state name, one approval id, hold, booked, criteria id, facility, clinic, duplicate, and dead-letter flag. A dead letter has an empty approval list, hold `none`, booked false, and a reason code `retry-budget` stored beside the event id. Compensate leaves state `approval.held`, hold `released`, and a compensation row `release-hold` in the same transaction as the state. If the process dies after the mock has taken the hold and before that transaction commits, the crash harness runs the worker again. The second run must release once and leave a single compensation row. That is the saga step this day can afford: one local effect, one compensating effect, business state unchanged.

The criteria pin is a column `criteria_id` written when the referral is first stored, copied from the document whose status is `in_force` on that start. A new pack file `criteria-flip.json` can mark `crit-endo-v4` as in force after a timestamp. Referrals whose start is before the flip keep v3. A referral whose start is after the flip would take v4, but the pack should not include that referral. The graded point is the pin, not a second policy. The flip file is the test that `_in_force` is called once at start and the stored id is what the log shows. The current end-of-batch lookup fails that test on purpose in the starter.

The letter stays in the event file for the scenarios, because claim check needs a store the day should not build. The log must not contain the letter. The check already rejects the watermark in `work/`. Extend that idea: the scenario log's allowed fields stay the current list. A worker that copies `letter` into the log fails a new message, `the log carries the letter`, and the message does not print the letter.

## Four alternatives

### Alternative A — Plain transactional messaging in the lesson harness

**What the student runs.** The modules above. SQLite in `work/`. The existing JSONL pack. One crash driver that stops the worker after the hold call and starts it again.

**What it teaches.** Idempotency that survives a second process. The outbox insert in the same transaction as the referral. Compensation as a row. The pin. The calendar and sequence rules the day already grades.

**What it refuses.** It does not resume arbitrary Python stack frames. A crash mid-function is recovered by reading the store, not by replaying a journal of every line. That limit is the point of the comparison card.

**Maturity.** Proven pattern, small enough for this lesson. Recommended.

### Alternative B — Temporal as the student runtime

**What it would be.** A workflow that calls activities for extract, criteria, duplicate, hold, and finish, then waits on the approval signal. The worker process polls a dev server. Replay history is the durability story.

**Why it is not this lesson.** The server, the worker, the determinism rules, and the activity timeouts are a second course inside the morning. The classroom day also contains Lesson 4. Temporal's own activity page says the activity can run more than once, so the student would still have to build Alternative A's idempotent hold. The framework would not remove the lesson. It would wrap it. The approval wait is real in Temporal and is Lesson 4's product behavior. Lesson 3 can show the pattern's shape in a figure: block, signal, timeout, query. It should not host the server.

**Maturity.** Proven product, emerging as a dependency here. Name-only.

### Alternative C — Restate as the student runtime

**What it would be.** A handler journaled by Restate, with `Idempotency-Key` set to `event_id`, and `ctx.run` around the hold.

**Why it is not this lesson.** Same operational cost as Temporal, plus a default retention of 24 hours that contradicts a permanent event-id rule unless the chapter changes the configuration and explains why. The journal is a good paragraph. The cluster is not a good install.

**Maturity.** Emerging product. Name-only.

### Alternative D — DBOS as a library inside the worker

**What it would be.** Decorators on the workflow and a Postgres or SQLite datasource transaction around the referral insert.

**Why it is not this lesson.** It is the closest library to Alternative A, and it would still teach a second API, a system database, and a determinism rule. The exactly-once story is true for writes in that database and false for `tools.hold` unless the hold is also keyed. Students who read only the word "exactly-once" on the tutorial title will over-claim. The comparison card quotes the tutorial's limit. The lab uses a visible transaction instead of a decorator, so the commit boundary is something the student can print.

**Maturity.** Emerging product. The database-transaction guarantee is real and narrow. Name-only.

A process manager product such as a BPMN engine is a fifth name, not a fifth lab. Hohpe's process-manager page uses AWS Step Functions as an example of a hub that keeps state in a document between steps. That is the same shape as Temporal's history and as this design's referral row. One sentence on the card is enough. The course should not add a modeler.

## Simulation and datasets

The dataset stays synthetic and small. The current generator in `problem_simulation/alwaha/events/stream.py` already builds the nine scenarios, the reversed order pair, the duplicated replay id, the watermark on one letter, the open-referral row, and the two faults. Keep that generator. Add two fixtures beside it.

1. `crash` scenario. Same shape as `happy`, with a fault `crash-after-hold` the harness understands. The first execution calls `hold` and stops before commit. The second execution completes. Gold: one approval, one hold id, duplicate-hold count 0, state `approval.held`, booked false.
2. `pin` scenario. A referral started while v3 is in force, then `criteria-flip.json` marks v4 in force. Gold `criteria_id` remains the v3 id. The check says `criteria moved after start` if the log shows v4, and it still does not print the id.

Do not add a public clinical dataset. Referral letters are the kind of text Lesson 1 treats as sensitive. The one-sentence letters (`Please accept this endocrinology referral to {facility}.`) are the right size. They make extraction testable and they keep the watermark obvious. A larger synthetic generator such as Synthea can wait for a later data lesson if the course ever needs populations. This morning needs cases, not volume. No accuracy, latency, or throughput number should be invented for the worker. The check is pass or fail per scenario.

Holiday rows stay a list of ISO dates. The chapter cites the civil-service week and tells the student the list is the announcement. The worker does not import a Hijri library. Ramadan hours are a reading box, not a column in the gold file. National Day's observed Thursday or Sunday is a reading question with no new fixture, so the gold due dates already published for Friday and holiday stay stable.

The scenario log's order can stay first-seen order: `order`, `happy`, `friday`, `holiday`, `ain`, `replay`, `duplicate`, `compensation`, `dead-letter`, then `pin`, then `crash`. The crash row is whatever the second run committed. The first run must not leave a graded log of its own.

## Failure catalog

The current check already covers the starter's misses. The redesign keeps every one of them.

| Failure | What the student sees | What must be true when it is fixed |
| --- | --- | --- |
| Friday counted as a working day | `{scenario} due date does not match the calendar` | Weekend names come from the file |
| Holiday counted | The same message | Holiday dates come from the file |
| Ain booked, or queued treated as booked | `ain booked a slot` | Hold `none`, booked false, clinic empty |
| Replay opens a second approval | `replay opened a second approval` | One id, persisted across a second delivery |
| Order keeps the later file line | `order suggestion does not match` | Higher sequence, facility `h-wadi` |
| Draft criteria chosen | `happy criteria is not the one in force` | Status `in_force`, not max version |
| Duplicate missed or over-flagged | `referral was not flagged` or `was flagged` | Flag true only for the open patient and specialty, still held, not booked |
| Compensate leaves the hold | `compensation hold does not match` | Hold `released`, state still `approval.held` |
| Poison event applied | `dead-letter applied the poison event` | No approval, hold not open, not booked |
| Watermark in `work/` or in the log | `a watermarked sample is in the work directory` | Message does not contain the watermark |
| Human step missing from the note | `the diagram does not show the human step` | The note names the coordinator |
| Crash retries the hold | `crash held twice` | Second run returns the same hold and does not call the effect again |
| Pin follows the flip | `pin criteria moved after start` | Stored id is the document in force at start |
| Letter copied into the log | `the log carries the letter` | Message does not quote the letter |
| Worker mints a boolean | `approval is a boolean` | State is `approval.held` or `dead-letter` |

Messages continue to omit due dates, clause ids, clinic codes, approval ids, and the watermark. The new messages name the case and the class of mistake. They do not print the expected hold count or the expected document id.

Failures the day should describe and not simulate: a relay that publishes the outbox twice (the replay row is the consumer-side lesson), a 24-hour idempotency window expiring, a Temporal activity that completed and crashed before history, a Hijri sighting that moves Eid by a day, a Ramadan timetable applied to a day-count SLA, and a coordinator timeout that auto-returns. Each of those is a paragraph. Each of them has a wrong "fix" that would break the acceptance line or the calendar.

## How the simulation stays modular

`store.py` exposes `begin`, `commit`, `already_seen`, `save_referral`, and `save_dead_letter`. It does not know clinic names. `effects.py` does not open SQLite. `select.py` does not call `hold`. `calendar_count.py` does not read the policy file. The worker is the only composition root. That split is what lets the chapter assign one function to one role without a 300-line paste. If a file grows past a single screen of policy, it is doing two jobs and should be split again. The given `store.py` can be longer than the student files. Students read its transaction boundary. They do not rewrite SQL.

## What the redesign explicitly does not build

No slot booking, no Ain schedule spec (`sched-ain.yaml` is already forbidden in the current release test), no accept, no return, no SMS, no model call, no vector index, no Temporal namespace, no Restate endpoint, no DBOS decorator, no multi-service choreography, no claim-check blob store, no HL7 parser, no Hijri arithmetic, no National Day encoder, no auto-escalation when the human is slow. The outbox payload is a status fact for the log. It is not a license to drive Lesson 4's book tool.

## Relationship to later lessons

Lesson 4 should find `approval.held` and an approval id in a row it can read. Its tool flag `approval: true` means the tool refuses to run without that id. The intake chapter's last paragraph should define the flag that way, so the boolean in the catalog does not replace the state. Module 3's retrieval check can keep grading the narrative form of the pin ("an in-flight referral is restarted on v4"). This day grades the stored id. The two checks ask different questions and can share the rule.

The facilitator syllabus line should be rewritten, when the course is edited, to the sentence the student background already uses: run intake from the submitted event to a held approval, under the calendar, the sequence, and the criteria status. Orchestration frameworks move to the comparison card.
