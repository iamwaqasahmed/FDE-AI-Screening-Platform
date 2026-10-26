"""Resume in-flight approvals from the workflow store.

recover keeps ids whose status is pending, sorts those
ids, and returns them under pending. seconds is
budget_seconds from the drill. site is site-b. A row
that is not pending is left out. A row with no status
is left out.
"""


def recover(drill: dict, rows: list) -> dict:
    """Return the sorted pending ids, the budget, and site-b.

    Only status pending is kept. seconds is the drill
    budget as an integer. site is always site-b.
    """
    pending = sorted(str(row["id"]) for row in rows if row.get("status") == "pending")
    # Resume on site-b, inside the drill budget.
    return {"pending": pending, "seconds": int(drill["budget_seconds"]), "site": "site-b"}
