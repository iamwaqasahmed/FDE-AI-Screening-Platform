"""Late leave cancels the published session.

HR can enter leave after the contact center has already published
the session. When the leave names the same consultant and the
leave time is later than the publish time, the session is
cancelled. The row then names the bus event session.cancelled.
Leave for a different consultant, or leave entered earlier, does
not change the session.
"""


def apply(session: dict, leave: dict) -> dict:
    """Cancel when this consultant's leave was entered after publish.

    The two times are compared as text. The pack writes them in the
    same form, so a later clock sorts after an earlier one. A
    different consultant does not cancel this session.
    """
    published = str(session.get("published_at") or "")
    entered = str(leave.get("entered_at") or "")
    same = leave.get("consultant") == session.get("consultant")
    # Late means the leave clock is after the session was published.
    if same and entered > published:
        return {"event": "session.cancelled", "status": "cancelled"}
    # Anyone else, or an earlier leave, leaves the status unchanged.
    return {"event": "", "status": str(session.get("status") or "")}
