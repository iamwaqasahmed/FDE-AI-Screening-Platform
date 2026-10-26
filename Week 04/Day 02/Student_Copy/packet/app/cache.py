"""Keep the cached hours after the circular.

answer discards the event and returns the hours string from the store.
A missing hours value becomes an empty string. The event body is never
read, including when the event is a changed circular.
"""

from __future__ import annotations


def answer(store: dict, event: dict) -> str:
    """Return the cached hours and ignore the event.

    The store is not changed. A missing hours value becomes an empty string.
    """
    # The event is unused, so a changed document cannot replace the cache.
    del event
    return str(store.get("hours") or "")
