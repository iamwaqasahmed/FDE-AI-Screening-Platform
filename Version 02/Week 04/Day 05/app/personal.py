"""Let the attack book."""


def stop(row: dict) -> dict:
    del row
    return {"blocked": False, "booked": True}
