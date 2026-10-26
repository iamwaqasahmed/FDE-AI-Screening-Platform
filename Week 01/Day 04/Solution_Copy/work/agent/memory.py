"""Session store for wf-self-service.

Facts stay inside one session. A later turn in that session can recall
them. A different session cannot.

A stored preference is returned only when consent allows it. When consent
does not allow it, preference returns an empty string. The caller then
leaves the preference string out of the trace.

Chapter 06 replaces the copy under work/agent. The starter's memory
kept nothing and ignored consent.
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
        # Hand back a copy. An unknown session is an empty dict.
        return dict(self._sessions.get(session, {}))

    def remember(self, session: str, **facts: object) -> None:
        """Merge facts into this session.

        A later remember for the same key replaces that fact.
        Other keys on the session stay.
        """
        # The first remember creates the session. Later keys replace only themselves.
        current = self._sessions.setdefault(session, {})
        current.update(facts)

    def preference(self, stored: str, allowed: bool) -> str:
        """Return the stored preference only when allowed is true.

        allowed comes from the scenario's consent flag. False means this
        later session may not reuse the preference. The stored string
        is not returned, so it cannot leak into the reply.
        """
        # This session may reuse the preference only when consent allows it.
        if not allowed:
            return ""
        return stored
