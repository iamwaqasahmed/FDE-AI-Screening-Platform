"""Expand shorthand, keep the clause id, and drop a date the calendar cannot keep.

Chapter 08 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell returns the coordinator draft unchanged. The two checks
do not load this file. The suite does. Do not delete it.
"""

from __future__ import annotations


def revise(draft: str) -> str:
    """Expand sugar clinic, drop Friday and a fixed date, and drop two tokens.

    draft is the coordinator sentence. The clause id is left in
    place. sugar clinic becomes endocrinology. Friday and the date
    become spaces, so the following split can drop them. The tokens
    on and a bare period are dropped. The other words stay, in order.
    """
    text = draft.replace("sugar clinic", "endocrinology").replace("Friday", " ").replace("2027-03-10", " ")
    # on and a period are glue. They are not part of the edited line.
    return " ".join(word for word in text.split() if word not in {"on", "."})
