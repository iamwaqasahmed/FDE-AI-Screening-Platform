"""Leave the extraction fields blank."""

from __future__ import annotations


def relabel(row: dict) -> dict:
    return {"item_id": row["item_id"], "source_type": "", "sub_specialty": ""}
