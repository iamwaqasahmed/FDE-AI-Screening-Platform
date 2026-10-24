# The check

From `problem_simulation`, with your work directory filled in:

```text
python -m alwaha.check approach --work "..\Week 01\Day 02\work"
python -m alwaha.check brief --work "..\Week 01\Day 02\work"
```

`chk-w1-approach` passes when [approach.md](templates/approach.md) has one row for every problem id, the family is one the day accepts, the sample measurements match the baselines you printed, and each row cites a release file or a persona. A failed row says that the family does not fit. It does not name the family that would.

`chk-w1-brief` passes when [brief.md](templates/brief.md) marks leader figures as claims, sizes every problem, and ranks all nine. A banned sentence fails the brief when it sits outside a claim row. Ranking `p-triage` first fails unless that line says who assigns urgency.

A watermarked letter copied into `work/` fails both checks. The message does not print the watermark. Remove the file.

Then write `work/knowledge.md` with two short answers:

1. Name a problem where retrieval fits better than fine-tuning.
2. Name one where a model is the wrong tool.

The day is done when both checks print `passed` and the knowledge file has both answers.
