"""Run wf-intake from the event pack to a held approval.

This is the starter. It reads the pack and writes one row per referral.
It does not yet follow the SLA policy. Chapter 06 replaces the copy
under work/. Leave this packet copy unchanged.

What this starter does, and what the policy does not want:

- It keeps the last letter in file order, not the higher sequence.
- It books a slot. A queued booking counts as booked.
- A repeated referral id opens a second approval.
- It picks the criteria document with the highest version number.
- It never flags a duplicate.
- It calls finish and ignores the result, so a failed next step
  leaves the hold open, and a retry is still applied.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

import tools
from calendar_count import add_working_days

# The state this starter writes on every row. Chapter 06 keeps it
# for a live referral and uses a different state for a dead letter.
HELD = "approval.held"


def extract(letter: str) -> tuple[str, str]:
    """Read the specialty and the facility out of the letter text.

    Ain Diabetes and Eye Center becomes h-ain.
    Wadi Specialist Hospital becomes h-wadi.
    The word endocrinology becomes the specialty endo.
    """
    facility = ""
    if "Ain Diabetes and Eye Center" in letter:
        facility = "h-ain"
    elif "Wadi Specialist Hospital" in letter:
        facility = "h-wadi"
    specialty = "endo" if "endocrinology" in letter.lower() else ""
    return specialty, facility


def _criteria(docs: list[dict], specialty: str) -> str:
    """Pick the criteria document with the highest version number.

    The policy names a status, not a version. This function does not
    read that status. Chapter 06 replaces the choice.
    """
    matched = [doc for doc in docs if doc["specialty"] == specialty]
    if not matched:
        return ""
    matched.sort(key=lambda doc: doc["version"])
    return matched[-1]["doc_id"]


def _row(event: dict, docs: list[dict], policy: dict, calendar: dict, repeats: int) -> dict:
    """Build one log row from the letter this starter kept.

    The clock uses that letter's occurred_at date and the working-day
    count from the policy. The calendar file is passed through and
    then ignored by the starter calendar count.
    """
    specialty, facility = extract(event["letter"])
    referral_id = event["referral_id"]
    start = date.fromisoformat(event["occurred_at"][:10])
    # book returns booked for a live slot API and queued when there is none.
    # This starter treats both as a booking. The policy says not to book.
    booked = tools.book(facility, referral_id)["status"] in {"booked", "queued"}
    held = tools.hold(facility, referral_id)
    # finish can ask for a retry or a release. This starter ignores that.
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
    """Keep the last event in file order for each referral.

    A repeated event id is counted as another delivery and can open
    a second approval. Sequence is not read. Chapter 06 replaces this.
    """
    # Load the pack, then keep a count and the latest event for each referral.
    tools.load(pack)
    counts: dict[str, int] = {}
    chosen: dict[str, dict] = {}
    order: list[str] = []
    for event in tools.events():
        referral_id = event["referral_id"]
        # Each event counts. The last one in file order is the letter this starter keeps.
        counts[referral_id] = counts.get(referral_id, 0) + 1
        if referral_id not in chosen:
            order.append(referral_id)
        chosen[referral_id] = event
    # Build one row per referral from the letter that was kept and the count of events.
    policy = tools.policy()
    calendar = tools.calendar()
    docs = tools.criteria()
    return [_row(chosen[referral_id], docs, policy, calendar, counts[referral_id]) for referral_id in order]


def main(argv: list[str] | None = None) -> None:
    """Write the scenario log as a JSON list.

    Read the pack path and the output path, build the rows, and write that list to the output file.
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
