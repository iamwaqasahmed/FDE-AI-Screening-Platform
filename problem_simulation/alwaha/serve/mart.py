"""Read the wait-time extract. The clock column is not the wait figure.

read() skips blank lines, takes the next line as the header and the line after that as the row, and returns the wait from the wait column. trusted is false because the clock column is the booking date, not the wait.
"""

from __future__ import annotations

CLOCK = "booking_date"
WAIT = "wait_days"


def read(text: str) -> dict:
    """Return the clock column name, trusted false, and the wait from the wait column.

    Blank lines are dropped. The reader expects a header and one data row. trusted stays false because the date column is not the wait figure.
    """
    # A blank line is not a row. A trailing break must not become the header.
    lines = [line for line in text.splitlines() if line.strip()]
    header = lines[0].split(",")
    values = lines[1].split(",")
    row = dict(zip(header, values))
    return {"clock": CLOCK, "trusted": False, "wait": int(row[WAIT])}
