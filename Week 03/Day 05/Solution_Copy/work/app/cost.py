"""Price the fix in labels, and stop when the budget is spent."""

from __future__ import annotations


def spend(count: int, price: float, budget_sar: float):
    # The cost is the label count times the label price.
    total = count * price
    # Past the annotation budget, the fix is not priced.
    if total > budget_sar:
        return None
    return total
