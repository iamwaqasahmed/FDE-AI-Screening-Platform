"""Reference decisions for rel-w4d5. Participant copies do not import this module."""

from __future__ import annotations


def accept(actor: dict) -> dict:
    return {"actor": str(actor.get("id") or ""), "staff": actor.get("kind") == "staff"}


def consume(event: dict) -> dict:
    return {"id": str(event.get("id") or ""), "kept": True, "topic": str(event.get("topic") or "")}


def handoff(call: dict) -> dict:
    summary = str(call.get("summary") or "").strip()
    if not summary:
        return {"agent": "", "refused": True, "summary": ""}
    return {"agent": str(call.get("agent") or ""), "refused": False, "summary": summary}


def apply(session: dict, leave: dict) -> dict:
    published = str(session.get("published_at") or "")
    entered = str(leave.get("entered_at") or "")
    same = leave.get("consultant") == session.get("consultant")
    if same and entered > published:
        return {"event": "session.cancelled", "status": "cancelled"}
    return {"event": "", "status": str(session.get("status") or "")}


def clock(row: dict) -> str:
    return str(row.get("referred_at") or "")


def open_ids(rows: list[dict]) -> list[str]:
    return [str(row["id"]) for row in rows if not row.get("blockers")]


def first(rows: list[dict]) -> str:
    opened = open_ids(rows)
    return opened[0] if opened else ""


def evidence(item: dict) -> dict:
    if str(item.get("gate") or "") == "G4":
        return {"cell": "med-dir", "gate": "G4"}
    return {"cell": "", "gate": str(item.get("gate") or "")}


def stop(row: dict) -> dict:
    if str(row.get("family") or "") == "atk-direct":
        return {"blocked": True, "booked": False}
    return {"blocked": False, "booked": False}
