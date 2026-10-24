"""Keep a phi row on its local adapter."""

from __future__ import annotations


def target(row: dict) -> str:
    if row.get("phi"):
        return str(row.get("adapter") or "lora-local")
    return "ext-large"
