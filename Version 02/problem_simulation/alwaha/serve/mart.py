"""Read the wait-time extract. The clock column is not the wait figure."""

from __future__ import annotations

CLOCK = "booking_date"
WAIT = "wait_days"


def read(text: str) -> dict:
    lines = [line for line in text.splitlines() if line.strip()]
    header = lines[0].split(",")
    values = lines[1].split(",")
    row = dict(zip(header, values))
    return {"clock": CLOCK, "trusted": False, "wait": int(row[WAIT])}
