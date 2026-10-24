"""Accept a staff role. Refuse a service token."""


def accept(actor: dict) -> dict:
    return {"actor": str(actor.get("id") or ""), "staff": actor.get("kind") == "staff"}
