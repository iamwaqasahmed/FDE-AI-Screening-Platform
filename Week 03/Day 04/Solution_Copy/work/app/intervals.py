"""Wilson intervals for a district slice."""

from __future__ import annotations


def bounds(successes: int, total: int) -> tuple[float, float]:
    # An empty slice covers the whole range.
    if total <= 0:
        return (0.0, 1.0)
    # 1.96 is the z for this interval.
    z = 1.96
    rate = successes / total
    denom = 1 + z * z / total
    center = (rate + z * z / (2 * total)) / denom
    margin = z * ((rate * (1 - rate) / total + z * z / (4 * total * total)) ** 0.5) / denom
    # Keep both ends inside 0 and 1.
    return (max(0.0, center - margin), min(1.0, center + margin))


def by_district(rows: list[dict]) -> dict[str, tuple[float, float]]:
    # Group the rows by district, then count the correct ones.
    grouped: dict[str, list[dict]] = {}
    for row in rows:
        grouped.setdefault(row["district"], []).append(row)
    found = {}
    for district, items in grouped.items():
        hits = sum(1 for item in items if item["correct"])
        found[district] = bounds(hits, len(items))
    return found
