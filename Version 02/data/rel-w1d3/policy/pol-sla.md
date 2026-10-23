# pol-sla

The SLA clock starts at `referral.submitted`. It does not start at booking.

working_days: 2

Count that many working days. The day of `referral.submitted` counts when it is a working day. If that day is not a working day, counting begins on the next one. The calendar file lists the weekend and the holidays.

Example. A referral submitted on Sunday counts Sunday as day one and Monday as day two.

retries: 2

A step that keeps asking to be retried is tried this many times. After that, record a dead letter and do not apply the event.

Apply events that share a referral in sequence order. The higher sequence is the letter you keep. A second delivery of the same event id changes nothing.

Use the criteria document whose status is in force when the referral starts.

An open row with the same patient and specialty is flagged. The referral still waits for a coordinator. It is not booked.

A coordinator holds the approval. The workflow does not accept or return the referral, and it does not book a slot.

If a hold is taken and the next step fails, release the hold.

`h-ain` has no slot API in this release. A hold or a booking there returns queued.
