# The check

From `problem_simulation`, with your work directory filled in:

```text
python -m alwaha.check auth --release rel-w2d1 --work "..\Week 02\Day 01\work"
python -m alwaha.check journey --release rel-w2d1 --work "..\Week 02\Day 01\work"
```

`chk-w2-auth` scores the patient, the coordinator, the session row, a staff role from the identity note, and a token that must be refused. A miss does not print the role list or the assurance level.

`chk-w2-journey` scores one signed-in status question. The trace has the status tool and no book call. A miss says the `his-wadi` read failed. It does not name a field or a count.

A watermarked scenario file copied into `work/` fails the check. The message does not print the watermark.

Then write `work/knowledge.md` with two short answers:

1. Which assurance level may book?
2. Where does the session row live?

The day is done when both checks print `passed` and the knowledge file has both answers.
