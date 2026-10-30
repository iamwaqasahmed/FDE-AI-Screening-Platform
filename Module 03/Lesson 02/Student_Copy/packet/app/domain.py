"""Train on every row, including the extraction letters.

keep copies the whole list and returns it in the same order. A
row that carries an item id stays beside a row that does not.
Nothing is filtered.
"""

from __future__ import annotations


def keep(rows: list[dict]) -> list[dict]:
    """Return every row, in the same order.

    rows may mix domain lines and extraction letters. This
    function does not look at keys. The new list holds the same
    row objects.
    """
    # A new list, with every row kept.
    return list(rows)
