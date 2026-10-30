# 01 — Existing lesson evaluation

`rel-m02-l02` is the day events replace the old poll. The syllabus line in `course_design/module-02.md` is "Integrate LLMs with enterprise systems, APIs, databases, and external services" and "event-driven integrations." The objective is narrower and better: intake and cancellation flow through cluster systems, and the mart's wait number stays a claim. The slide deck repeats four nouns — webhooks, HL7 v2 as a feed, the schema registry, messaging windows — then sends the room to a lab. That list is the right neighborhood. The lab does not make the student design any of the four.

## What the day actually is

The student copy is ten chapters, `00-background` through `09-finish`. One person holds lead, product, application, architect, and the SMS line. That self-paced rule is sound and should survive. The work product is three replaced modules (`intake.py`, `cancel.py`, `mart.py`) plus `sprint.md`, `states.md`, `zones.md`, `sms.md`, `mart.md`, and `knowledge.md`. `chk-journey` re-imports the worker. A hand-typed `trace.json` does not count. The checker hides `priorityHint`, `sub_specialty`, the wait figure, the owner string in the failure text, and the watermark. `test_m02_l02.py` locks the HL7 demo to two lines and forbids those secrets in the lesson-root README and the blank templates. Those guards are worth more than the paste.

The five steps in the background chapter are: read the feeds notice, the registry, and the HL7 demo; sequence the sprint so subscriptions precede the mart; subscribe so a repeated event books once, a failed text releases the hold, and a cancellation with no slot does not book; write the patient states, the zone crossing, the SMS line, and the mart clock; answer who owns `referral.submitted` and what a replay does.

Chapters 05, 06, 07, and 08 then paste the finished markdown and the finished Python. The "before you paste" prompts ("which function ignores a field", "which column is the clock") are rhetorical. A reader who pastes without answering still passes. `prepare_work.py` restores the shells and the blank pages, and the recovery path is "paste the blocks again." The instructional pattern is transcription. The concepts in the words chapter are defined well enough that a strong reader could implement the shell. The chapter then removes the need to implement it.

**Proven** as a teaching move: a checker that fails closed and does not echo the secret. **Experimental** as a teaching move: shipping the reference solution in the student chapter and calling the paste the lab. That second pattern is what this redesign deletes.

## The webhook is a function call

`packet/app/intake.py` returns `mode: poll` and ignores the body. The replacement calls `registry.keep` and returns `mode: webhook`. There is no HTTP server, no signature, no retry schedule, and no dead letter. `eref.yaml` has `readReferral` and `subscribeReferralSubmitted`. The student is told the first is the old poll and the second is today's path. The subscription is never registered by code the student writes. `run.py` loads a JSON file and calls `accept`.

That is a fair simulation of the *decision* (push, and tolerate an unknown key) and a poor simulation of the *operation*. Production webhooks are at-least-once. A 2xx often means "I accepted the HTTP request," which is the same split Meta documents for WhatsApp: the Messages API success body means the request was accepted, and delivery arrives later on a status webhook. HL7's enhanced acknowledgement mode draws the same line between commit accept (`CA`) and application accept (`AA`). The lesson's intake returns a record and never acknowledges anything. The student cannot point at a moment and say "this response released the sender."

Unknown-field behavior is the one real consumer rule the code enforces. `registry.keep` splits the body on the `referral.submitted` allow-list. `priorityHint` is ignored and must not be stored, and it must not set `rejected`. `letter` is on the allow-list, and the replacement then drops it because the value is the profile canary. The checker treats a canary in the result blob as a watermark failure and suppresses the other misses. Mixing a security canary with a schema field teaches a false rule: some registered fields are stored and one registered field is stripped for a reason that is not in the registry. An anti-corruption layer would record "this key is outside the contract" in one place and "this value must not be copied into work" in another. `keep` does the first. The dict comprehension does the second. The words chapter calls both "the schema registry."

The version cell in `topics.md` is `1` for both topics. `registry.py` reads column four and never reads the version. Owner is prose for `knowledge.md` (`eref` on the referral row, `hospital` on the cancellation row). The worker does not check owner. A registry that cannot reject a breaking change is a glossary.

## Idempotency is the happy path only

`session.cancelled.jsonl` delivers `evt-can-1` twice and then `evt-can-2`, which `sms-faults.json` rejects. The checker also sends a third event with `slot` false. The replacement in chapter 06:

1. Creates `deliveries` with `event_id` as primary key.
2. Returns the stored row when the id exists, with an empty body, and does not call `sms.send`.
3. On `slot` false, stores `escalated`, zero bookings, zero SMS, hold `none`.
4. Otherwise calls `sms.send`, then inserts `notified` or `compensated`.

The duplicate-id path is the right story for a replay that arrives after a commit. It is the wrong story for a crash. The text is sent before the row exists. If the process dies in between, the replay does not find a row, sends again, and books again. The checker never kills the process there, so the pasted file passes `replay booked again` while leaving the window open. The insert is also a separate `commit` from the send, because the send is not a database write. That is the dual-write the transactional outbox exists to avoid, seen from the consumer side.

