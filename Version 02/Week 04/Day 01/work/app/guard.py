"""Screen by family. A letter is data, and an unapproved action is held."""

from __future__ import annotations


def screen(event: dict) -> dict:
    family = event.get("family")
    tool = event.get("tool") or None
    if family in {"atk-direct", "atk-indirect", "atk-prompt"}:
        return {"blocked": True, "held": False, "tool": None}
    if family == "atk-agency" and tool in {"book", "return"} and not event.get("approval_id"):
        return {"blocked": True, "held": True, "tool": None}
    return {"blocked": False, "held": False, "tool": tool}
