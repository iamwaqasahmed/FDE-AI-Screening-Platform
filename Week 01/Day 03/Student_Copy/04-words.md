# 04 — Words

Read this page once. You will look back at it while you read the stream and replace the worker. You do not need to memorize it.

These are the words this day uses. A definition here is the everyday meaning. When the rule lives in a file, the link is beside the word. Open that file when you need the sentence itself.

## The service

| Word | Meaning |
| --- | --- |
| Health cluster | A group of hospitals and primary care centers that plan and deliver care for one population. This client is the Al-Waha Health Cluster |
| Referral | A request from a local clinic for a hospital appointment. Today's workflow starts when that request is submitted |
| Patient | The person the referral is about. The event carries a `patient_key`. That key is not a name |
| Coordinator | The staff member who holds the approval. The workflow stops for that person. It does not accept, return, or book |
| Specialty | One hospital service line. Today's letters are endocrinology, and the id is `endo` |
| Endocrinology | Hormones and diabetes. The letter says the word endocrinology. The id on the row is `endo` |
| Clinic | The bookable service inside a hospital. [clinics.csv](packet/release/catalog/clinics.csv) maps a facility and a specialty to a clinic code. Today's code for Wadi endocrinology is `ENDO-CLN` |
| Slot | One bookable appointment on a clinic's schedule. A sentence in a letter must not give a slot away. This workflow does not book one |
| Appointment | A booked time for a patient to be seen. Booking is a later day. Today stops before it |

## The clock

| Word | Meaning |
| --- | --- |
| Event | One notice that something happened. Today's topic is `referral.submitted`. The file is [intake.jsonl](packet/release/events/intake.jsonl). Each line is one event. The line is long. The names in quotes, such as `event_id` and `scenario`, are the fields. Search the file for a scenario name. You do not have to read every word on the first pass |
| `event_id` | The id of that one delivery. The same id can arrive twice. [pol-sla.md](packet/release/policy/pol-sla.md) says a second delivery of the same event id changes nothing |
| Topic | The name of the event. Every line today is `referral.submitted`. [referral.submitted.md](packet/release/contracts/referral.submitted.md) is the contract |
| `occurred_at` | The clock time on the event. The contract says this is the clock. The date is the first ten characters |
| Sequence | The order of letters that share a referral. The higher sequence is the letter you keep. Apply the events in sequence order, even when the file arrives out of order |
| SLA | The service promise for how soon the referral is due. [pol-sla.md](packet/release/policy/pol-sla.md) says the SLA clock starts at `referral.submitted`. It does not start at booking |
| Working day | A day the SLA clock counts. The day of `referral.submitted` counts when it is a working day. If that day is not a working day, counting begins on the next one. The count is in the policy. The names are in [business-calendar.json](packet/release/calendar/business-calendar.json) |
| Weekend | The days the clock skips. The calendar file lists Friday and Saturday. [zones.md](packet/kickoff/world/zones.md) says the same pair |
| Holiday | A date the clock skips even when the weekday would otherwise count. The calendar file lists those dates under `holidays` |
| Idempotency | Doing the same event twice changes nothing. Here that means a second delivery of the same `event_id` does not open a second approval |

## The workflow

