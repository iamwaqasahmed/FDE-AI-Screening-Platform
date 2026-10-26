"""Wait on insure until the request times out.

This is the starter. book does not branch. The breaker
stays closed, called stays true, and waited is
timeout_seconds. When timeout_seconds is missing,
waited is 0. The target is the partner, or insure when
the partner is missing.
"""


def book(outage: dict) -> dict:
    """Call the partner and wait out the timeout. Leave the breaker closed.

    A missing partner becomes insure. A missing timeout
    becomes 0.
    """
    # Always call. The breaker stays closed and the wait is the timeout.
    return {
        "breaker": "closed",
        "called": True,
        "target": str(outage.get("partner") or "insure"),
        "waited": int(outage.get("timeout_seconds") or 0),
    }
