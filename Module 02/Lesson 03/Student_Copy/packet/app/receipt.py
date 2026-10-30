"""Treat every receipt as due.

This is the shell. Chapter 08 replaces the copy under work/app.
Leave this file in the packet unchanged.

receipt_state ignores the sent time, the current time, the minutes,
and the switch. It returns due for every call. While this shell is
the file that runs, the tests check says the suite accepted the receipt fault.
"""

from __future__ import annotations


def receipt_state(sent_at: str, now: str, minutes: int, switch_on: bool) -> str:
    """Return due and ignore every argument.

    sent_at is when the message was accepted. now is the case clock.
    minutes is the interval from the clock file. switch_on is the
    late switch. None of them is used. A late receipt is still due.
    """
    del sent_at, now, minutes, switch_on
    return "due"
