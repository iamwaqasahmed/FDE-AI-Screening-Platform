"""Canonical counts, scaled by the profile. Aliases sit on top of these people and are not extra humans."""

from __future__ import annotations

from simulation.config import active

_P = active()


def _scaled(base: dict[str, int]) -> dict[str, int]:
    return {key: _P.count(value) for key, value in base.items()}


ELIGIBLE = _scaled({"North City": 9800, "East City": 2600, "Hill Counties": 3400, "River Districts": 2100})
DECEASED = _scaled({"North City": 650, "East City": 180, "Hill Counties": 220, "River Districts": 150})
MOVED = _scaled({"North City": 480, "East City": 140, "Hill Counties": 160, "River Districts": 120})

CANONICAL = sum(ELIGIBLE.values()) + sum(DECEASED.values()) + sum(MOVED.values())
ALIASES = _P.count(80)
FALSE_MERGE_PAIRS = _P.count(40)
SPLITS = _P.count(60)
REUSE_DONORS = _P.count(300)
TWIN_PAIRS = _P.count(25)
REVERSED_MERGE_PAIRS = 12
SILENT_MOVERS = _P.count(260)
PILOT_IMAGES = min(400, _P.count(178))
DECOYS = 250

ATTEND = {
    "North City": 0.72,
    "East City": 0.62,
    "Hill Counties": 0.28,
    "River Districts": 0.18,
}
UNCODED = {
    "North City": 0.06,
    "East City": 0.08,
    "Hill Counties": 0.40,
    "River Districts": 0.50,
}
GRADE_WEIGHTS = (("R0", 0.58), ("R1", 0.18), ("R2", 0.14), ("R3", 0.04), ("U", 0.06))
