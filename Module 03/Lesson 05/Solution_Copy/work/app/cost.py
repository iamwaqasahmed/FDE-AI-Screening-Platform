"""Price the fix in labels, and stop when the budget is spent.

spend multiplies the label count by the label price. A product above
the budget is not priced. A product that meets the budget is returned.
"""

from __future__ import annotations


def spend(count: int, price: float, budget_sar: float):
    """Return the label cost, or nothing when that cost is past the budget.

    count is how many labels are priced. price is the price of a
    label. budget_sar is the budget. The cost is count times price.
    """
    # The cost is the label count times the label price.
    total = count * price
    # Past the annotation budget, the fix is not priced.
    if total > budget_sar:
        return None
    return total
