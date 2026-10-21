"""One shape for every gold question: answer, citation, evidence, tags, and budget."""

from __future__ import annotations

from simulation.policy.apply import CLAUSES, catalog_document
from simulation.world.clock import iso

BUDGETS = {
    "lookup": {"max_tokens": 4_000, "max_seconds": 10, "max_cost_usd": 0.01},
    "multi_hop": {"max_tokens": 20_000, "max_seconds": 45, "max_cost_usd": 0.06},
    "analysis": {"max_tokens": 60_000, "max_seconds": 180, "max_cost_usd": 0.25},
    "written": {"max_tokens": 40_000, "max_seconds": 120, "max_cost_usd": 0.15},
}


OUTCOMES = {"discovery", "enterprise_data", "solution", "architecture", "delivery", "consulting", "fde"}
ROLES = {"ml", "data_science", "data_engineering", "software", "architect", "pm", "consultant"}


def citation_for(clause_id: str, site: str = "") -> dict:
    if not clause_id or clause_id not in CLAUSES:
        return {}
    document = catalog_document(CLAUSES[clause_id].document_id)
    return {
        "document_id": document.document_id,
        "version": document.version,
        "status": document.status,
        "effective": iso(document.effective),
        "sunset": iso(document.sunset) if document.sunset else "",
        "site": site or document.site,
        "clause_id": clause_id,
    }


def make_case(
    case_id: str,
    question: str,
    expected: dict,
    *,
    outcome: str,
    roles: tuple[str, ...],
    surfaces: tuple[str, ...],
    clause_id: str = "",
    site: str = "",
    truth_ids: list[str] | None = None,
    identity: bool = False,
    veto: str = "",
    refused: bool = False,
    budget: str = "lookup",
    sources: tuple[str, ...] = (),
    kind: str = "value",
) -> dict:
    if outcome not in OUTCOMES or not set(roles) <= ROLES:
        raise ValueError(f"{case_id}: unknown outcome {outcome!r} or roles {roles}")
    return {
        "case_id": case_id,
        "question": question,
        "kind": kind,
        "expected": expected,
        "citation": citation_for(clause_id, site),
        "sources": list(sources),
        "evidence": {"must_resolve_identity": identity, "clause_id": clause_id, "veto": veto, "refused": refused},
        "tags": {"outcome": outcome, "roles": list(roles), "surfaces": list(surfaces)},
        "budget": dict(BUDGETS[budget], tier=budget),
        "truth_ids": truth_ids or [],
    }
