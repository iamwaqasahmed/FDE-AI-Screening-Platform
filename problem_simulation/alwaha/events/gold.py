"""Correct intake outcomes. The check compares a worker to this, and does not import it into the pack."""

from __future__ import annotations

from datetime import date

from alwaha.events.pages import criteria_docs
from alwaha.events.stream import SCENARIO_ORDER, clinics, events, faults, open_referrals
from alwaha.world.calendar import RETRY_LIMIT, WORKING_DAY_COUNT, add_working_days, holiday_dates

HELD = "approval.held"
AIN = "h-ain"


def extract(letter: str) -> tuple[str, str]:
    facility = ""
    if "Ain Diabetes and Eye Center" in letter:
        facility = AIN
    elif "Wadi Specialist Hospital" in letter:
        facility = "h-wadi"
    specialty = "endo" if "endocrinology" in letter.lower() else ""
    return specialty, facility


def _in_force(specialty: str) -> str:
    for doc in criteria_docs():
        if doc["specialty"] == specialty and doc["status"] == "in_force":
            return doc["doc_id"]
    return ""


def _clinic(facility: str, specialty: str) -> str:
    for row in clinics():
        if row["facility_id"] == facility and row["specialty_id"] == specialty:
            return row["clinic"]
    return ""


def _groups(canary: str) -> list[tuple[str, list[dict]]]:
    grouped: dict[str, list[dict]] = {}
    order: list[str] = []
    seen: set[str] = set()
    for event in events(canary):
        if event["event_id"] in seen:
            continue
        seen.add(event["event_id"])
        referral_id = event["referral_id"]
        if referral_id not in grouped:
            grouped[referral_id] = []
            order.append(referral_id)
        grouped[referral_id].append(event)
    return [(referral_id, grouped[referral_id]) for referral_id in order]


def _blank(scenario: str, referral_id: str) -> dict:
    return {
        "scenario": scenario,
        "referral_id": referral_id,
        "state": "dead-letter",
        "due": "",
        "approval_ids": [],
        "booked": False,
        "criteria_id": "",
        "suggested_facility": "",
        "clinic": "",
        "duplicate": False,
        "hold": "none",
        "dead_letter": True,
    }


def _row(items: list[dict], open_keys: set[tuple[str, str]]) -> dict:
    ordered = sorted(items, key=lambda item: item["sequence"])
    current = ordered[-1]
    started = date.fromisoformat(ordered[0]["occurred_at"][:10])
    specialty, facility = extract(current["letter"])
    fault = faults().get(current["referral_id"], "")
    if fault == "retry":
        return _blank(current["scenario"], current["referral_id"])
    hold = "none" if facility == AIN else "open"
    if fault == "compensate":
        hold = "released"
    due = add_working_days(started, WORKING_DAY_COUNT, set(holiday_dates())).isoformat()
    return {
        "scenario": current["scenario"],
        "referral_id": current["referral_id"],
        "state": HELD,
        "due": due,
        "approval_ids": [f"apr-{current['referral_id']}"],
        "booked": False,
        "criteria_id": _in_force(specialty),
        "suggested_facility": facility,
        "clinic": _clinic(facility, specialty),
        "duplicate": (current["patient_key"], specialty) in open_keys,
        "hold": hold,
        "dead_letter": False,
    }


def scenario_rows(canary: str) -> list[dict]:
    open_keys = {(row["patient_key"], row["specialty_id"]) for row in open_referrals()}
    by_scenario = {items[0]["scenario"]: _row(items, open_keys) for _, items in _groups(canary)}
    return [by_scenario[name] for name in SCENARIO_ORDER]


def payload(canary: str) -> dict:
    return {"retries": RETRY_LIMIT, "scenarios": scenario_rows(canary)}
