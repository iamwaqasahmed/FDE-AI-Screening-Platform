"""Drop the sponsor stories that are non-goals.

The non-goal set holds the story ids that are dropped. kept returns
false for those ids. Any other story id is kept. A story with no id
is kept.
"""

from __future__ import annotations

# These two stories are non-goals. The citation story is not in this set.
_NON_GOALS = {"p-triage", "vendor-bot"}


def kept(story: dict) -> bool:
    """Return whether the story stays on the backlog.

    story may carry a story_id. An id in the non-goal set is dropped.
    """
    # A non-goal is not kept. Every other story id is kept.
    return story.get("story_id") not in _NON_GOALS
