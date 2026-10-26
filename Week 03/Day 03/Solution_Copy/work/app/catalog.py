"""Answer a preparation question from the service catalog.

lookup finds the catalog row whose clinic matches, and returns
that clinic with the row's preparation text. The result has no
document id.
"""

from __future__ import annotations


def lookup(rows: list[dict], clinic: str) -> dict:
    """Return the preparation text for this clinic.

    rows are catalog entries. clinic is the name to match. The
    first matching row supplies prep. The clinic in the result
    is the one that was asked for. A clinic with no row raises,
    because next() requires a match.
    """
    # The row whose clinic matches. The answer does not carry a document id.
    row = next(item for item in rows if item["clinic"] == clinic)
    return {"clinic": clinic, "prep": row["prep"]}
