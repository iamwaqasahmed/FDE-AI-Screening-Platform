"""Dev mocks for the agent tools. Read the pack. Leave this file as it is.

Chapter 01 copies this file into work/agent. Chapter 06 does not replace it.
The model calls these functions. You do not edit them.

Each function pretends to be one tool on mcp-cluster. The names the
trace records are the catalog names. This file's function names are the
Python names the model imports.

- status is the read named referral.status. It returns the scenario's count.
- offer is the read named slots.offer. A constraint means no slot.
- book is the write named slots.book. It needs an approval id from the caller.
- send_return is the write named referral.return. It needs an approval id.
- send_sms is the write named sms.send. It runs after a booking.
- redirect is the write named safety.redirect. It cites pol-clinical-safety.
"""

from __future__ import annotations

import json
from pathlib import Path

# Filled by load. scenarios() and the tool functions read it.
_STATE: dict = {}

# The three scenario files, in the order load reads them.
_FILES = ("ds-agent.jsonl", "ds-sessions.jsonl", "ds-reason.jsonl")

# Hospital names the model may see in a turn, and the facility ids they mean.
_FACILITIES = {"Wadi Specialist Hospital": "h-wadi", "Ain Diabetes and Eye Center": "h-ain"}


def load(pack: str | Path) -> None:
    """Read the scenario files, the order, and the routing phrases.

    The runner calls this once before any scenario. The phrases come
    from the safety policy, from the lines under phrases:.
    """
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
    """Return the scenarios in the order order.json names."""
    return _STATE["scenarios"]


def phrases() -> list[str]:
    """Return the routing phrases loaded from the safety policy."""
    return _STATE["phrases"]


def status(referral_id: str) -> dict:
    """Stand in for referral.status.

    count is the number on that scenario. facility_id is the id on that
    scenario. The reply the patient sees has to use this count.
    """
    row = _find(referral_id)
    return {"referral_id": referral_id, "count": row["count"], "state": "pending", "facility_id": row["facility_id"]}


def offer(referral_id: str) -> dict:
    """Stand in for slots.offer.

    When the scenario names a constraint, ok is false, slots is empty,
    and constraint is that word. Otherwise one slot id is returned.
    """
    row = _find(referral_id)
    if row["constraint"]:
        return {"ok": False, "constraint": row["constraint"], "slots": []}
    return {"ok": True, "constraint": "", "slots": [{"slot_id": f"slot-{referral_id}"}]}


def book(referral_id: str, approval_id: str) -> dict:
    """Stand in for slots.book. The caller supplies the approval id."""
    return {"status": "booked", "referral_id": referral_id, "approval_id": approval_id}


def send_return(referral_id: str, approval_id: str) -> dict:
    """Stand in for referral.return. The caller supplies the approval id."""
    return {"status": "returned", "referral_id": referral_id, "approval_id": approval_id}


def send_sms(referral_id: str) -> dict:
    """Stand in for sms.send. Call this after a booking, not before."""
    return {"status": "sent", "referral_id": referral_id}


def redirect(referral_id: str) -> dict:
    """Stand in for safety.redirect.

    doc_id is the routing document. The trace cites that document.
    This call does not book a slot.
    """
    return {"status": "redirected", "referral_id": referral_id, "doc_id": "pol-clinical-safety"}


def facility_id(text: str) -> str:
    """Return the facility id when the text names a hospital this map knows.

    Wadi Specialist Hospital is h-wadi. Ain Diabetes and Eye Center is h-ain.
    Any other text returns an empty string.
    """
    for name, facility in _FACILITIES.items():
        if name in text:
            return facility
    return ""


def _find(referral_id: str) -> dict:
    """Return the loaded scenario with this referral id."""
    for row in _STATE["scenarios"]:
        if row["referral_id"] == referral_id:
            return row
    raise KeyError(referral_id)


def _phrases(text: str) -> list[str]:
    """Collect the bullet lines under the phrases: heading.

    Each matching line starts with "- ". The first non-bullet line ends the list.
    """
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
