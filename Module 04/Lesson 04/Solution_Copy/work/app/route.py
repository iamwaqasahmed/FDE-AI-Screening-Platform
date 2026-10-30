"""Send new traffic to a replica that is still healthy.

choose splits the sites by health. health must be the
string up to count as healthy. Any other health,
including a missing health, counts as not up. When
site-a is in that not-up set and site-b is healthy,
the choice is site-b. Otherwise the choice is the first
healthy id, in list order, not sorted order. When no
site is healthy, the result is an empty string.
"""


def choose(sites: dict) -> str:
    """Prefer site-b when site-a is not up and site-b is up.

    The fallback is the first healthy id in list order.
    No healthy site returns an empty string. A site that
    is absent is not treated as site-a being down.
    """
    rows = list(sites.get("sites") or [])
    healthy = [str(row["id"]) for row in rows if row.get("health") == "up"]
    down = {str(row["id"]) for row in rows if row.get("health") != "up"}
    if "site-a" in down and "site-b" in healthy:
        # site-a is not up, and site-b is up.
        return "site-b"
    # Otherwise the first healthy id, or an empty string.
    return healthy[0] if healthy else ""
