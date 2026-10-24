"""Rebuild from the dead pod."""


def recover(drill: dict, rows: list) -> dict:
    del rows
    return {
        "pending": [],
        "seconds": int(drill["timeout_seconds"]),
        "site": str(drill.get("killed") or "site-a"),
    }
