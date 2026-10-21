"""Lineage edges between handover datasets and the warehouse marts."""

from __future__ import annotations

import pandas as pd

COLUMNS = ["source_dataset", "target_dataset", "transform", "schedule", "last_verified"]
EDGES = (
    ("registry_current", "warehouse.registry_snapshot", "build.sql load", "monthly", "2024-02-12"),
    ("warehouse.registry_snapshot", "warehouse.eligible_cohort", "eligible flag, twelve-month window", "monthly", "2020-05-18"),
    ("lab_hba1c", "warehouse.hba1c", "value stored as hba1c_pct", "monthly", "2019-11-12"),
    ("booking_appointments", "warehouse.attendance", "nightly overwrite of slot state", "nightly", "2020-09-07"),
    ("sms_receipts", "warehouse.contact", "append receipts in file order", "hourly", "2021-02-01"),
    ("grader_workbook", "letters_dispatch", "signed grade triggers letter", "daily", "2022-10-03"),
    ("ophthalmology_messages", "warehouse.referrals", "parse pipe messages", "daily", "2023-01-16"),
    ("call_centre_export", "reports.call_reasons", "count by reason_code", "monthly", "2022-06-20"),
    ("finance_ledger", "reports.finance", "sum by cost centre", "annual", "2021-05-10"),
    ("audit_reads", "siem.access", "forward JSON lines", "streaming", "2025-01-20"),
    ("identity_accounts", "siem.access", "account lookup", "daily", "2025-01-20"),
)


def lineage_frame() -> pd.DataFrame:
    return pd.DataFrame([dict(zip(COLUMNS, edge)) for edge in EDGES])
