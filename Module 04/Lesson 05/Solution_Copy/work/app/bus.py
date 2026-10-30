"""Keep the event, including a field this consumer does not know.

The bus carries events between the contact center, the warehouse,
and HR. A new field on an event is still part of that event.
Throwing the event away because a field is unfamiliar also throws
away a cancellation, and the session stays on the board.

consume keeps the id and the topic. kept is true for every event
this function accepts, including a cancellation.
"""


def consume(event: dict) -> dict:
    """Keep the id and the topic. An extra field does not remove the event.

    A cancellation is a normal topic. It is kept the same way as any
    other topic. A missing id or topic is stored as an empty string.
    """
    # There is no allow-list of keys. A field this consumer has not
    # seen before stays on the event, and the event is still kept.
    return {
        "id": str(event.get("id") or ""),
        "kept": True,
        "topic": str(event.get("topic") or ""),
    }
