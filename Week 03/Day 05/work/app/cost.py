"""Price the fix in labels, and stop when the budget is spent."""

from __future__ import annotations


def spend(count: int, price: float, budget_sar: float):
    total = count * price
    if total > budget_sar:
        return None
    return total
