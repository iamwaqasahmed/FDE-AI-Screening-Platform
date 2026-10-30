"""A patient sees public documents. Staff do not see restricted ones.

allow compares the document audience with the asker. A patient
sees a public document only. Staff see a public or staff
document. Records see a public, staff, or restricted document.
Any other asker sees nothing.
"""

from __future__ import annotations


def allow(doc: dict, asker: str) -> bool:
    """Return whether this asker may see the document.

    doc supplies the audience. A missing audience is empty text,
    which matches none of the allowed sets. asker selects the
    set. patient, staff, and records are the askers that can
    pass.
    """
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
