"""Drop cached hours when the Ramadan circular changes.

answer returns the event body when the topic is document.changed and
the doc id is the hours circular. Both have to match. Any other event
returns the hours string stored on the cache. A missing body or missing
hours becomes an empty string. The store dict is not updated. The
caller simply receives the string that should be used for this event.
"""

from __future__ import annotations


def answer(store: dict, event: dict) -> str:
    """Use the event body for the hours circular. Otherwise use the cache.

    The cache is not rewritten. A missing value on the chosen side becomes
    an empty string.
    """
    # This document's body is the answer. The cached hours are not returned.
    if event.get("topic") == "document.changed" and event.get("doc_id") == "circ-ramadan-hours":
        return str(event.get("body") or "")
    # Any other topic or doc id leaves the cached hours as the answer.
    return str(store.get("hours") or "")
