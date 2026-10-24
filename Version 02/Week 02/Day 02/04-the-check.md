# The check

From `problem_simulation`, with your work directory filled in:

```text
python -m alwaha.check journey --release rel-w2d2 --work "..\Week 02\Day 02\work"
```

`chk-w2-journey` scores the webhook intake, the cancellation deliveries, the mart read, and the notes from the mart step. A miss says the intake still polls, the replay booked again, or the wait number was used as truth. It does not name a field, a figure, or an owner.

A watermarked webhook file copied into `work/` fails the check. The message does not print the watermark.

Then write `work/knowledge.md` with two short answers:

1. Who owns `referral.submitted`?
2. What does a replay of `session.cancelled` do?

The day is done when the check prints `passed` and the knowledge file has both answers.
