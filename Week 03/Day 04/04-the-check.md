# The check

From `problem_simulation`, with your work directory filled in:

```text
python -m alwaha.check eval --release rel-w3d4 --work "..\Week 03\Day 04\work"
python -m alwaha.check judge --release rel-w3d4 --work "..\Week 03\Day 04\work"
```

`chk-w3-eval` scores the draft. It checks extraction F1, citation accuracy, and journey pass rate on the held-out rows, the forecast on the later window, and the four failure names. It also reads the sprint, the benchmark, the workshop notes, the knowledge file, and the evaluation gate. A miss says the extraction score misses the held-out slice, the citation score misses the held-out slice, the journey score misses the held-out slice, the forecast ignores the campaign, the forecast scores the fit window, the forecast misses the later window, a planted failure is misnamed, or the report misses a planted failure. It does not print a log id, a visit count, or an F1. This draft does not require a second measured run.

`slice-judge` passes when the judge agrees with the calibration subset. An uncalibrated judge fails it. The miss says the judge is not checked on the calibration set. It does not print the item.

A watermarked file copied into `work/` fails the check. The message does not print the watermark.

On `practice`, the instructor can show the fluent wrong citation:

```text
python -m alwaha.demo.judge --profile practice
```

The lines are that the judge marked the citation correct, and that the citation is not the in-force document. They do not include the item text.

Then write `work/knowledge.md` from [templates/knowledge.md](templates/knowledge.md), with two short answers:

1. What is a retrieval failure in this case?
2. Why calibrate a judge?

The day is done when both checks print `passed` and the knowledge file has both answers.
