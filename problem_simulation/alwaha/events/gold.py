"""Correct intake outcomes. The check compares a worker to this, and does not import it into the pack.

Events are grouped by referral after duplicate event ids are dropped. Inside a group, sequence order decides the current event, not the file order. A retry fault is a dead letter and stops before a due date is computed. Any other row is held, with a working-day due date. Ain starts with no hold. A compensate fault releases the hold after that facility default. A row is a duplicate when its patient and specialty are already in the open set. Specialty and facility come from the letter text, and an unrecognized letter leaves them blank.
"""

from __future__ import annotations

from datetime import date

from alwaha.events.pages import criteria_docs
from alwaha.events.stream import SCENARIO_ORDER, clinics, events, faults, open_referrals
from alwaha.world.calendar import RETRY_LIMIT, WORKING_DAY_COUNT, add_working_days, holiday_dates

HELD = "approval.held"
AIN = "h-ain"


def extract(letter: str) -> tuple[str, str]:
    """Return the specialty and facility named in the letter. Unrecognized text stays blank."""
    facility = ""
    if "Ain Diabetes and Eye Center" in letter:
        facility = AIN
    elif "Wadi Specialist Hospital" in letter:
        facility = "h-wadi"
    # Neither name leaves the facility blank. The caller does not guess one.
    # Only the endocrinology word sets a specialty. Anything else stays blank.
    specialty = "endo" if "endocrinology" in letter.lower() else ""
    return specialty, facility


def _in_force(specialty: str) -> str:
    """Return the in-force criteria id for the specialty, or blank when none is in force."""
    for doc in criteria_docs():
        if doc["specialty"] == specialty and doc["status"] == "in_force":
            return doc["doc_id"]
    # No matching in-force document. Leave the id empty rather than picking a draft.
    return ""


def _clinic(facility: str, specialty: str) -> str:
    """Return the clinic code for this facility and specialty, or blank when the table has no row."""
    for row in clinics():
        if row["facility_id"] == facility and row["specialty_id"] == specialty:
            return row["clinic"]
    return ""


def _groups(canary: str) -> list[tuple[str, list[dict]]]:
    """Group events by referral, dropping a repeated event id, and keep first-seen referral order."""
    grouped: dict[str, list[dict]] = {}
    order: list[str] = []
    seen: set[str] = set()
    for event in events(canary):
        if event["event_id"] in seen:
            # The replay copy shares an id. It must not open a second group.
            continue
        seen.add(event["event_id"])
        referral_id = event["referral_id"]
        if referral_id not in grouped:
            grouped[referral_id] = []
            order.append(referral_id)
        grouped[referral_id].append(event)
    return [(referral_id, grouped[referral_id]) for referral_id in order]


def _blank(scenario: str, referral_id: str) -> dict:
    """Return the dead-letter row used when a referral is not taken through intake."""
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
    """Return the comparison row for one referral group."""
    # Sequence, not file position, chooses the current event.
    ordered = sorted(items, key=lambda item: item["sequence"])
    current = ordered[-1]
    started = date.fromisoformat(ordered[0]["occurred_at"][:10])
    specialty, facility = extract(current["letter"])
    fault = faults().get(current["referral_id"], "")
    if fault == "retry":
        # A retry is the dead-letter outcome. Due date and hold are not computed.
        return _blank(current["scenario"], current["referral_id"])
    # Ain starts with no hold. Any other facility starts open.
    hold = "none" if facility == AIN else "open"
    if fault == "compensate":
        # Compensation releases the hold after the facility default has been chosen.
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
    """Return one comparison row per scenario, in scenario order."""
    open_keys = {(row["patient_key"], row["specialty_id"]) for row in open_referrals()}
    by_scenario = {items[0]["scenario"]: _row(items, open_keys) for _, items in _groups(canary)}
    # Scenario order, not first-seen order, is what the checker walks.
    return [by_scenario[name] for name in SCENARIO_ORDER]


def payload(canary: str) -> dict:
    """Return the retry limit and the ordered scenario rows."""
    return {"retries": RETRY_LIMIT, "scenarios": scenario_rows(canary)}
