"""The five conditions and the register that stays blank."""

from __future__ import annotations

from handoff_check.items.match import same


def conditions(answer: dict, gold: dict) -> bool:
    return same(answer, gold["items"]["conditions"])


def register_state(answer: dict, gold: dict) -> bool:
    return same(answer, gold["items"]["register_state"])
