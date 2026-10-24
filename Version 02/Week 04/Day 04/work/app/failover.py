"""Resume in-flight approvals from the workflow store."""


def recover(drill: dict, rows: list) -> dict:
    pending = sorted(str(row["id"]) for row in rows if row.get("status") == "pending")
    return {"pending": pending, "seconds": int(drill["budget_seconds"]), "site": "site-b"}
