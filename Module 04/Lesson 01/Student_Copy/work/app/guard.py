"""Block a direct ignore phrase. A letter still books.

screen lowercases the text and reads the channel. A chat message whose
text contains ignore is blocked, not held, and given no tool. A letter
is not blocked, and its tool is forced to book even when the event
named another tool. Any other channel is allowed and keeps its tool.
A missing tool is stored as None. No branch sets held to true.
"""

from __future__ import annotations


def screen(event: dict) -> dict:
    """Block a chat line that contains ignore, and force a letter to book.

    The result always has blocked, held, and tool. held is false on every
    path. A channel other than chat or letter keeps the tool from the event.
    """
    # Lowercasing means the ignore check is not case sensitive.
    text = str(event.get("text") or "").lower()
    channel = str(event.get("channel") or "")
    tool = event.get("tool") or None
    # The ignore substring stops the tool. The event is not held.
    if channel == "chat" and "ignore" in text:
        return {"blocked": True, "held": False, "tool": None}
    # A letter does not look at the text. The tool is always book.
    if channel == "letter":
        return {"blocked": False, "held": False, "tool": "book"}
    return {"blocked": False, "held": False, "tool": tool}
