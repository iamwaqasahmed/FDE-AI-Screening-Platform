"""Accept a staff role. Refuse a service token.

Staff sign-in is for a person. The contact center sends an actor
with an id, a kind, and a role. kind "staff" is a person who works
here. kind "service" is a machine token. A machine token can carry
role "admin" and still must not pass as staff.

accept keeps the id and reports whether this login is staff.
A missing id is stored as an empty string. A missing kind is not staff.
"""


def accept(actor: dict) -> dict:
    """Record the id. Count the login as staff only when kind is staff.

    Role is not read. An admin role on a service token does not
    make that token a person.
    """
    # Keep the id for the audit row. An absent id stays blank.
    actor_id = str(actor.get("id") or "")
    # kind is the only staff test. "service" fails it.
    is_staff = actor.get("kind") == "staff"
    return {"actor": actor_id, "staff": is_staff}
