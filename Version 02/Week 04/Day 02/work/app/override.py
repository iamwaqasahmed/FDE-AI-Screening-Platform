"""Share of stamped coordinator actions."""

from __future__ import annotations


def rate(rows: list[dict]) -> float:
    if not rows:
        return 0.0
    return sum(1 for row in rows if row.get("stamped")) / len(rows)
