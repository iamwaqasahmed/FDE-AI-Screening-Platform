"""A patient sees public documents. Staff do not see restricted ones."""

from __future__ import annotations


def allow(doc: dict, asker: str) -> bool:
    audience = doc.get("audience", "")
    # A patient sees public only. Staff and restricted stay off this path.
    if asker == "patient":
        return audience == "public"
    # Staff see public and staff. Restricted stays off this path.
    if asker == "staff":
        return audience in {"public", "staff"}
    # Records see public, staff, and restricted.
    if asker == "records":
        return audience in {"public", "staff", "restricted"}
    # Any other asker sees nothing.
    return False
