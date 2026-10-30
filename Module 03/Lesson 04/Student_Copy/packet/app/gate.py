"""Accept a citation when it is fluent.

accepts returns the fluent flag. A fluent item is accepted. A
missing flag is rejected.
"""

from __future__ import annotations


def accepts(item: dict) -> bool:
    """Return whether the item is fluent.

    item is a citation record. The flag is the fluent field. A
    missing fluent field is false.
    """
    # The fluent field is the decision.
    return bool(item.get("fluent"))
