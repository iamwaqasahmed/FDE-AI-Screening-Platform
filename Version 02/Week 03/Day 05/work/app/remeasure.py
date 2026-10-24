"""Score the citation slice before and after the repair."""

from __future__ import annotations

from repair import repair


def remeasure(rows: list[dict]) -> dict:
    before = _accuracy(rows)
    repaired = [{"label": row["label"], "pred": repair(dict(row["pred"]))} for row in rows]
    return {"after": _accuracy(repaired), "before": before}


def _accuracy(rows: list[dict]) -> float:
    if not rows:
        return 0.0
    hits = 0
    for row in rows:
        pred, label = row["pred"], row["label"]
        if pred.get("doc_id") == label.get("doc_id") and pred.get("span") == label.get("span"):
            hits += 1
    return hits / len(rows)
