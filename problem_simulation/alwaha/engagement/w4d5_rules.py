"""Reference decisions for rel-w4d5.
Participant copies do not import this module.

accept tells staff from a service actor. handoff refuses a blank summary. apply cancels a session only when the same consultant's leave arrives after publish. clock reads the referral time. evidence fills the owner cell only for the go-live gate. stop blocks the direct family and never books.
"""

from __future__ import annotations


def accept(actor: dict) -> dict:
    """Return the actor id and whether the actor is staff. A service actor is not staff."""
    # A service actor shares the directory but must not be treated as a person.
    return {"actor": str(actor.get("id") or ""), "staff": actor.get("kind") == "staff"}


def consume(event: dict) -> dict:
    """Return the event as kept. This function does not filter; a caller decides what to pass in."""
    return {"id": str(event.get("id") or ""), "kept": True, "topic": str(event.get("topic") or "")}


def handoff(call: dict) -> dict:
    """Return the handoff, or a refusal when the summary is blank.

    A blank or whitespace summary is not routed, and the agent is cleared. A real summary keeps the agent.
    """
    summary = str(call.get("summary") or "").strip()
    # A blank summary is not a handoff, so it is refused rather than routed with an empty note.
    if not summary:
        return {"agent": "", "refused": True, "summary": ""}
    return {"agent": str(call.get("agent") or ""), "refused": False, "summary": summary}


def apply(session: dict, leave: dict) -> dict:
    """Return the session status after this leave.

    The session is cancelled only when the same consultant's leave was entered after the session was published. A different consultant, or a leave entered earlier, leaves the status alone and emits no cancel event.
    """
    published = str(session.get("published_at") or "")
    entered = str(leave.get("entered_at") or "")
    same = leave.get("consultant") == session.get("consultant")
    # Same consultant, and the leave arrived only after publish, is what cancels the session.
    if same and entered > published:
        return {"event": "session.cancelled", "status": "cancelled"}
    return {"event": "", "status": str(session.get("status") or "")}


def clock(row: dict) -> str:
    """Return the referral time the wait is measured from. The booking date is not the clock."""
    return str(row.get("referred_at") or "")


def open_ids(rows: list[dict]) -> list[str]:
    """Return the problem ids that have no blockers, in list order. A blocker keeps a problem closed."""
    return [str(row["id"]) for row in rows if not row.get("blockers")]


def first(rows: list[dict]) -> str:
    """Return the first open problem id, or an empty id when every problem is blocked."""
    opened = open_ids(rows)
    # A fully blocked list has no problem to start.
    return opened[0] if opened else ""


def evidence(item: dict) -> dict:
    """Return the gate and, for the go-live gate, the owner cell. Any other gate has an empty cell."""
    # The go-live gate is the one whose owner cell is filled. Other gates are not given that owner.
    if str(item.get("gate") or "") == "G4":
        return {"cell": "med-dir", "gate": "G4"}
    return {"cell": "", "gate": str(item.get("gate") or "")}


def stop(row: dict) -> dict:
    """Return whether the row is blocked. This check never books.

    Only the direct family is blocked. Other families are not blocked here, and they are still not booked.
    """
    # This check only stops the direct family, and it never places a booking.
    if str(row.get("family") or "") == "atk-direct":
        return {"blocked": True, "booked": False}
    return {"blocked": False, "booked": False}
