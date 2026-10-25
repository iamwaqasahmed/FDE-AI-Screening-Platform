# 07 — Knowledge

This answers the knowledge file from the morning. Open the finished [knowledge.md](work/knowledge.md) and put it beside yours.

The check reads two numbered lines. The first line has to contain `nightly`, `file`, or `queued`. The second line has to contain `Week 4` or `Stage 2`. When the first line is wrong, the message is `knowledge.md does not say why ain waits`. When the second line is wrong, the message is `knowledge.md does not say what stage 2 adds`. When there are fewer than two numbered lines, the message is `knowledge.md needs two answers`. The messages do not name a clinic code.

The finished sentences are these.

## Why can Ain not confirm a slot today?

Ain cannot confirm a slot today because sched-ain publishes a nightly file, and a booking stays queued.

[sched-ain.md](sources/release/systems/sched-ain.md) says the schedule is a nightly full file and a real-time booking returns queued. [queued.json](sources/release/fixtures/queued.json) records that status. The first knowledge line says the same thing in one sentence.

## What will Stage 2 add to monitoring?

Stage 2 adds the operations stack beyond request rate, error rate, and model latency, in Week 4.

[starter.md](sources/day4/dashboard/starter.md) shows those three lines and says the rest of the operations stack arrives in Week 4. The second knowledge line names Stage 2 and Week 4.

You have the finished day. The trainer's session is [08 — Trainer session](08-trainer.md).
