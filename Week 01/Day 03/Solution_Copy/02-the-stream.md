# 02 — The stream

The rule is [pol-sla.md](sources/release/policy/pol-sla.md). The calendar is [business-calendar.json](sources/release/calendar/business-calendar.json). The contract is [referral.submitted.md](sources/release/contracts/referral.submitted.md).

## What each page is allowed to support

The policy starts the SLA clock at `referral.submitted`. It does not start at booking. The day of that event counts when it is a working day. The count is the policy's working-day count. The calendar names the weekend as Friday and Saturday, the working days as Sunday through Thursday, and three holidays: 2027-03-10, 2027-03-11, and 2027-03-12.

A second delivery of the same event id changes nothing. Events that share a referral are applied in sequence order. The higher sequence is the letter you keep. The clock uses the lowest sequence's `occurred_at` date.

The criteria page whose status is in force is [crit-endo-v3.md](sources/release/criteria/crit-endo-v3.md). [crit-endo-v4.md](sources/release/criteria/crit-endo-v4.md) is a draft. A higher version does not win. The clause id stays on the page. The workflow does not return the referral, so the log does not carry the clause.

An open row with the same patient and specialty is in [open-referrals.csv](sources/release/events/open-referrals.csv): `pt-160`, `endo`, `ref-existing`. That referral is flagged. It still waits for a coordinator. It is not booked.

A coordinator holds the approval. The workflow does not accept, return, or book. If a hold is taken and the next step fails, release the hold. [faults.json](sources/release/events/faults.json) names `ref-170` as compensate and `ref-180` as retry. After the policy's retry count, record a dead letter and do not apply the event.

`h-ain` has no slot API in this release. A hold or a booking there returns queued. The worker does not hold there and does not book. [clinics.csv](sources/release/catalog/clinics.csv) has one clinic, `ENDO-CLN`, for `h-wadi` and `endo`. Ain is not on that list, so the clinic is empty.

[eref.yaml](sources/release/openapi/eref.yaml) holds `decideReferral` for a coordinator. [his-wadi.yaml](sources/release/openapi/his-wadi.yaml) has a hold and a booking. The mock client can call both. The worker calls hold only when the facility is not `h-ain`, and it never calls book.

The contract owner is `eref`. Required fields are `event_id`, `topic`, `occurred_at`, `sequence`, `referral_id`, `patient_key`, and `letter`. A consumer ignores a field it does not know. `scenario` is extra. The worker reads it so the log can name the case.

[zones.md](sources/kickoff/world/zones.md) places `h-wadi` in `zone-private` and `h-ain`, `h-nakhl`, and `h-safra` in `zone-hospital`. The letters today use `h-wadi` and `h-ain`. [ea.md](sources/kickoff/personas/ea.md) says a live slot must not be promised where none exists. The policy is the sentence the worker follows.

The event file is not in this folder. One letter carries a watermark. [pol-assistant-use.md](sources/kickoff/corpus/pol-assistant-use.md) keeps that line out of the work the check reads.

Next: [03 — The worker](03-the-worker.md).
