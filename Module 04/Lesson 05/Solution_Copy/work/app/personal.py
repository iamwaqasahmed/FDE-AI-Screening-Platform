"""Stop a direct attack. Do not book.

The personal lab sees one row. family "atk-direct" is a direct
attack. That row is blocked, and nothing is booked. Any other
family is not this attack. It is not blocked, and it is not booked
either. This function does not book a visit. The wording of the
attack is not read here.
"""


def stop(row: dict) -> dict:
    """Block a direct attack. Never set booked to true.

    The family is the only field that matters.
    """
    if str(row.get("family") or "") == "atk-direct":
        # A direct attack stops here. The visit is not booked.
        return {"blocked": True, "booked": False}
    # Anything else is outside this guard. Still do not book.
    return {"blocked": False, "booked": False}
