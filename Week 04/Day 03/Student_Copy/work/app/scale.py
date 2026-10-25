"""Start when the peak arrives."""


def started(forecast: dict, sheet: dict) -> str:
    del sheet
    return str(forecast.get("peak_at") or "")
