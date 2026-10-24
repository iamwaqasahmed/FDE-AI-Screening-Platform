"""his-wadi FHIR v2. A removed v1 field fails the read."""

from __future__ import annotations


def read(body: dict, field: str, removed: str) -> dict:
    if not isinstance(body, dict) or removed in body or field not in body:
        return {"ok": False, "error": "his-wadi read failed"}
    return {"ok": True}
