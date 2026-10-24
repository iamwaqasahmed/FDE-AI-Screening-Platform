"""Stop a direct attack. Do not book."""


def stop(row: dict) -> dict:
    if str(row.get("family") or "") == "atk-direct":
        return {"blocked": True, "booked": False}
    return {"blocked": False, "booked": False}
