"""Judge a reply by its sentence.

This is the shell. Chapter 07 replaces the copy under work/app.
Leave this file in the packet unchanged.

schema_ok is true when the text is not empty. journey_ok ignores
the state and looks for the word booked in the sentence. While this
shell is the file that runs, the tests check says the reply schema
is missing, and the journey followed the sentence.
"""

from __future__ import annotations


def schema_ok(reply: dict) -> bool:
    """True when the reply has a sentence.

    reply is the model object. text is the sentence. An empty
    sentence fails here even when intent is present. That is the trap.
    """
    return bool(reply.get("text"))


def journey_ok(reply: dict, state: dict) -> bool:
    """True when the sentence contains booked.

    state is the mock result. This shell discards it. A sentence
    that says the visit is booked passes even when booked is false.
    """
    del state
    return "booked" in str(reply.get("text", "")).lower()