The hold is a string column (`none` or `released`), not a row in a booking table that a second worker could race. Compensation is "store compensated." There is no outbox row a later receipt lesson can consume. Lesson 3 will time the SMS receipt against a case clock and will fail tests that sleep. This lesson does not leave it a durable "send was attempted" record. The states page makes this worse for a careful reader: `rebooked` is what the patient is told, and the worker stores `notified`. The page says the worker does not store `rebooked`. Four patient-visible words and three stored words is a legitimate product distinction. It is presented as a paste of a table, so the student never decides which word is a status and which is a copy line.

`scenario` on the event (`happy`, `replay`, `compensate`) is a test tag inside the payload. A production consumer that branched on `scenario` would be coupled to the grader. The finished code ignores it and keys on `event_id`, which is the right accident. Nothing in the chapter says "do not branch on the scenario field."

## HL7 is a demo, and the loss is trainer-only

Chapter 03 runs `python -m alwaha.demo.hl7 --profile practice` and requires two lines: file order keeps sequence 1, sequence order keeps sequence 2. The student types those lines into `notes/feed-lines.md`. The checker does not read that file. `int-engine.jsonl` is two SIU rows out of order, then a mapping row. The generator's mapping has a raw `ZSS` value and a mapped object that keeps `specialty` and drops the other value. The demo is forbidden to print the dropped field, the extra field, `thyroid`, or `ZSS`. Solution `hl7.md` says the mapping drops `sub_specialty`. Students are told not to write `hl7.md`.

So the most important HL7 fact in the pack — the integration engine is a translation that loses a clinical qualifier, and arrival order is not sequence order — is visible as two sentences about sequence numbers. The student is warned not to invent a field the sample dropped. That warning protects the canary. It also blocks the design sentence an architect should write: "the engine's mapped object is smaller than the raw message; the loss is a defect in the translation, and the worker must not invent the missing qualifier." The words chapter calls HL7 "a feed" and "not the referral event `eref` owns." That sentence is true and thin. It does not mention acknowledgements at all. A hospital feed that only prints order lines will teach people to sort JSONL. It will not teach them that a commit accept releases the sender from resending, and an application reject means the booking did not happen.

`his-safra` in the facilitator systems note is the planted defect: SIU messages arrive out of order. `his-nakhl` reuses MRNs and has unmarked Hijri dates. `int-engine` drops the sub-specialty and, on another change, logs PHI. None of that reaches the graded page except the two order lines. The zone table (`int-engine` in `zone-hospital`, `wf-session-cancelled` in `zone-private`) is the architect's entire deliverable, and it is pasted. The placement is defensible: the engine follows the HL7 hospitals, and the worker follows `h-wadi`. A zone row is not an anti-corruption layer.

## WhatsApp is a definition

`wa.md` in the packet is three sentences: a template needs to be registered, a reply after the session window is rejected, SMS is what the check scores. The words chapter repeats them and says the student does not write a WhatsApp page. Chapter 03 says the same. The access-manager interview, which the checker does not read, says a reply dies after the session window. The interview is solution-side.

What is missing, against Meta's own service-message document, is the operational rule a product owner needs:

- The window is 24 hours.
- A WhatsApp user message or call opens it. Another user message or call resets it.
- A business send does not, by itself, open a new window.
- Outside the window the only sends are pre-approved templates.
- The user must have opted in.
- Acceptance by the API is not delivery. Status comes back on a webhook. Order of a burst is not guaranteed.

A cancelled clinic session is business-initiated. If the patient has not written in the last day, free text is the wrong tool, and "Your booking has a new time" as an SMS string does not become a legal WhatsApp session message by copying it. The SMS checker wants the word `booking` and rejects a ten-digit run. That is a real PHI-in-the-channel rule and it is graded. The channel *choice* is not. `sms.py` is sealed. The student pastes one sentence into `sms.md`.

`dms.md` says the change feed is not part of today's check. In the systems note, `dms` is versions, audiences, approvals, and a document change feed, with a planted misfiled circular. It is not Debezium and it is not AWS Database Migration Service. Leaving the file in the packet as a one-line refusal teaches the student to skip a noun. It does not teach when a change feed is the wrong pipe for a domain event. That distinction belongs in the redesign, and the document system should stay out of this day's build.

## The mart trap is the right idea and the wrong task

Facilitator problem `p-clock`: the dashboard understates waiting because the mart starts the clock at booking, not at referral. The fitting approach is to correct the SQL. The trap is treating the dashboard as the baseline for a business case. The `bi` export says the same thing, and adds that people are counted as rows and that eligibility SQL is stale. The access manager's graded-adjacent fact is that the mart wait figure is not the number at the desk. Module 1 Lesson 2 already found the date column. This lesson's job is to keep that finding attached to a feed the assistant might read.