| Word | Meaning |
| --- | --- |
| `wf-intake` | The workflow you leave today. It runs from `referral.submitted` to a held approval |
| Mock | A stand-in that pretends to be a hospital system. [tools.py](packet/workflow/tools.py) is the mock. You read it. You do not edit it |
| Scenario | The name of one case in the stream, such as `happy` or `replay`. The check names the case when a row is wrong. It does not print the due date, the clause, or the fitting state |
| State | Where the referral stopped. A live referral stops at `approval.held`. A dead letter stops at `dead-letter` |
| Approval | The decision a coordinator still has to make. One referral gets one approval id. The workflow holds that approval. It does not accept or return |
| Hold | A short reservation of a slot, not a booking. [his-wadi.yaml](packet/release/openapi/his-wadi.yaml) calls it a hold with a short TTL. TTL means how long the reservation lasts. The policy says: if a hold is taken and the next step fails, release the hold |
| Release | Letting go of a hold after the next step fails. The referral still waits for a coordinator |
| `queued` | The status that comes back when a facility has no live slot API. [pol-sla.md](packet/release/policy/pol-sla.md) says a hold or a booking at `h-ain` returns queued |
| Booked | A slot that was given away. Today's rows stay unbooked. The policy says the workflow does not book |
| Criteria | The rule document for a specialty. Two pages are in the pack: [crit-endo-v3.md](packet/release/criteria/crit-endo-v3.md) and [crit-endo-v4.md](packet/release/criteria/crit-endo-v4.md). The policy says to use the document whose status is in force when the referral starts |
| In force | The status of the criteria document that is the rule today. A higher version can still be a draft. Read the status on each page |
| Draft | A criteria document that is not the rule yet. The workflow does not select it |
| Clause | The line on the criteria page that a return would cite. The workflow does not return the referral, so the log does not carry the clause. The check does not print it |
| Duplicate | An open row with the same patient and specialty. [open-referrals.csv](packet/release/events/open-referrals.csv) is that list. The referral is flagged. It still waits for a coordinator. It is not booked |
| Dead letter | A record that an event was not applied. [pol-sla.md](packet/release/policy/pol-sla.md) says a step that keeps asking to be retried is tried the policy's count of times, and after that you record a dead letter and do not apply the event |
| Retry | The fault that means the next step keeps asking to be tried again. The names are in [faults.json](packet/release/events/faults.json) |
| Compensate | The fault that means a hold was taken and the next step failed. Release the hold. The referral still stops for a person |
| Poison event | The check's name for an event that had to become a dead letter. Applying it means the row still opened an approval, booked, or left a hold open |
| In-flight | A referral that has already started. It keeps the criteria version it started with, even if a later document appears |
| Watermark | A marker planted in a file so a copy can be recognized. [pol-assistant-use.md](packet/kickoff/corpus/pol-assistant-use.md) says the watermark stays out of prompts, tickets, and the work you submit. One letter in [intake.jsonl](packet/release/events/intake.jsonl) carries one. Read it where it sits |

## The hospitals and the systems

[zones.md](packet/kickoff/world/zones.md) is the map. Today's letters use two of the facility ids. The clinic catalog uses one.

| Id | Meaning |
| --- | --- |
| `h-nakhl` | Nakhl General Hospital, in `zone-hospital` |
| `h-safra` | Safra General Hospital, in `zone-hospital` |
| `h-wadi` | Wadi Specialist Hospital, in `zone-private`. The letters that say Wadi Specialist Hospital use this id. [clinics.csv](packet/release/catalog/clinics.csv) has its endocrinology clinic |
| `h-ain` | Ain Diabetes and Eye Center, in `zone-hospital`. [pol-sla.md](packet/release/policy/pol-sla.md) says it has no slot API in this release. A hold or a booking there returns queued. Do not hold and do not book |
| `phc-nakhl-01` | Nakhl Central PHC, a primary health care center |
| `phc-safra-03` | Safra South PHC, a primary health care center |
| `phc-wadi-02` | Wadi Family PHC, a primary health care center |
| `phc-rim` | Rim Village PHC, a primary health care center |
| `ENDO-CLN` | The clinic code for endocrinology at `h-wadi`. It is a clinic id, not a facility id |
| `eref` | The system that owns `referral.submitted`. [referral.submitted.md](packet/release/contracts/referral.submitted.md) names the owner. [eref.yaml](packet/release/openapi/eref.yaml) is the dev contract. `decideReferral` is held for a coordinator |
| `his-wadi` | The hospital system at Wadi for holds and bookings. [his-wadi.yaml](packet/release/openapi/his-wadi.yaml) has `holdSlot` and `bookSlot`. Today you may hold. You do not book |

You have the words the later chapters use.

Next: [05 — The stream](05-the-stream.md).
