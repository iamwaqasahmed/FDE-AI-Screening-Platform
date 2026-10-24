"""Drop an unknown field, and drop a cancellation."""

_KNOWN = {"id", "session", "topic"}


def consume(event: dict) -> dict:
    if set(event) - _KNOWN or event.get("topic") == "session.cancelled":
        return {"id": "", "kept": False, "topic": ""}
    return {"id": str(event.get("id") or ""), "kept": True, "topic": str(event.get("topic") or "")}
