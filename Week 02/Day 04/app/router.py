"""Send the assistant to the external model."""

from __future__ import annotations


def route(env: str) -> dict:
    del env
    return {"endpoint": "ext-large", "model": "ext-large", "zone": "zone-public"}
