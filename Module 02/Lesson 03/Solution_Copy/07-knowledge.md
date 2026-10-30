# 07 — Knowledge

This answers the knowledge file from the morning. Open the finished [knowledge.md](work/knowledge.md) and put it beside yours.

The check reads two numbered lines. The first line has to contain `clock` or `switch`. The second line has to contain `state` or `mock`, and also `fixture` or `recorded`. When the first line is wrong, the message is `knowledge.md does not say why a sleep fails`. When the second line is wrong, the message is `knowledge.md does not say what an AI journey asserts`. When there are fewer than two numbered lines, the message is `knowledge.md needs two answers`.

The finished sentences are these.

## Why is a fixed sleep a bad receipt test?

A fixed sleep follows the wall clock. The receipt follows the case clock, and the switch can hold it.

[guide.md](sources/release/clock/guide.md) says to advance the pinned time. [receipt.json](sources/release/clock/receipt.json) holds the interval and the switch. A wait on the wall clock still accepts a receipt while `receipt-late` is on. The case clock, and the switch that holds the receipt, are what the test has to follow.

## What makes a journey test an AI test?

The journey asserts the mock state from a recorded fixture, not the model's sentence.

The fixture stays in the pack. [test_journey.py](work/tests/test_journey.py) loads it and passes a state. [schema.py](work/app/schema.py) ignores the reply and reads `booked`. A sentence that says the visit is booked is not the result.

You have the finished day. The trainer's session is [08 — Trainer session](08-trainer.md).

## Carry this forward

You leave Module 2, Lesson 3 with a suite that goes red when the receipt switch is on, and with `status-short` and `caregiver` finished.

This lesson is done. The next day deploys, then sequences Ain. The deployment standard arrives. You leave with a private-cloud URL and a health probe that reports the registered hash.

The trainer chapter, if this page links one, is optional. Tomorrow's lesson is the [Module 2, Lesson 4 student copy](<../../Lesson 04/Student_Copy/README.md>), starting at its background.
