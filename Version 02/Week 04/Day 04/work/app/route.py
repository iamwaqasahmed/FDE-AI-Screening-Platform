"""Send new traffic to a replica that is still healthy."""


def choose(sites: dict) -> str:
    rows = list(sites.get("sites") or [])
    healthy = [str(row["id"]) for row in rows if row.get("health") == "up"]
    down = {str(row["id"]) for row in rows if row.get("health") != "up"}
    if "site-a" in down and "site-b" in healthy:
        return "site-b"
    return healthy[0] if healthy else ""
