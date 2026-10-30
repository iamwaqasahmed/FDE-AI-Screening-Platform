# 04 — Exercises, assessment, and instruction

One person holds every role. There is no cohort, no timetable, and no partner student. The chapter order is the staffing plan. Each role has a page in `work/` and a check. None of the pages is a pasted solution.

## Prerequisites

The student needs Module 1's claim-versus-fact habit, the finding that the wait chart's date column is the warehouse clock (`p-clock`, named as an id, not as a rate), zones, and the rule that a watermark stays out of `work/` and out of prompts. They need Module 1 Lesson 3's `referral.submitted` as an event that already existed on disk, so this lesson can say the new fact is the push. They need Lesson 1 of this module: a spec can drop a field, a generated client that still sends the old field fails, and booking from chat still waits.

They do not need Kafka, Debezium, dbt, an AsyncAPI toolchain, or a WhatsApp developer account. Readings are excerpts the packet already mirrors in the course's own words, plus the links in the research file for the facilitator. A student who can run `python -m alwaha.check` can do the day.

Words to define before they are used, on the words page, because the journey log for this lesson already treats that as a gate: webhook, subscription, inbox, replay, quarantine, anti-corruption layer, commit accept, application acknowledgement, customer service window, template, snapshot, data contract, grain, time anchor, authoritative. `session` is defined three times in one table. `dms` is defined as the document feed and explicitly as not a database change stream.

## The five roles, all on one person

| Order | Role | Work | Done when |
| --- | --- | --- | --- |
| 1 | Lead | `sprint.md` and `decision.md` | Each system has a pipe (A, B, or C from the redesign). The mart is a snapshot and comes after the subscription. CDC is rejected for `eref` with a reason. `dms` is left for later |
| 2 | Architect | `zones.md` and `loss.md` | Engine in `zone-hospital`, worker in `zone-private`. Loss count recorded. File order is not the applied order. Reply level is accept-only while the application result is open |
| 3 | Application | `intake.py`, `cancel.py` | Inbox on `source` + `id`. Breaking payload quarantined. Crash fixture sends once. Unknown compatible field ignored. Watermark not stored |
| 4 | Product | `states.md`, `channel.md` | Patient-visible lines match stored states. Closed WhatsApp window does not send free text. No national id. No wait figure |
| 5 | Data | `contract.md`, `mart.py` | Owner, grain, biased anchor, ban on baseline use, freshness. `authoritative` false. Figure absent from every graded note |

The AI-flavored work is the channel sentence and the ban on quoting the mart to a patient. It is not a model call. If a later chapter lets an assistant draft the SMS, the draft is still graded by the same checker: word `booking`, no ten-digit run, no wait figure, and the draft is not sent on a closed WhatsApp window. The assistant does not choose the pipe and does not repair HL7.

## Exercise sequence

The sequence fades. Early items show a shape. Later items withhold the answer. No chapter contains a finished `accept` or `apply`.

**1. Read the pack, do not copy it.** Feeds notice, registry, `eref.yaml` paths, HL7 demo, WhatsApp partner page that now states 24 hours and who opens the window, mart header. Run the demo. Write the two order lines on the ungraded scratch sheet if that helps, then write the graded `loss.md` from the key counts in the JSONL. The webhook file stays in the packet. Copying it into `work/` still fails.

**2. Decision memo, before code.** For `eref`, the two HL7 hospitals, `sched-ain`, and `bi`, one sentence each: pipe, and the failure mode you are buying (duplicates, stale file, or a translation loss). Reject CDC for `eref` because the domain event already exists. Reject a webhook for the mart because the extract is not an occurrence. Reject "we will poll `eref` a bit longer" because that path hid `referral.submitted`. This is the lead's page. The checker looks for the system ids and for the mart sentence after the subscription sentence, which is the current sprint rule extended to the memo.

**3. Registry evolution, on paper then in code.** v1 fixture and v2 fixture share `source` and differ by an optional field the v2 row lists. Both store one referral. The break fixture removes a required field. The student function quarantines it. A short comment in the memo names the compatibility mode as backward: new readers can read old payloads, and a rename is not registered. Do not ask them to run Schema Registry. The mode's name is the learning; the JSON files are the lab.

