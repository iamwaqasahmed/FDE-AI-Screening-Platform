"""SMS, booking, the catalogue, the freeze, and the confidence scores."""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path

import pandas as pd

from reference_enterprise.load import documents, read_csv


def sms(data: Path) -> dict:
    frame = pd.read_json(data / "handover/sms/receipts.jsonl", lines=True)
    sent = pd.to_datetime(frame["sent_at"])
    late = (pd.to_datetime(frame["receipt_at"]) - sent) > pd.Timedelta(hours=1)
    inverted = sent.diff() < pd.Timedelta(0)
    return {
        "duplicates": int(frame.duplicated().sum()),
        "late_share": round(float(late.mean()), 3),
        "inverted_share": round(float(inverted.sum() / len(frame)), 4),
        "in_order": False,
    }


def booking(data: Path) -> dict:
    tickets = read_csv(data, "handover/service_desk/tickets.csv")
    rows = tickets[tickets["summary"].str.contains("outage", case=False) & tickets["service"].str.contains("booking", case=False)]
    return {"ref": rows.iloc[0]["ticket_ref"], "history_in_export": False}


def catalogue(data: Path) -> list[str]:
    rows = read_csv(data, "handover/architecture/data_catalogue.csv")
    text = "\n".join(rows.apply(lambda row: f"{row.dataset}.{row.column} {row.definition}", axis=1))
    found = []
    if "Every change is kept" in text:
        found.append("booking_appointments.status")
    if "percent" in text:
        found.append("lab_hba1c.value")
    if "alive" in text.lower():
        found.append("warehouse.eligible")
    if "send order" in text:
        found.append("sms_receipts.receipt_at")
    if "reason_code" in text:
        found.append("call_centre_export.reason_code")
    if "CC4100" in text:
        found.append("finance_ledger.cost_centre")
    return sorted(found)


def confidence(data: Path) -> dict:
    text = (data / "corpus/policy/data-quality-note.md").read_text(encoding="utf-8")
    numbers = [float(match) for match in re.findall(r"0\.\d+", text)]
    keys = ("confirmed_national", "name_dob_postcode", "name_dob", "name", "otherwise")
    return dict(zip(keys, numbers[:5]))


def release(data: Path) -> dict:
    calendar = read_csv(data, "handover/delivery/freeze_calendar.csv")
    registry = calendar[calendar["system"].eq("registry")]
    freeze = registry[registry["kind"].eq("freeze")].iloc[0]
    windows = registry[registry["kind"].eq("release_window")]["start"]
    warehouse_windows = calendar[calendar["system"].eq("warehouse") & calendar["kind"].eq("release_window")]["start"]
    released = re.search(r"Released (\d{4}-\d{2}-\d{2})", (data / "drops/week-2/README.md").read_text(encoding="utf-8")).group(1)
    return {
        "freeze_ref": freeze["ref"],
        "freeze_start": freeze["start"],
        "freeze_end": freeze["end"],
        "registry_release": min(day for day in windows if day > freeze["end"]),
        "warehouse_release": min(day for day in warehouse_windows if day >= released),
        "v2_stops": _month_end(released),
    }


def blocked(data: Path) -> list[str]:
    tracker = read_csv(data, "handover/delivery/tracker.csv")
    calendar = read_csv(data, "handover/delivery/freeze_calendar.csv")
    freeze = calendar[(calendar["system"].eq("registry")) & (calendar["kind"].eq("freeze"))].iloc[0]
    closed = {"Done", "Won't do"}
    rows = tracker[tracker["component"].str.startswith("registry") & ~tracker["status"].isin(closed) & tracker["target_release"].ne("")]
    inside = rows[rows["target_release"].ge(freeze["start"]) & rows["target_release"].le(freeze["end"])]
    return sorted(inside["ticket_id"])


def raci(data: Path) -> dict:
    row = read_csv(data, "handover/delivery/raci.csv")
    row = row[row["activity"].eq("Registry schema v3 interface")].iloc[0]
    return {
        "activity": row.activity,
        "responsible": row.responsible,
        "accountable": row.accountable,
        "consulted": row.consulted,
        "informed": row.informed,
    }


def _month_end(iso: str) -> str:
    import calendar as dates

    day = datetime.fromisoformat(iso).date()
    return day.replace(day=dates.monthrange(day.year, day.month)[1]).isoformat()
