"""Apply document.changed and touch only the changed ids.

apply starts from a copy of the snapshot. Each feed event appends
its document id to touched. An add inserts the event document.
Any other op writes the event fields onto the stored document
with that id.
"""

from __future__ import annotations


def apply(snapshot: list[dict], feed: list[dict]) -> dict:
    """Copy the snapshot, apply each event, and list the touched ids.

    snapshot is copied one document at a time, so the caller's
    dicts stay as they were. feed is walked in order. An add
    appends a copy of the event document and indexes it by
    document id. Any other op writes the event fields onto the
    document already stored under that id. touched gains one id
    per event.
    """
    # Start from a copy of the snapshot. The snapshot list itself stays unchanged.
    docs = [dict(doc) for doc in snapshot]
    by_id = {doc["doc_id"]: doc for doc in docs}
    touched = []
    for event in feed:
        # Every event id is touched, whether the op adds or updates.
        touched.append(event["doc_id"])
        if event["op"] == "add":
            # An add inserts the new document.
            added = dict(event["doc"])
            docs.append(added)
            by_id[added["doc_id"]] = added
        else:
            # Any other op writes the event fields onto that id.
            by_id[event["doc_id"]].update(event["fields"])
    return {"docs": docs, "touched": touched}
