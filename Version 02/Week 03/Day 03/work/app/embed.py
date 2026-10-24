"""local-embed: a token vector, including codes."""

from __future__ import annotations

import re
from collections import Counter

_TOKEN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def tokens(text: str) -> list[str]:
    return _TOKEN.findall(text.lower())


def codes(text: str) -> list[str]:
    return [token for token in tokens(text) if "-" in token]


def embed(text: str) -> dict[str, float]:
    counts = Counter(tokens(text))
    total = sum(counts.values()) or 1
    return {token: count / total for token, count in counts.items()}


def nearness(left: dict[str, float], right: dict[str, float]) -> float:
    if not left or not right:
        return 0.0
    dot = sum(weight * right.get(token, 0.0) for token, weight in left.items())
    left_norm = sum(weight * weight for weight in left.values()) ** 0.5
    right_norm = sum(weight * weight for weight in right.values()) ** 0.5
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return dot / (left_norm * right_norm)
