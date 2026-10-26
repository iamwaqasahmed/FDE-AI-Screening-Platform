"""Charge nothing for the fix.

spend discards the label count, the price, and the budget, and
returns zero.
"""

from __future__ import annotations


def spend(count: int, price: float, budget_sar: float):
    """Return zero.

    count, price, and budget_sar are discarded.
    """
    # The arguments do not change the charge.
    del count, price, budget_sar
    return 0
