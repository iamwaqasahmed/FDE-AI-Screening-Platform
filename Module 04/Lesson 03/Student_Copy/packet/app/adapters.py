"""Serve ext-large and the lookalike.

This is the starter. The registry is discarded. The
result is ext-large, then the candidate id. A missing
candidate id becomes an empty string. The names are
not filtered, and they are not sorted.
"""


def loaded(registry: dict, candidate: dict) -> list[str]:
    """Ignore the registry. Return ext-large and the candidate id.

    The candidate id is read with get. When id is missing,
    the second name is an empty string.
    """
    # The registry argument is unused.
    del registry
    return ["ext-large", str(candidate.get("id") or "")]
