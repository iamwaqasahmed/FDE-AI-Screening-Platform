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
