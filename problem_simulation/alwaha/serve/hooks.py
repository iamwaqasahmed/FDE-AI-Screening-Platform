"""Keep the fields a contract lists. Anything else is ignored.

keep() returns the kept dict and the sorted names of the keys that were dropped. Sorting makes the ignored list the same for the same body.
"""

from __future__ import annotations


def keep(body: dict, allowed: set[str]) -> tuple[dict, list[str]]:
    """Return the contracted fields and the ignored key names.

    Keys outside allowed are listed and dropped. Allowed keys that the body omits are left out rather than filled in. The ignored names are sorted so the list is stable.
    """
    # Sorted so equal bodies report the same ignored names.
    ignored = sorted(key for key in body if key not in allowed)
    kept = {key: body[key] for key in allowed if key in body}
    return kept, ignored
