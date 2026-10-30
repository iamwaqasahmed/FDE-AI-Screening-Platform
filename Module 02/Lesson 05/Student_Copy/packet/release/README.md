# Today's file drop

From: the steering committee
Case date: 2027-01-21

These pages match the grader's copy of `rel-m02-l05`. [Chapter 03](../../03-the-change.md) and [chapter 04](../../04-words.md) tell you which file to open, and in what order. This list is the drawer.

- [notices/cr-ain.md](notices/cr-ain.md)
- [systems/sched-ain.md](systems/sched-ain.md)
- [steering/steer-m02.md](steering/steer-m02.md)
- [openapi/sched-ain.yaml](openapi/sched-ain.yaml)
- [fixtures/queued.json](fixtures/queued.json)
- [fixtures/nightly.json](fixtures/nightly.json)
- [fixtures/missed.json](fixtures/missed.json)
- [fixtures/live-slot.json](fixtures/live-slot.json)

Leave [live-slot.json](fixtures/live-slot.json) in this drawer. It carries a watermark. The contract test reads that file from the built pack. A copy in `work/` fails the check, and the message does not print the watermark.
