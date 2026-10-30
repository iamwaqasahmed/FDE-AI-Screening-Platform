# 01 — Evaluation of the existing lesson

Module 1, Lesson 3 is a policy lab dressed as a workflow lab. The policy lab is strong. The workflow lab stops at a batch script. This note says what the student is asked to do, what the checks actually grade, which ideas are already in the day, and which production claims the day cannot support. Course files were read and left unchanged.

## Where the lesson sits

`course_design/module-01.md` titles the day "Workflow orchestration." The objective is to run `wf-intake` from `referral.submitted` to a held approval. The concepts listed there are events, the working-day SLA calendar, idempotency, and tool calls inside a workflow. The lab is extract, retrieve, duplicate check, suggest a clinic, and stop for a human. The traps are counting Friday as a working day, and booking `h-ain`. The advanced layer on that facilitator page is compensation, dead letters, and a note that in-flight work keeps its criteria version.

The curriculum map is fuller. It adds sequence, in-force criteria, duplicate, hold, compensate, and dead letter. It says the student replaces `calendar_count.py` and `worker.py`, that the workflow does not book, that Ain has no slot API, and that human approval is still required. The student chapters match that map. `tools.py` stays the mock.

The syllabus sentence above the objective asks for AI-powered workflows, orchestration frameworks, LLMs, APIs, databases, and external tools. The student day does not use an orchestration framework or an LLM. The APIs are functions in `tools.py`. There is no database. That sentence is a facilitator claim the lab does not earn.

The classroom map pairs `rel-m01-l03` with `rel-m01-l04` on one classroom day. The self-paced path gives intake its own lesson, then the agent. Any redesign that installs Temporal, Restate, or DBOS spends the classroom pair and the self-paced morning on a runtime. The referral rules would lose.

## What the student actually does

The student reads the policy, the calendar, the contract, both criteria pages, both OpenAPI files, the stream, the faults, the open referrals, and the clinic catalog. The policy is concrete. The SLA clock starts at `referral.submitted`. `working_days` is 2, and the submitted day counts when it is a working day. `retries` is 2, then a dead letter, and the event is not applied. Shared referrals apply in sequence order. The higher sequence is the letter kept. A second delivery of the same event id changes nothing. The in-force criteria document is the rule, even when a higher version is a draft. A duplicate is flagged, still waits, and is not booked. A coordinator holds the approval. The workflow does not accept, return, or book. A failed next step releases the hold. `h-ain` has no slot API, and a queued reply there is not a booking.

The calendar file names Friday and Saturday as the weekend and Sunday through Thursday as the working-day names. Holidays are the data `2027-03-10`, `2027-03-11`, and `2027-03-12`. Those three dates are pack data. They are not labeled as Eid, and this evaluation does not treat them as an announced holiday.

The stream is nine scenarios, with file order that is not scenario order. The order pair is written sequence 2 first (`evt-150-2`, Wadi, `2027-01-12T09:05:00`) and sequence 1 later (`evt-150-1`, Ain, `2027-01-12T09:00:00`). The replay event `evt-110` is appended twice. Friday is `2027-01-14` (a Thursday). Holiday is `2027-03-09`. Ain is a letter that names Ain Diabetes and Eye Center. Duplicate matches `pt-160` and `endo` in `open-referrals.csv`. `ref-170` is compensate. `ref-180` is retry. One letter carries a watermark. The check must not echo it.

Chapter 06 then tells the student to select all of `work/workflow/calendar_count.py` and `work/workflow/worker.py`, delete them, and paste the finished functions from the chapter. The prose above the paste explains the design. The paste is the implementation. A syntax error is repaired by pasting again, not by editing. The command runs the worker once. The student copies fields into `notes/scenario-lines.md`, which the check does not read, and hand-counts the Friday and holiday due dates from a printed weekday list. That hand count is the best learning minute in the day. The paste is the weakest.

Chapter 07 pastes `intake.md`. The check looks for "coordinator" or "human," and for the words "in-flight," "criteria," and "version" together. The chapter says the pasted worker does not store an old version, and that no event today changes the document after a referral has started. The note claims a rule the program does not implement. The check accepts the claim.

Chapter 08 pastes a `knowledge.md` skeleton. The check requires two numbered lines with a word after the number. The finish page says the words "Your answer" already satisfy the check. The trainer is told to grade the sentences. The machine does not.

## What the starter gets wrong, and what the gold requires

The starter calendar ignores its calendar argument and counts Monday through Friday. The starter worker books, and it treats a queued reply as booked. It counts events per referral and can emit `apr-{id}-2`. It keeps the last letter in file order, so the order case keeps Ain. It picks the highest criteria version, which is the draft `crit-endo-v4`. It never flags a duplicate. It calls `finish` and ignores compensate and retry, so the hold stays open and the poison event is applied.

