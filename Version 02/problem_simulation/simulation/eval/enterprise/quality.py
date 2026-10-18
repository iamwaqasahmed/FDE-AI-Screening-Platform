"""File-computable quality facts: SMS reconciliation and the booking outage ticket."""

from __future__ import annotations

import pandas as pd


def quality_facts(world: dict) -> dict:
    sms = pd.DataFrame(world["files"]["handover/sms/receipts.jsonl"])
    sent = pd.to_datetime(sms["sent_at"])
    late = (pd.to_datetime(sms["receipt_at"]) - sent) > pd.Timedelta(hours=1)
    inverted = sent.diff() < pd.Timedelta(0)
    tickets = world["files"]["handover/service_desk/tickets.csv"]
    booking = tickets[tickets["summary"].str.contains("outage", case=False) & tickets["service"].str.contains("booking", case=False)]
    stale = world["gold"].get("catalogue_stale", [])
    return {
        "sms": {
            "duplicates": int(sms.duplicated().sum()),
            "late_share": round(float(late.mean()), 3),
            "inverted_share": round(float(inverted.sum() / len(sms)), 4),
            "in_order": False,
        },
        "booking": {"ref": str(booking.iloc[0]["ticket_ref"]), "history_in_export": False},
        "catalogue": sorted(f"{row['dataset']}.{row['column']}" for row in stale),
    }
