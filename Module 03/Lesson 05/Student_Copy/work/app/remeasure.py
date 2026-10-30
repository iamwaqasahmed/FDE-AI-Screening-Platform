"""Report the first score again.

The rows are scored once. That score is stored under before and
again under after. A hit is the same document id and the same span.
An empty slice scores as zero.
"""

from __future__ import annotations


def remeasure(rows: list[dict]) -> dict:
    """Return the same score under before and under after.

    rows carry a label and a pred. Both names on the result are the
    score of these rows.
    """
    # Score the slice once.
    before = _accuracy(rows)
    # The after name repeats that same score.
    return {"after": before, "before": before}


def _accuracy(rows: list[dict]) -> float:
    """Return the share of rows whose prediction matches the label.

    A match needs the same document id and the same span. An empty
    slice returns zero.
    """
    # An empty slice has no rate.
    if not rows:
        return 0.0
    hits = 0
    for row in rows:
        # pred is the citation being scored. label is the grader's citation.
        pred, label = row["pred"], row["label"]
        # A hit needs the same document id and the same span.
        if pred.get("doc_id") == label.get("doc_id") and pred.get("span") == label.get("span"):
            hits += 1
    return hits / len(rows)
