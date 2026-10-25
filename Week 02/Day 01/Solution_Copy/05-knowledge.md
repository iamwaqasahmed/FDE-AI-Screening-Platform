# 05 — Knowledge

This answers the knowledge file from the morning. Open the [finished knowledge.md](work/knowledge.md) and put it beside yours.

The journey check reads two numbered lines. The first line has to name the booking assurance level. The second line has to say where the session row lives. When the first line is wrong, the message is `knowledge.md does not name the booking assurance level`. The message does not print the level. When the second line is wrong, the message is `knowledge.md does not say where the session row lives`.

The finished sentences are these.

## Which assurance level may book?

Booking and cancellation require loa-2.

That sentence is the second bullet of [loa.md](sources/release/identity/loa.md). The first bullet, `loa-1`, is the level that opens the assistant. The booking level is the step-up this day does not build. The states table in [chapter 03](03-the-sign-in.md) already marks that row as not this day.

## Where does the session row live?

The session row lives in the application database.

That is the `sessions` table in [session.py](work/app/session.py). It is not the hospital record. [token-flow.md](work/token-flow.md) says the same thing.

You have the finished day. The trainer's session is [06 — Trainer session](06-trainer.md).
