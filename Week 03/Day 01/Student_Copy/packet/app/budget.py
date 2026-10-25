"""Spend the label budget in list order.

This is the shell. Chapter 08 replaces the copy under work/app.
Leave this file in the packet unchanged.

spend returns every item and ignores the price and the budget.
The three checks do not call this file. The suite does.
"""

from __future__ import annotations


def spend(items: list[dict], price: float, budget_sar: float) -> list[str]:
    """Return every item id. Price and budget are ignored."""
    del price, budget_sar
    return [item["item_id"] for item in items]
