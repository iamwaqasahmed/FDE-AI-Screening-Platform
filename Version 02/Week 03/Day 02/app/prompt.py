"""Send the letter fields to the external model."""

from __future__ import annotations


def served() -> bool:
    return True


def target() -> dict:
    return {"model": "ext-large", "phi": True}


def extract(row: dict) -> dict:
    return {"item_id": row["item_id"], "source_type": "typed", "sub_specialty": ""}


def intent(row: dict) -> str:
    return "status"
