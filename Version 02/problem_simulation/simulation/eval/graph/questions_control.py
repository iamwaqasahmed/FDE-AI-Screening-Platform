"""Single-hop notice questions. Keyword retrieval already answers these."""

from __future__ import annotations

from simulation.eval.graph.question import cite, make
from simulation.world.timeline import TIMELINE

SKIP = {"INC-0233", "CHG-0158"}


def cases(world: dict) -> list[dict]:
    found = []
    for item in TIMELINE:
        if item.ref in SKIP or item.kind == "freeze":
            continue
        document_id = f"notice-{item.ref.lower()}"
        if document_id not in world["catalog"] and document_id not in world["rendered"]:
            continue
        question = f"What cause was recorded for {item.ref}?"
        expected = {"must_mention": [[item.cause]], "must_not_claim": []}
        visit = [document_id]
        found.append(make(f"control-{len(found):02d}", question, expected, "written", "control", (),
                           _citation(world, document_id), "lookup", visit))
        if len(found) == 6:
            break
    return found


def _citation(world: dict, document_id: str) -> dict:
    if document_id in world["catalog"]:
        return cite(world["catalog"][document_id])
    return cite_rendered(world, document_id)


def cite_rendered(world: dict, document_id: str) -> dict:
    from simulation.policy.parse import parse_header
    header = parse_header(world["rendered"][document_id])
    return {
        "document_id": document_id,
        "version": header.get("version", ""),
        "status": header.get("status", ""),
        "effective": header.get("effective", ""),
        "sunset": header.get("sunset", "") or "",
        "site": header.get("site", ""),
        "clause_id": document_id,
    }
