"""Cost for one hospital.

cost sums sar for rows whose hospital is h-wadi and ignores every
other hospital. The result always has that one key. When no row
matches, the total is zero. A matching row must have sar.
"""

from __future__ import annotations


def cost(rows: list[dict]) -> dict:
    """Sum sar for h-wadi and ignore every other hospital.

    The result is a new dict with that single key. The input rows stay put.
    """
    # The hospital check runs before sar is read, so other rows need no sar.
    total = sum(int(row["sar"]) for row in rows if row.get("hospital") == "h-wadi")
    # The key is present even when the total is zero.
    return {"h-wadi": total}
