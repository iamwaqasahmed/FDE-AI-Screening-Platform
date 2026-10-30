"""Treat every token as staff.

This is the starter. It keeps the id, then marks the login as staff
without reading kind. A service token is a machine login. This shell
still accepts it. The finished module accepts a login only when
kind is staff, and it refuses a machine token.
"""


def accept(actor: dict) -> dict:
    """Record the id and mark every login as staff.

    kind and role are ignored. A service token gets the same result
    as a coordinator.
    """
    # Keep the id for the row. An absent id stays blank.
    actor_id = str(actor.get("id") or "")
    # The shell does not look at kind, so a machine token is marked staff.
    return {"actor": actor_id, "staff": True}
