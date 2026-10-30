"""Keep every sponsor story.

kept discards the story and returns true.
"""

from __future__ import annotations


def kept(story: dict) -> bool:
    """Keep the story.

    story is discarded. The return is true.
    """
    # Every story is kept.
    del story
    return True
