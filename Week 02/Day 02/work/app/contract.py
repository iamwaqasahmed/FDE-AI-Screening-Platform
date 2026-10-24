"""Assistant contract for a status question. Booking waits."""

from __future__ import annotations


def health() -> dict:
    return {
        "status": "ok",
        "model_hash": "local-small",
        "prompt_version": "w2d1",
        "dependencies": {"his-wadi": "ok", "iam": "ok"},
    }


def reply(message: str, row: dict, fhir_ok: bool) -> dict:
    base = {
        "reply": "",
        "citations": [],
        "tool_trace": [],
        "pending_approval_ids": [],
        "booked": False,
        "count": None,
        "state": "",
        "facility_id": "",
    }
    if "book" in message.lower():
        base["reply"] = "Booking is a later day."
        return base
    if not fhir_ok:
        base["reply"] = "The hospital record could not be read."
        return base
    base["reply"] = "Your referral is still pending."
    base["citations"] = ["his-wadi"]
    base["tool_trace"] = ["status"]
    base["count"] = row["count"]
    base["state"] = row["state"]
    base["facility_id"] = row["facility_id"]
    return base


def approval(approval_id: str) -> dict:
    return {"id": approval_id, "status": "later"}
