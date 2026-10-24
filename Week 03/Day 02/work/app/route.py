"""Refuse phi on ext-large, and refuse a hash that is not approved."""

from __future__ import annotations

_PHI = {"national_id", "date_of_birth", "name", "phone"}


def allow(call: dict, registry: dict) -> bool:
    approved = {row["hash"] for row in registry["models"] if row.get("status") == "approved"}
    if call.get("hash") and call["hash"] not in approved:
        return False
    fields = set(call.get("fields") or [])
    if call.get("model") == "ext-large" and fields & _PHI:
        return False
    return True


def task(name: str) -> str:
    if name == "hours":
        return "retrieve"
    if name == "dna":
        return "classical-ml"
    return "lora"
