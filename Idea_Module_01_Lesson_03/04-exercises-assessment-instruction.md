# 04 — Exercises, assessment, and instruction

This note is for the author of a later student chapter. It assumes the redesign in the architecture note: the same release id, a smaller set of student edits, a persisted idempotency key, a crash, and a criteria pin. It does not assume Temporal, Restate, or DBOS are installed. The student still does not book, and Ain still has no slot API.

## Prerequisites

The reader has finished Lesson 1 and Lesson 2 in this course.

From Lesson 1 they can follow a terminal command, they know the work folder is what the check reads, they know a letter can carry a watermark that must not enter a prompt or `work/`, and they know the three zones exist. They do not need the 2023 postmortem.

From Lesson 2 they know some problems are `no-model`. The SLA clock and the slot list are in that class. Intake is the first workflow that carries those problems. The reader should not arrive expecting a prompt.

Outside the course, the syllabus already assumes working English and some programming, data, or API experience, and Python 3.12 or newer. This lesson needs enough Python to read a function, edit it, and run a file. It needs dates, JSON, and the idea of a set. It does not need SQL beyond reading a comment that says "this transaction writes the row and the outbox together." The given `store.py` holds the SQL. It does not need FHIR, HL7, Arabic, or a workflow engine. A reader who has never heard of Temporal is the reader the comparison card is for.

Prior terms the words chapter may assume: referral, coordinator, PHI, watermark, claim versus fact, `practice`, `rel-m01-l03`. New terms stay the map's list, plus four that the current words page approaches without naming as production objects: idempotency key (the `event_id` stored in the table), outbox (the row written in the same transaction), compensation (the release recorded when finish fails), and pinned criteria (the document id stored at start). Dead letter, hold, sequence, and in force are already on the words page. Keep those definitions. Add one line under idempotency: the key has to be there after the process stops, or a second run is a new process with an empty memory.

## What the student is able to do at the end

1. Count two working days on the pack calendar, including a Thursday that crosses Friday and Saturday, and a start that crosses the three holiday dates.
2. Say which clock starts the SLA, and that a second delivery of the same event id leaves the approval count unchanged.
3. Keep the higher sequence as the letter and the earliest sequence as the clock.
4. Select the criteria document whose status is in force, and keep that id after a later flip.
5. Flag the open duplicate, leave it held, and leave it unbooked.
6. Leave Ain unheld and unbooked.
7. Release a hold on compensate and leave the state `approval.held`.
8. Spend the retry budget and write a dead letter that applies nothing.
9. Recover the crash scenario with a single hold.
10. Point at `approval.held` as a state with an id, and say a tool-catalog boolean in the next lesson is a gate on that id.
11. Name Temporal, Restate, DBOS, and the outbox, and say where exactly-once stops.

Items 1–8 are today's gold. Items 9–10 are the new graded behavior and the new note. Item 11 is read and answered in `knowledge.md` with a third short line, or it stays on the comparison card and is checked only for the presence of the three product names plus the outbox. Prefer the card plus two graded knowledge lines, so the machine check stays small. The trainer reads the exactly-once sentence.

## Exercise sequence

The chapter order can stay: background, setup, role, client, words, stream, worker, note, finish. The worker chapter changes.

### Exercise 1 — Recount the policy example

Before any paste, the student runs the existing weekday print for `2027-01-10` and checks the policy's Sunday-as-day-one example. Then they recount `friday` and `holiday` from the event dates and the calendar file. They write the two due dates only on the ungraded worksheet. This exercise is already in chapter 06 and should stay first. It is the lead's work. Do not print the gold dates in the chapter. The current trainer chapter reveals `2027-01-17` and `2027-03-14` after the attempt. That is the right place for the reveal.

### Exercise 2 — Replace the calendar function

The starter `add_working_days` deletes the calendar argument and walks Monday–Friday. The student replaces that function so weekend names and holiday dates come from the dict, and so the start counts when it is a working day. The rest of the file stays. A unit the student can run locally, without the full check, prints the policy example's due date for Sunday 10 January 2027. The policy example is public. The scenario due dates are not. If that local print matches the policy sentence (Sunday day one, Monday day two, count 2), the function is ready for the hidden Friday and holiday rows.

### Exercise 3 — Separate event id from referral id

The starter counts events per referral. The student replaces the grouping loop so a repeated `event_id` is ignored and a second sequence on the same referral is kept. The worksheet asks, for `replay` and for `order`, how many event ids and how many approval ids the log shows. The expected shape is one approval in both cases. The order case has two event ids. The replay case has one event id delivered twice. That question is the idempotency lesson in miniature.

### Exercise 4 — Sequence, criteria, duplicate, Ain

Four small functions, each with a failing scenario if left as the starter:

- sort by sequence, letter from the higher one, clock from the lower one
- criteria by status `in_force`, and store the id on first write
- duplicate from the open-referrals pair, without changing state or booked
- Ain skips `hold` and never calls `book`

The chapter shows the starter body and the policy sentence. It does not show the finished body. Hints are the check messages that already exist.

### Exercise 5 — Compensate and dead letter

The student handles the two fault names differently. Compensate calls release and records the compensation with the held state. Retry calls finish until the policy count and then writes the dead-letter row through the store, with no approval. A hint table in the chapter, already present in the current label section, stays. Add one sentence: the dead-letter row is the lesson's stand-in for a dead letter channel. An operator could replay it later. This worker does not auto-replay.

### Exercise 6 — Crash and pin

These two scenarios are new. The chapter tells the student to run the worker, expect the crash driver to start it twice, and open the log. If `crash held twice` prints, the hold ran before the event id was stored, or the second run did not pass the same key. The repair is in the order of operations inside the given transaction: write the seen key and the referral in the transaction, and call the mock with the key so a repeat returns the stored hold. The pin scenario fails with `criteria moved after start` if the worker re-reads status at the end. The repair is to copy `criteria_id` from the row already stored.

