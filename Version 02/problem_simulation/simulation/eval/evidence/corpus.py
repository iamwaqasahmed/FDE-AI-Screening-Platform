"""Corpus findings a team can count from the files: originals, tables, forwards, and the policy headers."""

from __future__ import annotations

from simulation.eval.evidence.bars import SCAN_PAIRS
from simulation.policy.apply import DOCUMENTS
from simulation.systems.catalog import STALE_REGISTER
from simulation.world.clock import iso


def facts(world: dict) -> dict:
    return {
        "policy_graph": _policy(),
        "originals": _originals(world),
        "table_only": _tables(world),
        "scan_damage": {"pairs": list(SCAN_PAIRS)},
        "near_duplicates": {"count": len(world["gold"].get("near_duplicates", [])), "suffix": "-fwd"},
    }


def _policy() -> dict:
    drafts, withdrawn, overlays = [], [], []
    for document in DOCUMENTS.values():
        if document.status == "draft":
            drafts.append(document.document_id)
        if document.status == "withdrawn":
            withdrawn.append({"document_id": document.document_id, "effective": iso(document.effective),
                              "sunset": iso(document.sunset) if document.sunset else ""})
        if document.status == "in_force" and document.applies_to:
            overlays.append({"document_id": document.document_id, "sites": sorted(document.applies_to),
                             "from": iso(document.effective)})
    return {
        "drafts": sorted(drafts),
        "withdrawn": sorted(withdrawn, key=lambda row: row["document_id"]),
        "overlays": sorted(overlays, key=lambda row: row["document_id"]),
        "stale_register": sorted(STALE_REGISTER),
    }


def _originals(world: dict) -> dict:
    counts = {"pdf": 0, "docx": 0, "xlsx": 0, "scan": 0}
    for path in world["files"]:
        name = str(path)
        if not name.startswith("corpus/") or "/originals/" not in name:
            continue
        if name.endswith(".scan.pdf"):
            counts["scan"] += 1
        elif name.endswith(".pdf"):
            counts["pdf"] += 1
        elif name.endswith(".docx"):
            counts["docx"] += 1
        elif name.endswith(".xlsx"):
            counts["xlsx"] += 1
    return counts


def _tables(world: dict) -> dict:
    facts = world["gold"].get("table_only_facts", [])
    return {
        "boards": len({row["doc_id"] for row in facts if str(row["doc_id"]).startswith("board-")}),
        "audits": len({row["doc_id"] for row in facts if str(row["doc_id"]).startswith("quality-audit-")}),
    }
