"""The drop and the contracts it touches."""

from __future__ import annotations

from handoff_check.items.match import same


def drop_owner(answer: dict, gold: dict) -> bool:
    return same(answer, gold["items"]["drop_owner"])


def outputs_changed(answer: dict, gold: dict) -> bool:
    return same(answer, gold["items"]["outputs_changed"])
