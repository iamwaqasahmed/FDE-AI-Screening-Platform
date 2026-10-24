# The check

From `problem_simulation`, with your work directory filled in:

```text
python -m alwaha.check agent --work "..\Week 01\Day 04\work"
python -m alwaha.check trajectory --work "..\Week 01\Day 04\work"
```

`chk-w1-agent` passes when the mock ends in the state the approval policy describes. `chk-w1-trajectory` passes when the trace uses the allowed tools, holds the approval, redirects on the routing list, and cites the tool and the document. A failed scenario names the case. It does not print the count, the slot, or the clause.

A watermarked scenario file copied into `work/` fails the check. The message does not print the watermark.

Then write `work/knowledge.md` with two short answers:

1. When is a second agent worth its tokens?
2. What must be true before a slot is booked?

The day is done when both checks print `passed` and the knowledge file has both answers.
