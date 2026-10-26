"""Attendance probability. The reminder uplift differs by district.

The base falls as lead time and travel grow, and it falls further when a prior miss is set. A reminder adds the district uplift, or the default uplift when the district is not in the table. The result is clamped. reminded_delta is the probability with a reminder minus the probability without one, on an otherwise identical row.
"""

from __future__ import annotations

UPLIFT = {"d-nakhl": 0.08, "d-safra": 0.04, "d-wadi": 0.06, "d-rim": 0.02}


def probability(row: dict) -> float:
    """Return the clamped attendance probability for one booking-shaped row."""
    base = 0.72
    base -= min(row.get("lead_days", 7), 30) * 0.005
    base -= min(row.get("travel_minutes", 25), 180) * 0.0004
    # A prior miss lowers the base. A missing or false prior leaves it unchanged.
    base -= 0.12 if row.get("prior_dna") else 0
    if row.get("reminded"):
        # Unknown districts still get a reminder effect, using the default uplift.
        base += UPLIFT.get(row.get("district", ""), 0.03)
    return max(0.05, min(0.95, base))


def reminded_delta(row: dict) -> float:
    """Return how much a reminder changes the probability, holding every other field fixed.

    The steps copy the row, score one copy with the reminder off and one copy with the reminder on, and subtract the silent probability from the reminded probability.
    """
    silent = dict(row)
    silent["reminded"] = False
    reminded = dict(row)
    reminded["reminded"] = True
    return probability(reminded) - probability(silent)
