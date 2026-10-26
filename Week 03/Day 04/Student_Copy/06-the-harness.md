# 06 — The harness

[Chapter 05](05-the-sprint.md) sequenced the score, then the failures, then the workshop. This chapter replaces the score, the forecast, and the failure names.

You replace three files under `work/`, in this order:

1. [score.py](work/app/score.py), under Replace the score
2. [forecast.py](work/app/forecast.py), under Replace the forecast
3. [failures.py](work/app/failures.py), under Replace the failure names

Paste only those three blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged. Do not paste a test. The tests are copied and not replaced.

Scroll down to the heading Replace the score. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. Two more Replace headings follow it. The four steps from [chapter 05](05-the-sprint.md) are repeated above each paste. Everything above that first Replace heading is a picture. You do not paste it.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, run `prepare_work.py` from the course folder and paste chapters 05 and 06 again from the chapter source. Do not repair the spaces by hand.

Do not run a check on this page. The checks are only in [chapter 10](10-finish.md).

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the comment at the top of each one. Do not edit them.

Open [metrics.json](packet/release/budget/metrics.json). Search for `extraction`. Open [score.jsonl](packet/release/slices/score.jsonl). Search for `photo`. That file has outputs and no label field. Open [campaign.md](packet/release/notices/campaign.md). Search for `Read the counts`. Open [ophth.csv](packet/release/demand/ophth.csv). Search for `,2027,2,`, then `,2027,3,`. You already read those visits in chapter 03. Read them again if you do not remember the lines. Do not copy a visit count onto this page. Open [failures.jsonl](packet/release/slices/failures.jsonl). Search for `log-night`. The type is not on the row. The three blocks below are pictures. The first paste is the heading Replace the score, further down.

1. [score.py](packet/app/score.py). Search for `perfect score`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/score.py](work/app/score.py) is under the Replace heading for this file.

```text
"""Report a perfect score for every slice.

extraction_f1, citation_accuracy, and journey_pass each discard
the rows and return a perfect score.
"""

from __future__ import annotations


def extraction_f1(rows: list[dict]) -> float:
    """Return a perfect extraction score.

    rows is discarded.
    """
    # The slice does not change this score.
    del rows
    return 1.0


def citation_accuracy(rows: list[dict]) -> float:
    """Return a perfect citation score.

    rows is discarded.
    """
    # The slice does not change this score.
    del rows
    return 1.0


def journey_pass(rows: list[dict]) -> float:
    """Return a perfect journey score.

    rows is discarded.
    """
    # The slice does not change this score.
    del rows
    return 1.0
```

2. [forecast.py](packet/app/forecast.py). Search for `Copy last year's month`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/forecast.py](work/app/forecast.py) is under the Replace heading for this file.

```text
"""Copy last year's month into the later window.

Months in the window are read from the prior year. Each district and
month keeps the prior year's visits, and the result is labeled with
the later year. The rows come back in district order, then month.
"""

from __future__ import annotations

# Months in the window, the year the visits are copied from, and the year written on the result.
_MONTHS = {2, 3}
_PRIOR = 2026
_LATER = 2027


def predict(rows: list[dict]) -> list[dict]:
    """Build later-year rows from the prior year's visits in the window.

    rows are visit records. A prior-year row is stored when its month
    is in the window. The result uses that visit count, the same
    district and month, and the later year.
    """
    # Visits from the prior year, keyed by district and month.
    prior = {}
    for row in rows:
        year = int(row["year"])
        month = int(row["month"])
        # Store the prior year only, and only months in the window.
        if year == _PRIOR and month in _MONTHS:
            prior[(row["district"], month)] = int(row["visits"])
    chosen = []
    # District, then month, so the result order is stable.
    for (district, month), visits in sorted(prior.items()):
        # The later year is written on the result. The visits stay the prior count.
        chosen.append({"district": district, "month": month, "visits": visits, "year": _LATER})
    return chosen
```

3. [failures.py](packet/app/failures.py). Search for `Name every log row a pass`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/failures.py](work/app/failures.py) is under the Replace heading for this file.

```text
"""Name every log row a pass.

classify discards the row and returns the same name on every call.
"""

from __future__ import annotations


def classify(row: dict) -> str:
    """Return a pass for the row.

    row is discarded. The name does not change from call to call.
    """
    # The row is unused. Every call gets the same name.
    del row
    return "pass"
```

The pictures end here. The next heading is the first paste.

## Replace the score

This block replaces [work/app/score.py](work/app/score.py). The full path is `Week 03/Day 04/Student_Copy/work/app/score.py`. It does not replace the packet copy. A long block is still one file. This one is `score.py`.

1. Open the work file named under this heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

