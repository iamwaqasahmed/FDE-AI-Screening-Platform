"""Allow the session and the holds.

admit discards the event and returns true on every call. No count is
compared, and no family is refused.
"""

from __future__ import annotations


def admit(event: dict) -> bool:
    """Admit every event.

    The argument is discarded. The result does not depend on its fields.
    """
    # The event is unused. del only drops this local name.
    del event
    return True
