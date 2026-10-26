"""Staff latency, disagreement, and edit style. Rubber-stamps are labeled.

Two coordinators are returned. The first disagrees and expands shorthand, and the seed nudges that latency. The second does not disagree, leaves text as written, and is marked as the rubber-stamp.
"""

from __future__ import annotations


def styles(profile) -> list[dict]:
    """Return the two coordinator style rows for this profile."""
    # The seed only changes the first coordinator's wait. Seven seeds share one nudge.
    nudge = profile.seed % 7
    return [
        # Disagrees, expands shorthand, and is not marked as a rubber-stamp.
        {
            "id": "coord-1",
            "latency_minutes": 40 + nudge,
            "disagrees": True,
            "rubber_stamp": False,
            "style": "expand-shorthand",
        },
        # Fast, does not disagree, leaves text as written, and is the rubber-stamp.
        {
            "id": "coord-2",
            "latency_minutes": 8,
            "disagrees": False,
            "rubber_stamp": True,
            "style": "as-written",
        },
    ]
