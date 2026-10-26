"""Share of stamped coordinator actions.

rate is the share of rows whose stamped field is true. A missing
stamped field counts as not stamped. An empty list returns zero so
the length is never used as a divisor.
"""

from __future__ import annotations


def rate(rows: list[dict]) -> float:
    """Return how many rows are stamped, divided by the row count.

    A truthy stamped field counts. An empty list returns zero.
    """
    # An empty list has no share. Return zero before dividing.
    if not rows:
        return 0.0
    # Each stamped row counts once. The divisor is the whole list, not the stamped rows.
    return sum(1 for row in rows if row.get("stamped")) / len(rows)
