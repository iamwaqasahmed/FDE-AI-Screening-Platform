# 06 — The fix

[Chapter 05](05-the-sprint.md) sequenced the fix, then the second measurement, then the spec. This chapter replaces the repair, the second run, and the label cost.

You replace three files under `work/`, in this order:

1. [repair.py](work/app/repair.py), under Replace the repair
2. [remeasure.py](work/app/remeasure.py), under Replace the second run
3. [cost.py](work/app/cost.py), under Replace the label cost

Paste only those three blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged. Do not paste a test. The tests are copied and not replaced.

Scroll down to the heading Replace the repair. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. Two more Replace headings follow it. The four steps from [chapter 05](05-the-sprint.md) are repeated above each paste. Everything above that first Replace heading is a picture. You do not paste it.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, open a terminal in the course folder and run `python "Week 03/Day 05/Student_Copy/prepare_work.py"`. Then paste chapters 05 and 06 again from the chapter source. Do not repair the spaces by hand.

Do not run a check on this page. The checks are only in [chapter 10](10-finish.md). Do not run the suite on this page. The suite is in [chapter 08](08-the-personal.md).

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the comment at the top of each one. Do not edit them.

Open [before.jsonl](packet/release/slices/before.jsonl). Search for `hours-c1`. That file has outputs and no label field. One row uses a document id that is not in force. Open [prices.csv](packet/release/finance/prices.csv). Search for `cost.label`. Read the sar from the file. Do not copy that amount onto this page. Open [labels.json](packet/release/budget/labels.json). Search for `price`. Do not copy the numbers onto this page. The three blocks below are pictures. The first paste is the heading Replace the repair, further down.

1. [repair.py](packet/app/repair.py). Search for `Leave every citation`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/repair.py](work/app/repair.py) is under the Replace heading for this file.

```text
"""Leave every citation as it was scored."""

from __future__ import annotations


def repair(row: dict) -> dict:
    return dict(row)
```

2. [remeasure.py](packet/app/remeasure.py). Search for `Report the first score again`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/remeasure.py](work/app/remeasure.py) is under the Replace heading for this file.

```text
"""Report the first score again."""

from __future__ import annotations


def remeasure(rows: list[dict]) -> dict:
    before = _accuracy(rows)
    return {"after": before, "before": before}


def _accuracy(rows: list[dict]) -> float:
    if not rows:
        return 0.0
    hits = 0
    for row in rows:
        pred, label = row["pred"], row["label"]
        if pred.get("doc_id") == label.get("doc_id") and pred.get("span") == label.get("span"):
            hits += 1
    return hits / len(rows)
```

3. [cost.py](packet/app/cost.py). Search for `Charge nothing`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/cost.py](work/app/cost.py) is under the Replace heading for this file.

```text
"""Charge nothing for the fix."""

from __future__ import annotations


def spend(count: int, price: float, budget_sar: float):
    del count, price, budget_sar
    return 0
```

You are done reading. The next heading, Replace the repair, is the first paste on this page.

## Replace the repair

This block replaces [work/app/repair.py](work/app/repair.py). The full path is `Week 03/Day 05/Student_Copy/work/app/repair.py`. It does not replace the copy in `packet/app`.

1. Open the work file named here, [work/app/repair.py](work/app/repair.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Replace a citation that is not in force.`

```text
"""Replace a citation that is not in force."""

from __future__ import annotations

# The document a patient may see. The other id is not in force.
_IN_FORCE = "circ-ramadan"
_UNAUTH = "circ-ramadan-unauth"


def repair(row: dict) -> dict:
    # Leave every other field as it was. Only the document id changes.
    if row.get("doc_id") == _UNAUTH:
        return {**row, "doc_id": _IN_FORCE}
    # An in-force citation stays. Copy it so the caller cannot change the row.
    return dict(row)
```

You should see `Replace a citation that is not in force.` You should not see `Leave every citation as it was scored.` If you still see that shell sentence, you pasted the picture. Delete the work file and paste the block under this heading again. The unauthorized id can still appear on the line that compares it. That is expected. It is the value being replaced.

## Replace the second run

This block replaces [work/app/remeasure.py](work/app/remeasure.py). The full path is `Week 03/Day 05/Student_Copy/work/app/remeasure.py`. It does not replace the copy in `packet/app`.

1. Open the work file named here, [work/app/remeasure.py](work/app/remeasure.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Score the citation slice before and after the repair.`

```text
"""Score the citation slice before and after the repair."""

from __future__ import annotations

from repair import repair


def remeasure(rows: list[dict]) -> dict:
    # The first score is the slice as it arrived.
    before = _accuracy(rows)
    # Each prediction is repaired. The label stays the grader's label.
    repaired = [{"label": row["label"], "pred": repair(dict(row["pred"]))} for row in rows]
    # After is the repaired slice. Before is the original slice.
    return {"after": _accuracy(repaired), "before": before}


def _accuracy(rows: list[dict]) -> float:
    # An empty slice has no rate.
    if not rows:
        return 0.0
    hits = 0
    for row in rows:
        pred, label = row["pred"], row["label"]
        # A hit needs the same document id and the same span.
        if pred.get("doc_id") == label.get("doc_id") and pred.get("span") == label.get("span"):
            hits += 1
    return hits / len(rows)
```

You should see `Score the citation slice before and after the repair.` You should not see `Report the first score again.` If you still see that shell sentence, you pasted the picture. Delete the work file and paste the block under this heading again. The name `before` is still in the file. That is expected. It is the first score. The function calls `repair`, then scores the slice again.

## Replace the label cost

This block replaces [work/app/cost.py](work/app/cost.py). The full path is `Week 03/Day 05/Student_Copy/work/app/cost.py`. It does not replace the copy in `packet/app`.

1. Open the work file named here, [work/app/cost.py](work/app/cost.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Price the fix in labels, and stop when the budget is spent.`

```text
"""Price the fix in labels, and stop when the budget is spent."""

from __future__ import annotations


def spend(count: int, price: float, budget_sar: float):
    # The cost is the label count times the label price.
    total = count * price
    # Past the annotation budget, the fix is not priced.
    if total > budget_sar:
        return None
    return total
```

You should see `Price the fix in labels, and stop when the budget is spent.` You should not see `Charge nothing for the fix.` If you still see that shell sentence, you pasted the picture. Delete the work file and paste the block under this heading again. The price and the budget are arguments. You do not type an amount from the price sheet into this file.

This page is done when the three work files show the new sentences, and the three shell sentences are gone. Do not run a check from this page.

Next: [07 — The spec](07-the-spec.md).
