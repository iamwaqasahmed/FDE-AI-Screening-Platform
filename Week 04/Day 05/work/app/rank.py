"""Return the first problem that has no blocker."""


def first(rows: list) -> str:
    opened = [str(row["id"]) for row in rows if not row.get("blockers")]
    return opened[0] if opened else ""
