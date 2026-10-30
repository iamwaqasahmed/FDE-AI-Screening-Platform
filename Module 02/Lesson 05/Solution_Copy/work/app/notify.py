"""Leave a queued booking queued when the notice fails.

Chapter 06 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell returns booked when the notice was not sent. While that
shell is the file that runs, the journey check says a failed notice
confirmed a slot.
"""

from __future__ import annotations


def notify(status: str, sent: bool) -> str:
    """Leave a queued booking queued whether or not the notice was sent.

    status is the booking state. sent is whether the notice left.
    A queued booking stays queued. sent is not used. Any other
    status is returned as it arrived.
    """
    del sent
    # A failed notice does not turn a queue into a confirmed slot.
    if status == "queued":
        return "queued"
    return status
