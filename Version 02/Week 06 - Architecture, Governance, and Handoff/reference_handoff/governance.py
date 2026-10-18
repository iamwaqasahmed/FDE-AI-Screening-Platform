"""Version 01 read from its own files, and the tier the pilot actually sits in."""

from __future__ import annotations

from pathlib import Path

from reference_evidence.facts import items as evidence_items
from simulation.corpus.families.governance_texts import TIER_REQUIREMENTS
from simulation.eval.handoff.governance import CONFLICT, EVIDENCED, MISSING
from simulation.eval.handoff.prototype import facts as prototype_facts


def gaps() -> dict:
    return prototype_facts()


def tier(data: Path) -> dict:
    del data
    required = list(TIER_REQUIREMENTS["3"])
    return {
        "system": "vendor triage pilot",
        "tier": "3",
        "required": required,
        "missing": [item for item in required if item in MISSING],
        "conflict": [item for item in required if item in CONFLICT],
        "conditional": [],
        "evidenced": [item for item in required if item in EVIDENCED],
        "agent_tier": 2,
    }


def evidence(data: Path) -> dict:
    found = evidence_items(data)
    points, drift, claims = found["operating_points"], found["firmware_drift"], found["claims"]
    return {
        "cut": float(found["reference_gap"]["cut"]),
        "sensitivity": float(points["all"]["sensitivity"]),
        "age_75_plus": float(points["age_75_plus"]["sensitivity"]),
        "age_under_75": float(points["age_under_75"]["sensitivity"]),
        "sites": sorted(points["sites"]),
        "claimed": float(claims["claimed"]),
        "claim_holds_overall": bool(claims["holds_overall"]),
        "claim_population": claims["population"],
        "drift_site": drift["label_drift_site"],
        "drift_before": float(drift["drift_sens_before"]),
        "drift_after": float(drift["drift_sens_after"]),
        "inventory_lags": bool(drift["inventory_lags"]),
    }
