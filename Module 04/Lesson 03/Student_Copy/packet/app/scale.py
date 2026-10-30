"""Start when the peak arrives.

This is the starter. started returns peak_at from the
forecast as text. A missing peak_at becomes an empty
string. The sheet is discarded.
"""


def started(forecast: dict, sheet: dict) -> str:
    """Return the peak time unchanged. Ignore the sheet.

    peak_at is turned into a string. When it is missing,
    the result is an empty string.
    """
    # The sheet is unused. The peak is returned as given.
    del sheet
    return str(forecast.get("peak_at") or "")
