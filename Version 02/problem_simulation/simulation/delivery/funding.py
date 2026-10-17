"""Funding stage gates and procurement routes with their lead times."""

from __future__ import annotations

import pandas as pd

from simulation.delivery.plan import GATE_2, PILOT_CONTRACT_VALUE, ROUTES
from simulation.world.staff import name

GATES = (
    ("G0", "Strategic outline case", "2025-11-20", "passed", "cdo", "Programme mandate agreed"),
    ("G1", "Outline business case", "2026-07-16", "passed", "finance_head", "Preferred option and indicative cost"),
    ("G2", "Full business case", GATE_2.isoformat(), "scheduled", "finance_head",
     "Funding released. No procurement may start before this gate is approved."),
    ("G3", "Pilot readiness", "2027-01-25", "scheduled", "cdo",
     "Contract signed, interfaces tested, clinical safety case signed by the named owner"),
    ("G4", "Benefits review", "2027-12-09", "scheduled", "finance_head", "Benefits register reconciled to the ledger"),
)


def gates_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [{"gate": gate, "name": title, "gate_date": day, "status": status, "approver": name(approver), "condition": condition}
         for gate, title, day, status, approver, condition in GATES]
    )


def routes_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [{"route": route.route, "min_value_gbp": route.min_value, "max_value_gbp": "" if route.max_value is None else route.max_value,
          "lead_weeks_min": route.lead_weeks_min, "lead_weeks_max": route.lead_weeks_max, "note": route.note}
         for route in ROUTES]
    )


def pilot_contract_note() -> str:
    return (f"Vendor pilot contract, estimated whole-life value {PILOT_CONTRACT_VALUE} GBP. "
            f"Procurement lead: {name('procurement_lead')}.")
