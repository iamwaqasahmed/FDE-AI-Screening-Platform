"""Spend the label budget on the uncertain items.

Chapter 08 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell returns every item and ignores the price. The three
checks do not call this file. The suite does. When the file is
present, spending stops before the next price would pass the budget.
"""

from __future__ import annotations


def spend(items: list[dict], price: float, budget_sar: float) -> list[str]:
    """Buy the least certain items until the next price would not fit.

    items carry item_id and uncertainty. price is the cost of one
    label. budget_sar is the budget. The sort is uncertainty
    descending, then item_id. A tie on uncertainty keeps item_id
    order. The loop stops before spent plus price would pass the
    budget.
    """
    ordered = sorted(items, key=lambda item: (-item["uncertainty"], item["item_id"]))
    chosen = []
    spent = 0.0
    for item in ordered:
        # The next label would pass the budget, so stop.
        if spent + price > budget_sar:
            break
        chosen.append(item["item_id"])
        spent += price
    return chosen
