# 07 — Knowledge

Open [knowledge.md](work/knowledge.md) and put it beside the two answers you wrote. The check wants two numbered lines. A second sentence on the next line, without a number, does not count.

## What a retrieval failure is

The first finished sentence says a retrieval failure is a citation that is not the in-force document the asker may see.

[failures.jsonl](sources/release/slices/failures.jsonl) shows the reply that uses a document that is not in force. The type name is not on that row. Week 3 Day 3 left an index that cites an in-force document the asker is allowed to see. The unauthorized circular is not a citation.

If the line is missing those facts, the eval check says knowledge.md does not say what a retrieval failure is.

## Why a judge is calibrated

The second finished sentence says calibrate a judge because a fluent wrong citation can be marked correct.

[calibration.jsonl](sources/release/slices/calibration.jsonl) is the subset. A fluent row can have a pass field of false. The demo prints that the judge marked the citation correct, and that the citation is not the in-force document. It does not print the calibration item, the span, or the doc id.

If the line is missing those facts, the eval check says knowledge.md does not say why a judge is calibrated.

The two checks print `passed` when this file and the rest of the folder match the day. `slice-judge` does not read this file. A miss here fails only the eval check.

[08 — Trainer session](08-trainer.md) is for the trainer. Students can skip it.

## Carry this forward

You leave Week 3 Day 4 with a draft benchmark that names the four planted failures with evidence, and with workshop notes. The second measured run waited.

Tomorrow you ship one fix, remeasure it, and write requirements a later team could start from.

The trainer chapter, if this page links one, is optional. Tomorrow's lesson is the [Week 3, Day 5 student copy](../../Day%2005/Student_Copy/README.md), starting at its background.
