"""Question matching.
A follow-up opens only after its parent has been asked.

The interview passes the question, the persona's tree, and the nodes already visited. match returns the open node that fits best, or nothing when no open node shares a keyword.
"""

from __future__ import annotations

import re

from alwaha.engagement.model import Node

WORD = re.compile(r"[a-z0-9]+")
SUFFIXES = ("ing", "ed", "s")


def stem(word: str) -> str:
    """Return the word with one trailing suffix removed, when the remainder is still a real stem.

    Only the first matching suffix is removed. A remainder that would be too short is left alone, so tiny words are not stripped to nothing.
    """
    for suffix in SUFFIXES:
        # A short remainder would not be a useful stem, so the suffix stays on the word.
        if word.endswith(suffix) and len(word) - len(suffix) >= 4:
            return word[: -len(suffix)]
    return word


def stems(text: str) -> set[str]:
    """Return the stemmed words in the text, lowercased, with punctuation dropped."""
    return {stem(word) for word in WORD.findall(text.lower())}


def open_nodes(tree: tuple[Node, ...], visited: set[str]) -> list[Node]:
    """Return nodes a question is allowed to hit.

    A root is always open. A follow-up stays closed until its parent has already been asked.
    """
    # A root has no parent. A follow-up waits until that parent is in the visited set.
    return [item for item in tree if not item.parent or item.parent in visited]


def match(question: str, tree: tuple[Node, ...], visited: set[str]) -> Node | None:
    """Return the open node that best fits the question, or nothing when no open node shares a keyword.

    More shared stems rank higher. A follow-up beats a root with the same number of hits. A node already visited ranks behind a new one. A tie keeps the earlier open node.
    """
    words = stems(question)
    best, best_score = None, 0.0
    for item in open_nodes(tree, visited):
        hits = len(words & {stem(keyword) for keyword in item.keywords})
        # No shared stem means this node is not an answer to the question.
        if not hits:
            continue
        # A follow-up outranks a root with the same hits. A node already used is pushed behind a new one.
        score = hits + (0.5 if item.parent else 0.0) - (0.75 if item.node_id in visited else 0.0)
        # Strictly greater, so an equal score keeps the node found earlier.
        if score > best_score:
            best, best_score = item, score
    return best
