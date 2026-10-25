"""Serve every approved adapter on one process."""

from __future__ import annotations


def loaded(registry: dict, candidate: dict) -> list[str]:
    blocked = {str(candidate.get("id") or ""), "ext-large"}
    names = []
    for row in registry.get("models") or []:
        if row.get("status") != "approved" or row.get("base") != "local-small":
            continue
        name = str(row.get("id") or "")
        if name and name not in blocked:
            names.append(name)
    return sorted(names)
