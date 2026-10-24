"""Reference decisions for rel-w4d4. Participant copies do not import this module."""

from __future__ import annotations

from datetime import date, timedelta


def placed(sites: dict) -> list[str]:
    return sorted(str(row["id"]) for row in sites.get("sites") or [])


def choose(sites: dict) -> str:
    rows = list(sites.get("sites") or [])
    healthy = [str(row["id"]) for row in rows if row.get("health") == "up"]
    down = {str(row["id"]) for row in rows if row.get("health") != "up"}
    if "site-a" in down and "site-b" in healthy:
        return "site-b"
    return healthy[0] if healthy else ""


def pending_ids(rows: list[dict]) -> list[str]:
    return sorted(str(row["id"]) for row in rows if row.get("status") == "pending")


def recover(drill: dict, rows: list[dict]) -> dict:
    return {"pending": pending_ids(rows), "seconds": int(drill["budget_seconds"]), "site": "site-b"}


def confirm(site: dict, register: list[dict]) -> list[str]:
    approved = {str(row["id"]): str(row["hash"]) for row in register}
    kept = [
        str(model["id"])
        for model in site.get("models") or []
        if approved.get(str(model.get("id"))) == str(model.get("hash"))
    ]
    return sorted(kept)


def book(outage: dict) -> dict:
    if str(outage.get("status")) == "down":
        return {"breaker": "open", "called": False, "target": "rules-worker", "waited": 0}
    return {"breaker": "closed", "called": True, "target": str(outage.get("partner") or ""), "waited": 0}


def reply(row: dict, model_up: bool) -> dict:
    text = str(row.get("text") or "")
    if model_up:
        return {"body": text, "mode": "model"}
    if row.get("kind") == "status":
        return {"body": text, "mode": "status"}
    return {"body": "rules-worker", "mode": "rules-worker"}


def choice(note: dict) -> str:
    start = date.fromisoformat(str(note["ordered_on"]))
    deadline = date.fromisoformat(str(note["deadline"]))
    bought = start + timedelta(weeks=int(note["purchase_weeks"]))
    rented = start + timedelta(days=int(note["rent_days"]))
    if bought <= deadline:
        return "buy"
    if rented <= deadline:
        return "rent"
    return "buy"


def arrival(note: dict, route: str) -> str:
    start = date.fromisoformat(str(note["ordered_on"]))
    if route == "buy":
        return (start + timedelta(weeks=int(note["purchase_weeks"]))).isoformat()
    return (start + timedelta(days=int(note["rent_days"]))).isoformat()


def split(sheet: dict, price_per_1k: int) -> dict[str, int]:
    tokens = int(sheet["tokens_per_referral"])
    return {
        str(row["hospital"]): int(row["referrals"]) * tokens * int(price_per_1k) // 1000
        for row in sheet["shares"]
    }