The chapter should show a six-line sketch of the transaction, with the hold key as a parameter, and should leave the student's functions responsible for deciding Ain, compensate, and the pin. Do not paste a finished `worker.py`.

### Exercise 7 — The note and the comparison card

`intake.md` keeps the six steps and the acceptance line. The in-flight section must name the pinned document as a stored id, not as a wish. Add two sentences the check can see without leaking ids: the state is `approval.held`, and a boolean is not the approval. The comparison card is a page in the packet, `patterns.md`, which the student reads and does not edit. It holds the four alternatives in the architecture note, the Temporal sentence about observed-once versus executed-more-than-once, the Restate 24-hour default, the DBOS limit to the application database, and the outbox duplicate-publish issue. `knowledge.md` line 1 is the clock. Line 2 is the second delivery. The trainer asks the student to say, out loud or in an optional third line, why a second execution of a hold is still possible under Temporal. That sentence is not a hidden gold value. It is comprehension.

## Assessment

`chk-events` remains the grader. It runs the worker, including the crash driver, and reads the log, `intake.md`, and `knowledge.md`.

Graded:

- every current scenario, with the current quiet messages
- `pin` and `crash` with the new quiet messages
- the note contains a human step and the words for the pinned criteria, and it contains `approval.held`
- the note does not contain a gold due date, a clause id, or the watermark
- `knowledge.md` line 1 contains `referral.submitted`
- `knowledge.md` line 2 says a second delivery does not open another approval (a small set of accepted phrases, tested as behavior: the line matches a pattern the author writes, and a placeholder fails)
- the log does not contain the letter text

Ungraded, trainer-read:

- the worksheet counts
- the exactly-once sentence
- the optional National Day question
- the optional Ramadan question: a shorter working day is still a working day when the SLA counts days

The rubric for a person reading the work, if a cohort wants a score besides pass/fail:

| Criterion | Pass looks like |
| --- | --- |
| Calendar | Friday and holiday rows match, and the student can walk the count |
| Identity | Replay has one approval; order has two event ids and one approval |
| Criteria | In-force document, and the pin survives the flip |
| Safety | Nothing booked; Ain unheld; duplicate flagged and held |
| Failure | Compensate releases; dead letter applies nothing; crash holds once |
| State | `approval.held` is the live state; the note names a person |
| Boundary | Watermark and letter stay out of `work/` |

A pass on the machine check with an empty worksheet is a weak pass. The current course already separates the trainer's reading of `knowledge.md` from the machine. Keep that. Close the hole where "Your answer" satisfies the machine.

Do not grade prose style. Do not grade a diagram tool. The "diagram" in the current check is the numbered list in `intake.md`. Keep calling it a diagram in the message if the message already exists, and keep the file as markdown. Adding a drawing tool is a new failure mode for a self-paced student.

## Instruction the chapter author should follow

Write the policy sentence, then the starter's mistake, then the function to edit, then the command, then the message the student will see if the starter is still in place. That is the current chapter's shape, and it is the right shape. The part to remove is the finished function inside the fence.

When a check fails, the existing table in chapter 08 is the repair map. Add rows for `crash held twice`, `criteria moved after start`, `the log carries the letter`, and `approval is a boolean`. Each row points at a function, not at a solution listing.

Tell the student a coding assistant may see `calendar_count.py`, `select.py`, `effects.py`, and `store.py`. It may not see `intake.jsonl`. The crash log and the pin file contain no letter. They may be pasted if a student needs help, because they contain ids and dates the policy already discusses. They must not be copied into the assistant along with the event file.

Run the commands from the course folder the way the current chapters do. The check stays `python -m alwaha.check events` with the work path and `--profile practice`. A second profile `small` remains the author's fixture. The canary differs. The tests that lock that difference stay.

The five roles stay one person. Lead owns Exercise 1. Application owns Exercises 2, 5, and 6. Architect owns the contract reading and the comparison card. Product owns the acceptance line and the sentence that the state is `approval.held`. The AI or data role owns the extract function and is explicitly not training or prompting a model. If that role feels thin, that is the Lesson 2 decision showing up. Do not fill it with a model to make the role look busy.

## Time

On the self-paced path, the reading is an hour, the calendar recount is twenty minutes, the function edits are the rest of a sitting, and the comparison card is twenty minutes. The crash and the pin add one sitting only if the transaction sketch is given. They add a day if the student must design SQLite. The store stays given.

On the classroom pairing with Lesson 4, do not attempt the crash in the room. Assign the card as reading and keep the current nine scenarios if the pair is tight. The self-paced artifact can contain the crash. The classroom script can mark Exercise 6 as the evening extension. Say that in the facilitator page so a cohort does not discover the extra scenarios with twenty minutes left.

## New lessons this day should not become

Do not split intake into a calendar day, a messaging day, and a Temporal day. The nine scenarios are one story. A later optional seminar, after Lesson 4's approval wait exists, can map `approval.held` onto Temporal's signal and onto a FHIR `Task` in `requested` state. That seminar is name-only and ungraded. It has no release id. It must not block Lesson 4.

Do not move booking, SMS, or the coordinator's decision backward into this lesson. Do not move the criteria pin forward into Module 3 only. Module 3 can keep the citation lab. This day stores the id the citation lab assumes.

## Deletions that affect assessment

Delete the full-file paste as the path to a pass. Delete placeholder knowledge lines as a pass. Delete the in-flight word search as the only evidence of versioning, once the pin scenario exists. Delete worker-minted approval ids from the reference worker when the mock grows `hold_approval`. Until that edit lands in the course, the current reference worker remains the solution of record. This packet does not change it.
