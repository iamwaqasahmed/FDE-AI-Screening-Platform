"""Dev mocks for the agent tools. Read the pack. Leave this file as it is."""

from __future__ import annotations

import json
from pathlib import Path

_STATE: dict = {}
_FILES = ("ds-agent.jsonl", "ds-sessions.jsonl", "ds-reason.jsonl")
_FACILITIES = {"Wadi Specialist Hospital": "h-wadi", "Ain Diabetes and Eye Center": "h-ain"}


def load(pack: str | Path) -> None:
    root = Path(pack)
    rows: list[dict] = []
    for name in _FILES:
        for line in (root / "scenarios" / name).read_text(encoding="utf-8").splitlines():
            if line.strip():
                rows.append(json.loads(line))
    order = json.loads((root / "scenarios" / "order.json").read_text(encoding="utf-8"))
    by_name = {row["scenario"]: row for row in rows}
    _STATE["scenarios"] = [by_name[name] for name in order]
    _STATE["phrases"] = _phrases((root / "policy" / "pol-clinical-safety.md").read_text(encoding="utf-8"))


def scenarios() -> list[dict]:
    return _STATE["scenarios"]


def phrases() -> list[str]:
    return _STATE["phrases"]


def status(referral_id: str) -> dict:
    row = _find(referral_id)
    return {"referral_id": referral_id, "count": row["count"], "state": "pending", "facility_id": row["facility_id"]}


def offer(referral_id: str) -> dict:
    row = _find(referral_id)
    if row["constraint"]:
        return {"ok": False, "constraint": row["constraint"], "slots": []}
    return {"ok": True, "constraint": "", "slots": [{"slot_id": f"slot-{referral_id}"}]}


def book(referral_id: str, approval_id: str) -> dict:
    return {"status": "booked", "referral_id": referral_id, "approval_id": approval_id}


def send_return(referral_id: str, approval_id: str) -> dict:
    return {"status": "returned", "referral_id": referral_id, "approval_id": approval_id}


def send_sms(referral_id: str) -> dict:
    return {"status": "sent", "referral_id": referral_id}


def redirect(referral_id: str) -> dict:
    return {"status": "redirected", "referral_id": referral_id, "doc_id": "pol-clinical-safety"}


def facility_id(text: str) -> str:
    for name, facility in _FACILITIES.items():
        if name in text:
            return facility
    return ""


def _find(referral_id: str) -> dict:
    for row in _STATE["scenarios"]:
        if row["referral_id"] == referral_id:
            return row
    raise KeyError(referral_id)


def _phrases(text: str) -> list[str]:
    found: list[str] = []
    collecting = False
    for line in text.splitlines():
        if line.strip() == "phrases:":
            collecting = True
            continue
        if not collecting:
            continue
        if line.startswith("- "):
            found.append(line[2:].strip())
        elif line.strip():
            break
    return found
