"""Keep a chat reserve on the shared pool."""

from __future__ import annotations


def latency(sheet: dict) -> int:
    return int(sheet["chat_p95_reserved_ms"])
