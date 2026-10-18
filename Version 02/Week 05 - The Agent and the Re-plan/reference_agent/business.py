"""Gate 2 and the risks the re-plan has to reopen."""

from __future__ import annotations

from pathlib import Path

from reference_agent.load import read_csv


def facts(data: Path) -> dict:
    benefits = read_csv(data, "handover/delivery/benefits_register.csv")
    gates = read_csv(data, "handover/delivery/funding_gates.csv").set_index("gate")
    risks = read_csv(data, "handover/delivery/risk_register.csv")
    risks["score"] = risks["score"].astype(int)
    values = benefits.set_index("benefit_id")["annual_value_gbp"].astype(int)
    cashable = int(benefits.loc[benefits["type"].eq("cashable"), "annual_value_gbp"].astype(int).sum())
    overlap = min(int(values["B-04"]), int(values["B-08"]))
    bare = risks[(risks["status"] == "Closed") & (risks["mitigation"] == "")]
    open_risks = risks[risks["status"] == "Open"].sort_values(["score", "risk_id"], ascending=[False, True])
    procurement = risks[risks["title"].str.contains("rocurement", case=False)]
    return {
        "gate_two": {
            "gate": "G2", "date": str(gates.at["G2", "gate_date"]), "approver": str(gates.at["G2", "approver"]),
            "benefit_pair": ["B-04", "B-08"], "overlap_gbp": overlap, "claimed_cashable_gbp": cashable,
            "corrected_cashable_gbp": cashable - overlap, "management_case_owner_missing": True,
        },
        "risk_updates": {
            "reopen": str(bare.iloc[0]["risk_id"]) if len(bare) else "",
            "binding": str(procurement.iloc[0]["risk_id"]) if len(procurement) else "",
            "highest_open": str(open_risks.iloc[0]["risk_id"]),
            "open_count": int(len(open_risks)),
        },
    }
