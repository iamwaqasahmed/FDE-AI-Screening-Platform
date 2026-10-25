"""Start one cold start before the peak."""

from __future__ import annotations

from datetime import datetime, timedelta


def started(forecast: dict, sheet: dict) -> str:
    peak = datetime.fromisoformat(str(forecast["peak_at"]))
    cold = int(sheet["cold_start_seconds"])
    return (peak - timedelta(seconds=cold)).isoformat()
