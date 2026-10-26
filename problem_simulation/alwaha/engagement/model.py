"""A persona node.
Keywords open it. Releases names the facts it may say.

One node is one step in an interview. Matching opens it from the keywords, the interview says the answer, and the releases name facts that step may reveal.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    """One step in a persona's question tree.

    node_id identifies the step. keywords are the words that open it.
    answer is what the persona says. releases names fact ids revealed
    the first time this step is visited. parent is the step that must
    already have been asked. An empty parent is a root and can match
    on the first question.
    """

    node_id: str
    keywords: tuple[str, ...]
    answer: str
    releases: tuple[str, ...] = ()
    parent: str = ""
