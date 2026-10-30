"""Call the model for a cached public answer.

This is the starter. The store is discarded. answer
always returns the row text and a call count of 1.
A missing text becomes an empty string. A stored body
is never read.
"""


def answer(store: dict, row: dict) -> dict:
    """Ignore the store. Return the row text and one call.

    calls is 1 for every row. A missing text becomes an
    empty string.
    """
    # The store is unused, so every row spends a call.
    del store
    return {"body": str(row.get("text") or ""), "calls": 1}
