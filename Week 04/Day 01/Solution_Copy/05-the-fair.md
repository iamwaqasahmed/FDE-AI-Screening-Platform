# 05 — The fair measure

The shell reports a gap of zero and a stamp rate of zero. That shell makes the fair check say `the disparity table hides a district or an insurance class` and `the rubber-stamp rate is missing`.

[fair.py](work/app/fair.py) takes the spread of yes decisions by district and by insurance class, and returns the larger spread. The stamp rate is the share of stamped rows. The rows are in [outcomes.jsonl](sources/release/fairness/outcomes.jsonl) and [approvals.jsonl](sources/release/fairness/approvals.jsonl). The bound is the one field in [bound.json](sources/release/fairness/bound.json). The check does not print a rate or the bound.

A gap above that bound makes the fair check say `the disparity is outside the published bound`. The filled file does not return a fixed gap. The fixture in [test_fair.py](work/tests/test_fair.py) is a small pair of rows. It is not the pack.

The suite, from this folder, prints a line that starts with `Ran 19 tests`, then `OK`. The shell suite, beside the shell app and the shell tests, prints `Ran 16 tests` and `OK`. That shell pass is not the finished day. The suite imports all eight app modules. It does not read the pages, and it does not read the workflow.

A `fair.py` miss fails only the fair check.

## The path through the files

The morning chapter [08-the-fair.md](../Student_Copy/08-the-fair.md) has the section How the replacement works. That section is the path through the files this page compares. Read it beside the finished file. The notes above are the decisions the check names.

Next: [06 — The pages](06-the-pages.md).
