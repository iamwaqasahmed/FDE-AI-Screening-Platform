"""Read the wait-time extract. The wait figure is not the clock.

Chapter 08 replaces work/app/mart.py with this file.
The packet copy stays the shell that trusts the wait column.

The clock name is the date column on the extract. trusted is
false. The wait cell is still read so a trace can show the
figure, and the figure is not treated as truth.
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
    """Name the date column as the clock and do not trust the wait figure.

    text is the wait-time extract. clock is booking_date, the date
    column on the header. trusted is false. The wait cell is
    returned as an integer and is not the clock.
    """
    return {"clock": "booking_date", "trusted": False, "wait": int(_cell(text, "wait_days"))}
