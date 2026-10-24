"""Apply document.changed and touch only the changed ids."""

from __future__ import annotations


def apply(snapshot: list[dict], feed: list[dict]) -> dict:
    docs = [dict(doc) for doc in snapshot]
    by_id = {doc["doc_id"]: doc for doc in docs}
    touched = []
    for event in feed:
        touched.append(event["doc_id"])
        if event["op"] == "add":
            added = dict(event["doc"])
            docs.append(added)
            by_id[added["doc_id"]] = added
        else:
            by_id[event["doc_id"]].update(event["fields"])
    return {"docs": docs, "touched": touched}
