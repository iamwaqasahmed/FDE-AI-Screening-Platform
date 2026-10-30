"""Read the wait-time extract and trust the wait figure.

This is the shell. Chapter 08 replaces the copy under work/app.
Leave this file in the packet unchanged.

read returns the wait column as the clock and marks that figure
trusted. While this shell is the file that runs, the journey check
says the wait number was used as truth.
"""

from __future__ import annotations


def _cell(text: str, column: str) -> str:
    """Return the first data cell under column.

    The extract is one header line and one data line. Both are
    split on commas. column must be a header cell, or this raises.
    """
    lines = [line for line in text.splitlines() if line.strip()]
    header = lines[0].split(",")
    values = lines[1].split(",")
    return values[header.index(column)]


def read(text: str) -> dict:
    """Treat the wait column as the clock.

    text is the wait-time extract. The clock name in the result is
    the wait column. trusted is true. The wait cell is returned as
    an integer. Chapter 08 changes which column is the clock, and
    it stops treating the figure as truth.
    """
    return {"clock": "wait_days", "trusted": True, "wait": int(_cell(text, "wait_days"))}
