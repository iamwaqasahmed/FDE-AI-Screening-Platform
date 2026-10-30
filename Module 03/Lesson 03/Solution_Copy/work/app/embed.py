"""local-embed: a token vector, including codes.

tokens splits lower-case text into letter and digit pieces. A
hyphen keeps a code inside one token. codes returns the tokens
that contain a hyphen. embed maps each token to its share of
the text. nearness is cosine similarity. An empty side scores
zero.
"""

from __future__ import annotations

import re
from collections import Counter

# A token is letters or digits. A hyphen keeps a code in one token.
_TOKEN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def tokens(text: str) -> list[str]:
    """Return the tokens in text, in order.

    text is lower-cased before the pattern runs. Each match is
    one token. A hyphenated code stays together.
    """
    # Lower case, then keep every token the pattern finds.
    return _TOKEN.findall(text.lower())


def codes(text: str) -> list[str]:
    """Return the tokens that contain a hyphen, in order.

    text is tokenized the same way as embed. A token with no
    hyphen is left out.
    """
    # A code is a token that contains a hyphen.
    return [token for token in tokens(text) if "-" in token]


def embed(text: str) -> dict[str, float]:
    """Map each token to its share of the text.

    Repeated tokens are counted together. The divisor is the
    number of tokens, or one when the text has none. Text with
    no tokens returns an empty map.
    """
    # Each token's share of the text. An empty text still divides by one.
    counts = Counter(tokens(text))
    total = sum(counts.values()) or 1
    return {token: count / total for token, count in counts.items()}


def nearness(left: dict[str, float], right: dict[str, float]) -> float:
    """Return the cosine similarity of two token maps.

    left and right map tokens to weights. An empty map scores
    zero. A side whose squared weights sum to zero also scores
    zero. Otherwise the score is the shared weight divided by
    the two lengths.
    """
    # A missing side is not near. Otherwise this is cosine similarity.
    if not left or not right:
        return 0.0
    dot = sum(weight * right.get(token, 0.0) for token, weight in left.items())
    left_norm = sum(weight * weight for weight in left.values()) ** 0.5
    right_norm = sum(weight * weight for weight in right.values()) ** 0.5
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return dot / (left_norm * right_norm)
