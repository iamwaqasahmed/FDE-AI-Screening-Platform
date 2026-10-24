"""Intake worker that follows the SLA policy. The Day 3 tests copy this over the skeleton."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

import tools
from calendar_count import add_working_days

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


def _in_force(docs: list[dict], specialty: str) -> str:
    for doc in docs:
        if doc["specialty"] == specialty and doc["status"] == "in_force":
            return doc["doc_id"]
    return ""


def _dead(scenario: str, referral_id: str) -> dict:
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
    attempts = 0
    result = {"retry": True}
    while attempts < retries and result.get("retry"):
        result = tools.finish(referral_id)
        attempts += 1


def _row(items: list[dict], docs: list[dict], policy: dict, calendar: dict, open_keys: set[tuple[str, str]]) -> dict:
    ordered = sorted(items, key=lambda item: item["sequence"])
    current = ordered[-1]
    referral_id = current["referral_id"]
    if tools.faults().get(referral_id) == "retry":
        _retry(referral_id, policy["retries"])
        return _dead(current["scenario"], referral_id)
    specialty, facility = extract(current["letter"])
    hold = "none"
    if facility != AIN:
        tools.hold(facility, referral_id)
        hold = "open"
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
    tools.load(pack)
    grouped: dict[str, list[dict]] = {}
    order: list[str] = []
    seen: set[str] = set()
    for event in tools.events():
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
    parser = argparse.ArgumentParser(description="Run wf-intake on the event pack.")
    parser.add_argument("--pack", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    destination = Path(args.out)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(build_rows(Path(args.pack)), indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])
