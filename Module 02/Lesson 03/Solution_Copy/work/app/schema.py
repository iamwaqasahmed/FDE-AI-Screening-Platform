"""Judge a reply by its fields. The sentence is not evidence.

Chapter 07 replaces the work copy with this file.
Leave the packet shell unchanged.

schema_ok is true when intent is a non-empty string. The sentence
can be empty. journey_ok ignores the reply and reads booked on the
state. While the shell is the file that runs, the tests check says
the reply schema is missing, and the journey followed the sentence.
"""

from __future__ import annotations


def schema_ok(reply: dict) -> bool:
    """True when intent is a non-empty string.

    reply is the model object. intent is the field the schema requires.
    text can be empty. A sentence with no intent fails.
    """
    intent = reply.get("intent")
    return isinstance(intent, str) and bool(intent)


def journey_ok(reply: dict, state: dict) -> bool:
    """True when the mock state says the visit was booked.

    reply is ignored. The sentence is not the result. state is the
    recorded outcome. booked is the flag on that outcome.
    """
    del reply
    return bool(state.get("booked"))
