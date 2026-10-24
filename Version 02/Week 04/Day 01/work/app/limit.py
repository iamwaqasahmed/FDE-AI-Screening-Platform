"""Hold a session to a token cap and expire a slot hoard."""

from __future__ import annotations

TOKEN_CAP = 800
HOLD_CAP = 3


def admit(event: dict) -> bool:
    if event.get("family") == "atk-tokens":
        return int(event.get("tokens") or 0) <= TOKEN_CAP
    if event.get("family") == "atk-hoard":
        return int(event.get("holds") or 0) <= HOLD_CAP
    return True
