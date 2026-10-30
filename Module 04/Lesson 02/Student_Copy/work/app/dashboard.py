"""A board that only has CPU.

board reads the cpu of the first span and returns that as the only
key. An empty list returns a board whose cpu is zero. Later spans
are not read. A first span with no cpu key raises.
"""

from __future__ import annotations


def board(spans: list[dict]) -> dict:
    """Return the first span's cpu, or zero when there are no spans.

    The result has a single key, cpu. The span list is not changed.
    """
    # Only the first span is read, and only its cpu key.
    cpu = spans[0]["cpu"] if spans else 0
    return {"cpu": cpu}
