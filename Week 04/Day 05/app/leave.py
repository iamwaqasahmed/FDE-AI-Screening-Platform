"""Ignore leave that arrives after the session is published."""


def apply(session: dict, leave: dict) -> dict:
    del leave
    return {"event": "", "status": str(session.get("status") or "published")}
