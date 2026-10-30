"""Wilson intervals for a district slice.

bounds builds an interval around the success rate. An empty slice
covers the whole range. by_district groups the rows, counts the
correct ones, and returns an interval for each district.
"""

from __future__ import annotations


def bounds(successes: int, total: int) -> tuple[float, float]:
    """Return the low and high ends of a Wilson interval.

    successes is how many rows are correct. total is the size of
    the slice. An empty slice returns the full range. Otherwise the
    center and the margin use the z below, and both ends stay inside
    the full range.
    """
    # An empty slice covers the whole range.
    if total <= 0:
        return (0.0, 1.0)
    # 1.96 is the z for this interval.
    z = 1.96
    # The observed success rate.
    rate = successes / total
    # Shared denominator for the center and the margin.
    denom = 1 + z * z / total
    # Center of the interval, shifted by the z term.
    center = (rate + z * z / (2 * total)) / denom
    # Width around the center. The power is the square-root term.
    margin = z * ((rate * (1 - rate) / total + z * z / (4 * total * total)) ** 0.5) / denom
    # Keep both ends inside 0 and 1.
    return (max(0.0, center - margin), min(1.0, center + margin))


def by_district(rows: list[dict]) -> dict[str, tuple[float, float]]:
    """Return a Wilson interval for each district in the rows.

    rows carry a district and a correct flag. Rows for the same
    district are counted together. The interval uses the correct
    count and how many rows that district has.
    """
    # Group the rows by district, then count the correct ones.
    grouped: dict[str, list[dict]] = {}
    for row in rows:
        grouped.setdefault(row["district"], []).append(row)
    found = {}
    for district, items in grouped.items():
        # Each correct row adds to the success count.
        hits = sum(1 for item in items if item["correct"])
        found[district] = bounds(hits, len(items))
    return found
