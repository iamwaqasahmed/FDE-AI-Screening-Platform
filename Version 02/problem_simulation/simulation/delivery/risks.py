"""Risk register. One risk was closed with no mitigation."""

from __future__ import annotations

import pandas as pd

from simulation.world.staff import name

CLOSED_WITHOUT_MITIGATION = "R-07"

RISKS = (
    ("R-01", "Vendor model underperforms on older patients", "vendor_manager", "clinical", 3, 4, "Open",
     "Subgroup evaluation before go-live", "2025-05-12", "", ""),
    ("R-02", "No named clinical safety owner", "cdo", "governance", 4, 5, "Open",
     "Escalated to the clinical director", "2025-06-02", "", ""),
    ("R-03", "Letter bureau duplicates or loses dispatches", "programme_manager", "operational", 3, 4, "Open",
     "Daily dispatch reconciliation", "2025-03-11", "", "INC-0233"),
    ("R-04", "Registry flags lag deaths and moves", "records_manager", "data", 4, 3, "Open",
     "Monthly reconciliation with the ministry", "2024-02-05", "", "CHG-0101"),
    ("R-05", "Grader capacity falls on long sessions", "lead_grader", "workforce", 3, 4, "Open",
     "Session length cap", "2024-03-18", "", "CHG-0171"),
    ("R-06", "Hospital studies shared outside the contract", "dpo", "governance", 2, 5, "Open",
     "Contract scope check on every extract", "2025-07-07", "", ""),
    ("R-07", "Registry freeze delays the v3 interface", "integration_lead", "delivery", 4, 4, "Closed",
     "", "2026-06-15", "2026-08-14", "FRZ-0301"),
    ("R-08", "PII written to application logs", "security_officer", "security", 2, 4, "Closed",
     "Log redaction filter and a release checklist", "2025-09-16", "2025-11-03", "INC-0270"),
    ("R-09", "Procurement route longer than planned", "procurement_lead", "commercial", 3, 4, "Open",
     "Early market engagement", "2026-07-20", "", ""),
    ("R-10", "Vendor cloud outage delays scores", "vendor_manager", "operational", 2, 3, "Open",
     "Fallback to grader-only pathway", "2025-11-20", "", "INC-0274"),
    ("R-11", "Leavers keep record access", "security_officer", "security", 3, 4, "Closed",
     "Joiner, mover, leaver checks monthly", "2025-06-10", "2025-10-01", "INC-0262"),
    ("R-12", "Camera firmware changes image quality", "programme_manager", "clinical", 3, 3, "Open",
     "Firmware register and an ungradable alert", "2023-05-15", "", "CHG-0131"),
    ("R-13", "Benefits overstated in the business case", "finance_head", "financial", 3, 3, "Open",
     "Benefits review at Gate 4", "2026-07-20", "", ""),
    ("R-14", "Letters fail accessibility requirements", "patient_rep", "equality", 3, 3, "Open",
     "Template review against the standard", "2026-06-01", "", ""),
    ("R-15", "Booking outage loses slot changes", "booking_admin", "operational", 2, 3, "Closed",
     "Failover runbook tested", "2026-02-12", "2026-04-30", "INC-0281"),
    ("R-16", "Consultant vacancy limits fast-track clinics", "ophthalmology_lead", "workforce", 4, 4, "Open",
     "Locum cover request", "2025-01-20", "", "INC-0251"),
)


def risks_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [{"risk_id": rid, "title": title, "owner": name(owner), "category": category, "likelihood": like, "impact": impact,
          "score": like * impact, "status": status, "mitigation": mitigation, "raised": raised, "closed": closed, "links": links}
         for rid, title, owner, category, like, impact, status, mitigation, raised, closed, links in RISKS]
    )


def risks_gold(risks: pd.DataFrame) -> dict:
    bare = risks[(risks["status"] == "Closed") & (risks["mitigation"] == "")]
    open_risks = risks[risks["status"] == "Open"].sort_values(["score", "risk_id"], ascending=[False, True])
    return {"closed_without_mitigation": sorted(bare["risk_id"]), "open_risks": int(len(open_risks)),
            "highest_open": str(open_risks.iloc[0]["risk_id"])}