The shell sets `clock` to `wait_days` and `trusted` to true. The replacement sets `clock` to `booking_date`, `trusted` to false, and still returns the wait cell as an integer so the trace can show it. `journey_m02._run` appends `wait number was used as truth` when `trusted` is true, when `clock` is not the date column, or when the figure appears in the cancellation rows. `notes_w2._mart_note` requires the column name in `mart.md` and rejects the figure digit. The sprint must mention a subscription or webhook before the word mart.

Read as a checker, this is coherent: do not trust the wait cell, and do name the date column you were shown in Module 1. Read as a data contract, it is inverted. `booking_date` is the biased anchor. Requiring it as "the clock" lets a student write "the clock column is booking_date" and believe they have found the source of truth. The chapter even says "That date column is the clock." The distrust flag sits on the wait cell, which is a projection of the biased anchor, so both columns are one lie seen twice. The student is not asked:

- whose definition this is (`bi`, not the desk);
- what event starts the wait the desk believes (referral, which this lesson is finally receiving as `referral.submitted`);
- whether one CSV row is one person (the systems note says people are counted as rows; the fixture is one row, so the grain bug cannot appear);
- what a downstream assistant is forbidden to say ("you will be seen in N days" copied from the extract).

dbt's model contracts, cited in the research file, fail a build when column names and types drift. They do not fail a build when an integer column means the wrong interval. This lesson grades the analogue of the type check. The semantic defect is `p-clock`, and the paste never states it.

The extract picture in chapter 08 includes the wait cell for the practice profile. The failure message hides the figure. The chapter does not. A student on a different seed still passes by pasting a note with no digits, so the lab is robust to the seed. The reading is not: it shows one profile's number and then says not to copy it. Blank templates are clean. `test_m02_l02.py` only scans the lesson-root README and `packet/templates` for the clock name and the hidden fields. Student chapters are outside that scan, which is why the answer can live in chapter 08.

`mart.read` still returns the integer. The trace is allowed to contain it. The note is not. That split is a good instinct (operators may see a value they must not promote) and it is unexplained. A contract would call the column `published_and_non_authoritative` and would name the consumer ban. A boolean `trusted: false` on a Python dict is a sticker.

## What the knowledge file measures

Two lines: a first line containing `eref`, a second containing `book` and either `not` or `once`. The finished sentences are "eref owns referral.submitted" and "A replay does not book a second time." The checker accepts any wording inside that net. Ownership of a topic is a real registry idea. The question does not ask what the owner owes the consumer when the payload grows, or what the hospital owes when `session.cancelled` is replayed after a crash. The second answer describes the stored-row path only.

Interviews exist on the solution side (`ea.notes.md`, `access-mgr.notes.md`) with claim versus fact rows. Students are not asked to write them. The architect's facts (HL7 still flows from two hospitals, `eref` pushes, the engine sits in `zone-hospital`) and the access manager's facts (SMS for a cancelled session, WhatsApp window, mart figure is not the desk) are the raw material of the decision memo. They sit where the student is told not to look until the check has passed. By then the pastes are done.

## What is already good enough to keep

The lesson is not empty. These pieces match how integration actually fails, and they are already wired to a checker:

| Piece | Why it belongs | Maturity of the current treatment |
| --- | --- | --- |
| Secret-hiding failures | The miss names the behavior, not the canary | Proven pedagogy. Keep |
| Duplicate `event_id` returns the first outcome | Consumer idempotency under at-least-once | Proven idea, partial implementation |
| Rejected receipt releases the hold and books nothing | Compensation when the channel says no | Proven idea, in-process only |
| No slot escalates with no SMS | Do not invent a place | Proven product rule |
| Unknown key ignored, event not rejected | Tolerant consumer | Proven for a compatible add; silent on a breaking remove |
| Subscription ordered before the mart read | Do not let a warehouse number drive the workflow | Proven sequence |
| Watermark must not land in `work/` or in the stored letter | Untrusted payload, assistant-use rule from Module 1 | Proven guard, confused with the schema |
| SMS must not carry a ten-digit identifier | Channel content policy | Proven and too narrow |
| HL7 file order versus sequence order | Arrival order is not clinical order | Proven demo, ungraded |
| One person, five parts | Matches the self-paced course | Proven structure |

The dependency the curriculum map names is right: Module 1's date column, Module 1's `referral.submitted`, yesterday's sign-in. The lead to Lesson 3 is right: freeze receipt timing, fail the suite when a fault is on. This lesson should hand Lesson 3 a receipt that was produced by an outbox, not a new vocabulary list.

## Evaluation in one judgement

The day discovers the correct trap and then grades a label. Enterprise integration, as an FDE has to practice it, is the choice of pipe, the translation at the boundary, the compatibility rule when the payload changes, the idempotent consumer under replay and crash, the channel rule that decides SMS versus a WhatsApp template, and the data contract that says the mart's number is a published claim with a known bias. `rel-m02-l02` mentions each of those and grades a paste of three short functions. The paste is what to delete. The trap is what to build the lesson around.