```text
"""Field F1, citation accuracy, and journey pass rate.

Each extraction field is scored on its own. Citation accuracy and the journey rate count a row only when every field they compare matches. An empty slice has no rate.
"""

from __future__ import annotations

# The three extraction fields. A match is counted per field, not per row.
_FIELDS = ("source_type", "specialty", "sub_specialty")


def extraction_f1(rows: list[dict]) -> float:
    """Return the share of extraction fields that match.

    Each field is its own trial, so one mismatch lowers the score even when the other fields match. When no field matches, the score is zero.
    """
    # A matching field is a true positive. A mismatch counts against it.
    true_positive = false = 0
    for row in rows:
        for field in _FIELDS:
            if row["pred"].get(field) == row["label"].get(field):
                true_positive += 1
            else:
                false += 1
    # No true positive is a zero.
    if true_positive == 0:
        return 0.0
    return true_positive / (true_positive + false)


def _rate(rows: list[dict], same) -> float:
    """Return the share of rows that same accepts.

    same decides whether the prediction matches the label. An empty slice returns zero, because there is no rate to report.
    """
    # An empty slice has no rate.
    if not rows:
        return 0.0
    hits = sum(1 for row in rows if same(row["pred"], row["label"]))
    return hits / len(rows)


def citation_accuracy(rows: list[dict]) -> float:
    """Return the share of rows whose document and span both match.

    A row that matches only one of those fields is a miss. The shared rate helper turns an empty slice into zero.
    """
    # Both the document id and the span have to match.
    return _rate(
        rows,
        lambda pred, label: pred.get("doc_id") == label.get("doc_id") and pred.get("span") == label.get("span"),
    )


def journey_pass(rows: list[dict]) -> float:
    """Return the share of rows whose state and approval both match.

    A row that matches only one of those fields is a miss. The shared rate helper turns an empty slice into zero.
    """
    # Both the state and the approval have to match.
    return _rate(
        rows,
        lambda pred, label: pred.get("state") == label.get("state") and pred.get("approved") == label.get("approved"),
    )
```

Open [work/app/score.py](work/app/score.py). Search inside that file, not inside this chapter. You should see `Field F1, citation accuracy, and journey pass rate.`. `extraction_f1`, `citation_accuracy`, and `journey_pass` are still the function names. That is expected. You should not see `Report a perfect score for every slice`. If you see that text, you pasted the picture.

## Replace the forecast

This block replaces [work/app/forecast.py](work/app/forecast.py). The full path is `Week 03/Day 04/Student_Copy/work/app/forecast.py`. It does not replace the packet copy. A long block is still one file. This one is `forecast.py`.

1. Open the work file named under this heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

```text
"""Return the later window, which includes the campaign.

A row is kept when its year is the later year and its month is in
the window. District, month, visits, and year on the result come
from that same row. A row from another year is left out, and a
month outside the window is left out.
"""

from __future__ import annotations

# The later year, and the two months that follow the announcement.
_LATER = 2027
_MONTHS = {2, 3}


def predict(rows: list[dict]) -> list[dict]:
    """Keep later-year rows in the month window, with their own visits.

    rows are visit records with district, month, visits, and year.
    Year, month, and visits are read as integers. A kept row copies
    the visits written on that row.
    """
    # Keep a row only when its own year is the later year and its month is in the window.
    # The visits stay the visits written on that row.
    chosen = []
    for row in rows:
        # Year and month are compared as integers.
        year = int(row["year"])
        month = int(row["month"])
        if year == _LATER and month in _MONTHS:
            # Visits are copied from this row and stored as an integer.
            chosen.append({"district": row["district"], "month": month, "visits": int(row["visits"]), "year": year})
    return chosen
```

Open [work/app/forecast.py](work/app/forecast.py). Search inside that file, not inside this chapter. You should see `Return the later window, which includes the campaign.`. `_LATER` and `_MONTHS` are still in the file. That is expected. You should not see `_PRIOR`. You should not see `Copy last year's month`. If you see that text, you pasted the picture.

## Replace the failure names

This block replaces [work/app/failures.py](work/app/failures.py). The full path is `Week 03/Day 04/Student_Copy/work/app/failures.py`. It does not replace the packet copy. A long block is still one file. This one is `failures.py`.

1. Open the work file named under this heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

```text
"""Name each planted failure from the log text.

The name is read from the reply text. A row that is not a planted case returns pass.
"""

from __future__ import annotations


def classify(row: dict) -> str:
    """Return the planted failure name for this row.

    The type is not a field on the row. It is read from the reply text. A document that is not in force is retrieval. An offer that uses Friday is reasoning. A booking that has no approval is workflow. A clause that is not on file is hallucination. Anything else returns pass.
    """
    # The type is not a field on the row. It is read from the reply text.
    text = str(row.get("output", "")).lower()
    # A document that is not in force.
    if "unauthorized" in text:
        return "retrieval"
    # An offer that uses Friday.
    if "friday" in text:
        return "reasoning"
    # A booking that has no approval.
    if "approval" in text and "none" in text:
        return "workflow"
    # A clause that is not on file.
    if "not on file" in text:
        return "hallucination"
    # Anything else is not one of the four planted rows.
    return "pass"
```

Open [work/app/failures.py](work/app/failures.py). Search inside that file, not inside this chapter. You should see `Name each planted failure from the log text.`. `return "pass"` is still the last line. That is expected. It is the row that is not one of the four. You should not see `Name every log row a pass`. If you see that text, you pasted the picture.

This page is done when the three work files show the sentences above, and you do not see the shell sentences. Do not run a check from this page.

Next: [07 — The gate](07-the-gate.md).
