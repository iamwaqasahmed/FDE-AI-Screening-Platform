"""Open the breaker and leave the partner uncalled.

book reads status. When status is down, the breaker is
open, called is false, the target is rules-worker, and
waited is 0. The partner name is not used on that path.
Any other status, including a missing status, leaves the
breaker closed, sets called to true, and uses the partner
name. A missing partner becomes an empty string. waited
is 0 on that path too.
"""


def book(outage: dict) -> dict:
    """Open the breaker when status is down. Otherwise call the partner.

    The down path targets rules-worker and does not call
    the partner. The other path targets the partner.
    waited is 0 either way.
    """
    # A down partner is not called.
    if str(outage.get("status")) == "down":
        return {"breaker": "open", "called": False, "target": "rules-worker", "waited": 0}
    return {
        "breaker": "closed",
        "called": True,
        "target": str(outage.get("partner") or ""),
        "waited": 0,
    }
