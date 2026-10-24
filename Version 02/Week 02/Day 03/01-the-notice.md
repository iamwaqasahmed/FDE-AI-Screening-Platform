# The notice

The morning is a stand-up. You have the Week 1 packs, the Day 1 and Day 2 shells, and nothing from later this week.

Open the release readme, [data/rel-w2d3/README.md](../../data/rel-w2d3/README.md). Then read:

1. [notices/timing.md](../../data/rel-w2d3/notices/timing.md)
2. [clock/guide.md](../../data/rel-w2d3/clock/guide.md)
3. [clock/receipt.json](../../data/rel-w2d3/clock/receipt.json)
4. [openapi/clock.yaml](../../data/rel-w2d3/openapi/clock.yaml)
5. [openapi/sms.yaml](../../data/rel-w2d3/openapi/sms.yaml)
6. [standards/access.md](../../data/rel-w2d3/standards/access.md)

The SMS receipt follows the case clock. The interval is in the clock file. Read it from there. A test that sleeps still accepts `receipt-late`.

The Day 1 and Day 2 notes still stand. A new conversation uses the same shape and can live in `Week 02/Day 03/work/interviews`.

From `problem_simulation`:

```text
python -m alwaha.interview --persona patient-rep --script "..\Week 02\Day 03\work\interviews\patient-rep.questions.txt"
```

Ask about the phone line first, then the daytime slots his mother misses in Ramadan, then who books for her. Write what you hear.

The lead copies [templates/sprint.md](templates/sprint.md) to `work/sprint.md` and sequences the suite before usability sign-off.
