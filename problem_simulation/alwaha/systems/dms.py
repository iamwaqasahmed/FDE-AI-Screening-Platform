"""dms. An unauthorized Ramadan circular is filed as public."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "dms",
        "unauthorized-public",
        ["doc:circ-ramadan-unauth"],
        ["doc_id", "status", "audience"],
    )
