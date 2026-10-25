"""Field F1, citation accuracy, and journey pass rate."""

from __future__ import annotations

# The three extraction fields. A match is counted per field, not per row.
_FIELDS = ("source_type", "specialty", "sub_specialty")


def extraction_f1(rows: list[dict]) -> float:
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
    # An empty slice has no rate.
    if not rows:
        return 0.0
    hits = sum(1 for row in rows if same(row["pred"], row["label"]))
    return hits / len(rows)


def citation_accuracy(rows: list[dict]) -> float:
    # Both the document id and the span have to match.
    return _rate(
        rows,
        lambda pred, label: pred.get("doc_id") == label.get("doc_id") and pred.get("span") == label.get("span"),
    )


def journey_pass(rows: list[dict]) -> float:
    # Both the state and the approval have to match.
    return _rate(
        rows,
        lambda pred, label: pred.get("state") == label.get("state") and pred.get("approved") == label.get("approved"),
    )
