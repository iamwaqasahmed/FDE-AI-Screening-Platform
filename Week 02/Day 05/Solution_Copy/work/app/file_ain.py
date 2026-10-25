"""Keep yesterday's file when the night drop is missing.

Chapter 06 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell returns None when the night file is missing. While that
shell is the file that runs, the journey check says a missed night
cleared the slots.
"""

from __future__ import annotations


def apply_file(previous: dict | None, arrived: dict | None) -> dict | None:
    """Keep yesterday when the night file is missing.

    previous is the file already held. arrived is the file that
    landed tonight. None means the night drop did not arrive.
    A missing night returns previous. A file that arrived replaces it.
    """
    # A missed night leaves yesterday in place.
    if arrived is None:
        return previous
    # The last file wins. Today's file replaces yesterday.
    return arrived
