"""Reference scoring for rel-m03-l04.
Participant copies do not import this module.

The score functions return the share of pairs that match. classify names the failure in a log line from the cue that appears. predict returns the campaign window, and ignore returns the copy that pretends the campaign did not happen. bounds is the interval around a success count. report names the arm with the higher rate.
"""

from __future__ import annotations

from alwaha.engagement.m03_l04_demand import LATER_MONTHS, LATER_YEAR, seasonal, window
from alwaha.engagement.m03_l04_rows import fields


def extraction_f1(rows: list[dict]) -> float:
    """Return the share of extraction fields that match.

    Each field is counted on its own, so one wrong field does not fail the whole row. No matching field returns nothing rather than dividing an empty match.
    """
    true_positive = false = 0
    for row in rows:
        for field in fields():
            if row["pred"].get(field) == row["label"].get(field):
                true_positive += 1
            else:
                false += 1
    # No field matched, including the case where there were no rows.
    if true_positive == 0:
        return 0.0
    return true_positive / (true_positive + false)


def _rate(rows: list[dict], same) -> float:
    """Return the share of rows for which same says the prediction matches the label. No rows scores as nothing."""
    # An empty score list is not a perfect score.
    if not rows:
        return 0.0
    hits = sum(1 for row in rows if same(row["pred"], row["label"]))
    return hits / len(rows)


def citation_accuracy(rows: list[dict]) -> float:
    """Return the share of citations whose document and span both match. Either mismatch fails the row."""
    return _rate(rows, lambda pred, label: pred.get("doc_id") == label.get("doc_id") and pred.get("span") == label.get("span"))


def journey_pass(rows: list[dict]) -> float:
    """Return the share of journeys whose state and approval both match. A booked step with the wrong approval fails.

    The steps count a journey only when its state and its approval both equal the label, and the hidden figures stay in this file and are not copied into a new comment.
    """
    return _rate(
        rows,
        lambda pred, label: pred.get("state") == label.get("state") and pred.get("approved") == label.get("approved"),
    )


def classify(row: dict) -> str:
    """Return the failure type of a log line, or pass when none of the cues appear.

    The cues are tested from the retrieval cue through the workflow cue. A line that matches none of them is a pass, not an unknown type.
    """
    text = str(row.get("output", "")).lower()
    # An unauthorized source is a retrieval failure even if the rest of the sentence sounds fluent.
    if "unauthorized" in text:
        return "retrieval"
    # A weekday offer that ignores the stated preference is a reasoning failure.
    if "friday" in text:
        return "reasoning"
    # Booked with an empty approval is a workflow failure.
    if "approval" in text and "none" in text:
        return "workflow"
    # A source the file does not contain is a hallucination.
    if "not on file" in text:
        return "hallucination"
    return "pass"


def mark(item: dict) -> bool:
    """Return whether the judge item passed. A missing flag counts as a failure."""
    return bool(item.get("pass"))


def predict(rows: list[dict]) -> list[dict]:
    """Return the later campaign window, which keeps the extra visits."""
    return window(rows, LATER_YEAR, LATER_MONTHS)


def ignore(rows: list[dict]) -> list[dict]:
    """Return the later campaign window with the earlier year copied forward, dropping the campaign extra."""
    return seasonal(rows)


def bounds(successes: int, total: int) -> tuple[float, float]:
    """Return the low and high ends of the interval around a success count.

    No trials means the interval is the whole range. Otherwise the interval is the usual score interval around the success rate, pulled back inside the range.
    """
    # No trials: there is no evidence to narrow the interval.
    if total <= 0:
        return (0.0, 1.0)
    z = 1.96
    rate = successes / total
    denom = 1 + z * z / total
    center = (rate + z * z / (2 * total)) / denom
    margin = z * ((rate * (1 - rate) / total + z * z / (4 * total * total)) ** 0.5) / denom
    return (max(0.0, center - margin), min(1.0, center + margin))


def report(protocol: dict) -> dict:
    """Return the metric and the arm with the higher rate on that metric.

    The rate is the arm's count divided by its size. Equal rates keep the earlier arm.
    """
    metric = protocol["metric"]
    rates = {arm: row[metric] / row["n"] for arm, row in protocol["counts"].items()}
    # The higher rate wins. An equal rate keeps the arm that was inserted first.
    winner = max(rates, key=rates.get)
    return {"metric": metric, "winner": winner}
