"""Restart in-flight work on v4, and treat every v4 as in force.

criteria ignores the start day. It returns the first document
for the specialty whose version is 4. Status is not read, so
any version 4 document is returned. When no document matches,
the result is an empty dict.
"""

from __future__ import annotations


def criteria(docs: list[dict], specialty: str, started: str) -> dict:
    """Return the first version 4 document for this specialty.

    docs is the document list. specialty must match the document
    specialty. started is discarded, so the start day does not
    choose the document. The first match is returned as it is.
    """
    # The start day is not part of this choice.
    del started
    for doc in docs:
        # Version 4 is enough. Status is not consulted.
        if doc.get("specialty") == specialty and doc.get("version") == 4:
            return doc
    # No version 4 for this specialty.
    return {}
