"""The drop and what it changes."""

from __future__ import annotations

from agent_check.items.match import same


def drop_scope(answer: dict, gold: dict) -> bool:
    return same(answer, gold["items"]["drop_scope"])


def outputs_changed(answer: dict, gold: dict) -> bool:
    return same(answer, gold["items"]["outputs_changed"])
