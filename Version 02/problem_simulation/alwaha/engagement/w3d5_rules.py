"""Reference scoring for rel-w3d5. Participant copies do not import this module."""

from __future__ import annotations

from alwaha.engagement.w3d1 import budget
from alwaha.engagement.w3d5_rows import IN_FORCE, UNAUTH, before_labeled
from alwaha.samples.prices import price_rows

NON_GOALS = ("p-triage", "vendor-bot")
REQUIREMENT = "req-cite"
GATE = "G1"


def repair(row: dict) -> dict:
    if row.get("doc_id") == UNAUTH:
        return {**row, "doc_id": IN_FORCE}
    return dict(row)


def accuracy(rows: list[dict]) -> float:
    if not rows:
        return 0.0
    hits = 0
    for row in rows:
        pred, label = row["pred"], row["label"]
        if pred.get("doc_id") == label.get("doc_id") and pred.get("span") == label.get("span"):
            hits += 1
    return hits / len(rows)


def remeasure(rows: list[dict]) -> dict:
    repaired = [{"label": row["label"], "pred": repair(row["pred"])} for row in rows]
    return {"after": accuracy(repaired), "before": accuracy(rows)}


def moved(rows: list[dict]) -> int:
    return sum(1 for row in rows if row["pred"].get("doc_id") != row["label"].get("doc_id"))


def label_price(seed: int) -> int:
    for row in price_rows(seed):
        if row["key"] == "cost.label":
            return int(row["sar"])
    raise KeyError("cost.label")


def spend(count: int, price: float, budget_sar: float):
    total = count * price
    if total > budget_sar:
        return None
    return total


def cost_for(profile) -> dict:
    count = moved(before_labeled())
    price = label_price(profile.seed)
    ceiling = budget(profile)["sar"]
    return {"budget_sar": ceiling, "count": count, "price": price, "spend": spend(count, price, ceiling)}


def cite(row: dict) -> dict | None:
    if row.get("asker") == "patient" and row.get("audience") == "staff":
        return None
    return {"audience": row.get("audience"), "doc_id": row.get("doc_id"), "version": row.get("version")}


def meets_budget(value: float, floor: float) -> bool:
    return float(value) + 1e-9 >= float(floor)


def kept(story: dict) -> bool:
    return story.get("story_id") not in NON_GOALS


def gate_for(requirement_id: str) -> str:
    if requirement_id == REQUIREMENT:
        return GATE
    return ""
