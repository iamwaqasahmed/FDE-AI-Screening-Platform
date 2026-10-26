"""Return an empty index.

build discards the documents and returns a list with no rows.
No clause is stored, and no vector is stored.
"""

from __future__ import annotations


def build(docs: list[dict]) -> list[dict]:
    """Return no rows.

    docs is discarded. The documents are not split into clauses,
    and their text is not embedded.
    """
    del docs
    return []
