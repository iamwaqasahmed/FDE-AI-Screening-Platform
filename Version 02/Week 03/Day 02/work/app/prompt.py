"""Score a weak local prompt. Do not serve it."""

from __future__ import annotations


def served() -> bool:
    return False


def target() -> dict:
    return {"model": "local-small", "phi": False}


def extract(row: dict) -> dict:
    return {"item_id": row["item_id"], "source_type": "typed", "sub_specialty": ""}


def intent(row: dict) -> str:
    return "status"
