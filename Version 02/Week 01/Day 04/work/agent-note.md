# Agent note

## Tool list

- `referral.status` reads the queue. The reply count is that result.
- `slots.offer` lists a slot, or names the constraint that blocks it.
- `slots.book` writes a booking. It waits for an approval id.
- `sms.send` runs after the booking.
- `referral.return` sends a return. It waits for an approval id.
- `safety.redirect` hands the conversation to a person.

## Privilege boundary

The extractor reads the letter and does not hold the book tool or the message tool. A second agent is worth its tokens when a letter would otherwise be able to book. Status stays one agent and one tool, `referral.status`.

## Refusal

A coordinator will answer, and this visit is not booked.
