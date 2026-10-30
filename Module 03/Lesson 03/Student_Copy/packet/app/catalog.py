"""Cite the leaflet instead of the service catalog row.

lookup ignores the catalog rows. It returns the clinic that was
asked for, the leaflet document id, and an empty preparation
string.
"""

from __future__ import annotations


def lookup(rows: list[dict], clinic: str) -> dict:
    """Return a leaflet citation for the clinic.

    rows is discarded, so no catalog preparation text is used.
    clinic is copied into the result. The document id is the
    leaflet. prep is empty.
    """
    # The catalog rows are not searched.
    del rows
    return {"clinic": clinic, "doc_id": "leaflet-prep", "prep": ""}
