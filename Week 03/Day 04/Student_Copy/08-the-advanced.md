# 08 — The advanced path

[Chapter 07](07-the-gate.md) marked with the calibration label and uncommented the evaluation gate. This chapter replaces the intervals and the experiment report. Then you run the suite.

You replace two files under `work/`, in this order:

1. [intervals.py](work/app/intervals.py), under Replace the intervals
2. [experiment.py](work/app/experiment.py), under Replace the experiment

Paste only those two blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged. Do not paste a test. The tests are copied and not replaced.

Scroll down to the heading Replace the intervals. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. One more Replace heading follows it. The four steps from [chapter 05](05-the-sprint.md) are repeated above each paste. Everything above that first Replace heading is a picture. You do not paste it.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, run `prepare_work.py` from the course folder and paste chapters 05 through 08 again from the chapter source. Do not repair the spaces by hand.

The two checks do not require these two files. You still replace them. You do not delete them. The suite imports them. A deleted file fails the suite. You do not delete `gate.py`. The suite imports that file too.

Do not run a check on this page. The checks are only in [chapter 10](10-finish.md).

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the comment at the top of each one. Do not edit them.

Open [ab-status.md](packet/release/notices/ab-status.md). Search for `not stated`. The effect is not stated. Open [ab-status.json](packet/release/experiment/ab-status.json). Search for `honest_pending`. You do not write which arm won.

1. [intervals.py](packet/app/intervals.py). Search for `point at one`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/intervals.py](work/app/intervals.py) is under the Replace heading for this file.

```text
"""Treat every district as a point at one.

bounds ignores the success count and the slice size and returns a
point whose ends are both one. by_district maps every district on
the rows to that same point.
"""

from __future__ import annotations


def bounds(successes: int, total: int) -> tuple[float, float]:
    """Return a point at one.

    successes and total are ignored. Both ends are one.
    """
    # The arguments do not change the point.
    del successes, total
    return (1.0, 1.0)


def by_district(rows: list[dict]) -> dict[str, tuple[float, float]]:
    """Map each district named on the rows to a point at one.

    rows supply the district names. A repeated district stays that
    same point.
    """
    return {row["district"]: (1.0, 1.0) for row in rows}
```

2. [experiment.py](packet/app/experiment.py). Search for `contained count`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/experiment.py](work/app/experiment.py) is under the Replace heading for this file.

```text
"""Report the contained count instead of the pre-registered metric.

Every arm is scored on the contained count divided by n. The report
names that contained field as the metric, and names the arm with the
highest contained rate. When rates tie, the earliest arm in the
counts is the winner.
"""

from __future__ import annotations

# The count this report divides by n.
_PEEK = "contained"


def report(protocol: dict) -> dict:
    """Return the contained field as the metric, and the winning arm.

    protocol has a counts map. Each arm has a contained count and an
    n. The rate is that contained count divided by n. The winner is
    the arm whose rate is highest.
    """
    # Score every arm on the contained count.
    rates = {arm: row[_PEEK] / row["n"] for arm, row in protocol["counts"].items()}
    # The higher contained rate is the arm this report returns.
    winner = max(rates, key=rates.get)
    return {"metric": _PEEK, "winner": winner}
```

The pictures end here. The next heading is the first paste.

## Replace the intervals

This block replaces [work/app/intervals.py](work/app/intervals.py). The full path is `Week 03/Day 04/Student_Copy/work/app/intervals.py`. It does not replace the packet copy. A long block is still one file. This one is `intervals.py`.

1. Open the work file named under this heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

```text
"""Wilson intervals for a district slice.

bounds builds an interval around the success rate. An empty slice
covers the whole range. by_district groups the rows, counts the
correct ones, and returns an interval for each district.
"""

from __future__ import annotations


def bounds(successes: int, total: int) -> tuple[float, float]:
    """Return the low and high ends of a Wilson interval.

    successes is how many rows are correct. total is the size of
    the slice. An empty slice returns the full range. Otherwise the
    center and the margin use the z below, and both ends stay inside
    the full range.
    """
    # An empty slice covers the whole range.
    if total <= 0:
        return (0.0, 1.0)
    # 1.96 is the z for this interval.
    z = 1.96
    # The observed success rate.
    rate = successes / total
    # Shared denominator for the center and the margin.
    denom = 1 + z * z / total
    # Center of the interval, shifted by the z term.
    center = (rate + z * z / (2 * total)) / denom
    # Width around the center. The power is the square-root term.
    margin = z * ((rate * (1 - rate) / total + z * z / (4 * total * total)) ** 0.5) / denom
    # Keep both ends inside 0 and 1.
    return (max(0.0, center - margin), min(1.0, center + margin))


def by_district(rows: list[dict]) -> dict[str, tuple[float, float]]:
    """Return a Wilson interval for each district in the rows.

    rows carry a district and a correct flag. Rows for the same
    district are counted together. The interval uses the correct
    count and how many rows that district has.
    """
    # Group the rows by district, then count the correct ones.
    grouped: dict[str, list[dict]] = {}
    for row in rows:
        grouped.setdefault(row["district"], []).append(row)
    found = {}
    for district, items in grouped.items():
        # Each correct row adds to the success count.
        hits = sum(1 for item in items if item["correct"])
        found[district] = bounds(hits, len(items))
    return found
```

Open [work/app/intervals.py](work/app/intervals.py). Search inside that file, not inside this chapter. You should see `Wilson intervals for a district slice.`. `by_district` is still the function name. That is expected. You should not see `Treat every district as a point at one`. If you see that text, you pasted the picture.

## Replace the experiment

