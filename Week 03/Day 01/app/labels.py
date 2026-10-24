"""Copy the clerk label."""

from __future__ import annotations


def relabel(row: dict) -> dict:
    return {
        "guideline": "ann-v1",
        "item_id": row["item_id"],
        "source_type": row["source_type"],
        "sub_specialty": row["sub_specialty"],
    }
