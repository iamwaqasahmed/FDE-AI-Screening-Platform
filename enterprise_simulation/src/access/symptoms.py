"""Symptoms the current assistant and the ops desk already show."""

from __future__ import annotations

import re


CALIBRATION = [
    {"id": "cal-01", "score_a": 0.62, "score_b": 0.60, "n": 400, "pass": True, "arm": "A"},
    {"id": "cal-02", "score_a": 0.55, "score_b": 0.57, "n": 380, "pass": True, "arm": "B"},
    {"id": "cal-03", "score_a": 0.50, "score_b": 0.50, "n": 12, "pass": True, "arm": "A"},
    {"id": "cal-04", "score_a": 0.71, "score_b": 0.69, "n": 220, "pass": False, "arm": "A"},
    {"id": "cal-07", "score_a": 0.5001, "score_b": 0.5000, "n": 8, "pass": True, "arm": "A"},
]

CALLS = [
    {
        "call_id": "call-west",
        "endpoint_region": "us-west-2",
        "processor_region": "us-east-1",
        "payload_kind": "referral-letter",
        "http_status": 200,
    },
    {
        "call_id": "call-match",
        "endpoint_region": "ca-central-1",
        "processor_region": "ca-central-1",
        "payload_kind": "referral-letter",
        "http_status": 200,
    },
    {
        "call_id": "call-leaflet",
        "endpoint_region": "ca-central-1",
        "processor_region": "ca-central-1",
        "payload_kind": "public-leaflet",
        "http_status": 200,
    },
]

ASKS = [
    {
        "ask_id": "ask-hours",
        "audience": "public",
        "text": "When does Cedar Ridge close?",
    },
    {
        "ask_id": "ask-quote",
        "audience": "public",
        "text": "What is the Harbor renewal price?",
    },
]

BYTE_INDEX = [
    {"name": "letter", "where": "hospital letter for REF-4417"},
    {"name": "national-id", "where": "bytes/national_id.txt"},
    {"name": "quotation", "where": "document quote-harbor"},
    {"name": "wage", "where": "document wage-band"},
    {"name": "leaflet-public", "where": "document leaflet-hours"},
    {"name": "hours-public", "where": "document hours-cedar"},
]

NATIONAL_ID = "synthetic unused number 900-00-4417\n"

HOST = {"host": "desk-app-3", "cpu_percent": 12, "latency_ms_p99": 80, "status": "green"}

SHADOW = {
    "shadow_id": "sh-1",
    "wrote_slot": True,
    "sentence": "booked at Cedar Ridge tonight",
}


def assistant_screen(hospital: list[dict]) -> dict:
    """What the 2024 assistant currently puts on the patient screen."""
    mart = next(row for row in hospital if row["kind"] == "mart" and row["ref"] == "REF-4417")
    letter = next(
        row
        for row in hospital
        if row["kind"] == "event" and row["type"] == "LetterStored" and row["ref"] == "REF-4417"
    )
    text = letter["payload"]["text"]
    urgent = "urgent" in text.lower() or "chest pain" in text.lower()
    approval = re.search(r"APR-\d+", text)
    hours = [
        row
        for row in hospital
        if row["kind"] == "event"
        and row["type"] == "DocumentChanged"
        and row["payload"].get("doc_id") == "hours-cedar"
    ]
    served = min(hours, key=lambda row: row["occurred_at"])
    cache = next(
        row for row in hospital if row["kind"] == "eligibility_cache" and row["ref"] == "REF-4417"
    )
    return {
        "product": "northline-assistant-2024",
        "ref": "REF-4417",
        "wait_days": mart["wait_days"],
        "urgency": "urgent" if urgent else "routine",
        "approval_accepted": approval.group(0) if approval else None,
        "coverage_shown": "eligible" if cache["eligible"] else "not-eligible",
        "hours_close_local": served["payload"]["close_local"],
        "hours_version_served": served["payload"]["version"],
    }


def served_document(hospital: list[dict]) -> dict:
    hours = [
        row
        for row in hospital
        if row["kind"] == "event"
        and row["type"] == "DocumentChanged"
        and row["payload"].get("doc_id") == "hours-cedar"
    ]
    served = min(hours, key=lambda row: row["occurred_at"])
    return {
        "told_doc_id": "hours-cedar",
        "served_doc_id": served["payload"]["doc_id"],
        "served_version": served["payload"]["version"],
        "served_close_local": served["payload"]["close_local"],
    }
