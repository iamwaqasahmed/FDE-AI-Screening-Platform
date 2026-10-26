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
