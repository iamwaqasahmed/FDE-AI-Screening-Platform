# The check

From `problem_simulation`, with your work directory filled in:

```text
python -m alwaha.check incident --release rel-w4d2 --work "..\Week 04\Day 02\work"
python -m alwaha.check cache --release rel-w4d2 --work "..\Week 04\Day 02\work"
```

`chk-w4-incident` scores the trace, the board, the meter, the drifts, the override rate, the shadow comparison, the dashboard note, the timeline, the runbook, the sprint order, both interviews, and the knowledge file. A miss says the trace is missing a tool, a hash, or a token count, the dashboard only has CPU, the alert is outside the SLO, cost is missing a hospital, a drift is unnamed, the override rate is missing, shadow traffic changes the patient reply, a hash is promoted with no comparison, the timeline does not match the replay, the runbook misses a required field, sprint.md does not open the replay first, the ciso notes miss the replay or the dashboard, the patient-rep notes miss the old hours, knowledge.md does not name the three drifts, or knowledge.md does not say which event drops the cache. It does not print a timestamp, a hash, a rate, or a cost.

`slice-cache` scores the hours cache. A miss says old clinic hours are still served.

A watermarked file copied into `work/` fails the check. The message does not print the watermark.

On `practice`, the instructor can show one trace:

```text
python -m alwaha.demo.trace --profile practice
```

The lines are a tool, a hash, and a token count. They do not include the error text.

Then write `work/knowledge.md` from [templates/knowledge.md](templates/knowledge.md), with two short answers:

1. Name the three drifts.
2. What event invalidates a cached answer?

The day is done when both checks print `passed` and the knowledge file has both answers.
