"""Spend the label budget on the uncertain items."""

from __future__ import annotations


def spend(items: list[dict], price: float, budget_sar: float) -> list[str]:
    ordered = sorted(items, key=lambda item: (-item["uncertainty"], item["item_id"]))
    chosen = []
    spent = 0.0
    for item in ordered:
        if spent + price > budget_sar:
            break
        chosen.append(item["item_id"])
        spent += price
    return chosen
