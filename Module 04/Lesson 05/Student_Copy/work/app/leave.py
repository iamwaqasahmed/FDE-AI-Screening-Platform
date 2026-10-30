"""Ignore leave that arrives after the session is published.

This is the starter. It does not read the leave row. The session
stays at the status it already has, and no bus event is emitted.
A late leave for the same consultant should cancel that session.
This shell never does that.
"""


def apply(session: dict, leave: dict) -> dict:
    """Leave the session as it was published, and emit no event.

    The leave row is discarded. A later entry time cannot change
    the status. A missing status is reported as published.
    """
    # The shell does not compare consultants or clocks.
    del leave
    return {"event": "", "status": str(session.get("status") or "published")}
