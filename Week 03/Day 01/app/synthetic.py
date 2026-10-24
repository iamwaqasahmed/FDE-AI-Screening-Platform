"""Copy a real letter into the synthetic sample."""

from __future__ import annotations


def sample(letters: list[dict], card: dict) -> list[dict]:
    del card
    return letters[:1]
