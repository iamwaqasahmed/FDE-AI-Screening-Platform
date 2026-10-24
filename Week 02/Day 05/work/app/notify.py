"""Leave a queued booking queued when the notice fails."""

from __future__ import annotations


def notify(status: str, sent: bool) -> str:
    del sent
    if status == "queued":
        return "queued"
    return status
