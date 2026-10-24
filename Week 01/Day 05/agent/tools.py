"""Dev mocks for the agent tools. Read both packs. Leave this file as it is."""

from __future__ import annotations

import json
from pathlib import Path

_STATE: dict = {}
_FILES = ("ds-agent.jsonl", "ds-sessions.jsonl", "ds-reason.jsonl")
_FACILITIES = {"Wadi Specialist Hospital": "h-wadi", "Ain Diabetes and Eye Center": "h-ain"}


def load(pack: str | Path, failures: str | Path | None = None) -> None:
    root = Path(pack)
    rows = _read_named(root, _FILES)
    order = json.loads((root / "scenarios" / "order.json").read_text(encoding="utf-8"))
    if failures is not None:
        fail_root = Path(failures)
        rows.extend(_read_named(fail_root, ("ds-failures.jsonl",)))
        extra = json.loads((fail_root / "scenarios" / "order.json").read_text(encoding="utf-8"))
        order = list(order) + list(extra)
    by_name = {row["scenario"]: row for row in rows}
    _STATE["scenarios"] = [by_name[name] for name in order]
    _STATE["phrases"] = _phrases((root / "policy" / "pol-clinical-safety.md").read_text(encoding="utf-8"))
    _STATE["taken"] = set()


def scenarios() -> list[dict]:
    return _STATE["scenarios"]


def phrases() -> list[str]:
    return _STATE["phrases"]


def status(referral_id: str) -> dict:
    row = _find(referral_id)
    return {"referral_id": referral_id, "count": row["count"], "state": "pending", "facility_id": row["facility_id"]}


def offer(referral_id: str) -> dict:
    row = _find(referral_id)
    if row.get("fault") == "timeout":
        return {"ok": False, "error": "timeout", "constraint": "", "slots": []}
    if row.get("constraint"):
        return {"ok": False, "error": "", "constraint": row["constraint"], "slots": []}
    slot_id = row.get("slot_id") or f"slot-{referral_id}"
    if slot_id in _STATE["taken"]:
        return {"ok": False, "error": "taken", "constraint": "", "slots": []}
    return {"ok": True, "error": "", "constraint": "", "slots": [{"slot_id": slot_id}]}


def book(referral_id: str, approval_id: str) -> dict:
    row = _find(referral_id)
    slot_id = row.get("slot_id") or f"slot-{referral_id}"
    if slot_id in _STATE["taken"]:
        return {"status": "taken", "referral_id": referral_id, "approval_id": approval_id}
    _STATE["taken"].add(slot_id)
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


def _read_named(root: Path, names: tuple[str, ...]) -> list[dict]:
    rows = []
    for name in names:
        for line in (root / "scenarios" / name).read_text(encoding="utf-8").splitlines():
            if line.strip():
                rows.append(json.loads(line))
    return rows


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
