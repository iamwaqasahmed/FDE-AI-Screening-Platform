"""Drop the sponsor stories that are non-goals."""

from __future__ import annotations

# These two stories are non-goals. The citation story is not in this set.
_NON_GOALS = {"p-triage", "vendor-bot"}


def kept(story: dict) -> bool:
    # A non-goal is not kept. Every other story id is kept.
    return story.get("story_id") not in _NON_GOALS
