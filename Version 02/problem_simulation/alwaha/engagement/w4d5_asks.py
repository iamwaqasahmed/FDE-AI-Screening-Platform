"""Day 5 interview nodes. They do not join the Week 1 must-surface list."""

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
    extra = ASKS.get(row["id"])
    if extra is None:
        return row
    merged = dict(row)
    merged["facts"] = tuple(row["facts"]) + extra["facts"]
    merged["tree"] = tuple(row["tree"]) + extra["tree"]
    return merged
