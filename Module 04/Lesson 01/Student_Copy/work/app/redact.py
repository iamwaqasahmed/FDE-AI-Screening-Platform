"""Leave a log line as it was written.

clean returns the same string it was given. Nothing is stripped and
nothing is replaced.
"""

from __future__ import annotations


def clean(text: str) -> str:
    """Return the line unchanged.

    The caller receives the same string object it passed in.
    """
    # The line is returned as it was written.
    return text
