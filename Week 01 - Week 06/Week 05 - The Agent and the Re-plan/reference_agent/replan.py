"""The pilot path from the assumptions memo, the gates, the routes, and the freeze calendar."""

from __future__ import annotations

import re
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

from reference_agent.load import durations, next_monday, read_csv


def facts(data: Path, build_done: date) -> dict:
    spec, test, mobilise = durations(data)
    routes = read_csv(data, "handover/delivery/procurement_routes.csv").set_index("route")
    gates = read_csv(data, "handover/delivery/funding_gates.csv").set_index("gate")
    roadmap = read_csv(data, "handover/delivery/roadmap.csv").set_index("item_id")
    calendar = read_csv(data, "handover/delivery/freeze_calendar.csv")
    value = int(float(roadmap.at["RM-02", "estimated_value_gbp"]))
    required = _route(routes, value)
    direct = routes.loc["direct_award"]
    gate = date.fromisoformat(str(gates.at["G2", "gate_date"]))
    freeze_end = date.fromisoformat(str(calendar[(calendar["ref"] == "FRZ-0301")].iloc[0]["end"]))
    windows = sorted(date.fromisoformat(day) for day in calendar[(calendar["system"] == "registry") & (calendar["kind"] == "release_window")]["start"])
    early = _trace(build_done, required["route"], int(required["lead_weeks_min"]), spec, test, mobilise, gate, freeze_end, windows)
    late = _trace(build_done, required["route"], int(required["lead_weeks_max"]), spec, test, mobilise, gate, freeze_end, windows)
    assumed = _trace(build_done, "direct_award", int(direct["lead_weeks_min"]), spec, test, mobilise, gate, freeze_end, windows)
    requested = _requested(data)
    return {
        "procurement_route": _procurement(value, required, direct, gate),
        "critical_path": _critical(early, late, assumed, requested, str(roadmap.at["RM-03", "target_date"])),
        "roadmap_items": _roadmap(roadmap, gates, early),
    }


def _route(routes: pd.DataFrame, value: int):
    for name, row in routes.iterrows():
        ceiling = row["max_value_gbp"]
        if int(row["min_value_gbp"]) <= value and (ceiling == "" or value <= int(ceiling)):
            found = row.copy()
            found["route"] = name
            return found
    raise ValueError(value)


def _trace(build_done, route, lead, spec, test, mobilise, gate, freeze_end, windows) -> dict:
    award = gate + timedelta(weeks=lead)
    spec_ready = award + timedelta(weeks=spec)
    after = freeze_end + timedelta(days=1)
    window = next(day for day in windows if day >= max(spec_ready, after, build_done))
    tested = window + timedelta(weeks=test)
    mobilised = award + timedelta(weeks=mobilise)
    go_live = next_monday(max(tested, mobilised))
    latest = max(spec_ready, after, build_done)
    binding = "procurement" if latest == spec_ready else "freeze" if latest == after else "build"
    return {
        "route": route, "lead_weeks": lead, "gate_2": gate.isoformat(), "contract_award": award.isoformat(),
        "spec_ready": spec_ready.isoformat(), "registry_freeze_end": freeze_end.isoformat(),
        "build_done": build_done.isoformat(), "registry_window": window.isoformat(), "tested": tested.isoformat(),
        "mobilised": mobilised.isoformat(), "go_live": go_live.isoformat(), "binding": binding,
    }


def _procurement(value, required, direct, gate: date) -> dict:
    ceiling = int(direct["max_value_gbp"])
    return {
        "value": value, "route": required["route"], "direct_award_ceiling": ceiling,
        "lead_weeks_min": int(required["lead_weeks_min"]), "lead_weeks_max": int(required["lead_weeks_max"]),
        "gate": "G2", "gate_date": gate.isoformat(), "assumed_route": "direct_award", "assumed_holds": value <= ceiling,
    }


def _critical(early, late, assumed, requested: str, original: str) -> dict:
    return {
        "earliest": early, "latest": late, "assumed_earliest": assumed["go_live"], "assumed_binding": assumed["binding"],
        "binding": early["binding"], "requested_feasible": assumed["go_live"] <= requested,
        "original_feasible": late["go_live"] <= original,
    }


def _roadmap(roadmap, gates, early: dict) -> dict:
    return {
        "rm02_target": str(roadmap.at["RM-02", "target_date"]),
        "rm02_feasible": str(roadmap.at["RM-02", "target_date"]) >= early["contract_award"],
        "g3_date": str(gates.at["G3", "gate_date"]),
        "g3_passes": str(gates.at["G3", "gate_date"]) >= early["tested"],
        "g3_not_before": early["tested"],
        "unowned": sorted(roadmap.index[roadmap["owner"].eq("")].astype(str)),
    }


def _requested(data: Path) -> str:
    text = (data / "drops/week-5/scope_change_cdo.md").read_text(encoding="utf-8")
    return re.search(r"(\d{4}-\d{2}-\d{2})", text).group(1)
