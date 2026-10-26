"""Session store that keeps a session and honors consent. The Day 4 tests copy this over the skeleton.

Facts stay inside one session. A later turn in that session can recall
them. A different session cannot.

A stored preference is returned only when consent allows it. When consent
does not allow it, preference returns an empty string. The caller then
leaves the preference string out of the trace.
"""

from __future__ import annotations


class Memory:
    """Facts keyed by session id."""

    def __init__(self) -> None:
        """Start with no sessions."""
        self._sessions: dict[str, dict] = {}

    def recall(self, session: str) -> dict:
        """Return a copy of the facts stored for this session.

        The copy means a caller cannot change the store by editing the dict
        it received. An unknown session returns an empty dict.
        """
        return dict(self._sessions.get(session, {}))

    def remember(self, session: str, **facts: object) -> None:
        """Merge facts into this session.

        A later remember for the same key replaces that fact.
        Other keys on the session stay.
        """
        current = self._sessions.setdefault(session, {})
        current.update(facts)

    def preference(self, stored: str, allowed: bool) -> str:
        """Return the stored preference only when allowed is true.

        allowed is the consent flag. When it is false, the stored string
        is withheld. When it is true, the stored string is returned.
        """
        if not allowed:
            return ""
        return stored
