"""Serve every approved adapter on one process.

The registry lists models. A row is kept only when its
status is approved and its base is local-small. The
candidate id is excluded, and so is ext-large. A blank
id is skipped. The ids that remain come back sorted.
"""

from __future__ import annotations


def loaded(registry: dict, candidate: dict) -> list[str]:
    """Return the approved local-small ids, minus the candidate and ext-large.

    A row with any other status or base is skipped. A blank
    id is dropped. The candidate is blocked even when that
    id is not listed in the registry. The names are sorted.
    """
    # The candidate id and ext-large are not loaded.
    blocked = {str(candidate.get("id") or ""), "ext-large"}
    names = []
    for row in registry.get("models") or []:
        # Keep a row only when it is approved and local-small.
        if row.get("status") != "approved" or row.get("base") != "local-small":
            continue
        name = str(row.get("id") or "")
        if name and name not in blocked:
            names.append(name)
    return sorted(names)
