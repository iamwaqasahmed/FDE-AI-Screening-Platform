"""The route, the critical path as a range, and the roadmap dates that miss it."""

from __future__ import annotations

from datetime import date

from simulation.delivery.plan import CDO_ASSUMED_ROUTE, PILOT_CONTRACT_VALUE, required_route, route_named
from simulation.eval.agent.paths import assumed, earliest, latest
from simulation.world.engagement import PILOT_DATE_ORIGINAL, PILOT_DATE_REQUESTED


def facts(world: dict) -> dict:
    done = date.fromisoformat(world["gold"]["pilot_date"]["critical_path"]["build_done"])
    early, late, direct = earliest(done), latest(done), assumed(done)
    return {
        "procurement_route": _route(),
        "critical_path": _path(early, late, direct),
        "roadmap_items": _roadmap(world, early),
    }


def _route() -> dict:
    required, direct = required_route(PILOT_CONTRACT_VALUE), route_named(CDO_ASSUMED_ROUTE)
    return {
        "value": PILOT_CONTRACT_VALUE,
        "route": required.route,
        "direct_award_ceiling": direct.max_value,
        "lead_weeks_min": required.lead_weeks_min,
        "lead_weeks_max": required.lead_weeks_max,
        "gate": "G2",
        "gate_date": early_gate(),
        "assumed_route": CDO_ASSUMED_ROUTE,
        "assumed_holds": PILOT_CONTRACT_VALUE <= (direct.max_value or 0),
    }


def early_gate() -> str:
    return earliest(date.min)["gate_2"]


def _path(early: dict, late: dict, direct: dict) -> dict:
    return {
        "earliest": early,
        "latest": late,
        "assumed_earliest": direct["go_live"],
        "assumed_binding": direct["binding"],
        "binding": early["binding"],
        "requested_feasible": direct["go_live"] <= PILOT_DATE_REQUESTED.isoformat(),
        "original_feasible": late["go_live"] <= PILOT_DATE_ORIGINAL.isoformat(),
    }


def _roadmap(world: dict, early: dict) -> dict:
    frame = world["files"]["handover/delivery/roadmap.csv"].set_index("item_id")
    gates = world["files"]["handover/delivery/funding_gates.csv"].set_index("gate")
    tested = early["tested"]
    return {
        "rm02_target": str(frame.at["RM-02", "target_date"]),
        "rm02_feasible": str(frame.at["RM-02", "target_date"]) >= early["contract_award"],
        "g3_date": str(gates.at["G3", "gate_date"]),
        "g3_passes": str(gates.at["G3", "gate_date"]) >= tested,
        "g3_not_before": tested,
        "unowned": sorted(frame.index[frame["owner"].eq("")].astype(str)),
    }
