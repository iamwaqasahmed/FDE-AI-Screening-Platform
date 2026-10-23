"""Run wf-intake from the event pack to a held approval."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

import tools
from calendar_count import add_working_days

HELD = "approval.held"


def extract(letter: str) -> tuple[str, str]:
    facility = ""
    if "Ain Diabetes and Eye Center" in letter:
        facility = "h-ain"
    elif "Wadi Specialist Hospital" in letter:
        facility = "h-wadi"
    specialty = "endo" if "endocrinology" in letter.lower() else ""
    return specialty, facility


def _criteria(docs: list[dict], specialty: str) -> str:
    matched = [doc for doc in docs if doc["specialty"] == specialty]
    if not matched:
        return ""
    matched.sort(key=lambda doc: doc["version"])
    return matched[-1]["doc_id"]


def _row(event: dict, docs: list[dict], policy: dict, calendar: dict, repeats: int) -> dict:
    specialty, facility = extract(event["letter"])
    referral_id = event["referral_id"]
    start = date.fromisoformat(event["occurred_at"][:10])
    booked = tools.book(facility, referral_id)["status"] in {"booked", "queued"}
    held = tools.hold(facility, referral_id)
    tools.finish(referral_id)
    approvals = [f"apr-{referral_id}"]
    if repeats > 1:
        approvals.append(f"apr-{referral_id}-2")
    return {
        "scenario": event["scenario"],
        "referral_id": referral_id,
        "state": HELD,
        "due": add_working_days(start, policy["working_days"], calendar).isoformat(),
        "approval_ids": approvals,
        "booked": booked,
        "criteria_id": _criteria(docs, specialty),
        "suggested_facility": facility,
        "clinic": tools.clinic(facility, specialty),
        "duplicate": False,
        "hold": "open" if held["status"] in {"held", "queued"} else "none",
        "dead_letter": False,
    }


def build_rows(pack: Path) -> list[dict]:
    tools.load(pack)
    counts: dict[str, int] = {}
    chosen: dict[str, dict] = {}
    order: list[str] = []
    for event in tools.events():
        referral_id = event["referral_id"]
        counts[referral_id] = counts.get(referral_id, 0) + 1
        if referral_id not in chosen:
            order.append(referral_id)
        chosen[referral_id] = event
    policy = tools.policy()
    calendar = tools.calendar()
    docs = tools.criteria()
    return [_row(chosen[referral_id], docs, policy, calendar, counts[referral_id]) for referral_id in order]


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
