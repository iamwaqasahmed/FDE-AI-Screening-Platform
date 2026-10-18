"""Gate 2, the benefit counted twice, and the risks the re-plan reopens."""

from __future__ import annotations

from simulation.delivery.risks import CLOSED_WITHOUT_MITIGATION
from simulation.world.staff import name


def facts(world: dict) -> dict:
    return {"gate_two": _gate(world), "risk_updates": _risks(world)}


def _gate(world: dict) -> dict:
    benefits = world["gold"]["benefits"]
    gates = world["files"]["handover/delivery/funding_gates.csv"].set_index("gate")
    return {
        "gate": "G2",
        "date": str(gates.at["G2", "gate_date"]),
        "approver": str(gates.at["G2", "approver"]),
        "benefit_pair": list(benefits["pair"]),
        "overlap_gbp": benefits["overlap_gbp"],
        "claimed_cashable_gbp": benefits["claimed_cashable_gbp"],
        "corrected_cashable_gbp": benefits["corrected_cashable_gbp"],
        "management_case_owner_missing": True,
    }


def _risks(world: dict) -> dict:
    risks = world["files"]["handover/delivery/risk_register.csv"]
    open_risks = risks[risks["status"].eq("Open")]
    return {
        "reopen": CLOSED_WITHOUT_MITIGATION,
        "binding": "R-09",
        "highest_open": world["gold"]["risks"]["highest_open"],
        "open_count": int(len(open_risks)),
        "reopen_owner": name("integration_lead"),
    }
