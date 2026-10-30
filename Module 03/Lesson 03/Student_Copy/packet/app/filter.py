"""Keep every audience, including a staff document for a patient.

allow does not read the document or the asker. It returns true
for every pair, so each asker passes with each audience.
"""

from __future__ import annotations


def allow(doc: dict, asker: str) -> bool:
    """Allow the document for this asker.

    doc and asker are discarded. The audience is not compared
    with the asker.
    """
    del doc, asker
    return True
