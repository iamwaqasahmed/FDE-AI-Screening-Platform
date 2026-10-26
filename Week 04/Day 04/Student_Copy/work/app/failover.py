"""Rebuild from the dead pod.

This is the starter. The rows are discarded, so pending
is always an empty list. seconds is timeout_seconds
from the drill. site is the killed name, or site-a when
killed is missing.
"""


def recover(drill: dict, rows: list) -> dict:
    """Drop the rows. Report the timeout and the killed site.

    pending is empty. A missing killed value becomes site-a.
    """
    # The workflow rows are unused.
    del rows
    return {
        "pending": [],
        "seconds": int(drill["timeout_seconds"]),
        "site": str(drill.get("killed") or "site-a"),
    }
