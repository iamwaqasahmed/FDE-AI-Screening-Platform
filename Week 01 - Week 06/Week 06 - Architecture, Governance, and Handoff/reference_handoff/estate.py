"""Zones, tiers, load, and the rules a flow has to cite."""

from __future__ import annotations

from pathlib import Path

import yaml

from simulation.architecture.components import callback_path
from simulation.architecture.ea_document import ZONE_TEXT
from simulation.eval.handoff.bars import SLOS
from simulation.systems.catalog import SCORE_SYSTEM, SIGNED_GRADE_SYSTEM, SYSTEMS


def facts(data: Path, sites: list[str], decided_by: str) -> dict:
    components = _components(data)
    return {"current_state": _state(data, components), "service_levels": _levels(components), "flow_rules": _rules(sites, decided_by)}


def _components(data: Path):
    import pandas as pd

    return pd.read_csv(data / "handover/architecture/components.csv", dtype=str).fillna("")


def _state(data: Path, components) -> dict:
    tiers = components.set_index("component")["dr_tier"].astype(int)
    path = list(callback_path())
    zones = components.set_index("component")["zone"]
    hosting = _hosting(data)
    fhir = sorted(components.loc[components["protocol"].str.contains("FHIR"), "component"])
    backup = sorted(components.loc[components["dr_tier"].astype(int).eq(4), "component"])
    return {
        "zones": list(ZONE_TEXT),
        "callback_path": path,
        "callback_zones": [str(zones.at[item]) for item in path],
        "fhir": fhir,
        "no_backup": backup,
        "tiers": {key: int(tiers.at[key]) for key in ("shared-folder", "grader", "vendor")},
        "vendor_hosting": hosting,
    }


def _hosting(data: Path) -> str:
    catalog = next(item["hosting"] for item in SYSTEMS if item["system_id"] == "vendor")
    text = (data / "handover/interfaces/vendor.md").read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.lower().startswith("hosting:"):
            return line.split(":", 1)[1].strip()
    return catalog


def _levels(components) -> dict:
    levels = yaml.safe_load(SLOS.read_text(encoding="utf-8"))
    hours = levels["load_profile"]["by_hour"]
    season = levels["load_profile"]["season_multiplier"]
    band, month = max(hours, key=hours.get), max(season, key=season.get)
    peak, factor = int(hours[band]), float(season[month])
    tiers = components.set_index("component")["dr_tier"].astype(int)
    availability = float(levels["systems"]["vendor"]["availability"])
    return {
        "peak_band": str(band), "peak_rpm": peak, "peak_month": str(month), "season_max": factor,
        "design_rpm": int(round(peak * factor)), "vendor_availability": availability,
        "vendor_downtime_hours": round((1 - availability) * 24 * 30, 1),
        "event_lag_minutes": int(levels["event_delivery"]["booking"]["p95_lag_minutes"]),
        "grader_tier": int(tiers.at["grader"]), "vendor_tier": int(tiers.at["vendor"]), "grader_waits": False,
    }


def _rules(sites: list[str], decided_by: str) -> dict:
    from simulation.drops.rules import BANNED_FIELD, REPLACEMENT_FIELD

    return {
        "allowed_sites": sites,
        "banned_field": BANNED_FIELD,
        "replacement_field": REPLACEMENT_FIELD,
        "inbound_terminates": "integration-engine",
        "result_system": SIGNED_GRADE_SYSTEM,
        "score_system": SCORE_SYSTEM,
        "region_decided_by": decided_by,
    }
