"""Ignore the tokens. Every text has the same vector.

codes returns an empty list. embed returns one fixed weight
under the shell key. nearness returns the same score for every
pair, so two texts are always equally near.
"""

from __future__ import annotations


def codes(text: str) -> list[str]:
    """Return no codes.

    text is discarded. A hyphenated token in the text is not
    collected.
    """
    del text
    return []


def embed(text: str) -> dict[str, float]:
    """Return the same one-key vector for every text.

    text is discarded. The only key is shell, and its weight
    is one.
    """
    del text
    return {"shell": 1.0}


def nearness(left: dict[str, float], right: dict[str, float]) -> float:
    """Return the same score for every pair of vectors.

    left and right are discarded. The score is one, including
    when a side is empty.
    """
    del left, right
    return 1.0
