"""Treat every district as a point at one.

bounds ignores the success count and the slice size and returns a
point whose ends are both one. by_district maps every district on
the rows to that same point.
"""

from __future__ import annotations


def bounds(successes: int, total: int) -> tuple[float, float]:
    """Return a point at one.

    successes and total are ignored. Both ends are one.
    """
    # The arguments do not change the point.
    del successes, total
    return (1.0, 1.0)


def by_district(rows: list[dict]) -> dict[str, tuple[float, float]]:
    """Map each district named on the rows to a point at one.

    rows supply the district names. A repeated district stays that
    same point.
    """
    return {row["district"]: (1.0, 1.0) for row in rows}
