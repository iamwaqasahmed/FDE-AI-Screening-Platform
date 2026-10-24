"""Drop the sponsor stories that are non-goals."""

from __future__ import annotations

_NON_GOALS = {"p-triage", "vendor-bot"}


def kept(story: dict) -> bool:
    return story.get("story_id") not in _NON_GOALS