The reference worker in `problem_simulation/tests/m01_l03_worker.py`, which the student paste matches, does the inverse. `build_rows` skips a repeated `event_id`. `_row` sorts by sequence, keeps the last, and starts the clock from the first event's date. `add_working_days` skips weekend names and holiday dates from the file. `_in_force` selects `status == "in_force"`. Ain gets hold `none` and is not booked. Any other facility is held. A compensate fault releases the hold and the state stays `approval.held`. A retry fault calls `finish` up to `policy["retries"]` and then writes a dead letter with no approval, no booking, and no open hold. A duplicate is a boolean on a row that is still held. `booked` is false on every row. The approval id is the string `apr-{referral_id}` written by the worker. `tools.py` has `hold`, `book`, `finish`, and `release`. It has no `decideReferral`, even though `eref.yaml` says that call returns 202, held for a coordinator.

`chk-events` runs the worker and compares the log to hidden gold. A live row needs one approval, the gold state, due date, criteria id, suggestion, clinic, duplicate flag, and hold, and it stays unbooked. A second approval is its own message. A poison row fails if it was applied at all. Messages name the scenario and the kind of miss. They withhold the due date, the clause id, the clinic code, the watermark, and `approval.held`. The release tests lock the rest: Friday 15 January 2027 is not a working day; two working days from Thursday 14 January 2027 land on Sunday 17 January 2027; the order pair stays reversed; the replay line appears twice; v3 is in force and v4 is draft; learner notes omit clause ids, the policy counts, and gold due dates; the unfinished calendar still mentions Friday and does not mention holidays.

The trainer chapter, after the attempt, names the misses in plain language and does print `crit-endo-v3`, the Friday due date `2027-01-17`, the holiday due date `2027-03-14`, and the duplicate key `pt-160`. That chapter is for the trainer. The student check stays quiet. Keep that split.

## What the day already teaches well

The Friday trap is the right trap for this client. The starter encodes a Monday–Friday week. The pack encodes Sunday–Thursday, which is the Kingdom's civil-service week (see the research note). A student who pastes without reading will still fail `friday` and `holiday`, and the message will not show the date. The hand count in chapter 06 forces a weekday walk. That is teaching, and it is graded by behavior.

Sequence is taught with a pair that shares a calendar day, so the due date cannot reveal which letter won. The facility reveals it. File order would choose Ain. Sequence order chooses Wadi. That is a real messaging bug, the one a resequencer exists to prevent, and the demo is allowed to show the two arrivals and one approval without naming the defect.

Criteria status against version number is the right clinical-policy lesson for a first workflow day. The draft has the higher version. The check says the criteria is not the one in force and does not print the document id. Students who sort by version fail. Students who read the status line pass.

The duplicate is not a silent reject. It is flagged and still waits. That matches a coordinator's job. Auto-closing a duplicate would be a clinical decision the day correctly withholds.

Compensate and dead letter are different faults, and the gold treats them differently. Compensate releases a hold and still stops for a person. Retry spends the budget and applies nothing. Collapsing both into "error" would be the wrong lesson. The day keeps them apart.

Ain is a missing dependency, not a coding error. Queued is not booked. The starter's `status in {"booked", "queued"}` is the exact mistake. The reference worker never calls `book`.

The watermark rule continues Lesson 1. Copying `intake.jsonl` into `work/` fails the check, and the failure text does not contain the watermark. Coding assistants may see the scripts and may not see the event file. That constraint is operational, and the tests cover both a copied file and a worker that writes the stream into the log.

The five roles are one person. Lead checks due dates. The AI or data role is a string match from the letter to `endo`, `h-wadi`, and `h-ain`. Product writes the acceptance line. Architect reads the contract, including the rule that an unknown field is ignored and that `scenario` is not part of the contract. Application replaces the two files. For a self-paced forward-deployed day, holding all five parts is honest. The AI part is deliberately not a model. Lesson 2 already marked clocks and slots as the wrong place for a language model. This day should keep extraction as a small, visible function. An LLM as the reader of the letter would hide the facility rule inside a prompt and would put the watermark one paste away from a prompt. That would undo Lesson 1.

## Where the day under-teaches production workflow

The worker is a pure function from a folder to a JSON list. `build_rows` loads the pack, groups events, and returns rows. Nothing is saved until `main` writes the file. If the process died after `tools.hold` and before the write, a second run would call `hold` again. The mock returns a new dict every time. Nothing counts the calls. The graded path runs the worker once per check. Idempotency is "skip this id inside this loop." Gregor Hohpe's idempotent receiver has to be safe when the same message arrives again in a later delivery, after a crash, or from a second consumer. The lesson's set does not live that long.

There is no outbox. The worker does not update a referral row and emit `referral.submitted` was consumed, or `approval.held`, as a message. The log is the whole result. Chris Richardson's transactional outbox exists because a database commit and a broker send do not share a transaction. The lesson never faces that split, so it cannot teach it.

