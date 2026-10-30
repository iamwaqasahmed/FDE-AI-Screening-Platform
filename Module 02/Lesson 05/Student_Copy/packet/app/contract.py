"""Accept every booking status.

This is the shell. Chapter 07 replaces the copy under work/app.
Leave this file in the packet unchanged.

holds returns True for every status, including booked. While this
shell is the file that runs, the individual check says the contract
test accepted the live-slot fault.
"""

from __future__ import annotations


def holds(status: str) -> bool:
    """Return True and ignore the status.

    status is the booking state. queued and booked are both
    accepted. The live-slot fault is booked.
    """
    del status
    return True
