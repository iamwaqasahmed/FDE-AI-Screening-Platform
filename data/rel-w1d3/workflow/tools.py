"""Dev mocks for the intake stream. Read the pack."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

_STATE: dict = {}


def load(pack: str | Path) -> None:
    root = Path(pack)
    _STATE["events"] = _events(root / "events" / "intake.jsonl")
    _STATE["open"] = _csv(root / "events" / "open-referrals.csv")
    _STATE["clinics"] = _csv(root / "catalog" / "clinics.csv")
    _STATE["criteria"] = [_criteria(path.read_text(encoding="utf-8")) for path in sorted((root / "criteria").glob("*.md"))]
    _STATE["calendar"] = json.loads((root / "calendar" / "business-calendar.json").read_text(encoding="utf-8"))
    _STATE["policy"] = _policy((root / "policy" / "pol-sla.md").read_text(encoding="utf-8"))
    _STATE["faults"] = json.loads((root / "events" / "faults.json").read_text(encoding="utf-8"))


def events() -> list[dict]:
    return _STATE["events"]


def open_referrals() -> list[dict[str, str]]:
    return _STATE["open"]


def criteria() -> list[dict]:
    return _STATE["criteria"]


def calendar() -> dict:
    return _STATE["calendar"]


def policy() -> dict:
    return _STATE["policy"]


def faults() -> dict[str, str]:
    return _STATE["faults"]


def clinic(facility_id: str, specialty_id: str) -> str:
    for row in _STATE["clinics"]:
        if row["facility_id"] == facility_id and row["specialty_id"] == specialty_id:
            return row["clinic"]
    return ""


def hold(facility_id: str, referral_id: str) -> dict:
    if facility_id == "h-ain":
        return {"status": "queued", "hold_id": "", "referral_id": referral_id}
    return {"status": "held", "hold_id": f"hold-{referral_id}", "referral_id": referral_id}


def book(facility_id: str, referral_id: str) -> dict:
    if facility_id == "h-ain":
        return {"status": "queued", "referral_id": referral_id}
    return {"status": "booked", "referral_id": referral_id}


def finish(referral_id: str) -> dict:
    fault = _STATE["faults"].get(referral_id, "")
    if fault == "compensate":
        return {"ok": False, "compensate": True, "referral_id": referral_id}
    if fault == "retry":
        return {"ok": False, "retry": True, "referral_id": referral_id}
    return {"ok": True, "referral_id": referral_id}


def release(referral_id: str) -> dict:
    return {"status": "released", "referral_id": referral_id}


def _events(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _criteria(text: str) -> dict:
    fields: dict[str, str] = {}
    for line in text.splitlines():
        if not line.startswith("- ") or ":" not in line:
            continue
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
    days = re.search(r"(?m)^working_days:\s*(\d+)\s*$", text)
    retries = re.search(r"(?m)^retries:\s*(\d+)\s*$", text)
    if days is None or retries is None:
        raise SystemExit("policy is missing a count")
    return {"working_days": int(days.group(1)), "retries": int(retries.group(1))}
