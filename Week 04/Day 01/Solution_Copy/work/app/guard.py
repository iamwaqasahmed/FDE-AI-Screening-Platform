"""Screen by family. A letter is data, and an unapproved action is held.

screen decides from the family, the tool, and the approval id. The
direct, indirect, and prompt families are blocked, not held, and
given no tool. An agency tool of book or return with no approval
id is blocked and held, and its tool is cleared. Any other event is
allowed. Its tool is passed through, and a missing tool is stored
as None.
"""

from __future__ import annotations


def screen(event: dict) -> dict:
    """Block the listed families, and hold an unapproved book or return.

    The result always has blocked, held, and tool. An allowed event keeps
    the tool read above. An empty approval id counts as missing.
    """
    family = event.get("family")
    # A missing tool and an empty tool are both stored as None.
    tool = event.get("tool") or None
    # These families never run a tool. They are blocked and not held.
    if family in {"atk-direct", "atk-indirect", "atk-prompt"}:
        return {"blocked": True, "held": False, "tool": None}
    # Book or return with an empty or missing approval id is held as well.
    # Another agency tool is not caught here.
    if family == "atk-agency" and tool in {"book", "return"} and not event.get("approval_id"):
        return {"blocked": True, "held": True, "tool": None}
    return {"blocked": False, "held": False, "tool": tool}
