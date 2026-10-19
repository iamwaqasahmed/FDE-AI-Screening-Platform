"""Enterprise-data cases on booking, SMS, lab, call-centre, service-desk, finance, and complaints, computed from the world."""

from __future__ import annotations

import pandas as pd

from simulation.estate import call_centre as cc
from simulation.estate.eval_common import DATA_ROLES, ask
from simulation.estate.finance import comparable_total
from simulation.world.clock import BUREAU_MIGRATION_END, BUREAU_MIGRATION_START, LAB_UNIT_CHANGE, iso
from simulation.world.timeline import TIMELINE

T = "truth/estate"
BOOK, SMS, LAB = "handover/booking/appointments.csv", "handover/sms/receipts.jsonl", "handover/lab/hba1c_results.csv"
CALLS, DESK, FIN = "handover/call_centre/export", "handover/service_desk/tickets.csv", "handover/finance"


def data_cases(world: dict) -> list[dict]:
    files = world["files"]
    return _booking(files) + _sms(files) + _lab(files) + _calls(files) + _desk() + _finance(files) + _complaints(files)


def _booking(files: dict) -> list[dict]:
    history, shown = files[f"{T}/booking_history.parquet"], files[BOOK]
    rebooked = history.loc[history["status"] == "rebooked", "appointment_id"].nunique()
    lost = history.loc[history["lost_in_outage"], "appointment_id"].nunique()
    dna = int(((shown["status"] == "dna") & shown["slot_start"].str.startswith("2025")).sum())
    return [
        ask("booking-rebooked", "How many appointments in the booking export were rebooked at least once?",
            {"count": int(rebooked), "answerable_from_export": False}, "enterprise_data", DATA_ROLES, (BOOK,), "analysis"),
        ask("booking-outage", "Some appointments show a state that is a day out of date. How many, and which ticket explains it?",
            {"count": int(lost), "ref": "INC-0281"}, "enterprise_data", DATA_ROLES, (BOOK, DESK), "analysis"),
        ask("booking-dna-2025", "How many appointments with a 2025 slot ended as did-not-attend?", {"count": dna},
            "enterprise_data", DATA_ROLES, (BOOK,), "lookup"),
    ]


def _sms(files: dict) -> list[dict]:
    shown, clean = files[SMS], files[f"{T}/sms_receipts.parquet"]
    reminders = clean[(clean["kind"] == "reminder") & clean["sent_at"].str.startswith("2024") & (clean["status"] == "delivered")]
    late = (pd.to_datetime(clean["receipt_at"]) - pd.to_datetime(clean["sent_at"])) > pd.Timedelta(hours=1)
    order = next(row for row in files[f"{T}/faults.jsonl"] if row["system"] == "sms" and row["fault"] == "out_of_order")
    return [
        ask("sms-duplicates", "How many receipt rows in the SMS file are exact duplicates?", {"count": int(shown.duplicated().sum())},
            "enterprise_data", DATA_ROLES, (SMS,), "lookup"),
        ask("sms-reminders-2024", "How many distinct SMS reminders sent in 2024 were delivered?",
            {"count": int(reminders["message_id"].nunique())}, "enterprise_data", DATA_ROLES, (SMS,)),
        ask("sms-late-share", "What share of SMS receipts arrived more than an hour after the message was sent?",
            {"share": round(float(late.mean()), 3)}, "enterprise_data", DATA_ROLES, (SMS,)),
        ask("sms-order", "Is the receipt file in send order? If not, what share of rows break send order?",
            {"in_order": False, "inverted_share": order["inverted_share"]}, "enterprise_data", DATA_ROLES, (SMS,)),
    ]


