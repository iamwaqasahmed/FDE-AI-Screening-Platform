"""dms. An unauthorized Ramadan circular is filed as public.

fault() returns that public-filing defect. The affected key is the unauthorized circular. The clean columns are the document id, the status, and the audience.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the document-store fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "dms",
        "unauthorized-public",
        ["doc:circ-ramadan-unauth"],
        ["doc_id", "status", "audience"],
    )
