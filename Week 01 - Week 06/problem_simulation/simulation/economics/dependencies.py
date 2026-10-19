"""Which opportunity must come first, and which blocker stops which opportunity."""

from __future__ import annotations

import pandas as pd

from simulation.economics.opportunities import BLOCKERS, OPPORTUNITIES

PRECEDES = (
    ("identity_resolution", "dna_prediction", "Previous did-not-attend history splits across alias records"),
    ("identity_resolution", "reminder_targeting", "Shared family phones send one reminder for several people"),
    ("identity_resolution", "grader_triage_ai", "Evaluating triage needs each person's prior grades on one record"),
    ("identity_resolution", "vendor_model_expansion", "The 2023 merge left studies on the wrong person"),
    ("letter_bureau_fix", "call_deflection", "Most avoidable calls are about letters that never arrived"),
    ("letter_bureau_fix", "reminder_targeting", "A reminder for an appointment whose letter was lost does not help"),
    ("grader_triage_ai", "vendor_model_expansion", "Triage on primary-care captures has to be proven first"),
)


def edges() -> list[dict]:
    rows = [{"source": a, "target": b, "kind": "precedes", "reason": why} for a, b, why in PRECEDES]
    for item in OPPORTUNITIES:
        rows.extend({"source": blocker, "target": item.key, "kind": "blocks", "reason": BLOCKERS[blocker]}
                    for blocker in item.blockers)
    return rows


def dependencies_frame() -> pd.DataFrame:
    return pd.DataFrame(edges())


def prerequisites(key: str) -> list[str]:
    return sorted(a for a, b, _ in PRECEDES if b == key)


def unlocks(key: str) -> list[str]:
    found: set[str] = set()
    frontier = [key]
    while frontier:
        current = frontier.pop()
        for a, b, _ in PRECEDES:
            if a == current and b not in found:
                found.add(b)
                frontier.append(b)
    return sorted(found)
