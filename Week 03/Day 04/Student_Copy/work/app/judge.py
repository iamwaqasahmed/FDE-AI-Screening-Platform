"""Mark a citation correct when it is fluent.

mark returns the fluent field. A fluent item is a pass. A missing
fluent field is not a pass.
"""

from __future__ import annotations


def mark(item: dict) -> bool:
    """Return whether the item is fluent.

    item is a citation record. The flag is the fluent field.
    """
    # The fluent field is the mark.
    return bool(item.get("fluent"))
