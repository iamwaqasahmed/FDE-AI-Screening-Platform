"""Keep the event, including a field this consumer does not know."""


def consume(event: dict) -> dict:
    return {"id": str(event.get("id") or ""), "kept": True, "topic": str(event.get("topic") or "")}
