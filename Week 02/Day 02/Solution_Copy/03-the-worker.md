# 03 — The worker

This is the intake and the cancellation worker from the morning. Open [intake.py](work/app/intake.py) and [cancel.py](work/app/cancel.py) and put them beside yours.

Every other file under `work/app` matches the starter. The check imports those modules and calls them. It does not compare the bytes. `intake.py`, `cancel.py`, and `mart.py` are the three that differ. `mart.py` is explained in [chapter 05](05-the-mart.md).

## Intake

[eref.yaml](sources/release/openapi/eref.yaml) still lists a poll path. The finished intake does not use it. `mode` is `webhook`.

[topics.md](sources/release/registry/topics.md) lists the fields a consumer may store for `referral.submitted`. [registry.py](work/app/registry.py) reads that row. `keep` returns those fields, and a sorted list of every other key. The event is not rejected for an extra key. `letter` is on the list, and the record then leaves it off, because the letter value is the watermark.

While the shell is still in place, the check says `intake still polls`. When an unknown key is rejected, or is missing from `ignored`, the check says `an unknown field stopped intake`. When that key is stored on the record, the check says `an unknown field was stored`. None of those messages names the key.

## Cancellations

[session.cancelled.jsonl](sources/release/events/session.cancelled.jsonl) has three lines. The first two share `evt-can-1`. The third is `evt-can-2`, booking `bkg-2`.

[sms-faults.json](sources/release/channels/sms-faults.json) rejects `bkg-2`.

`apply` returns the stored row when the event id is already in the table, so the replay stays at one booking and one SMS. The shell booked again on that second call. The check says `replay booked again`.

An accepted receipt stores `notified`, one booking, and one SMS. A rejected receipt stores `compensated`, zero bookings, zero SMS, and `hold` `released`. The shell left the hold open. The check says `the hold was left open`.

The check then sends one event that is not in the file. `slot` is false. The finished worker stores `escalated`, with no booking and no SMS. The shell booked that case too. The check says `no-slot cancellation was booked`.

[sms.py](work/app/sms.py) writes the body `Your booking {booking_id} has a new time.` when the receipt is accepted, and an empty body when it is rejected.

The webhook file is not in this folder. The check reads it from the built pack. A copy under `work/` fails. The message is `a watermarked sample is in the work directory`, and it does not print the watermark.

## The path through the files

The morning chapter [06-the-worker.md](../Student_Copy/06-the-worker.md) has the section How the replacement works. That section is the path through the files this page compares. Read it beside the finished file. The notes above are the decisions the check names.

Next: [04 — The pages](04-the-pages.md).
