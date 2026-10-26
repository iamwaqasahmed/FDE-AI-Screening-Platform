"""Report the contained count instead of the pre-registered metric.

Every arm is scored on the contained count divided by n. The report
names that contained field as the metric, and names the arm with the
highest contained rate. When rates tie, the earliest arm in the
counts is the winner.
"""

from __future__ import annotations

# The count this report divides by n.
_PEEK = "contained"


def report(protocol: dict) -> dict:
    """Return the contained field as the metric, and the winning arm.

    protocol has a counts map. Each arm has a contained count and an
    n. The rate is that contained count divided by n. The winner is
    the arm whose rate is highest.
    """
    # Score every arm on the contained count.
    rates = {arm: row[_PEEK] / row["n"] for arm, row in protocol["counts"].items()}
    # The higher contained rate is the arm this report returns.
    winner = max(rates, key=rates.get)
    return {"metric": _PEEK, "winner": winner}
