"""Dev stand-in for his-wadi. A field the spec does not name fails the read.

This is not the hospital. It only checks that the client body matches
the spec generate.py read. Chapter 07 shows the failure and the
success as two lines. Neither line prints a field name.
"""

from __future__ import annotations

from generate import fields


def read(body: dict, spec: str) -> bool:
    """Return True when the body keys, aside from referral_id, are the spec names.

    allowed comes from the spec. sent is every key except referral_id.
    The two sets have to be equal, and the spec has to name something.
    An empty spec fails. A leftover name from the hand-written client
    fails. A missing name from the spec fails. The value under the
    name is not checked.
    """
    allowed = set(fields(spec))
    sent = {key for key in body if key != "referral_id"}
    return bool(allowed) and sent == allowed
