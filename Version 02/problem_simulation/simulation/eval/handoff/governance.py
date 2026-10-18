"""The vendor pilot is tier 3. The Week 3 evaluation is the evidence, and it does not clear the pilot."""

from __future__ import annotations

from simulation.corpus.families.governance_texts import TIER_REQUIREMENTS

MISSING = (
    "register entry", "transparency record", "model card", "named clinical safety owner",
    "human oversight plan", "incident runbook entry",
)
CONFLICT = ("DPIA signed by the DPO",)
EVIDENCED = ("subgroup evaluation",)


def facts(world: dict) -> dict:
    required = list(TIER_REQUIREMENTS["3"])
    return {
        "tier_three": {
            "system": "vendor triage pilot",
            "tier": "3",
            "required": required,
            "missing": [item for item in required if item in MISSING],
            "conflict": [item for item in required if item in CONFLICT],
            "conditional": [],
            "evidenced": [item for item in required if item in EVIDENCED],
            "agent_tier": 2,
        },
        "model_evidence": _metrics(world),
    }


def _metrics(world: dict) -> dict:
    items = _evidence(world)
    points, drift, claims = items["operating_points"], items["firmware_drift"], items["claims"]
    return {
        "cut": float(items.get("reference_gap", {}).get("cut", 0.5)),
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


def _evidence(world: dict) -> dict:
    cached = world["gold"].get("evidence", {}).get("items")
    if cached and "operating_points" in cached:
        return cached
    from simulation.devices.inventory import inventory_frame
    from simulation.eval.evidence import claims, drift, drop, vendor
    from simulation.eval.evidence.rates import clean
    from simulation.ml.retrospective import handover_frame, scored_frame

    full = clean(handover_frame(scored_frame(world["events"])))
    allowed = drop.facts(world, full["site"].unique())["drop_restriction"]["allowed_sites"]
    kept, joined = vendor.cohort(world, allowed)
    operating = vendor.points(joined)
    located = claims.locate(world["rendered"], world["files"]["corpus/proposals/originals/proposal-retinalytics-2026.pdf"])
    return {
        "operating_points": operating,
        "firmware_drift": drift.firmware(full, inventory_frame(True), allowed),
        "claims": claims.judge(operating, located["claimed"], located["source"], located["stopped_document"],
                               located["postmortem"], located["injection_document"]),
        "reference_gap": vendor.gap(kept, joined),
    }
