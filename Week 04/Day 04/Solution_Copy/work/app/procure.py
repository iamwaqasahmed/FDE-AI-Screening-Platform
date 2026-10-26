"""Rent when a purchase misses the deadline.

choice reads ordered_on, deadline, purchase_weeks, and
rent_days. The purchase date is ordered_on plus
purchase_weeks. The rental date is ordered_on plus
rent_days. When the purchase date is on or before the
deadline, the choice is buy. When the purchase misses
and the rental date is on or before the deadline, the
choice is rent. When both miss, the choice is buy.
"""

from __future__ import annotations

from datetime import date, timedelta


def choice(note: dict) -> str:
    """Return buy when the purchase fits, otherwise rent when the rental fits.

    purchase_weeks is added as weeks. rent_days is added
    as days. If the rental also misses the deadline, the
    result is buy.
    """
    start = date.fromisoformat(str(note["ordered_on"]))
    deadline = date.fromisoformat(str(note["deadline"]))
    bought = start + timedelta(weeks=int(note["purchase_weeks"]))
    rented = start + timedelta(days=int(note["rent_days"]))
    # Buy when the purchase date meets the deadline.
    if bought <= deadline:
        return "buy"
    # The purchase is late. Rent if the rental still meets it.
    if rented <= deadline:
        return "rent"
    return "buy"
