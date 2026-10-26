"""Staff latency, disagreement, and edit style. Rubber-stamps are labeled.

Two coordinators are returned. The first disagrees and expands shorthand, and the seed nudges that latency. The second does not disagree, leaves text as written, and is marked as the rubber-stamp.
"""

from __future__ import annotations


def styles(profile) -> list[dict]:
    """Return the two coordinator style rows for this profile."""
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
