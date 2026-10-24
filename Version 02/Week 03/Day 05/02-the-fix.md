# The fix

Copy [app](app) to `Week 03/Day 05/work/app`. Copy [tests](tests) to `Week 03/Day 05/work/tests`. Leave the copies in this folder unchanged, and edit the copies.

The same tests sit in both folders. They fail on the shell. They pass on the copy once the shell's choices are fixed.

The shipped improvement is one retrieval failure. The other three planted failures stay named and stay open.

Read [slices/before.jsonl](../../data/rel-w3d5/slices/before.jsonl). It has predictions and no labels. The grading service holds the labels. `repair` keeps an in-force citation and replaces one that is not in force. `remeasure` reports the citation accuracy before that repair and after it. The after rate is higher. A second run that copies the first score does not move the failure.

Read [finance/prices.csv](../../data/rel-w3d5/finance/prices.csv) and [budget/labels.json](../../data/rel-w3d5/budget/labels.json). `spend` is the label count times `cost.label` when that product fits the annotation budget. It returns nothing when the product does not fit. The shell returns zero. GPU hours are not the cost of this fix.

From `work`:

```text
python -m unittest discover -s tests -q
```
