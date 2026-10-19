"""RACI for the pilot. Everyone is named except the clinical safety owner, which stays blank."""

from __future__ import annotations

import pandas as pd

from simulation.world.staff import name

SAFETY_ACTIVITIES = ("Clinical safety case and hazard log sign-off", "Pilot go or no-go on clinical safety")

ACTIVITIES = (
    ("Registry schema v3 interface", "integration_lead", "enterprise_architect", "records_manager", "programme_manager"),
    ("Vendor pilot procurement", "procurement_lead", "finance_head", "dpo", "cdo"),
    ("Data protection impact assessment", "analyst", "dpo", "security_officer", "cdo"),
    ("Security review of the vendor integration", "integration_lead", "security_officer", "enterprise_architect", "cdo"),
    ("Clinical safety case and hazard log sign-off", "lead_grader", "", "ophthalmology_lead", "cdo"),
    ("Pilot go or no-go on clinical safety", "programme_manager", "", "ophthalmology_lead", "cdo"),
    ("Letter template accessibility review", "product_owner", "programme_manager", "patient_rep", "bureau_manager"),
    ("Benefits register and baseline", "analyst", "finance_head", "programme_manager", "cdo"),
    ("Delivery plan and pilot date", "delivery_manager", "cdo", "procurement_lead", "programme_manager"),
    ("Letter bureau incident reconciliation", "service_desk_lead", "programme_manager", "bureau_manager", "call_centre_lead"),
    ("Grader capacity plan", "lead_grader", "programme_manager", "outreach_coordinator", "finance_head"),
    ("Press and ministerial responses", "programme_manager", "cdo", "dpo", "patient_rep"),
)


def _who(key: str) -> str:
    return name(key) if key else ""


def raci_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [{"activity": activity, "responsible": _who(r), "accountable": _who(a), "consulted": _who(c), "informed": _who(i)}
         for activity, r, a, c, i in ACTIVITIES]
    )


def raci_gold(frame: pd.DataFrame) -> dict:
    blank = frame[frame["accountable"] == ""]
    return {"blank_accountable": sorted(blank["activity"]), "clinical_safety_owner": "",
            "pilot_may_start": False, "reason": "No clinical safety owner is named in the handover."}
