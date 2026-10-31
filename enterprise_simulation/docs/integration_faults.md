# Integration symptoms

Desk notes from 7 January 2027 through 12 January 2027.

## Handset

The channel log has an outbox row `int-outbox-17` for INT-17. The consumer acknowledgement on that row is missing. The same outbox id is delivered a second time. Both deliveries carry idempotency key `int-outbox-17`, attempt 1 and attempt 2. The handset transcripts contain two texts, each reading: Northline: visit filed for referral INT-17 at Cedar Ridge.

## Slot

Hospital stream `int-17` has a slot file and a slot cancellation for INT-17. The cancellation time is 2027-01-11T18:10:00Z. The file time is 2027-01-11T21:00:00Z. The cancellation revision is 2. The file revision is 1.

## Partner

A partner message for INT-30 has status timeout on attempt 3.

## Morning board

On the morning of 12 January the board still shows 11 January. The queue snapshot at that reading has visible backlog 40, an oldest age of 960 seconds, and a live consumer.
