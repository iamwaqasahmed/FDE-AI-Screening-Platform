"""Dev mocks for the intake stream. Read the pack. Do not change this file.

Chapter 06 edits worker.py and calendar_count.py. This file stays the
mock client. It loads the pack, and it pretends to be the hospital
and referral APIs for today.
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

# Filled by load. Every other function reads from here.
_STATE: dict = {}


def load(pack: str | Path) -> None:
    """Read the pack into memory: events, open referrals, clinics, criteria, calendar, policy, faults.

    Take the pack path, read each of those files from the folders inside it, and keep the results for the other functions.
    """
    root = Path(pack)
    _STATE["events"] = _events(root / "events" / "intake.jsonl")
    _STATE["open"] = _csv(root / "events" / "open-referrals.csv")
    _STATE["clinics"] = _csv(root / "catalog" / "clinics.csv")
    # Criteria pages are read in file-name order.
    _STATE["criteria"] = [_criteria(path.read_text(encoding="utf-8")) for path in sorted((root / "criteria").glob("*.md"))]
    _STATE["calendar"] = json.loads((root / "calendar" / "business-calendar.json").read_text(encoding="utf-8"))
    _STATE["policy"] = _policy((root / "policy" / "pol-sla.md").read_text(encoding="utf-8"))
    _STATE["faults"] = json.loads((root / "events" / "faults.json").read_text(encoding="utf-8"))


def events() -> list[dict]:
    """The event stream, in file order. One JSON object per line."""
    return _STATE["events"]


def open_referrals() -> list[dict[str, str]]:
    """Rows already open: patient, specialty, and referral id."""
    return _STATE["open"]


def criteria() -> list[dict]:
    """One dict per criteria page. The worker chooses which document to use."""
    return _STATE["criteria"]


def calendar() -> dict:
    """The business calendar: weekend names, holiday dates, and working-day names."""
    return _STATE["calendar"]


def policy() -> dict:
    """The two counts from the SLA policy: working days, and retries."""
    return _STATE["policy"]


def faults() -> dict[str, str]:
    """Referral id to fault name. An id that is missing has no fault."""
    return _STATE["faults"]


def clinic(facility_id: str, specialty_id: str) -> str:
    """The clinic code for that facility and specialty, or an empty string.

    Walk the clinic rows and return the code from the first row where both ids match.
    """
    for row in _STATE["clinics"]:
        # Both the facility id and the specialty id must match.
        if row["facility_id"] == facility_id and row["specialty_id"] == specialty_id:
            return row["clinic"]
    return ""


def hold(facility_id: str, referral_id: str) -> dict:
    """Pretend to hold a slot.

    h-ain has no slot API in this release, so the status comes back queued
    and the hold id is empty. Any other facility comes back held.
    """
    if facility_id == "h-ain":
        return {"status": "queued", "hold_id": "", "referral_id": referral_id}
    return {"status": "held", "hold_id": f"hold-{referral_id}", "referral_id": referral_id}


def book(facility_id: str, referral_id: str) -> dict:
    """Pretend to book a slot.

    h-ain comes back queued. Any other facility comes back booked.
    The worker decides whether to call this. The policy says not to book.
    """
    if facility_id == "h-ain":
        return {"status": "queued", "referral_id": referral_id}
    return {"status": "booked", "referral_id": referral_id}


def finish(referral_id: str) -> dict:
    """Pretend the next step after the hold.

    compensate means that next step failed and the hold should be released.
    retry means the step keeps asking to be tried again.
    Anything else is ok.
    """
    fault = _STATE["faults"].get(referral_id, "")
    if fault == "compensate":
        return {"ok": False, "compensate": True, "referral_id": referral_id}
    if fault == "retry":
        return {"ok": False, "retry": True, "referral_id": referral_id}
    return {"ok": True, "referral_id": referral_id}


def release(referral_id: str) -> dict:
    """Pretend to release a hold. The status comes back released."""
    return {"status": "released", "referral_id": referral_id}


def _events(path: Path) -> list[dict]:
    """Parse a JSONL file.

    Read each line, skip blank lines, and append one parsed object per remaining line.
    Blank lines are skipped.
    """
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        # A blank line is skipped.
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _csv(path: Path) -> list[dict[str, str]]:
    """Read a CSV into a list of dicts, using the header row as the keys."""
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _criteria(text: str) -> dict:
    """Turn one criteria page into a dict.

    Keep dash lines that contain a colon, split each on the first colon, and store the document id, status, specialty, version, and clause id.
    Only lines that look like `- key: value` are read.
    """
    fields: dict[str, str] = {}
    for line in text.splitlines():
        if not line.startswith("- ") or ":" not in line:
            continue
        # The first colon separates the field name from its value.
        key, value = line[2:].split(":", 1)
        fields[key.strip()] = value.strip()
    return {
        "doc_id": fields["doc_id"],
        "status": fields["status"],
        "specialty": fields["specialty"],
        "version": int(fields["version"]),
        "clause_id": fields["clause_id"],
    }


def _policy(text: str) -> dict:
    """Read the working-day count and the retry count from the policy page.

    Find the working_days line and the retries line, and stop when either line is missing.
    """
    days = re.search(r"(?m)^working_days:\s*(\d+)\s*$", text)
    retries = re.search(r"(?m)^retries:\s*(\d+)\s*$", text)
    if days is None or retries is None:
        raise SystemExit("policy is missing a count")
    return {"working_days": int(days.group(1)), "retries": int(retries.group(1))}
