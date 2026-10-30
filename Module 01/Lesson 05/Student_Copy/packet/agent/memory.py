"""Session store. The starter keeps nothing.

Chapter 06 replaces the copy under work/. Leave this packet copy unchanged.

recall always returns an empty dict, so a hospital named on an earlier
turn is gone by the next turn. remember discards the facts it is given.
preference returns the stored string and ignores the consent flag,
so a later session can reuse a preference the patient did not allow.

The Lesson 4 scenarios still have to pass today. They need a store that
keeps a session and honors consent. This file does not.
"""

from __future__ import annotations


class Memory:
    """A store with the three methods the model calls. This one stores nothing."""

    def recall(self, session: str) -> dict:
        """Return what this session remembers. The starter remembers nothing."""
        _ = session
        return {}

    def remember(self, session: str, **facts: object) -> None:
        """Accept facts for a session, then drop them."""
        _ = (session, facts)

    def preference(self, stored: str, allowed: bool) -> str:
        """Return the stored preference. The allowed flag is ignored."""
        _ = allowed
        return stored
