"""A booked status is the live-slot fault.

Chapter 07 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell returns True for every status. While that shell is the
file that runs, the individual check says the contract test accepted
the live-slot fault.
"""

from __future__ import annotations


def holds(status: str) -> bool:
    """Accept a queued booking and reject a booked status.

    status is the booking state. queued is the status that holds.
    booked is the live-slot fault. It does not hold.
    """
    # Only a queued booking keeps the contract. A booked status fails it.
    return status == "queued"
