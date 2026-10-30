"""Disparity by district and insurance class, and the Thursday stamp rate.

gap is the wider yes-rate spread across district and across insurance.
A yes decision is the decision text yes. For each key, rows are grouped
and each group's rate is the share of yes decisions. The spread is the
highest rate minus the lowest. gap returns the larger spread. No rows,
or a key with no groups, contributes nothing, and no spreads at all
returns zero.

stamp_rate is the share of rows whose stamped field is true. An empty
list returns zero so the length is never used as a divisor.
"""

from __future__ import annotations


def _rates(rows: list[dict], key: str) -> list[float]:
    """Group rows by key and return the yes-rate of each group.

    Group order follows the first time each key value appears. The spread
    later uses the highest and lowest rates, so that order does not matter.
    """
    groups: dict[str, list[bool]] = {}
    for row in rows:
        # The row must have this key and a decision. Other decision text counts as no.
        groups.setdefault(row[key], []).append(row["decision"] == "yes")
    # Skip an empty group so the rate is never a division by an empty length.
    return [sum(flags) / len(flags) for flags in groups.values() if flags]


def gap(rows: list[dict]) -> float:
    """Return the wider yes-rate spread across district and insurance.

    Each spread is the highest group rate minus the lowest. The result is
    the larger of those spreads, or zero when neither key produced one.
    """
    spreads = []
    for key in ("district", "insurance"):
        rates = _rates(rows, key)
        # A key that formed no groups does not add a spread.
        if rates:
            spreads.append(max(rates) - min(rates))
    if not spreads:
        return 0.0
    return max(spreads)


def stamp_rate(rows: list[dict]) -> float:
    """Return the share of rows with a true stamped field.

    A missing stamped field counts as not stamped. An empty list returns zero.
    """
    # An empty list has no share. Return zero before dividing.
    if not rows:
        return 0.0
    return sum(1 for row in rows if row.get("stamped")) / len(rows)