Compensation is one `if` after `finish`. The release is not recorded as a step that must run if the process dies between the failure and the release. A saga, in the sense Richardson uses and that Garcia-Molina and Salem introduced, is a sequence of local transactions with compensations. Here the only local effect that needs undoing is the hold, and the business process continues. That is the right scope for this day. The program does not show the scope. A reader can think "we handled the error" and miss that the hold is a resource with a TTL the OpenAPI file mentions and the worker never reads.

The human step is a string on a row and a sentence in a note. The process does not wait. There is no timer, no assignee, no signal, and no path from `approval.held` to accepted or returned. Lesson 4 owns the patient-facing wait and correctly refuses to book without an approval id. Lesson 3's risk is that students leave thinking the string is the approval. The id was never issued by `eref`. A boolean `approved: false` would be worse, and the day avoids that boolean in the log. It still ends the workflow at the moment the interesting state begins. Temporal's approval pattern blocks until a signal or a timeout, and the wait is durable. Teaching that pattern by installing Temporal is the wrong cost. Teaching that `approval.held` is a state a later signal will resolve is the right sentence, and the log should be something a second process could load.

In-flight criteria are a known hole the chapter admits. The worker calls `_in_force` at the end of the single pass. If v4's status flipped to in force between the first event and the pass, every referral in the file would take v4, including one that had already started. Module 3's retrieval check later grades "an in-flight referral is restarted on v4." Lesson 3 introduces the rule as words. The handoff is intentional and thin. A student who trusts the note will think the worker pinned the document. The chapter says otherwise, in one sentence under the paste. That sentence is easy to skip.

Tool calls are not tools in the agent sense. `extract` is a substring test. `tools.clinic` is a CSV scan. `tools.hold` does not touch a network. The words page defines mock honestly. The facilitator syllabus does not. Calling these "tool calls inside a workflow" borrows Lesson 4's vocabulary a day early. Lesson 4 has a real tool catalog and a trace. This day has a function table. The distinction is worth one sentence in the student chapter so "tool" does not mean two things.

Dead letter is a row with `dead_letter: true`, empty approvals, and hold `none`. Hohpe's dead letter channel is a place a message goes when it cannot be delivered, with enough context to inspect it later. The lesson records that the event was not applied. It does not keep the event, the fault, or a way for an operator to replay it after the fault clears. The check's phrase "applied the poison event" is the right failure. The channel is missing. For this day, a row is enough if the note says the row is the record and a queue would be the production shape. The current note does not say that.

## What is proven, emerging, and experimental inside this lesson

The graded policy behaviors are a proven teaching pattern: a hidden gold file, messages that name the case and not the answer, a starter with one bug per case, and a calendar the student can recount by hand. That pattern should stay.

The claim that this is an orchestration-framework lab is experimental relative to the artifact. Nothing in the student folder is a process manager that waits on intermediate results. Hohpe describes a process manager as a hub that holds the sequence and chooses the next step from replies. This worker chooses every field in one function and stops.

Durable execution, as a product the student operates, is not in the lesson at all. Adding it as a required install would be an emerging teaching bet on top of a day that already has nine scenarios. The research note separates the products.

Using a language model to read the letter, pick the criteria, or decide the hold would be experimental here and would fight Lesson 2. Leave it out.

## Explicit deletions

1. Delete the chapter-06 paste of the complete correct `calendar_count.py` and `worker.py`. The starter comments already list the bugs. A replacement chapter should show the function boundaries and ask the student to replace `add_working_days`, the event-id skip, the sequence sort, `_in_force`, the Ain branch, the compensate branch, and the retry branch. The check already grades behavior, so it does not need the paste.
2. Delete "Your answer" as a passing knowledge file. Require the clock name `referral.submitted` and a second-delivery sentence. Keep refusing to score by hidden due dates.
3. Delete the facilitator sentence that this day integrates LLMs and orchestration frameworks, or replace it with the policy-lab sentence the chapters already use.
4. Delete the word-search for in-flight criteria as proof of versioning. The redesign note specifies a pinned id. Until that exists, the note should say the rule is recorded for later and is not in the log.
5. Delete worker-minted approval ids. `tools` should return the held id the way it returns a hold id. The worker stores it. Still no accept, no return, no book.
6. Delete the in-memory set as the whole idempotency story. The redesign adds a persisted key and a crash. The single-pass skip can remain the first exercise.
7. Do not delete the Friday trap, the holiday list, the order pair, the replay, the draft criteria, the duplicate-still-held rule, the Ain queued rule, the compensate versus retry split, the watermark, or the quiet check messages.
8. Do not add a booking path, an Ain slot API, or a coordinator screen. Lesson 4 owns booking and the approval wait on the agent. This day owns the state the agent will find.

## Judgment

The lesson is the right story for Al-Waha intake, told one level below production execution. Students who do the hand count and read the nine log rows will know the referral rules. Students who only paste will pass `chk-events` and will not have practiced a crash, an outbox, a compensation record, or a pinned policy version. The checks are better pedagogy than the paste. A redesign should trust the checks, shrink the paste, and add two behaviors the current gold cannot see: a second run after a crash, and a criteria document that changes after a referral has started.
