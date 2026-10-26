"""Return the first problem that has no blocker.

The value model lists problems in order. A problem with a blocker
cannot start. The start is the first row whose blocker list is
empty. If every row is blocked, there is nothing to start, and
the result is blank.
"""


def first(rows: list) -> str:
    """Walk the rows in order. Return the first id with no blockers.

    An empty blocker list means the problem can open. This function
    does not sort again. It keeps the model's order and skips a row
    that still names a blocker.
    """
    opened = [str(row["id"]) for row in rows if not row.get("blockers")]
    # The first open id is the start. No open row means a blank start.
    return opened[0] if opened else ""
