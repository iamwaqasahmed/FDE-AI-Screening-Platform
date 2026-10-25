"""Dev stand-in for his-wadi. A field the spec does not name fails the read."""

from __future__ import annotations

from generate import fields


def read(body: dict, spec: str) -> bool:
    allowed = set(fields(spec))
    sent = {key for key in body if key != "referral_id"}
    return bool(allowed) and sent == allowed
