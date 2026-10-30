"""Start one cold start before the peak.

started reads peak_at from the forecast and
cold_start_seconds from the sheet. It moves the peak
earlier by that many seconds and returns the new time
with isoformat.
"""

from __future__ import annotations

from datetime import datetime, timedelta


def started(forecast: dict, sheet: dict) -> str:
    """Return the peak time minus the cold-start seconds.

    peak_at is parsed as a date and time. cold_start_seconds
    is a whole number of seconds. The return value is isoformat.
    """
    peak = datetime.fromisoformat(str(forecast["peak_at"]))
    cold = int(sheet["cold_start_seconds"])
    # Lead the peak by the cold start on the sheet.
    return (peak - timedelta(seconds=cold)).isoformat()
