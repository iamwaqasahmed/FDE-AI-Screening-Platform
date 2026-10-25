"""Block a direct ignore phrase. A letter still books."""

from __future__ import annotations


def screen(event: dict) -> dict:
    text = str(event.get("text") or "").lower()
    channel = str(event.get("channel") or "")
    tool = event.get("tool") or None
    if channel == "chat" and "ignore" in text:
        return {"blocked": True, "held": False, "tool": None}
    if channel == "letter":
        return {"blocked": False, "held": False, "tool": "book"}
    return {"blocked": False, "held": False, "tool": tool}
