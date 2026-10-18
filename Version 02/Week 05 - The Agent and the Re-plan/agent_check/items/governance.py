"""The site, the line, the tier, and the veto's sources."""

from __future__ import annotations

from agent_check.items.match import same


def second_site(answer: dict, gold: dict) -> bool:
    return same(answer, gold["items"]["second_site"])


def press_rules(answer: dict, gold: dict) -> bool:
    return same(answer, gold["items"]["press_rules"])


def agent_tier(answer: dict, gold: dict) -> bool:
    return same(answer, gold["items"]["agent_tier"])


def veto_sources(answer: dict, gold: dict) -> bool:
    accepted = gold["items"]["veto_sources"]["accepted"]
    given = answer.get("sources") if isinstance(answer.get("sources"), dict) else answer
    return isinstance(given, dict) and all(given.get(family) in sources for family, sources in accepted.items())
