"""Word-overlap score. screened and screening count as the same word."""

from __future__ import annotations

import re
from collections import Counter

from screening_retrieval.chunks import Chunk

STOP = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "the",
    "this",
    "to",
    "with",
}


def stem(word: str) -> str:
    for suffix in ("ing", "ed", "es", "s"):
        if len(word) > len(suffix) + 3 and word.endswith(suffix):
            return word[: -len(suffix)]
    return word


def tokens(text: str) -> list[str]:
    words = re.findall(r"[a-z0-9]+", text.lower())
    return [stem(word) for word in words if word not in STOP]


def overlap(question: str, chunk: Chunk, weights: dict[str, float] | None = None) -> tuple[int, float]:
    question_terms = set(tokens(question))
    counts = Counter(tokens(chunk.text))
    matched = [term for term in question_terms if counts[term]]
    scale = weights or {}
    weighted = sum(scale.get(term, 1.0) * counts[term] for term in matched)
    return (len(matched), weighted)


def weights_for(chunks: list[Chunk]) -> dict[str, float]:
    """Rare words count more, so 'model' beats a heading that only says 'what' and 'do'."""
    seen: Counter[str] = Counter()
    for chunk in chunks:
        seen.update(set(tokens(chunk.text)))
    total = max(len(chunks), 1)
    return {term: total / count for term, count in seen.items()}
