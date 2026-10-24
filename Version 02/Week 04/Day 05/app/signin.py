"""Treat every token as staff."""


def accept(actor: dict) -> dict:
    return {"actor": str(actor.get("id") or ""), "staff": True}
