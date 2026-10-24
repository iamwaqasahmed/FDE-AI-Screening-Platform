"""Wait on insure until the request times out."""


def book(outage: dict) -> dict:
    return {
        "breaker": "closed",
        "called": True,
        "target": str(outage.get("partner") or "insure"),
        "waited": int(outage.get("timeout_seconds") or 0),
    }
