"""Reference scoring for rel-w3d5.
Participant copies do not import this module.

repair points an unauthorized citation at the in-force document. remeasure reports accuracy before that repair and after it. cost_for prices the rows that still disagree with the label. cite drops a staff document asked for by a patient. gate_for maps only the citation requirement onto the gate.
"""

from __future__ import annotations

from alwaha.engagement.w3d1 import budget
from alwaha.engagement.w3d5_rows import IN_FORCE, UNAUTH, before_labeled
from alwaha.samples.prices import price_rows

NON_GOALS = ("p-triage", "vendor-bot")
REQUIREMENT = "req-cite"
GATE = "G1"


def repair(row: dict) -> dict:
    """Return the prediction with an unauthorized document id rewritten to the in-force id.

    Any other prediction is copied unchanged, including a prediction that was already correct.
    """
    # An unauthorized citation is repaired onto the in-force document.
    if row.get("doc_id") == UNAUTH:
        return {**row, "doc_id": IN_FORCE}
    return dict(row)


def accuracy(rows: list[dict]) -> float:
    """Return the share of rows whose document and span both match. No rows scores as nothing."""
    # An empty list is not a perfect score.
    if not rows:
        return 0.0
    hits = 0
    for row in rows:
        pred, label = row["pred"], row["label"]
        if pred.get("doc_id") == label.get("doc_id") and pred.get("span") == label.get("span"):
            hits += 1
    return hits / len(rows)


def remeasure(rows: list[dict]) -> dict:
    """Return accuracy before the repair and accuracy after unauthorized citations are rewritten."""
    repaired = [{"label": row["label"], "pred": repair(row["pred"])} for row in rows]
    return {"after": accuracy(repaired), "before": accuracy(rows)}


def moved(rows: list[dict]) -> int:
    """Return how many predictions name a different document from the label. The span is not part of this count."""
    return sum(1 for row in rows if row["pred"].get("doc_id") != row["label"].get("doc_id"))


def label_price(seed: int) -> int:
    """Return the label price on this seed's sheet. A sheet without that price is an error."""
    for row in price_rows(seed):
        if row["key"] == "cost.label":
            return int(row["sar"])
    # The sheet is required to carry the label price. Silence here would hide a missing row.
    raise KeyError("cost.label")


def spend(count: int, price: float, budget_sar: float):
    """Return the total cost, or nothing when that total is over the budget.

    Nothing means the labeling does not fit, rather than a clipped total.
    """
    total = count * price
    # Over the budget the work is not done, so there is no spend to report.
    if total > budget_sar:
        return None
    return total


def cost_for(profile) -> dict:
    """Return the moved count, the label price, the budget, and the spend for this profile.

    The count comes from the labeled rows. The budget comes from the earlier day's ceiling.
    """
    count = moved(before_labeled())
    price = label_price(profile.seed)
    ceiling = budget(profile)["sar"]
    return {"budget_sar": ceiling, "count": count, "price": price, "spend": spend(count, price, ceiling)}


def cite(row: dict) -> dict | None:
    """Return the citation a caller may show, or nothing when a patient would be shown a staff document."""
    # A patient must not be shown a staff document, so the citation is dropped.
    if row.get("asker") == "patient" and row.get("audience") == "staff":
        return None
    return {"audience": row.get("audience"), "doc_id": row.get("doc_id"), "version": row.get("version")}


def meets_budget(value: float, floor: float) -> bool:
    """Return whether the value meets the floor.

    A value that lands on the floor after floating-point error still meets it.
    """
    # The tiny allowance keeps a value that is the floor, but printed just under it, from failing.
    return float(value) + 1e-9 >= float(floor)


def kept(story: dict) -> bool:
    """Return whether the story stays in the proof. Stories on the non-goal list do not."""
    return story.get("story_id") not in NON_GOALS


def gate_for(requirement_id: str) -> str:
    """Return the gate for the citation requirement, or an empty gate for any other requirement."""
    # Only the citation requirement is wired to the gate.
    if requirement_id == REQUIREMENT:
        return GATE
    return ""
