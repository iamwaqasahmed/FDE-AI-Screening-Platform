"""Let the attack book.

This is the starter. It ignores the row. blocked is false and
booked is true, so a direct attack is allowed through and a visit
is booked. The finished module blocks family atk-direct and does
not book.
"""


def stop(row: dict) -> dict:
    """Ignore the row. Let the visit book.

    family is not read, so a direct attack gets the same result
    as any other row.
    """
    # The argument is unused. The shell does not look at family.
    del row
    return {"blocked": False, "booked": True}
