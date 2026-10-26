"""Reference decisions for rel-w4d4.
Participant copies do not import this module.

choose sends traffic to the backup when the primary is down. confirm keeps a model only when its hash is the registered one. book refuses a down partner. reply falls back by kind when the model is down. choice and arrival compare purchase and rental with the deadline. split prices each hospital's own share.
"""

from __future__ import annotations

from datetime import date, timedelta


def placed(sites: dict) -> list[str]:
    """Return the site ids in sorted order. A missing site list is treated as no sites."""
    return sorted(str(row["id"]) for row in sites.get("sites") or [])


def choose(sites: dict) -> str:
    """Return the site that should serve.

    When the primary is down and the backup is healthy, the backup takes over. Otherwise the first healthy site serves. No healthy site returns an empty id.
    """
    rows = list(sites.get("sites") or [])
    healthy = [str(row["id"]) for row in rows if row.get("health") == "up"]
    down = {str(row["id"]) for row in rows if row.get("health") != "up"}
    # The named backup takes over only when the primary is the one that is down.
    if "site-a" in down and "site-b" in healthy:
        return "site-b"
    # Any other healthy site can serve. None healthy means nowhere to send the call.
    return healthy[0] if healthy else ""


def pending_ids(rows: list[dict]) -> list[str]:
    """Return the ids that are still pending, in sorted order. Other statuses are left out."""
    return sorted(str(row["id"]) for row in rows if row.get("status") == "pending")


def recover(drill: dict, rows: list[dict]) -> dict:
    """Return the pending approvals, the drill budget, and the site that takes over."""
    return {"pending": pending_ids(rows), "seconds": int(drill["budget_seconds"]), "site": "site-b"}


def confirm(site: dict, register: list[dict]) -> list[str]:
    """Return the model ids whose hash matches the register, in sorted order.

    An id that is missing from the register, or present with a different hash, is dropped. That is how the lookalike is excluded after failover.
    """
    approved = {str(row["id"]): str(row["hash"]) for row in register}
    kept = [
        str(model["id"])
        for model in site.get("models") or []
        # The id must be registered, and the hash must be that registration's hash.
        if approved.get(str(model.get("id"))) == str(model.get("hash"))
    ]
    return sorted(kept)


def book(outage: dict) -> dict:
    """Return whether the partner was called.

    A down partner is not called. The breaker stays open and the rules worker is the target. An up partner is called with the breaker closed.
    """
    # A down partner is not called. The rules worker answers instead.
    if str(outage.get("status")) == "down":
        return {"breaker": "open", "called": False, "target": "rules-worker", "waited": 0}
    return {"breaker": "closed", "called": True, "target": str(outage.get("partner") or ""), "waited": 0}


def reply(row: dict, model_up: bool) -> dict:
    """Return the body and the mode that produced it.

    While the model is up, every kind is answered by the model. While it is down, a status row still returns its stored text, and any other kind goes to the rules worker.
    """
    text = str(row.get("text") or "")
    # The model answers every kind while it is up.
    if model_up:
        return {"body": text, "mode": "model"}
    # Status can still be read from the stored text when the model is down.
    if row.get("kind") == "status":
        return {"body": text, "mode": "status"}
    # Booking and anything else go to the rules worker instead of inventing a model answer.
    return {"body": "rules-worker", "mode": "rules-worker"}


def choice(note: dict) -> str:
    """Return which route meets the deadline.

    A purchase that arrives by the deadline is chosen first. Otherwise a rental that arrives by the deadline is chosen. If neither date works, the result is still the purchase route.
    """
    start = date.fromisoformat(str(note["ordered_on"]))
    deadline = date.fromisoformat(str(note["deadline"]))
    bought = start + timedelta(weeks=int(note["purchase_weeks"]))
    rented = start + timedelta(days=int(note["rent_days"]))
    # A purchase that arrives by the deadline is the route.
    if bought <= deadline:
        return "buy"
    # Otherwise rent, when the rental also meets the deadline.
    if rented <= deadline:
        return "rent"
    # Neither date works. The caller still receives the purchase route.
    return "buy"


def arrival(note: dict, route: str) -> str:
    """Return the arrival date for the route. A purchase adds weeks. Any other route adds the rental days.

    The steps start at the order date and add the purchase length or the rental length for the chosen route, and the hidden figures stay in this file and are not copied into a new comment.
    """
    start = date.fromisoformat(str(note["ordered_on"]))
    if route == "buy":
        return (start + timedelta(weeks=int(note["purchase_weeks"]))).isoformat()
    return (start + timedelta(days=int(note["rent_days"]))).isoformat()


def split(sheet: dict, price_per_1k: int) -> dict[str, int]:
    """Return each hospital's cost from that hospital's own referrals, the shared token count, and the price.

    The steps scale each hospital's referrals by the shared token count and the price, and the hidden figures stay in this file and are not copied into a new comment.
    """
    tokens = int(sheet["tokens_per_referral"])
    return {
        str(row["hospital"]): int(row["referrals"]) * tokens * int(price_per_1k) // 1000
        for row in sheet["shares"]
    }
