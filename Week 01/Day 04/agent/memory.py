"""Session store. The starter keeps nothing."""

from __future__ import annotations


class Memory:
    def recall(self, session: str) -> dict:
        _ = session
        return {}

    def remember(self, session: str, **facts: object) -> None:
        _ = (session, facts)

    def preference(self, stored: str, allowed: bool) -> str:
        _ = allowed
        return stored
