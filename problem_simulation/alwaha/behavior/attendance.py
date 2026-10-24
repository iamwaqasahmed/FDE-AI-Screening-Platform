"""Attendance probability. The reminder uplift differs by district."""

from __future__ import annotations

UPLIFT = {"d-nakhl": 0.08, "d-safra": 0.04, "d-wadi": 0.06, "d-rim": 0.02}


def probability(row: dict) -> float:
    base = 0.72
    base -= min(row.get("lead_days", 7), 30) * 0.005
    base -= min(row.get("travel_minutes", 25), 180) * 0.0004
    base -= 0.12 if row.get("prior_dna") else 0
    if row.get("reminded"):
        base += UPLIFT.get(row.get("district", ""), 0.03)
    return max(0.05, min(0.95, base))


def reminded_delta(row: dict) -> float:
    silent = dict(row)
    silent["reminded"] = False
    reminded = dict(row)
    reminded["reminded"] = True
    return probability(reminded) - probability(silent)
