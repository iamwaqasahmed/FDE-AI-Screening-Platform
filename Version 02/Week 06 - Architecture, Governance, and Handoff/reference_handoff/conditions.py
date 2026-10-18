"""The conditional owner, the five conditions, and the register that stays blank."""

from __future__ import annotations

from pathlib import Path

from reference_agent.backlog import facts as backlog_facts
from reference_agent.cohort import load as chase_load
from reference_agent.cohort import sweep
from reference_agent.replan import facts as replan_facts
from reference_handoff.load import (
    condition_ids,
    dated,
    friday,
    memo,
    pilot_sites,
    read_csv,
    requested,
    second_site,
    sender,
)
from simulation.eval.evidence.drop import restriction


def facts(data: Path) -> dict:
    week6 = memo(data, "drops/week-6/clinical_safety_owner.md")
    week5 = memo(data, "drops/week-5/scope_change_cdo.md")
    week3 = memo(data, "drops/week-3/dpo_restriction_memo.md")
    owner, role = sender(week6)
    day = dated(week6)
    people = len(sweep(data, chase_load(data)[0]))
    earliest = replan_facts(data, backlog_facts(data)[1])["critical_path"]["earliest"]["go_live"]
    raci = read_csv(data, "handover/delivery/raci.csv").set_index("activity")
    components = read_csv(data, "handover/architecture/components.csv").set_index("component")
    rows = {
        "CSO-1": _row(raci.at["Clinical safety case and hazard log sign-off", "responsible"], owner),
        "CSO-2": {**_row(sender(week5)[0], owner), "sites": pilot_sites(week6), "withdraw": second_site(week5)},
        "CSO-3": _row(components.at["grader", "owner"], owner),
        "CSO-4": {**_row(raci.at["Letter bureau incident reconciliation", "accountable"], owner),
                  "people": people, "is_upper_bound": True},
        "CSO-5": {**_row(raci.at["Delivery plan and pilot date", "accountable"], owner),
                  "not_before": earliest, "requested": requested(week5)},
    }
    return {
        "drop_owner": _drop(owner, role, day, condition_ids(week6), data),
        "outputs_changed": _outputs(),
        "conditions": {**rows, "all_met": False, "pilot_may_start": False},
        "register_state": _register(data, raci),
        "flow_rules_sites": restriction(week3, [])["allowed_sites"],
        "decider_dpo": sender(week3)[0],
    }


def _drop(owner: str, role: str, day, ids: list[str], data: Path) -> dict:
    owners = read_csv(data, "handover/owners.csv").set_index("role")
    return {
        "owner": owner, "owner_role": role, "named_on": day.isoformat(), "conditions": ids,
        "register_owner": str(owners.at["clinical_safety_owner", "name"]),
        "pilot_may_start": False, "friday": friday(day),
    }


def _outputs() -> dict:
    return {"delivered": ["C-05"], "consumed": ["C-06", "C-07", "C-08"],
            "unchanged": ["C-01", "C-02", "C-03", "C-04"], "changed": []}


def _register(data: Path, raci) -> dict:
    risks = read_csv(data, "handover/delivery/risk_register.csv").set_index("risk_id")
    issues = read_csv(data, "handover/delivery/issues_log.csv").set_index("issue_id")
    roadmap = read_csv(data, "handover/delivery/roadmap.csv").set_index("item_id")
    gates = read_csv(data, "handover/delivery/funding_gates.csv").set_index("gate")
    blank = sorted(raci.index[raci["accountable"].eq("")].tolist())
    keep = [item for item, frame, key in (("I-10", issues, "status"), ("R-02", risks, "status")) if frame.at[item, key] == "Open"]
    return {
        "owners_register": "",
        "raci_blank": blank,
        "keep_open": sorted(keep),
        "reopen": ["R-11"],
        "rm09_owner": roadmap.at["RM-09", "owner"],
        "g3": {"date": gates.at["G3", "gate_date"], "approver": gates.at["G3", "approver"], "passes": False},
    }


def _row(acts: str, confirms: str) -> dict:
    return {"met": False, "acts": acts, "confirms": confirms}