This block replaces [work/app/experiment.py](work/app/experiment.py). The full path is `Week 03/Day 04/Student_Copy/work/app/experiment.py`. It does not replace the packet copy. A long block is still one file. This one is `experiment.py`.

1. Open the work file named under this heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

```text
"""Report the pre-registered metric and its winning arm.

The protocol names the metric. Each arm is scored by dividing that
metric's count by n. The report names the metric and the arm whose
rate is highest. When rates tie, the earliest arm in the counts is
the winner.
"""

from __future__ import annotations


def report(protocol: dict) -> dict:
    """Return the protocol metric and the arm with the highest rate.

    protocol has a metric name and a counts map. Each arm in counts
    has a value for that metric and an n. The rate is the metric
    count divided by n.
    """
    # The metric name comes from the protocol. Another field is not substituted.
    metric = protocol["metric"]
    # The rate is that metric divided by n, once per arm.
    rates = {arm: row[metric] / row["n"] for arm, row in protocol["counts"].items()}
    # The higher rate on that metric is the arm this report returns.
    winner = max(rates, key=rates.get)
    return {"metric": metric, "winner": winner}
```

Open [work/app/experiment.py](work/app/experiment.py). Search inside that file, not inside this chapter. You should see `Report the pre-registered metric and its winning arm.`. You do not write which arm won. You should not see `_PEEK`. You should not see `Report the contained count`. If you see that text, you pasted the picture.

## Search before the suite

These strings exist in the replaced work files. A pasted picture fails the search. Open the work file named in the row. A match in this chapter does not count. A match in `packet/` does not count.

| Work file | Search for this | You should find it |
| --- | --- | --- |
| [score.py](work/app/score.py) | `Field F1, citation accuracy, and journey pass rate.` | Yes. `extraction_f1` is still the function name. That is expected. You should not see `Report a perfect score for every slice` |
| [forecast.py](work/app/forecast.py) | `Return the later window, which includes the campaign.` | Yes. `_LATER` is still in the file. That is expected. You should not see `_PRIOR` |
| [failures.py](work/app/failures.py) | `Name each planted failure from the log text.` | Yes. `return "pass"` is still the last line. That is expected. You should not see `Name every log row a pass` |
| [judge.py](work/app/judge.py) | `Mark a citation with the calibration label.` | Yes. You should not see `when it is fluent` |
| [gate.py](work/app/gate.py) | `Reject a fluent citation that the calibration label marks wrong.` | Yes. You should not see `Accept a citation when it is fluent` |
| [ci.yml](work/.github/workflows/ci.yml) | `name: regression` | Yes. The `test` job is still there. That is expected. You should not see `# evaluation-gate:` |
| [intervals.py](work/app/intervals.py) | `Wilson intervals for a district slice.` | Yes. You should not see `point at one` |
| [experiment.py](work/app/experiment.py) | `Report the pre-registered metric and its winning arm.` | Yes. You should not see `_PEEK` |

If a row fails, you pasted a picture or you skipped that file. The score, forecast, and failure rows are the blocks in [chapter 06](06-the-harness.md). The judge, regression, and workflow rows are the blocks in [chapter 07](07-the-gate.md). The interval and experiment rows are the blocks above. Paste the failed row's block again from that chapter. Search the work file, not the packet file.

## Run the suite

Leave the window you used for the demo. That window is inside `problem_simulation`, and this command is not. Open a new terminal in the course folder, the same way as chapter 01. `dir` should list `problem_simulation` and `Week 03`. If chapter 01 told you to use `py`, use `py` here.

```text
cd "Week 03/Day 04/Student_Copy/work"
python -m unittest discover -s tests -q
```

If the `cd` line says the path cannot be found, this window is not the course folder. Open a new one and run both lines again. Do not chain `cd ..` to climb out of another folder.

If you run this command before the app files are replaced, it fails. That failure is the shell. The tests are already the shared tests. The app is still the shell. Finish the Replace headings on chapters 06, 07, and 08, then run it again.

You should see a line that starts with `Ran 11 tests`, then a blank line, then `OK`. A line of dashes can sit above the `Ran` line. The time on the `Ran` line can differ. There is no `FAIL` and no `ERROR`. The prompt returns after `OK`.

`Ran 11 tests` also appears when the suite fails. Read the line under it. That line has to be `OK`. If the line is `FAILED`, the shell is still in place. One test can pass while the others fail. That is still the shell. Do not stop at the `Ran` line. Do not go to chapter 09 while that line is `FAILED`. Stay here and use the search table.

A `FAIL` block names a file under `tests\`, such as `test_score.py`. The app file to replace is the same name without `test_`. `test_score.py` means [score.py](work/app/score.py). `test_forecast.py` means [forecast.py](work/app/forecast.py). The same pattern holds for failures, judge, intervals, experiment, and gate. Do not edit the test. The tests are shared. Use the search table, then paste that app file again from the chapter that owns it.

If the terminal says `SyntaxError` or `IndentationError`, run this from the course folder:

```text
python "Week 03/Day 04/Student_Copy/prepare_work.py"
```

A second run erases the pasted files and puts the commented gate back. Paste chapters 05 through 08 again from the chapter source. Do not repair the spaces by hand. Then run the suite again. Do not run `prepare_work.py` on this page unless the terminal shows `SyntaxError` or `IndentationError`.

A green suite can still fail chapter 10. The suite does not read the four pages. The suite does not read the workflow. The eval check does.

This page is done when the suite prints `Ran 11 tests` and `OK`, and the eight searches above pass in the work files.

Next: [09 — The pages](09-the-pages.md).
