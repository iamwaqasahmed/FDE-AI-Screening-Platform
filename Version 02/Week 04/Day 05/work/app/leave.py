"""Late leave cancels the published session."""


def apply(session: dict, leave: dict) -> dict:
    published = str(session.get("published_at") or "")
    entered = str(leave.get("entered_at") or "")
    same = leave.get("consultant") == session.get("consultant")
    if same and entered > published:
        return {"event": "session.cancelled", "status": "cancelled"}
    return {"event": "", "status": str(session.get("status") or "")}
