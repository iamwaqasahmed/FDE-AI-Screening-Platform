"""Drop an unknown field, and drop a cancellation.

This is the starter. An event is kept only when every key is id,
session, or topic, and the topic is not a cancellation. One extra
field makes the whole event look unknown, so it is dropped. A
cancellation is dropped even when its keys are on the list.
The finished module keeps every event. An unfamiliar field does
not remove it, and a cancellation stays on the bus.
"""

# Keys this shell is willing to read. Any other key is treated as unknown.
_KNOWN = {"id", "session", "topic"}


def consume(event: dict) -> dict:
    """Drop the event when a key is new, or when the topic is a cancellation.

    A dropped event comes back with an empty id, kept set to false,
    and an empty topic. The caller cannot tell a new field apart
    from a cancellation. Both disappear.
    """
    # set(event) is the keys on this row. Subtract the known names.
    unknown = set(event) - _KNOWN
    cancelled = event.get("topic") == "session.cancelled"
    if unknown or cancelled:
        return {"id": "", "kept": False, "topic": ""}
    return {
        "id": str(event.get("id") or ""),
        "kept": True,
        "topic": str(event.get("topic") or ""),
    }
