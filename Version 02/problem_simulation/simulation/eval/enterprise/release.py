"""The registry freeze, the release windows around it, and the tickets it blocks."""

from __future__ import annotations

from simulation.delivery.contracts import contracts_frame
from simulation.delivery.plan import first_window, freeze, release_windows
from simulation.delivery.raci import raci_frame
from simulation.eval.enterprise.drop import month_end
from simulation.world.clock import iso
from simulation.world.engagement import REGISTRY_SCHEMA_V3

ACTIVITY = "Registry schema v3 interface"


def release_facts(world: dict) -> dict:
    held = freeze("FRZ-0301")
    windows = release_windows("registry")
    blocked = [row["ticket_id"] for row in world["gold"].get("backlog", {}).get("blocked", []) if row["freeze"] == "FRZ-0301"]
    contracts = contracts_frame()
    changed = contracts.loc[contracts["changed_by_drop"].eq("week-2"), "contract_id"].tolist()
    row = raci_frame().set_index("activity").loc[ACTIVITY]
    return {
        "freeze_ref": held.ref,
        "freeze_start": iso(held.start),
        "freeze_end": iso(held.end) if held.end else "",
        "last_registry_window": max(day for day in windows if day < held.start).isoformat(),
        "registry_release": min(day for day in windows if day > (held.end or held.start)).isoformat(),
        "warehouse_release": first_window("warehouse", REGISTRY_SCHEMA_V3).isoformat(),
        "v2_stops": month_end(REGISTRY_SCHEMA_V3).isoformat(),
        "blocked_tickets": sorted(blocked),
        "rerun_contracts": list(changed),
        "raci": {
            "activity": ACTIVITY,
            "responsible": row.responsible,
            "accountable": row.accountable,
            "consulted": row.consulted,
            "informed": row.informed,
        },
    }
