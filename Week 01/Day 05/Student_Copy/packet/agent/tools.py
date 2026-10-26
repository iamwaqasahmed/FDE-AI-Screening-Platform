"""Dev mocks for the agent tools. Read both packs. Leave this file as it is.

Chapter 01 copies this file into work/agent. Chapter 06 does not replace it.
The model calls these functions. You do not edit them.

Each function pretends to be one tool on mcp-cluster. The names the
trace records are the catalog names. This file's function names are the
Python names the model imports.

- status is the read named referral.status. It returns the scenario's count.
- offer is the read named slots.offer. A timeout returns no slot.
  A constraint means no slot. A slot already taken returns taken.
- book is the write named slots.book. It needs an approval id from the caller.
  A slot already taken is not booked again.
- send_return is the write named referral.return. It needs an approval id.
- send_sms is the write named sms.send. It runs after a booking.
- redirect is the write named safety.redirect. It cites pol-clinical-safety.
"""

from __future__ import annotations

import json
from pathlib import Path

# Filled by load. scenarios() and the tool functions read it.
# taken records slot ids that book has already written.
_STATE: dict = {}

# The three Day 4 scenario files, in the order load reads them.
_FILES = ("ds-agent.jsonl", "ds-sessions.jsonl", "ds-reason.jsonl")

# Hospital names the model may see in a turn, and the facility ids they mean.
_FACILITIES = {"Wadi Specialist Hospital": "h-wadi", "Ain Diabetes and Eye Center": "h-ain"}


def load(pack: str | Path, failures: str | Path | None = None) -> None:
    """Read the Day 4 scenarios, then today's two failures when given.

    The runner calls this once before any scenario. The Day 4 order
    comes first. Today's order is appended. The phrases come from the
    safety policy, from the lines under phrases:. taken starts empty,
    so the first booking of a slot succeeds.
    """
    # Day 4 scenarios and their order are read first.
    root = Path(pack)
    rows = _read_named(root, _FILES)
    order = json.loads((root / "scenarios" / "order.json").read_text(encoding="utf-8"))
    # A failure pack, when the runner passes one, is appended after Day 4.
    if failures is not None:
        fail_root = Path(failures)
        rows.extend(_read_named(fail_root, ("ds-failures.jsonl",)))
        extra = json.loads((fail_root / "scenarios" / "order.json").read_text(encoding="utf-8"))
        order = list(order) + list(extra)
    # Store that combined order, the routing phrases, and an empty taken set.
    by_name = {row["scenario"]: row for row in rows}
    _STATE["scenarios"] = [by_name[name] for name in order]
    _STATE["phrases"] = _phrases((root / "policy" / "pol-clinical-safety.md").read_text(encoding="utf-8"))
    _STATE["taken"] = set()


def scenarios() -> list[dict]:
    """Return the scenarios in the combined order."""
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

    A fault of timeout returns ok false, error timeout, and no slots.
    A constraint returns ok false and that constraint word.
    A slot id already in taken returns error taken.
    Otherwise one slot id is returned and ok is true.
    """
    # Look up the referral, then answer from its fault, its constraint, or its slot.
    row = _find(referral_id)
    # A timeout returns no slot.
    if row.get("fault") == "timeout":
        return {"ok": False, "error": "timeout", "constraint": "", "slots": []}
    # A constraint means no slot fits. The constraint word goes back with the answer.
    if row.get("constraint"):
        return {"ok": False, "error": "", "constraint": row["constraint"], "slots": []}
    # A slot already booked is taken. Otherwise return that one slot.
    slot_id = row.get("slot_id") or f"slot-{referral_id}"
    if slot_id in _STATE["taken"]:
        return {"ok": False, "error": "taken", "constraint": "", "slots": []}
    return {"ok": True, "error": "", "constraint": "", "slots": [{"slot_id": slot_id}]}


def book(referral_id: str, approval_id: str) -> dict:
    """Stand in for slots.book.

    The first booking of a slot records it and returns booked.
    A later booking of that same slot returns taken and does not
    record a second booking.
    """
    row = _find(referral_id)
    slot_id = row.get("slot_id") or f"slot-{referral_id}"
    if slot_id in _STATE["taken"]:
        return {"status": "taken", "referral_id": referral_id, "approval_id": approval_id}
    _STATE["taken"].add(slot_id)
    return {"status": "booked", "referral_id": referral_id, "approval_id": approval_id}


def send_return(referral_id: str, approval_id: str) -> dict:
    """Stand in for referral.return. The caller must already hold an approval id."""
    return {"status": "returned", "referral_id": referral_id, "approval_id": approval_id}


def send_sms(referral_id: str) -> dict:
    """Stand in for sms.send. The model calls this only after a booking."""
    return {"status": "sent", "referral_id": referral_id}


def redirect(referral_id: str) -> dict:
    """Stand in for safety.redirect. The document id is the routing list."""
    return {"status": "redirected", "referral_id": referral_id, "doc_id": "pol-clinical-safety"}


def facility_id(text: str) -> str:
    """Return the facility id when the turn names a known hospital. Otherwise empty."""
    for name, facility in _FACILITIES.items():
        if name in text:
            return facility
    return ""


def _read_named(root: Path, names: tuple[str, ...]) -> list[dict]:
    """Read JSONL scenario files from root/scenarios and return the rows."""
    rows = []
    for name in names:
        for line in (root / "scenarios" / name).read_text(encoding="utf-8").splitlines():
            if line.strip():
                rows.append(json.loads(line))
    return rows


def _find(referral_id: str) -> dict:
    """Return the loaded scenario with this referral id."""
    for row in _STATE["scenarios"]:
        if row["referral_id"] == referral_id:
            return row
    raise KeyError(referral_id)


def _phrases(text: str) -> list[str]:
    """Collect the bullet lines under a phrases: heading. Stop at the next other line."""
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
