# The check

From `problem_simulation`, with your work directory filled in:

```text
python -m alwaha.check tests --release rel-w2d3 --work "..\Week 02\Day 03\work"
python -m alwaha.check ux --release rel-w2d3 --work "..\Week 02\Day 03\work"
```

`chk-w2-tests` scores the calendar, the reply schema, the receipt clock, and the journey. A miss says the calendar does not match, the receipt test sleeps, the suite accepted the receipt fault, or the journey followed the sentence. It does not name an interval or a delay.

`chk-w2-ux` scores the scripts, the clauses, the definition of done, the zone crossings, the fixture note, and the sprint. A miss says a script is unfinished, a clause is missing, the fault is not in the definition of done, or a zone-crossing case is missing.

A watermarked fixture copied into `work/` fails the check. The message does not print the watermark.

Then write `work/knowledge.md` with two short answers:

1. Why is a fixed sleep a bad receipt test?
2. What makes a journey test an AI test?

The day is done when both checks print `passed` and the knowledge file has both answers.
