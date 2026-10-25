"""Disparity by district and insurance class, and the Thursday stamp rate."""

from __future__ import annotations


def _rates(rows: list[dict], key: str) -> list[float]:
    groups: dict[str, list[bool]] = {}
    for row in rows:
        groups.setdefault(row[key], []).append(row["decision"] == "yes")
    return [sum(flags) / len(flags) for flags in groups.values() if flags]


def gap(rows: list[dict]) -> float:
    spreads = []
    for key in ("district", "insurance"):
        rates = _rates(rows, key)
        if rates:
            spreads.append(max(rates) - min(rates))
    if not spreads:
        return 0.0
    return max(spreads)


def stamp_rate(rows: list[dict]) -> float:
    if not rows:
        return 0.0
    return sum(1 for row in rows if row.get("stamped")) / len(rows)
