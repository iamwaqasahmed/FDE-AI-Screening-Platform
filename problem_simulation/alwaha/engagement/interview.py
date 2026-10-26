"""Run an interview.
The participant command prints the answer and nothing else.

run asks a persona's tree and returns the turns. score_turns checks whether the required facts were released. winning_questions builds an order the tests can ask. The participant command uses run and prints answers only.
"""

from __future__ import annotations

from alwaha.engagement.matching import match
from alwaha.engagement.personas import BUDGET


def run(data: dict, questions: list[str], budget: int = BUDGET) -> list[dict]:
    """Ask one persona and return the turns.

    Blank lines are dropped, and the list stops at the budget. Each turn has the question, the answer, and the fact ids released on that turn. A question that matches nothing gets the opening line and releases nothing. A match says the node answer and, the first time that node is visited, appends released fact text that is not already in the answer.
    """
    texts = {fact["id"]: fact["text"] for fact in data["facts"]}
    visited: set[str] = set()
    turns = []
    for question in [line.strip() for line in questions if line.strip()][:budget]:
        found = match(question, data["tree"], visited)
        # Nothing open shared a keyword, so the persona repeats the opening line.
        if found is None:
            turns.append({"question": question, "answer": data["card"]["says_first"], "released": []})
            continue
        # Facts on this node are released only the first time the node is visited.
        fresh = [fact_id for fact_id in found.releases if found.node_id not in visited]
        visited.add(found.node_id)
        # Fact text already inside the answer is not spoken a second time.
        answer = " ".join([found.answer, *(texts[fact_id] for fact_id in fresh if texts[fact_id] not in found.answer)])
        turns.append({"question": question, "answer": answer, "released": fresh})
    return turns


def score_turns(data: dict, turns: list[dict]) -> dict:
    """Return whether the required facts were released.

    ok is true only when nothing required is missing. reached keeps the required ids that appeared, in the catalog order. missed keeps the required ids that never appeared.
    """
    must = list(data["must_surface"])
    released = {fact_id for turn in turns for fact_id in turn["released"]}
    reached = [fact_id for fact_id in must if fact_id in released]
    missed = [fact_id for fact_id in must if fact_id not in released]
    return {"ok": not missed, "reached": reached, "missed": missed}


def winning_questions(data: dict) -> list[str]:
    """Parent before child. Used by tests, not by the participant command.

    Return one keyword string per node, in an order that can open the whole tree. A parent is asked before its children. Siblings are taken in node-id order. The empty string starts the opened set so roots, whose parent is empty, are ready immediately.
    """
    remaining = list(data["tree"])
    opened = {""}
    ordered = []
    while remaining:
        ready = sorted((node for node in remaining if node.parent in opened), key=lambda node: node.node_id)
        # A node whose parent is never opened cannot be ordered.
        if not ready:
            raise ValueError(f"{data['id']} has a broken tree")
        node = ready[0]
        ordered.append(" ".join(node.keywords))
        opened.add(node.node_id)
        remaining.remove(node)
    return ordered
