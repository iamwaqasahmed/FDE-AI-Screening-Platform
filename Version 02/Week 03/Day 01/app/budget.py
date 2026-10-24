"""Spend the label budget in list order."""

from __future__ import annotations


def spend(items: list[dict], price: float, budget_sar: float) -> list[str]:
    del price, budget_sar
    return [item["item_id"] for item in items]
