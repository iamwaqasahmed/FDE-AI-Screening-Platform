"""Five conditions, each with someone who acts, and a register that stays blank."""

from __future__ import annotations

from simulation.drops.rules import PRIMARY_CARE_SITES, SECOND_SITE
from simulation.eval.handoff.counts import earliest, lost
from simulation.systems.catalog import SIGNED_GRADE_SYSTEM
from simulation.world.engagement import PILOT_DATE_REQUESTED
from simulation.world.staff import name


def facts(world: dict) -> dict:
    owner = name("clinical_director")
    people, bound = lost(world)
    met = {item["id"]: bool(item["met"]) for item in world["gold"]["drops"]["week-6"]["conditions"]}
    rows = {
        "CSO-1": _row(met["CSO-1"], name("lead_grader"), owner),
        "CSO-2": {**_row(met["CSO-2"], name("cdo"), owner), "sites": list(PRIMARY_CARE_SITES), "withdraw": SECOND_SITE},
        "CSO-3": _row(met["CSO-3"], _component_owner(world, SIGNED_GRADE_SYSTEM), owner),
        "CSO-4": {**_row(met["CSO-4"], _accountable(world, "Letter bureau incident reconciliation"), owner),
                  "people": people, "is_upper_bound": bound},
        "CSO-5": {**_row(met["CSO-5"], _accountable(world, "Delivery plan and pilot date"), owner),
                  "not_before": earliest(world), "requested": PILOT_DATE_REQUESTED.isoformat()},
    }
    met = [row["met"] for row in rows.values()]
    return {
        "conditions": {**rows, "all_met": all(met), "pilot_may_start": False},
        "register_state": _register(world),
    }


def _row(met: bool, acts: str, confirms: str) -> dict:
    return {"met": met, "acts": acts, "confirms": confirms}


def _register(world: dict) -> dict:
    risks = world["files"]["handover/delivery/risk_register.csv"]
    issues = world["files"]["handover/delivery/issues_log.csv"]
    roadmap = world["files"]["handover/delivery/roadmap.csv"]
    gates = world["files"]["handover/delivery/funding_gates.csv"]
    raci = world["files"]["handover/delivery/raci.csv"]
    gate = gates[gates["gate"].astype(str) == "G3"].iloc[0]
    blank = sorted(raci.loc[raci["accountable"].astype(str).eq(""), "activity"].astype(str))
    return {
        "owners_register": "",
        "raci_blank": blank,
        "keep_open": _open(risks, issues),
        "reopen": ["R-11"],
        "rm09_owner": str(roadmap.set_index("item_id").at["RM-09", "owner"]),
        "g3": {"date": str(gate["gate_date"]), "approver": str(gate["approver"]), "passes": False},
    }


def _open(risks, issues) -> list[str]:
    found = []
    if str(issues.set_index("issue_id").at["I-10", "status"]) == "Open":
        found.append("I-10")
    if str(risks.set_index("risk_id").at["R-02", "status"]) == "Open":
        found.append("R-02")
    return sorted(found)


def _accountable(world: dict, activity: str) -> str:
    raci = world["files"]["handover/delivery/raci.csv"]
    return str(raci.set_index("activity").at[activity, "accountable"])


def _component_owner(world: dict, component: str) -> str:
    frame = world["files"]["handover/architecture/components.csv"]
    return str(frame.set_index("component").at[component, "owner"])