**4. Inbox.** Replace the shell that books every delivery. The starter still polls and still inserts after a fictional send. The chapter describes the failure window in prose (send, crash, replay, second send) and shows the *table* (`inbox` primary key `source, id`, `outbox` status) without the control flow. The student writes the control flow. Hints are the Azure steps: if the key exists, return the stored outcome; if not, write the key and the business row together; send only after that commit. A unit fixture calls `apply` twice. A second fixture loads a half-finished database file where an outbox row is `pending` and the inbox row is missing, and expects one send.

**5. Channel policy.** Given four rows (window open, window closed with template, window closed without template, opt-in false), the function returns the four outcomes. `states.md` uses only words the worker stores, plus a separate "words the patient sees" column if product wants `rebooked` as copy. The current four-name paste with `rebooked` stored nowhere is the confusion to remove. Suggested map, which the solution may use: `notified` means partner accepted; `delivered` waits for Lesson 3; `compensated` means the hold was released; `escalated` means a person calls; the SMS sentence is copy, not a status.

**6. Contract.** Open the CSV. The header is visible. The chapter does not print a data row. The student names the date column they see, says it starts at booking, says the wait column is a published claim, says two rows with one person key are two rows, and says the assistant must not speak the number. `mart.py` returns that verdict. Then, and only then, the knowledge file: who owns `referral.submitted` (`eref`), who owns the extract (`bi`), what a replay does (returns the committed outcome and does not send again), what a replay does *not* do (it does not prove the first attempt's SMS was delivered).

**7. Finish.** One check command, same entry point as today, still `chk-journey`, still profile `practice`.

Facilitator traps to keep in the pocket, updated: memo that picks CDC because it sounds modern; loss page that invents the qualifier; inbox that sends before commit; WhatsApp page that copies the SMS sentence into a closed window; contract that calls the date column the true clock; note that contains the wait integer; webhook file copied into `work/`; knowledge line that names the owner of the wrong topic.

## Assessment

Keep the checker philosophy from `journey_m02` and `notes_w2`. Failures name the behavior. They do not print the extra field, the dropped field, the segment, the wait figure, the canary, or the owner. `test_m02_l02.py` should grow, not loosen: demo stdout stays the two lines; templates and the door README stay free of the secrets; only the trap modules differ from the shell, and the set of trap modules grows by `channel.py` if that file is a shell. Sealed modules (`registry.py`, `sms.py`, Lesson 1 auth and chat) stay byte-identical unless the redesign deliberately adds a policy hook. Prefer a new small module over editing `sms.py`, so Lesson 1's surface stays stable.

| Check line (behavior) | Pass condition |
| --- | --- |
| `intake still polls` | Mode is the push path and a referral id from the v1 body is stored |
| `an unknown field stopped intake` / `an unknown field was stored` | Compatible extra key ignored, not rejected, not stored |
| `a breaking change was stored` | Break fixture quarantined, no success referral |
| `replay booked again` | Second call, same source and id, same booking count |
| `a crash sent twice` | Half-finished fixture ends with one send |
| `a conflicting replay was applied` | Same id, different booking, quarantined |
| `the hold was left open` | Reject releases the hold in a row a second call can see |
| `no-slot cancellation was booked` | Escalated, no send |
| `the mapping loss was not recorded` | Loss count present and non-zero on the mapping row |
| `file order was treated as clinical order` | Applied sequence is the higher sequence, not the last line |
| `whatsapp free text outside the window` | Closed window does not take the SMS sentence |
| `a patient-visible state is missing` | Every stored state has a patient line, and every patient line maps to a stored state or is marked copy |
| `sms wording carries a national id` | No ten-digit run |
| `wait number was used as truth` | Figure absent from notes, states, SMS, sprint, contract; `authoritative` is false |
| `the mart clock is not named` | Date column named and described as the warehouse start, not as referral time |
| `the contract treats a row as a person` | Grain clause refuses that claim when the two-row fixture is in the pack |
| `sprint.md does not sequence the subscription before the mart` | Existing order rule |
| `knowledge.md does not name the owner` | `eref` on the referral event, and the extract owner is not substituted |
| `knowledge.md does not say what a replay does` | Does not book or send a second time after commit |
| `a watermarked sample is in the work directory` | Existing canary rule |

A poison event that raises should be reported as `a poison event stopped the batch` only if later fixtures did not run. If the worker isolates it, the rest of the report stands. Change the broad `except` only for that isolation. A syntax error in the student file still means `the worker did not run`.

Do not grade style, docstring length, or whether they mentioned CloudEvents by name. Do grade `source` and `id` if the inbox key is part of the pass. A student who uses a single column that concatenates the two has met the rule. A student who keys only on `event_id` passes today's fixtures and fails a new fixture where two sources share an id. Add that fixture. It is the reason the CloudEvents citation is in the course.

Scores stay binary per line, many lines, as now. A narrative rubric on top invites the facilitator to pass a fluent memo that the checker would fail. The memo is graded by required phrases and by order, the way `sprint.md` is graded today, plus the negative tests (the words CDC and `eref` appear in a sentence that rejects the pairing; the exact rejection sentence is not the only acceptable wording, so the check looks for both ids and a rejection cue such as `not` near `cdc` or `log`). Keep that cue loose enough for a paraphrase and tight enough that "we should CDC everything" fails.

## Solution approach the facilitator holds

The solution copy keeps a working tree the checker can run, as it does now. It does not become the student chapter.

Intake: `registry.keep` for the topic and version; drop keys not on that version; if a required key is absent, return `rejected` true and store a quarantine row; never copy the canary field, and do not list that field as required business data. Cancellation: transaction for inbox plus booking state; commit; send through the channel function; record outbox; compensate in a second transaction. Mart: read the header, refuse authority, echo the claim only under `published_claim`. Contract markdown matches the clauses in the redesign file. Loss markdown uses counts and sequence numbers only.

The trainer session walks the crash window with the half-finished database open, then the closed WhatsApp window, then the contract sentence "booking is when the warehouse starts, referral is when the patient started waiting." Interviews stay optional debrief. They are claim-versus-fact practice, and the day no longer depends on them for facts the packet pages already state. If they remain, the student writes them before the check, because reading them only in the solution wastes the access manager's line about the desk.

Lesson 3 receives an outbox row and a receipt fixture. It should fail a test that sleeps, as it does now, and it should fail a test that treats `accepted` as `delivered`. That is a one-line dependency in Lesson 3's background, not a second integration course.

## Self-paced instructional design

Chapters stay short enough to finish in one sitting on a laptop. The target is the current length of the day, not a new module. Readings that exceed a page are facilitator links. The student packet carries a one-screen partner page for WhatsApp (24 hours, user opens, template outside, accept is not delivery, opt-in) and a one-screen acknowledgement page (commit accept versus application accept, no segment grammar). Both pages are the course's words, checked against the public documents so the fiction does not contradict Meta or HL7.

Worked example: the happy cancellation, narrated, not pasted as the function. Practice: the replay, which the current chapter already explains well. Novel problem: the crash fixture and the closed window, which the worked example does not solve. That is the line between instruction and answer key.

Errors the finish table must keep explaining in behavior language: poll left in place, replay booked, hold open, no-slot booked, watermark, missing state, missing zone, national id, mart figure, subscription ordered after the mart, knowledge shape. Add rows for the new lines. Recovery stays `prepare_work.py` plus rewriting the pages. Tell the student to repair their own function. Remove "paste the block again," because there is no block.

One person can stall by trying to build Kafka. The decision chapter says, in the done line, that a rejected architecture is a paragraph and a running broker is a wrong turn. The setup chapter does not install Docker services beyond what Lesson 1 already required for the shell.

Accessibility of the teaching: the same plain language as the current words chapter. Tables for states and zones stay, because the checker already reads them. New tables for the contract use the same two-column habit so the note parser can grow rather than a new prose scorer.

## What the student must not be handed

The finished functions. A data row of the mart. The hidden field names. The wait integer. A sentence of the form "the clock column is booking_date" with no bias clause. A WhatsApp page that says only "there is a window." An instruction that `dms` is something they might build today. A diagram with no human escalate state. A design that lets the assistant quote `wait_days` to a patient or use it as the value baseline. Those last two are the same family as the Module 1 traps (no human step, promising triage): the feed is allowed to move a booking notice, and it is not allowed to become the clinical or operational authority.
