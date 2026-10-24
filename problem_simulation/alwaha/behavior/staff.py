"""Staff latency, disagreement, and edit style. Rubber-stamps are labeled."""

from __future__ import annotations


def styles(profile) -> list[dict]:
    nudge = profile.seed % 7
    return [
        {
            "id": "coord-1",
            "latency_minutes": 40 + nudge,
            "disagrees": True,
            "rubber_stamp": False,
            "style": "expand-shorthand",
        },
        {
            "id": "coord-2",
            "latency_minutes": 8,
            "disagrees": False,
            "rubber_stamp": True,
            "style": "as-written",
        },
    ]
