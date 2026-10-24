"""Open the breaker and leave the partner uncalled."""


def book(outage: dict) -> dict:
    if str(outage.get("status")) == "down":
        return {"breaker": "open", "called": False, "target": "rules-worker", "waited": 0}
    return {
        "breaker": "closed",
        "called": True,
        "target": str(outage.get("partner") or ""),
        "waited": 0,
    }