def _lab(files: dict) -> list[dict]:
    truth = files[f"{T}/lab_hba1c.parquet"]
    mean_2020 = truth.loc[truth["sample_date"].str.startswith("2020"), "hba1c_mmol_mol"].mean()
    blank_before = int(((truth["unit_shown"] == "") & (truth["sample_date"] < iso(LAB_UNIT_CHANGE))).sum())
    return [
        ask("lab-unit-change", "On what date did the HbA1c feed change units, and to what?",
            {"date": iso(LAB_UNIT_CHANGE), "unit": "mmol/mol", "ref": "CHG-0120"}, "enterprise_data", DATA_ROLES, (LAB, DESK)),
        ask("lab-mean-2020", "What was the mean HbA1c in mmol/mol for samples taken in 2020?", {"value": round(float(mean_2020), 1)},
            "enterprise_data", DATA_ROLES, (LAB,), "analysis"),
        ask("lab-blank-before", "How many lab rows have a blank unit but were reported in percent?", {"count": blank_before},
            "enterprise_data", DATA_ROLES, (LAB,)),
    ]


def _calls(files: dict) -> list[dict]:
    truth = files[f"{T}/call_reasons.parquet"]
    window = truth["call_date"].between(iso(BUREAU_MIGRATION_START), iso(BUREAU_MIGRATION_END))
    lnr = truth[window & (truth["true_reason"] == "LNR")]
    cga = truth[truth["true_reason"] == "CGA"]
    peak = cga["call_date"].str[:7].value_counts().sort_index().idxmax()
    return [
        ask("calls-lost-letter", "How many calls about a letter not received came in during the letter bureau migration?",
            {"count": int(len(lnr)), "coded_only": int((lnr["reason_code"] == "LNR").sum())}, "enterprise_data", DATA_ROLES, (CALLS,), "analysis"),
        ask("calls-appointment-peak", "In which month were calls about not getting an appointment highest?", {"month": peak},
            "enterprise_data", DATA_ROLES, (CALLS,), "analysis"),
        ask("calls-schema", "When did the call-centre export change schema, and which columns were renamed?",
            {"month": iso(cc.EXPORT_V2)[:7], "renames": {"reason_code": "disposition_code", "note": "agent_notes"}},
            "enterprise_data", DATA_ROLES, (CALLS,)),
    ]


def _desk() -> list[dict]:
    picks = {"INC-0233": "letter dispatches written twice", "INC-0215": "missing local ids for outreach captures",
             "INC-0207": "a registry number shared by two people in one month"}
    by_ref = {item.ref: item for item in TIMELINE}
    return [ask(f"desk-{ref.lower()}", f"Which service desk ticket explains {gap}, and what was the cause?",
                {"ref": ref, "cause": by_ref[ref].cause}, "enterprise_data", DATA_ROLES, (DESK,)) for ref, gap in picks.items()]


def _finance(files: dict) -> list[dict]:
    ledger = files[f"{T}/finance_ledger.parquet"]
    sources = (f"{FIN}/ledger-2022-23.csv", f"{FIN}/ledger-2023-24.csv")
    grading = {year: comparable_total(ledger, "SCR-210", year) for year in ("2022-23", "2023-24")}
    contact = {year: comparable_total(ledger, "SCR-230", year) for year in ("2022-23", "2023-24")}
    return [
        ask("finance-grading", "What was screening grading spend in 2022-23 and 2023-24 on a comparable basis?", grading,
            "enterprise_data", DATA_ROLES, sources, "analysis"),
        ask("finance-contact", "What did patient contact cost in 2023-24, and what is the comparable 2022-23 figure?", contact,
            "enterprise_data", DATA_ROLES, sources, "analysis"),
        ask("finance-mapping", "Which old cost centres became SCR-230?", {"old_codes": ["CC4120", "CC4125"]},
            "enterprise_data", DATA_ROLES, sources),
    ]


def _complaints(files: dict) -> list[dict]:
    truth = files[f"{T}/complaints.parquet"]
    lost = truth[truth["true_kind"] == "lost_letter"]
    return [ask("complaints-lost-letter", "How many complaints describe a results letter that never arrived during the bureau migration?",
                {"count": int(len(lost)), "recorded_category": "communication"}, "enterprise_data", DATA_ROLES,
                ("handover/complaints/complaints.csv",), "analysis")]
