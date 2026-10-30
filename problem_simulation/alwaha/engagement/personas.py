"""Load the catalog into the shape the interview and the checker share.

Each catalog row becomes a public card, fact records, the fact ids that must surface, the banned sentences, and a tree of nodes. load_personas refuses to return a catalog that fails validate.
"""

from __future__ import annotations

from alwaha.engagement.catalog import PERSONAS
from alwaha.engagement.model import Node
from alwaha.engagement.m04_l05_asks import extend

BUDGET = 12


def _fact(entry: tuple) -> dict:
    """Return one fact record.

    A pair is an id and text that the checker requires. A third value is the explicit surface flag, used when the fact may be said but is not required.
    """
    # A pair has no flag, so the fact is required. A longer entry carries the flag itself.
    if len(entry) == 2:
        fact_id, text = entry
        surface = True
    else:
        fact_id, text, surface = entry
    return {"id": fact_id, "text": text, "must_surface": bool(surface)}


def _as_persona(row: dict) -> dict:
    """Return the interview shape for one catalog row.

    The card keeps the public fields. must_surface lists fact ids whose flag is set. The tree becomes nodes in the catalog's row order.
    """
    # Each catalog fact becomes a record. A pair is required; a longer entry carries its own flag.
    facts = tuple(_fact(entry) for entry in row["facts"])
    # The tree stays in catalog order, and each node keeps its parent.
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
        # Required facts are the ones whose surface flag is set.
        "must_surface": tuple(fact["id"] for fact in facts if fact["must_surface"]),
        "banned": tuple(row["banned"]),
        "tree": tree,
    }


def load_personas() -> dict[str, dict]:
    """Return the personas keyed by id.

    Day-five asks are folded in before validation. A catalog that fails validation stops the process instead of being returned.
    """
    personas = {row["id"]: _as_persona(extend(row)) for row in PERSONAS}
    problems = validate(personas)
    # A broken catalog is a startup failure, not an interview with quiet gaps.
    if problems:
        raise SystemExit("Persona catalog: " + "; ".join(problems))
    return personas


def validate(personas: dict[str, dict]) -> list[str]:
    """Return problems in the shared persona shape. An empty list means the catalog is usable.

    The roster size is fixed. Every parent must name a node in that persona. Every release must name a known fact. Every fact, required or not, must be released by some node.
    """
    problems = []
    # The interview contract is a fixed roster, so a missing or extra id is reported before the trees are walked.
    if len(personas) != 12:
        problems.append(f"expected 12 personas, found {len(personas)}")
    for key, data in personas.items():
        node_ids = {node.node_id for node in data["tree"]}
        known = {fact["id"] for fact in data["facts"]}
        released: set[str] = set()
        for node in data["tree"]:
            released.update(node.releases)
            # An empty parent is a root. A named parent that is not a node id is a broken link.
            if node.parent and node.parent not in node_ids:
                problems.append(f"{key} node {node.node_id} has a missing parent")
            unknown = set(node.releases) - known
            # A release id with no fact would be spoken as a missing lookup later.
            if unknown:
                problems.append(f"{key} releases unknown facts {sorted(unknown)}")
        missing = set(data["must_surface"]) - released
        # Required facts have to be reachable. The next check also catches optional facts no node names.
        if missing:
            problems.append(f"{key} never releases {sorted(missing)}")
        orphans = known - released
        if orphans:
            problems.append(f"{key} never releases {sorted(orphans)}")
    return problems
