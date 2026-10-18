"""Write truth, corpus, the handover drop, every surface file, and eval."""

from __future__ import annotations

import shutil

import pandas as pd

from simulation.corpus.register import write_register
from simulation.eval.cases import write_cases
from simulation.files import write_all
from simulation.paths import CORPUS, DATA, DROPS, ENGAGEMENT, EVAL, HANDOVER, TRUTH
from simulation.systems.grader import write_grader
from simulation.systems.letters import write_letters
from simulation.systems.notes import write_breast, write_interfaces, write_owners
from simulation.systems.ophthalmology import write_ophthalmology
from simulation.systems.pacs import write_pacs
from simulation.systems.registry import write_registry
from simulation.systems.shared import write_shared
from simulation.systems.vendor import write_vendor
from simulation.systems.warehouse import write_warehouse
from simulation.world.clock import iso

GENERATED = (TRUTH, EVAL, CORPUS, HANDOVER, DROPS, ENGAGEMENT)


def write_world(world: dict) -> None:
    for folder in GENERATED:
        if folder.exists():
            shutil.rmtree(folder)
    print("Writing truth...")
    _write_truth(world)
    print("Writing corpus...")
    paths = _write_corpus(world)
    write_register(world["catalog"], paths, CORPUS / "register.csv", world.get("corpus_meta"))
    print("Writing handover...")
    _write_handover(world)
    print(f"Writing {len(world['files'])} surface files...")
    write_all(DATA, world["files"])
    from simulation.eval.discovery_gold import build as discovery_gold
    from simulation.eval.enterprise import build as enterprise_gold
    from simulation.eval.evidence import build as evidence_gold
    from simulation.eval.graph import build as graph_gold
    from simulation.eval.agent import build as agent_gold

    world["gold"]["discovery"] = discovery_gold(world)
    payload, records = enterprise_gold(world)
    world["gold"]["enterprise"] = payload
    evidence, extract = evidence_gold(world)
    world["gold"]["evidence"] = evidence
    graph, reconciliation = graph_gold(world)
    world["gold"]["graph"] = graph
    agent, backlog, sweep = agent_gold(world)
    world["gold"]["agent"] = agent
    write_all(TRUTH / "gold", {f"{key}.{'jsonl' if isinstance(value, list) else 'json'}": value for key, value in world["gold"].items()})
    records.to_parquet(TRUTH / "gold" / "identity_records.parquet", index=False)
    extract.to_parquet(TRUTH / "gold" / "evidence_extract.parquet", index=False)
    reconciliation.to_parquet(TRUTH / "gold" / "graph_reconciliation.parquet", index=False)
    backlog.to_parquet(TRUTH / "gold" / "agent_backlog.parquet", index=False)
    sweep.to_parquet(TRUTH / "gold" / "agent_sweep.parquet", index=False)
    print("Writing eval...")
    write_cases(world, EVAL / "cases.jsonl")


def _write_truth(world: dict) -> None:
    TRUTH.mkdir(parents=True, exist_ok=True)
    world["people"].to_parquet(TRUTH / "person.parquet", index=False)
    world["events"].to_parquet(TRUTH / "event.parquet", index=False)
    world["identifiers"].to_parquet(TRUTH / "identifier.parquet", index=False)
    edges = []
    for document in world["catalog"].values():
        for kind in ("supersedes", "cites", "applies_to", "constrains"):
            for target in getattr(document, kind):
                edges.append(
                    {
                        "source": document.document_id,
                        "edge": kind,
                        "target": target,
                        "status": document.status,
                        "effective": iso(document.effective),
                        "sunset": iso(document.sunset) if document.sunset else "",
                    }
                )
    pd.DataFrame(edges).to_parquet(TRUTH / "policy_edge.parquet", index=False)


def _write_corpus(world: dict) -> dict[str, str]:
    paths: dict[str, str] = {}
    for document_id, text in world["rendered"].items():
        relative = world.get("paths", {}).get(document_id) or _relative(document_id)
        dest = CORPUS / relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        paths[document_id] = relative.replace("\\", "/")
    return paths


def _write_handover(world: dict) -> None:
    people, events, identifiers = world["people"], world["events"], world["identifiers"]
    write_registry(people, identifiers, events, HANDOVER / "registry")
    write_pacs(events, people, identifiers, HANDOVER / "pacs")
    write_shared(events, HANDOVER / "shared")
    write_grader(events, people, identifiers, HANDOVER / "grader")
    write_letters(events, identifiers, HANDOVER / "letters")
    write_ophthalmology(events, identifiers, HANDOVER / "ophthalmology")
    write_vendor(events, HANDOVER / "vendor")
    write_warehouse(people, events, identifiers, HANDOVER / "warehouse")
    write_interfaces(HANDOVER / "interfaces")
    write_owners(HANDOVER / "owners.csv")
    write_breast(HANDOVER / "breast")


def _relative(document_id: str) -> str:
    if document_id.startswith("board-"):
        return f"boards/{document_id}.md"
    if document_id.startswith("site-note-"):
        return f"notes/{document_id}.md"
    return f"policy/{document_id}.md"
