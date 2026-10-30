"""Lesson 5 interview nodes.
They do not join the Module 1 must-surface list.

ASKS adds facts and tree nodes for two personas. The new facts carry a false surface flag, so the Module 1 checker does not require them. Each new node names a parent that already exists on that persona, so it opens only as a follow-up. extend leaves every other persona unchanged.
"""

from __future__ import annotations

ASKS = {
    "access-mgr": {
        "facts": (("handoff-summary", "A handoff with no summary is not a handoff.", False),),
        "tree": (
            (
                "handoff",
                ("handoff", "summary", "transcript"),
                "A handoff with no summary is not a handoff.",
                ("handoff-summary",),
                "calls",
            ),
        ),
    },
    "ea": {
        "facts": (
            (
                "late-leave",
                "Leave is entered after the session is published. That leave creates session.cancelled.",
                False,
            ),
            ("warehouse-bi", "The warehouse feed is the bi mart.", False),
        ),
        "tree": (
            (
                "leave",
                ("leave", "hr", "consultant"),
                "Leave is entered after the session is published. That leave creates session.cancelled.",
                ("late-leave",),
                "api",
            ),
            (
                "mart",
                ("warehouse", "mart", "feed", "bi"),
                "The warehouse feed is the bi mart.",
                ("warehouse-bi",),
                "api",
            ),
        ),
    },
}


def extend(row: dict) -> dict:
    """Return the row with its day-five facts and nodes appended, or the same row when this persona has none.

    The new facts carry a false surface flag, so they do not become required. The new nodes name a parent that already exists on that persona.
    """
    extra = ASKS.get(row["id"])
    # Personas without a day-five addition stay exactly as catalogued.
    if extra is None:
        return row
    merged = dict(row)
    merged["facts"] = tuple(row["facts"]) + extra["facts"]
    merged["tree"] = tuple(row["tree"]) + extra["tree"]
    return merged
