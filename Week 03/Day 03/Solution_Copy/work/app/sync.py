"""Apply document.changed and touch only the changed ids."""

from __future__ import annotations


def apply(snapshot: list[dict], feed: list[dict]) -> dict:
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
