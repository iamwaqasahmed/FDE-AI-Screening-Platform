"""The estate as it runs: zones, the callback path, recovery tiers, and the load it has to meet."""

from __future__ import annotations

import yaml

from simulation.architecture.components import callback_path, zone_of
from simulation.architecture.ea_document import ZONE_TEXT
from simulation.eval.handoff.bars import SLOS
from simulation.systems.catalog import SYSTEMS


def facts(world: dict) -> dict:
    components = world["files"]["handover/architecture/components.csv"]
    levels = yaml.safe_load(SLOS.read_text(encoding="utf-8"))
    return {"current_state": _state(components), "service_levels": _levels(components, levels)}


def _state(components) -> dict:
    tiers = components.set_index("component")["dr_tier"]
    fhir = sorted(components.loc[components["protocol"].astype(str).str.contains("FHIR"), "component"])
    backup = sorted(components.loc[components["dr_tier"].astype(int) == 4, "component"])
    path = list(callback_path())
    vendor = next(item for item in SYSTEMS if item["system_id"] == "vendor")
    return {
        "zones": list(ZONE_TEXT),
        "callback_path": path,
        "callback_zones": [zone_of(components, item) for item in path],
        "fhir": fhir,
        "no_backup": backup,
        "tiers": {key: int(tiers[key]) for key in ("shared-folder", "grader", "vendor")},
        "vendor_hosting": vendor["hosting"],
    }


def _levels(components, levels: dict) -> dict:
    hours = levels["load_profile"]["by_hour"]
    season = levels["load_profile"]["season_multiplier"]
    band = max(hours, key=hours.get)
    month = max(season, key=season.get)
    peak, factor = int(hours[band]), float(season[month])
    tiers = components.set_index("component")["dr_tier"]
    availability = float(levels["systems"]["vendor"]["availability"])
    return {
        "peak_band": band,
        "peak_rpm": peak,
        "peak_month": month,
        "season_max": factor,
        "design_rpm": int(round(peak * factor)),
        "vendor_availability": availability,
        "vendor_downtime_hours": round((1 - availability) * 24 * 30, 1),
        "event_lag_minutes": int(levels["event_delivery"]["booking"]["p95_lag_minutes"]),
        "grader_tier": int(tiers["grader"]),
        "vendor_tier": int(tiers["vendor"]),
        "grader_waits": False,
    }
