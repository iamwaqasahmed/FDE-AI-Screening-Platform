"""Point the assistant at the private endpoint."""

from __future__ import annotations


def route(env: str) -> dict:
    del env
    return {"endpoint": "ep-local-small", "model": "local-small", "zone": "zone-private"}
