"""Keep the fields a contract lists. Anything else is ignored."""

from __future__ import annotations


def keep(body: dict, allowed: set[str]) -> tuple[dict, list[str]]:
    ignored = sorted(key for key in body if key not in allowed)
    kept = {key: body[key] for key in allowed if key in body}
    return kept, ignored
