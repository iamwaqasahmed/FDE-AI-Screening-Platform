"""Load the catalog into the shape the interview and the checker share."""

from __future__ import annotations

from alwaha.engagement.catalog import PERSONAS
from alwaha.engagement.model import Node

BUDGET = 12


def _as_persona(row: dict) -> dict:
    facts = tuple({"id": fact_id, "text": text, "must_surface": True} for fact_id, text in row["facts"])
    tree = tuple(
        Node(node_id, tuple(keywords), answer, tuple(releases), parent)
        for node_id, keywords, answer, releases, parent in row["tree"]
    )
    return {
        "id": row["id"],
        "card": {
            "name": row["name"],
            "role": row["role"],
            "says_first": row["says_first"],
            "goals": tuple(row["goals"]),
        },
        "facts": facts,
        "must_surface": tuple(fact["id"] for fact in facts),
        "banned": tuple(row["banned"]),
        "tree": tree,
    }


def load_personas() -> dict[str, dict]:
    personas = {row["id"]: _as_persona(row) for row in PERSONAS}
    problems = validate(personas)
    if problems:
        raise SystemExit("Persona catalog: " + "; ".join(problems))
    return personas


def validate(personas: dict[str, dict]) -> list[str]:
    problems = []
    if len(personas) != 12:
        problems.append(f"expected 12 personas, found {len(personas)}")
    for key, data in personas.items():
        node_ids = {node.node_id for node in data["tree"]}
        released: set[str] = set()
        for node in data["tree"]:
            released.update(node.releases)
            if node.parent and node.parent not in node_ids:
                problems.append(f"{key} node {node.node_id} has a missing parent")
            unknown = set(node.releases) - set(data["must_surface"])
            if unknown:
                problems.append(f"{key} releases unknown facts {sorted(unknown)}")
        missing = set(data["must_surface"]) - released
        if missing:
            problems.append(f"{key} never releases {sorted(missing)}")
    return problems
