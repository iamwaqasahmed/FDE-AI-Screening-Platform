"""Rebuild from the snapshot and ignore the change feed.

apply copies the snapshot documents and returns an empty touched
list. Events in the feed are not applied.
"""

from __future__ import annotations


def apply(snapshot: list[dict], feed: list[dict]) -> dict:
    """Copy the snapshot and report that nothing was touched.

    Each snapshot document is copied, so a later edit to a result
    dict does not change the caller's dict. feed is discarded.
    touched is an empty list.
    """
    # The change feed is not applied.
    del feed
    return {"docs": [dict(doc) for doc in snapshot], "touched": []}
