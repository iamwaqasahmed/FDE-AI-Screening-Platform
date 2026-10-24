"""A persona node. Keywords open it. Releases names the facts it may say."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    node_id: str
    keywords: tuple[str, ...]
    answer: str
    releases: tuple[str, ...] = ()
    parent: str = ""
