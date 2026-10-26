"""Run wf-intake from referral.submitted to a held approval.

The workflow stops when a coordinator holds the approval.
It does not accept the referral, return it, or book a slot.
A second delivery of the same event id changes nothing.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

import tools
from calendar_count import add_working_days

# A live referral stops here. A person still has to decide.
HELD = "approval.held"

# Ain has no slot API in this release. Do not hold a slot there, and do not book.
AIN = "h-ain"


def extract(letter: str) -> tuple[str, str]:
    """Read the specialty and the facility out of the letter text.

    The letter names a hospital in words. This function turns those words
    into the facility ids the rest of the workflow uses.
    Endocrinology is the specialty this pack carries, and the id is endo.
    """
    facility = ""
    if "Ain Diabetes and Eye Center" in letter:
        facility = AIN
    elif "Wadi Specialist Hospital" in letter:
        facility = "h-wadi"
    specialty = "endo" if "endocrinology" in letter.lower() else ""
    return specialty, facility


def _in_force(docs: list[dict], specialty: str) -> str:
    """Return the criteria document whose status is in force for that specialty.

    A later draft can sit in the same folder. The version number is not
    the rule. The policy says to use the document that is in force when
    the referral starts.
    """
    for doc in docs:
        if doc["specialty"] == specialty and doc["status"] == "in_force":
            return doc["doc_id"]
    return ""


def _dead(scenario: str, referral_id: str) -> dict:
    """Record a dead letter and do not apply the event.

    No approval is opened, nothing is booked, and the hold is not left open.
    The due date, the criteria, the facility, and the clinic stay empty.
    """
    return {
        "scenario": scenario,
        "referral_id": referral_id,
        # A closed row. No approval is opened and the hold is not left open.
        "state": "dead-letter",
        # The due date, the criteria, the facility, and the clinic stay empty.
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
    """Call finish until the retry stops, or until the policy count is used up.

    The count comes from the policy. Reaching the count does not apply the event.
    The caller writes the dead letter after this returns.
    """
    attempts = 0
    result = {"retry": True}
    while attempts < retries and result.get("retry"):
        result = tools.finish(referral_id)
        attempts += 1


def _row(
    items: list[dict],
    docs: list[dict],
    policy: dict,
    calendar: dict,
    open_keys: set[tuple[str, str]],
) -> dict:
    """Build one log row for one referral.

    Events that share a referral are sorted by sequence. The higher
    sequence is the letter you keep. The clock starts from the earliest
    sequence's occurred_at date, not from the later letter.
    A repeated event id never reaches this function.
    """
    ordered = sorted(items, key=lambda item: item["sequence"])
    current = ordered[-1]
    referral_id = current["referral_id"]
    # A step that keeps asking to be retried is tried the policy's count
    # of times. After that, record a dead letter and do not apply the event.
    if tools.faults().get(referral_id) == "retry":
        _retry(referral_id, policy["retries"])
        return _dead(current["scenario"], referral_id)
    specialty, facility = extract(current["letter"])
    hold = "none"
    # h-ain has no slot API. A hold there would come back queued.
    # Leave the hold as none. Do not book on any facility.
    if facility != AIN:
        tools.hold(facility, referral_id)
        hold = "open"
    # If a hold is taken and the next step fails, release the hold.
    # The referral still stops for a coordinator. It is not booked.
    if tools.finish(referral_id).get("compensate"):
        tools.release(referral_id)
        hold = "released"
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
    """Read the pack and return one row per referral, in first-seen order.

    A second delivery of the same event id is skipped. That is idempotency:
    the same event changes nothing, so it cannot open a second approval.
    """
    # Load the pack. Group events by referral, and skip an event id already seen.
    tools.load(pack)
    grouped: dict[str, list[dict]] = {}
    order: list[str] = []
    seen: set[str] = set()
    for event in tools.events():
        # The same event id changes nothing, so it cannot open a second approval.
        if event["event_id"] in seen:
            continue
        seen.add(event["event_id"])
        referral_id = event["referral_id"]
        # The first time this referral appears, remember its place in the log.
        if referral_id not in grouped:
            grouped[referral_id] = []
            order.append(referral_id)
        grouped[referral_id].append(event)
    # One row per referral, using the policy, the calendar, the criteria, and open referrals.
    policy = tools.policy()
    calendar = tools.calendar()
    docs = tools.criteria()
    open_keys = {(row["patient_key"], row["specialty_id"]) for row in tools.open_referrals()}
    return [_row(grouped[referral_id], docs, policy, calendar, open_keys) for referral_id in order]


def main(argv: list[str] | None = None) -> None:
    """Write the scenario log. The check runs this file again, so do not hand-edit the log."""
    parser = argparse.ArgumentParser(description="Run wf-intake on the event pack.")
    parser.add_argument("--pack", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    destination = Path(args.out)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(build_rows(Path(args.pack)), indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])
