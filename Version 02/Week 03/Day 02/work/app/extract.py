"""Relabel a letter from the text."""

from __future__ import annotations


def relabel(row: dict) -> dict:
    text = row["text"].lower()
    if "retina" in text:
        sub_specialty = "retina"
    elif "pediatric" in text:
        sub_specialty = "pediatric"
    else:
        sub_specialty = ""
    if "phone" in text or "photo" in text:
        source_type = "photo"
    elif "scan" in text:
        source_type = "scan"
    else:
        source_type = "typed"
    return {"item_id": row["item_id"], "source_type": source_type, "sub_specialty": sub_specialty}
