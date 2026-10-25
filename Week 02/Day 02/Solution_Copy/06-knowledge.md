# 06 — Knowledge

This answers the knowledge file from the morning. Open the [finished knowledge.md](work/knowledge.md) and put it beside yours.

The check reads two numbered lines. The first line has to contain `eref`. The second line has to contain `book`, and either `not` or `once`. When the first line is wrong, the message is `knowledge.md does not name the owner`. The message does not print the owner. When the second line is wrong, the message is `knowledge.md does not say what a replay does`.

The finished sentences are these.

## Who owns referral.submitted?

eref owns referral.submitted.

That is the owner cell on the `referral.submitted` row of [topics.md](sources/release/registry/topics.md). The same page says `session.cancelled` is owned by the hospital that holds the session. The question asks about the referral event.

## What does a replay of session.cancelled do?

A replay does not book a second time.

The cancellation file delivers `evt-can-1` twice. [cancel.py](work/app/cancel.py) returns the stored row on the second call. The booking count stays at one. The shell added a second booking. [Chapter 03](03-the-worker.md) is that worker.

You have the finished day. The trainer's session is [07 — Trainer session](07-trainer.md).
