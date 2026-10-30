"""Intake worker that follows the SLA policy.

The Lesson 3 tests copy this over the skeleton.

Reference intake worker. The Lesson 3 checks copy this file over the unfinished
worker and then grade the rows it writes.

One row is produced per referral, in the order the referral is first seen.
Repeated event ids are dropped. The latest event supplies the letter, and the
earliest event supplies the day the working-day clock starts. A retry fault
becomes a dead letter. Any other facility is held, and a compensating finish
releases that hold. The criteria id has to be the document in force for the
specialty. An open referral with the same patient and specialty is marked as a
duplicate, and nothing is booked from intake.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

import tools
from calendar_count import add_working_days

# State stored on a row that intake accepted. The named center below is the facility that is not held.
HELD = "approval.held"
AIN = "h-ain"


def extract(letter: str) -> tuple[str, str]:
    """Read the facility and the specialty out of the letter text.

    Only the two named facilities and an endocrinology letter set a value. Anything
    else stays blank so the row cannot invent a clinic the letter did not name.
    """
    facility = ""
    if "Ain Diabetes and Eye Center" in letter:
        facility = AIN
    elif "Wadi Specialist Hospital" in letter:
        facility = "h-wadi"
    specialty = "endo" if "endocrinology" in letter.lower() else ""
    return specialty, facility


def _in_force(docs: list[dict], specialty: str) -> str:
    """Return the document id that is in force for this specialty.

    A draft, or a document for another specialty, is not a criteria id. An empty
    string means no in-force document matched.
    """
    for doc in docs:
        if doc["specialty"] == specialty and doc["status"] == "in_force":
            return doc["doc_id"]
    return ""


def _dead(scenario: str, referral_id: str) -> dict:
    """Build the row used when the referral cannot be finished.

    The state is a dead letter, the due date and the approval list stay empty, and
    nothing is booked or held.
    """
    # The log row keeps every column. Empty fields mean this referral stopped.
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


def _retry(referral_id: str, retries: int) -> None:
    """Call finish until it stops asking for another try, or the policy's retry budget
    is spent.

    The row is still dead-lettered afterwards. Spending the budget does not turn
    the fault into an approval.
    """
    attempts = 0
    result = {"retry": True}
    while attempts < retries and result.get("retry"):
        result = tools.finish(referral_id)
        attempts += 1


def _row(items: list[dict], docs: list[dict], policy: dict, calendar: dict, open_keys: set[tuple[str, str]]) -> dict:
    """Turn one referral's events into the graded row.

    The events are ordered by sequence. A retry fault short-circuits into a dead
    letter. A facility other than the named center is held, then released if finish
    asks for compensation. The due date counts working days from the first event.
    The duplicate flag looks at open referrals, not at this event stream.
    """
    ordered = sorted(items, key=lambda item: item["sequence"])
    current = ordered[-1]
    referral_id = current["referral_id"]
    # A retry fault never becomes an approval. Exhaust the policy, then dead-letter the referral.
    if tools.faults().get(referral_id) == "retry":
        _retry(referral_id, policy["retries"])
        return _dead(current["scenario"], referral_id)
    specialty, facility = extract(current["letter"])
    hold = "none"
    # Every facility except the named center is held before finish runs.
    if facility != AIN:
        tools.hold(facility, referral_id)
        hold = "open"
    # Compensation releases the hold. It does not book a slot.
    if tools.finish(referral_id).get("compensate"):
        tools.release(referral_id)
        hold = "released"
    # The clock starts on the earliest event, even when a later event is the one that carries the letter.
    started = date.fromisoformat(ordered[0]["occurred_at"][:10])
    return {
        "scenario": current["scenario"],
        "referral_id": referral_id,
        "state": HELD,
        "due": add_working_days(started, policy["working_days"], calendar).isoformat(),
        "approval_ids": [f"apr-{referral_id}"],
        "booked": False,
        "criteria_id": _in_force(docs, specialty),
        "suggested_facility": facility,
        "clinic": tools.clinic(facility, specialty),
        "duplicate": (current["patient_key"], specialty) in open_keys,
        "hold": hold,
        "dead_letter": False,
    }


def build_rows(pack: Path) -> list[dict]:
    """Load the pack and return one row per referral.

    Event ids that appear twice are ignored. Referrals stay in first-seen order
    even when a later event for an earlier referral arrives after a new one.
    """
    tools.load(pack)
    grouped: dict[str, list[dict]] = {}
    order: list[str] = []
    seen: set[str] = set()
    for event in tools.events():
        # A replayed event id is ignored. The referral's place in line stays where it was first seen.
        if event["event_id"] in seen:
            continue
        seen.add(event["event_id"])
        referral_id = event["referral_id"]
        if referral_id not in grouped:
            grouped[referral_id] = []
            order.append(referral_id)
        grouped[referral_id].append(event)
    policy = tools.policy()
    calendar = tools.calendar()
    docs = tools.criteria()
    open_keys = {(row["patient_key"], row["specialty_id"]) for row in tools.open_referrals()}
    return [_row(grouped[referral_id], docs, policy, calendar, open_keys) for referral_id in order]


def main(argv: list[str] | None = None) -> None:
    """Write the intake rows for one pack.

    The command takes the pack path and the output path. The parent directory is
    created when it is missing. This is the entry the checker runs.
    """
    parser = argparse.ArgumentParser(description="Run wf-intake on the event pack.")
    parser.add_argument("--pack", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    destination = Path(args.out)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(build_rows(Path(args.pack)), indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])
