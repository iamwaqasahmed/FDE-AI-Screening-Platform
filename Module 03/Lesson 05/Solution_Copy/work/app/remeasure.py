"""Score the citation slice before and after the repair.

The before score is the slice as it arrived. Each prediction is
then repaired, the label stays the grader's label, and the after
score is that repaired slice. A hit is the same document id and
the same span. An empty slice scores as zero.
"""

from __future__ import annotations

# The citation fix applied to a prediction before the second score.
from repair import repair


def remeasure(rows: list[dict]) -> dict:
    """Return the score before the repair and the score after it.

    rows carry a label and a pred. before scores the rows as they
    arrived. after scores a copy whose prediction has been repaired.
    """
    # The first score is the slice as it arrived.
    before = _accuracy(rows)
    # Each prediction is repaired. The label stays the grader's label.
    repaired = [{"label": row["label"], "pred": repair(dict(row["pred"]))} for row in rows]
    # After is the repaired slice. Before is the original slice.
    return {"after": _accuracy(repaired), "before": before}


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
        pred, label = row["pred"], row["label"]
        # A hit needs the same document id and the same span.
        if pred.get("doc_id") == label.get("doc_id") and pred.get("span") == label.get("span"):
            hits += 1
    # The rate is the hit count divided by how many rows were scored.
    return hits / len(rows)
