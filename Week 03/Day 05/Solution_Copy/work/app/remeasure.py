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
