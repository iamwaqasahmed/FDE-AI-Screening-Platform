# The harness

Copy [app](app) to `Week 03/Day 04/work/app`. Copy [tests](tests) to `Week 03/Day 04/work/tests`. Leave the copies in this folder unchanged, and edit the copies.

The same tests sit in both folders. They fail on the shell. They pass on the copy once the shell's choices are fixed.

The shell score reports a perfect extraction, citation, and journey. The shell forecast copies last year's month into the later window.

Read [slices/score.jsonl](../../data/rel-w3d4/slices/score.jsonl). It has outputs and no labels. The grading service holds the labels. Score extraction F1, citation accuracy, and journey pass rate against [budget/metrics.json](../../data/rel-w3d4/budget/metrics.json). Extraction keeps the floor of 0.8 from the Day 2 price cap.

Read [demand/ophth.csv](../../data/rel-w3d4/demand/ophth.csv). `predict` returns the two months after the announcement, with the campaign included. Returning last year's months scores the fit window. Copying those months forward ignores the campaign.

From `work`:

```text
python -m unittest discover -s tests -q
```
