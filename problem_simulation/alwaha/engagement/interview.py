"""Run an interview. The participant command prints the answer and nothing else."""

from __future__ import annotations

from alwaha.engagement.matching import match
from alwaha.engagement.personas import BUDGET


def run(data: dict, questions: list[str], budget: int = BUDGET) -> list[dict]:
    texts = {fact["id"]: fact["text"] for fact in data["facts"]}
    visited: set[str] = set()
    turns = []
    for question in [line.strip() for line in questions if line.strip()][:budget]:
        found = match(question, data["tree"], visited)
        if found is None:
            turns.append({"question": question, "answer": data["card"]["says_first"], "released": []})
            continue
        fresh = [fact_id for fact_id in found.releases if found.node_id not in visited]
        visited.add(found.node_id)
        answer = " ".join([found.answer, *(texts[fact_id] for fact_id in fresh if texts[fact_id] not in found.answer)])
        turns.append({"question": question, "answer": answer, "released": fresh})
    return turns


def score_turns(data: dict, turns: list[dict]) -> dict:
    must = list(data["must_surface"])
    released = {fact_id for turn in turns for fact_id in turn["released"]}
    reached = [fact_id for fact_id in must if fact_id in released]
    missed = [fact_id for fact_id in must if fact_id not in released]
    return {"ok": not missed, "reached": reached, "missed": missed}


def winning_questions(data: dict) -> list[str]:
    """Parent before child. Used by tests, not by the participant command."""
    remaining = list(data["tree"])
    opened = {""}
    ordered = []
    while remaining:
        ready = sorted((node for node in remaining if node.parent in opened), key=lambda node: node.node_id)
        if not ready:
            raise ValueError(f"{data['id']} has a broken tree")
        node = ready[0]
        ordered.append(" ".join(node.keywords))
        opened.add(node.node_id)
        remaining.remove(node)
    return ordered
