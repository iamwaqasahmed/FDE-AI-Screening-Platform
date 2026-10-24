"""Reference scoring for rel-w3d4. Participant copies do not import this module."""

from __future__ import annotations

from alwaha.engagement.w3d4_demand import LATER_MONTHS, LATER_YEAR, seasonal, window
from alwaha.engagement.w3d4_rows import fields


def extraction_f1(rows: list[dict]) -> float:
    true_positive = false = 0
    for row in rows:
        for field in fields():
            if row["pred"].get(field) == row["label"].get(field):
                true_positive += 1
            else:
                false += 1
    if true_positive == 0:
        return 0.0
    return true_positive / (true_positive + false)


def _rate(rows: list[dict], same) -> float:
    if not rows:
        return 0.0
    hits = sum(1 for row in rows if same(row["pred"], row["label"]))
    return hits / len(rows)


def citation_accuracy(rows: list[dict]) -> float:
    return _rate(rows, lambda pred, label: pred.get("doc_id") == label.get("doc_id") and pred.get("span") == label.get("span"))


def journey_pass(rows: list[dict]) -> float:
    return _rate(
        rows,
        lambda pred, label: pred.get("state") == label.get("state") and pred.get("approved") == label.get("approved"),
    )


def classify(row: dict) -> str:
    text = str(row.get("output", "")).lower()
    if "unauthorized" in text:
        return "retrieval"
    if "friday" in text:
        return "reasoning"
    if "approval" in text and "none" in text:
        return "workflow"
    if "not on file" in text:
        return "hallucination"
    return "pass"


def mark(item: dict) -> bool:
    return bool(item.get("pass"))


def predict(rows: list[dict]) -> list[dict]:
    return window(rows, LATER_YEAR, LATER_MONTHS)


def ignore(rows: list[dict]) -> list[dict]:
    return seasonal(rows)


def bounds(successes: int, total: int) -> tuple[float, float]:
    if total <= 0:
        return (0.0, 1.0)
    z = 1.96
    rate = successes / total
    denom = 1 + z * z / total
    center = (rate + z * z / (2 * total)) / denom
    margin = z * ((rate * (1 - rate) / total + z * z / (4 * total * total)) ** 0.5) / denom
    return (max(0.0, center - margin), min(1.0, center + margin))


def report(protocol: dict) -> dict:
    metric = protocol["metric"]
    rates = {arm: row[metric] / row["n"] for arm, row in protocol["counts"].items()}
    winner = max(rates, key=rates.get)
    return {"metric": metric, "winner": winner}
