# The check

From `problem_simulation`, with your work directory filled in:

```text
python -m alwaha.check agent --release rel-w1d5 --work "..\Week 01\Day 05\work"
python -m alwaha.check trajectory --release rel-w1d5 --work "..\Week 01\Day 05\work"
python -m alwaha.check design --work "..\Week 01\Day 05\work"
python -m alwaha.check readout --work "..\Week 01\Day 05\work"
python -m alwaha.check individual --work "..\Week 01\Day 05\work"
```

`chk-w1-agent` and `chk-w1-trajectory` score the Day 4 scenarios and the two new ones. A miss names the scenario. It does not print the count, the slot, or an interview sentence.

`chk-w1-design` scores [architecture.md](templates/architecture.md) and [design.md](templates/design.md). `chk-readout` scores [readout.md](templates/readout.md). `chk-individual-w1` scores [trace-note.md](templates/trace-note.md) for the emergency scenario: the tool, the document, and whether the reply was refused. That note is yours. It is not the team diagram.

A watermarked scenario file copied into `work/` fails the check. The message does not print the watermark.

Then write `work/knowledge.md` with two short answers:

1. Name one failure the scenario set exposed.
2. Which stage gate is still open?

After the readout, take five minutes for a retrospective: what to keep, what to drop, and what is still open. The lead writes the open asks in the readout.

The day is done when the five checks print `passed` and the knowledge file has both answers.
