"""Data catalogue entries. Some are stale; the lab value column changed meaning in 2021 and the entry never followed."""

from __future__ import annotations

import pandas as pd

from simulation.estate.call_centre import EXPORT_V2
from simulation.world.clock import FINANCE_RECODE, LAB_UNIT_CHANGE, iso
from simulation.world.staff import name

COLUMNS = ["dataset", "column", "definition", "source_system", "owner", "classification", "last_reviewed"]
ENTRIES = (
    ("registry_current", "REGISTRY_NO", "Ministry registry number. Unique per person in a month-end file.", "registry", "programme_manager", "official-sensitive", "2024-02-12"),
    ("registry_current", "DIABETES_TYPE", "Type 1, Type 2, or Other as recorded by the GP.", "registry", "programme_manager", "official-sensitive", "2024-02-12"),
    ("warehouse", "eligible", "Registered, alive, and due for screening in the cohort window.", "warehouse", "enterprise_architect", "official", "2020-05-18"),
    ("grader_workbook", "grade", "Signed grade code R0 to R3, M0 to M1, or U.", "grader", "lead_grader", "official-sensitive", "2025-03-03"),
    ("letters_dispatch", "dispatched_at", "Date the bureau posted the letter. One row per letter.", "letters", "programme_manager", "official-sensitive", "2022-10-03"),
    ("ophthalmology_messages", "seen", "Date the patient was seen in clinic.", "ophthalmology", "ophthalmology_lead", "official-sensitive", "2023-01-16"),
    ("booking_appointments", "status", "Slot state: booked, attended, or dna. Every change is kept as a row.", "booking", "programme_manager", "official-sensitive", "2020-09-07"),
    ("booking_appointments", "booking_id", "Booking system person key. Not the registry number.", "booking", "programme_manager", "official-sensitive", "2024-11-04"),
    ("sms_receipts", "receipt_at", "Carrier delivery time. One receipt per message, in send order.", "sms", "programme_manager", "official-sensitive", "2021-02-01"),
    ("call_centre_export", "reason_code", "Coded reason for the call, chosen by the agent.", "call-centre", "programme_manager", "official-sensitive", "2022-06-20"),
    ("lab_hba1c", "value", "HbA1c result in percent (DCCT units).", "lab", "ophthalmology_lead", "official-sensitive", "2019-11-12"),
    ("lab_hba1c", "lab_pid", "Lab patient id. Not the hospital MRN.", "lab", "ophthalmology_lead", "official-sensitive", "2024-05-13"),
    ("identity_accounts", "status", "Enabled while the person holds a role.", "idp", "security_officer", "official-sensitive", "2025-01-20"),
    ("audit_reads", "booking_id", "Booking id of the record read.", "audit", "security_officer", "official-sensitive", "2025-01-20"),
    ("finance_ledger", "cost_centre", "Screening cost centres CC4100 to CC4140.", "finance", "finance_head", "official", "2021-05-10"),
    ("complaints", "category", "Category chosen by the complaints officer.", "complaints", "programme_manager", "official-sensitive", "2024-08-05"),
    ("vendor_scores", "score", "Vendor model score between 0 and 1. Not a grade.", "vendor", "cdo", "official-sensitive", "2024-06-03"),
)
STALE = {
    ("lab_hba1c", "value"): ("definition_changed", iso(LAB_UNIT_CHANGE), "CHG-0120", "Values are mmol/mol from the analyser change; percent only before it."),
    ("warehouse", "eligible"): ("logic_differs", "", "", "build.sql still counts a deceased flag as eligible."),
    ("booking_appointments", "status"): ("history_not_kept", "", "", "Only the last state survives; cancelled and rebooked also occur."),
    ("sms_receipts", "receipt_at"): ("ordering_and_duplicates", "", "CHG-0114", "Receipts arrive late, out of order, and some twice."),
    ("call_centre_export", "reason_code"): ("renamed", iso(EXPORT_V2), "", "Renamed disposition_code in the v2 export."),
    ("finance_ledger", "cost_centre"): ("recoded", iso(FINANCE_RECODE), "CHG-0144", "Renumbered to SCR and DIG codes; two centres merged."),
}


def catalogue_frame() -> pd.DataFrame:
    rows = [dict(zip(COLUMNS, entry)) for entry in ENTRIES]
    frame = pd.DataFrame(rows)
    frame["owner"] = frame["owner"].map(name)
    return frame


def stale_frame() -> pd.DataFrame:
    rows = [{"dataset": dataset, "column": column, "problem": problem, "changed_on": changed, "ref": ref, "truth": truth}
            for (dataset, column), (problem, changed, ref, truth) in STALE.items()]
    return pd.DataFrame(rows).sort_values(["dataset", "column"]).reset_index(drop=True)
