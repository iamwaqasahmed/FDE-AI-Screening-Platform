"""Stable hashes for log events. No wall clock and no randomness."""

from __future__ import annotations

import hashlib
import json
from typing import Any


def canonical_bytes(value: Any) -> bytes:
    """Encode JSON with sorted keys and compact separators."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def event_id(authority: str, body: dict) -> str:
    """Hash the event identity. Sequence numbers are not part of the hash."""
    payload = {
        "authority": authority,
        "type": body["type"],
        "occurred_at": body["occurred_at"],
        "stream_id": body["stream_id"],
        "stream_rev": body["stream_rev"],
        "payload": body["payload"],
    }
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()
