"""Session store that keeps a session and honors consent. The Day 4 tests copy this over the skeleton."""

from __future__ import annotations


class Memory:
    def __init__(self) -> None:
        self._sessions: dict[str, dict] = {}

    def recall(self, session: str) -> dict:
        return dict(self._sessions.get(session, {}))

    def remember(self, session: str, **facts: object) -> None:
        current = self._sessions.setdefault(session, {})
        current.update(facts)

    def preference(self, stored: str, allowed: bool) -> str:
        if not allowed:
            return ""
        return stored
