"""The policy documents: national versions, local adoptions, one withdrawn memo, and governance rules."""

from __future__ import annotations

from datetime import date

from simulation.policy.clauses import build_clauses
from simulation.policy.types import Document
from simulation.world.clock import (
    HARBOUR_ADOPT,
    HILL_RECALL,
    INCIDENT_START,
    NCEC_ADOPT,
    OAKRIDGE_MEMO,
    OAKRIDGE_WITHDRAW,
    VENDOR_START,
)
from simulation.world.sites import HARBOUR, HILL_SITES, NCEC, OAKRIDGE, short

PROGRAMME = "diabetic-eye"
ALWAYS = date(2018, 1, 1)

# document_id, title, status, effective, sunset, version, extra fields
_ROWS: tuple[tuple, ...] = (
    ("sop-national-v1", "Issued screening procedure", "superseded", date(2016, 3, 1), date(2019, 3, 1), "v1", {}),
    ("sop-national-v2", "Register and coverage rules, 2019", "superseded", date(2019, 3, 1), date(2023, 4, 1), "v2",
     {"supersedes": ("sop-national-v1",)}),
    ("sop-national-v3", "Register and grade codes, 2023", "in_force", date(2023, 4, 1), None, "v3",
     {"supersedes": ("sop-national-v2",)}),
    ("sop-urgent-draft", "Urgent pathway draft", "draft", date(2023, 11, 1), None, "draft",
     {"cites": ("sop-national-v3",)}),
    ("site-sop-ncec-2024", f"{NCEC} local pathway", "in_force", NCEC_ADOPT, None, "ncec-2024",
     {"site": NCEC, "cites": ("sop-urgent-draft",), "applies_to": (NCEC,)}),
    ("site-sop-harbour-2025", f"{HARBOUR} local pathway", "in_force", HARBOUR_ADOPT, None, "harbour-2025",
     {"site": HARBOUR, "cites": ("sop-urgent-draft",), "applies_to": (HARBOUR,)}),
    ("site-sop-hill-2022", "Hill primary repeat interval", "in_force", HILL_RECALL, None, "hill-2022",
     {"applies_to": HILL_SITES}),
    ("memo-oakridge-2024", f"{short(OAKRIDGE)} coverage note", "withdrawn", OAKRIDGE_MEMO, OAKRIDGE_WITHDRAW,
     "oakridge-2024", {"site": OAKRIDGE, "applies_to": (OAKRIDGE,)}),
    ("memo-oakridge-recirculated", f"Recirculated {short(OAKRIDGE)} note", "draft", date(2026, 1, 20), None,
     "recirculated", {"site": OAKRIDGE, "cites": ("memo-oakridge-2024",), "applies_to": (OAKRIDGE,)}),
    ("minutes-2024-11", "Screening board minutes November 2024", "in_force", OAKRIDGE_WITHDRAW, None,
     "minutes-2024-11", {"supersedes": ("memo-oakridge-2024",), "cites": ("memo-oakridge-2024", "sop-national-v3")}),
    ("dpo-rule-2018", "Data-protection operating rule", "in_force", ALWAYS, None, "dpo-2018",
     {"constrains": ("vendor-contract-2024",)}),
    ("vendor-contract-2024", "Vendor model contract", "in_force", VENDOR_START, None, "vendor-2024",
     {"cites": ("dpo-rule-2018",)}),
    ("dpia-vendor-2024", "Vendor pilot DPIA", "in_force", VENDOR_START, None, "dpia-2024",
     {"cites": ("vendor-contract-2024", "dpo-rule-2018"), "constrains": ("vendor-contract-2024",)}),
    ("grade-codes", "Grade-code list", "in_force", ALWAYS, None, "grades", {}),
    ("data-quality-note", "Identity confidence and known gaps", "in_force", ALWAYS, None, "dq", {}),
    ("owner-governance", "Pilot owner rule", "in_force", ALWAYS, None, "owner", {}),
    ("retention-rule", "What the archive keeps", "in_force", ALWAYS, None, "retention", {}),
    ("district-circular-2022", "District name variants", "in_force", date(2022, 2, 1), None, "districts-2022", {}),
    ("incident-letter-2025", "Letter bureau duplicate week", "in_force", INCIDENT_START, None, "incident-2025", {}),
    ("letter-template-result", "Result letter template", "in_force", ALWAYS, None, "letter-result", {}),
    ("letter-template-recall", "Recall letter template", "in_force", ALWAYS, None, "letter-recall", {}),
    ("breast-memo", "Breast programme boundary", "in_force", date(2024, 1, 15), None, "breast",
     {"programme": "breast"}),
    ("sop-national-v2-scan", "Scanned copy of the 2019 register rules", "draft", date(2024, 8, 1), None, "v2-scan",
     {"cites": ("sop-national-v2",)}),
)


def make_document(
    document_id: str,
    title: str,
    status: str,
    effective: date,
    sunset: date | None,
    version: str,
    clause_ids: tuple[str, ...] = (),
    site: str = "",
    programme: str = PROGRAMME,
    supersedes: tuple[str, ...] = (),
    cites: tuple[str, ...] = (),
    applies_to: tuple[str, ...] = (),
    constrains: tuple[str, ...] = (),
) -> Document:
    return Document(
        document_id, title, status, effective, sunset, site, programme, version,
        supersedes, cites, applies_to, constrains, clause_ids,
    )


def build_documents() -> dict[str, Document]:
    clauses = build_clauses()
    docs = {}
    for document_id, title, status, effective, sunset, version, extra in _ROWS:
        owned = tuple(clause.clause_id for clause in clauses.values() if clause.document_id == document_id)
        docs[document_id] = make_document(document_id, title, status, effective, sunset, version, owned, **extra)
    return docs
