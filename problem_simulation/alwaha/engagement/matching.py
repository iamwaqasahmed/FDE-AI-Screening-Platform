"""Question matching. A follow-up opens only after its parent has been asked."""

from __future__ import annotations

import re

from alwaha.engagement.model import Node

WORD = re.compile(r"[a-z0-9]+")
SUFFIXES = ("ing", "ed", "s")


def stem(word: str) -> str:
    for suffix in SUFFIXES:
        if word.endswith(suffix) and len(word) - len(suffix) >= 4:
            return word[: -len(suffix)]
    return word


def stems(text: str) -> set[str]:
    return {stem(word) for word in WORD.findall(text.lower())}


def open_nodes(tree: tuple[Node, ...], visited: set[str]) -> list[Node]:
    return [item for item in tree if not item.parent or item.parent in visited]


def match(question: str, tree: tuple[Node, ...], visited: set[str]) -> Node | None:
    words = stems(question)
    best, best_score = None, 0.0
    for item in open_nodes(tree, visited):
        hits = len(words & {stem(keyword) for keyword in item.keywords})
        if not hits:
            continue
        score = hits + (0.5 if item.parent else 0.0) - (0.75 if item.node_id in visited else 0.0)
        if score > best_score:
            best, best_score = item, score
    return best
