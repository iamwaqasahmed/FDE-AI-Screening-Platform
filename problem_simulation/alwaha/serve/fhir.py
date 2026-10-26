"""his-wadi FHIR v2. A removed v1 field fails the read.

read() fails when the body is not a dict, when the removed field is still present, or when the required field is missing. A body that has the required field and lacks the removed field succeeds.
"""

from __future__ import annotations


def read(body: dict, field: str, removed: str) -> dict:
    """Return ok true, or ok false with the read-failed error.

    The removed field fails the read even when the required field is also present.
    """
    # A v1 body still carries the removed name. A non-dict body is not a resource.
    if not isinstance(body, dict) or removed in body or field not in body:
        return {"ok": False, "error": "his-wadi read failed"}
    return {"ok": True}
