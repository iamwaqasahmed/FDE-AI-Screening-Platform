# 03 — The worker

[calendar_count.py](work/workflow/calendar_count.py) reads the weekend and the holidays from the calendar. [worker.py](work/workflow/worker.py) is the workflow. [tools.py](work/workflow/tools.py) stays the mock.

## The calendar

The starter counted Monday through Friday and dropped the calendar. Friday then counted, and Sunday did not, and a holiday counted when it fell on Monday through Friday.

The finished count uses the calendar's names. The start day counts when it is a working day. The policy's count is passed in. It is not written as a second copy of the number.

The case named `friday` is submitted on Thursday 2027-01-14. Thursday counts as day one. Friday and Saturday are the weekend. Sunday 2027-01-17 is day two. A Monday-to-Friday count would have landed on Friday 2027-01-15. That is the miss the check names, and it does not print the date.

The case named `holiday` is submitted on Tuesday 2027-03-09. Tuesday counts as day one. 2027-03-10, 2027-03-11, and 2027-03-12 are holidays, and Friday and Saturday are the weekend. Sunday 2027-03-14 is day two.

A referral submitted on Tuesday 2027-01-12 counts Tuesday as day one and Wednesday 2027-01-13 as day two. That is the due date on the ordinary rows. `ain` is submitted on Wednesday 2027-01-13, so Wednesday is day one and Thursday 2027-01-14 is day two.

## One approval, and the letter you keep

A second delivery of the same `event_id` is skipped. The replay row keeps `apr-ref-110` and does not add a second id.

Events that share a referral are sorted by sequence. The `order` case arrives as sequence 2, then sequence 1. Sequence 2 names Wadi. Sequence 1 names Ain and is later in the file. The letter you keep is sequence 2, so the suggestion is `h-wadi` and the clinic is `ENDO-CLN`. Both timestamps are 2027-01-12, so the due date does not change. The clock still uses the lowest sequence.

## Criteria, duplicate, hold, dead letter

The criteria id is `crit-endo-v3`, the document whose status is in force. The draft is not selected.

`duplicate` is true only for the patient and specialty already in the open-referrals file. That row is still `approval.held`, with one approval, and `booked` is false.

`h-ain` does not take a hold. `hold` is `none`. No row calls book. `booked` is false on every row, including Ain, where a queued reply would otherwise look like a booking.

`ref-170` is compensate. The hold is taken, finish fails, and the hold is released. The state stays `approval.held`.

`ref-180` is retry. Finish is called for the policy's retry count. The row is then a dead letter: state `dead-letter`, no approval, empty due date, hold `none`, `dead_letter` true. The event is not applied.

Every live row stops at `approval.held` with one approval id. That is the held approval a coordinator still has to decide.

Next: [04 — The note](04-the-note.md).
