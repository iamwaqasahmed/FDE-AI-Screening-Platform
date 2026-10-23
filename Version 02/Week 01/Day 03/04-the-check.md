# The check

From `problem_simulation`, with your work directory filled in:

```text
python -m alwaha.check events --work "..\Week 01\Day 03\work"
```

`chk-w1-events` passes when the scenario log follows the policy: the calendar, one approval for a repeated event, the criteria status the policy names, no booking, a released hold when the next step fails, and a dead letter that is not applied. A failed scenario names the case. It does not print the due date or the clause.

A watermarked event file copied into `work/` fails the check. The message does not print the watermark.

Then write `work/knowledge.md` with two short answers:

1. Which clock starts an SLA?
2. What should a second delivery of the same event do?

The day is done when the check prints `passed` and the knowledge file has both answers.
