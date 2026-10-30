# 05 — The stream

[Chapter 04](04-words.md) defined the words. This chapter is the reading. Open the files in this order. A sentence in the policy is the rule. A date in the calendar is the calendar. The worker in chapter 06 follows these pages.

Today's drop is listed in [the release readme](packet/release/README.md). The case date is 12 January 2027. The sender is the enterprise architect.

## 1. The policy

Open [pol-sla.md](packet/release/policy/pol-sla.md).

The SLA clock starts at `referral.submitted`. It does not start at booking. Count the policy's working days. The day of `referral.submitted` counts when it is a working day. The calendar file lists the weekend and the holidays. The Sunday example on that page is the shape of the count: the start day is day one when it counts.

A second delivery of the same event id changes nothing. Events that share a referral are applied in sequence order. The higher sequence is the letter you keep.

Use the criteria document whose status is in force when the referral starts. An open row with the same patient and specialty is flagged. The referral still waits for a coordinator. It is not booked.

A coordinator holds the approval. The workflow does not accept or return the referral, and it does not book a slot. If a hold is taken and the next step fails, release the hold.

`h-ain` has no slot API in this release. A hold or a booking there returns queued.

The retry count is on the same page. After that many tries, record a dead letter and do not apply the event.

## 2. The calendar

Open [business-calendar.json](packet/release/calendar/business-calendar.json).

`weekend` is Friday and Saturday. The list named `working_days` in this file is Sunday through Thursday. That list is the names of the days. The number of days to count is in the policy, not in this list. `holidays` is three dates. Those dates are skipped even when the weekday name is on the list. Chapter 06 does not print the due date for you. You will copy it from the log after the worker runs, and you will check it against this file.

## 3. The contract

Open [referral.submitted.md](packet/release/contracts/referral.submitted.md).

The owner is `eref`. The required fields are `event_id`, `topic`, `occurred_at`, `sequence`, `referral_id`, `patient_key`, and `letter`. The clock time is `occurred_at`. A consumer ignores a field it does not know. `scenario` is on the stream and is not in this list. The worker may read it. It is not part of the contract.

## 4. The criteria

Open [crit-endo-v3.md](packet/release/criteria/crit-endo-v3.md) and [crit-endo-v4.md](packet/release/criteria/crit-endo-v4.md).

Read the status on each page. One document is in force. One is a draft. The policy says which status counts. The clause id sits on the page. The workflow does not return the referral, so you do not copy the clause into `work/`. The check will not print the clause if you pick the wrong document. It will name the case and say the criteria is not the one in force.

## 5. The two API files

Open [eref.yaml](packet/release/openapi/eref.yaml) and [his-wadi.yaml](packet/release/openapi/his-wadi.yaml).

`decideReferral` answers 202, held for a coordinator. `holdSlot` is a hold with a short TTL. `bookSlot` is a booked slot. The mock in [tools.py](packet/workflow/tools.py) pretends to be these calls. You do not edit that file. You do not call book from the worker you leave.

## 6. The stream

Open [intake.jsonl](packet/release/events/intake.jsonl). Read it where it sits.

Each line is one event. The line is long. The names in quotes are the fields. Search the file. In most editors the search box is Ctrl+F. On macOS it is Command+F. Type the text below, including the quotes, and press Enter.

1. Search for `"scenario": "replay"`. Two lines. Read `event_id` on each line. It is the same id. That is a second delivery. A second delivery changes nothing.
2. Search for `"scenario": "order"`. Two lines, one referral, two sequences. The higher `sequence` is the earlier of the two lines. Its letter names Wadi Specialist Hospital. The lower `sequence` is the later line. Its letter names Ain Diabetes and Eye Center. Keep the higher sequence. The clock uses the date on the lower sequence. That date is the ten characters of `occurred_at` before the letter T. Both of those timestamps fall on 2027-01-12, so the due date will not show which sequence started the clock. The facility will. The higher sequence names Wadi, so the row's facility is `h-wadi`.
3. Search for `"scenario": "ain"`. One line. The letter names Ain Diabetes and Eye Center and no other hospital.

The other lines are one referral, one sequence, and Wadi Specialist Hospital. You will match the duplicate in the next section, after the open-referrals file is open.

One letter has extra words after the hospital name. Those extra words are the watermark. Read them where they sit. Do not copy the file into `work/`. Do not paste the line into a prompt. [pol-assistant-use.md](packet/kickoff/corpus/pol-assistant-use.md) is the rule. The check's message does not print the watermark.

## 7. Faults, open referrals, and clinics

Open [faults.json](packet/release/events/faults.json). Two referral ids are named. One value is `compensate`. One value is `retry`.

Search the event file for each of those referral ids. Read the `scenario` name on that line. That name is the case the fault belongs to. You will use those two names when you label the log.

Open [open-referrals.csv](packet/release/events/open-referrals.csv). One row is already open. Copy the `patient_key`. Search the event file for it. That line is the duplicate. The specialty on the row is `endo`, and the letter says endocrinology. The new referral still waits for a coordinator. It is not booked.

Open [clinics.csv](packet/release/catalog/clinics.csv). One row: `h-wadi`, `endo`, `ENDO-CLN`. `h-ain` is not on this list, so a clinic lookup for Ain is empty.

You have read the pack the worker uses.

Next: [06 — The worker](06-the-worker.md).
