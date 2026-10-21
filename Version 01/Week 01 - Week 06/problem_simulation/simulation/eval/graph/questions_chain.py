"""Two documents, joined by an edge in the header."""

from __future__ import annotations

from simulation.eval.graph.question import cite, make
from simulation.world.clock import OAKRIDGE_WITHDRAW, iso
from simulation.world.sites import NCEC, OAKRIDGE, short


def cases(world: dict) -> list[dict]:
    return [_row(world, *spec) for spec in _specs()]


def _specs() -> list[tuple]:
    return [
        ("chain-national", "On 2020-06-01, which national procedure is in force, and which document does it supersede?",
         {"in_force": "sop-national-v2", "supersedes": "sop-national-v1"}, "sop-national-v2",
         ["sop-national-v2", "sop-national-v1"]),
        ("chain-current", "On 2024-06-01, which national procedure is in force, and which document does it supersede?",
         {"in_force": "sop-national-v3", "supersedes": "sop-national-v2"}, "sop-national-v3",
         ["sop-national-v3", "sop-national-v2"]),
        ("chain-oakridge", f"Which document withdrew the {short(OAKRIDGE)} coverage note, and on what date did that note stop binding?",
         {"document_id": "minutes-2024-11", "sunset": iso(OAKRIDGE_WITHDRAW)}, "minutes-2024-11",
         ["minutes-2024-11", "memo-oakridge-2024"]),
        ("chain-recirculated", f"The recirculated {short(OAKRIDGE)} coverage note is dated 2026-01-20. Does it bind on 2026-02-01, and which document does it cite?",
         {"binds": False, "cites": "memo-oakridge-2024"}, "memo-oakridge-recirculated",
         ["memo-oakridge-recirculated", "memo-oakridge-2024"]),
        ("chain-ncec", f"Which document does the {NCEC} local pathway cite that never came into force?",
         {"document_id": "sop-urgent-draft"}, "sop-urgent-draft", ["site-sop-ncec-2024", "sop-urgent-draft"]),
        ("chain-constrains", "Which documents constrain the vendor model contract?",
         {"documents": ["dpia-vendor-2024", "dpo-rule-2018"]}, "dpia-vendor-2024",
         ["dpia-vendor-2024", "dpo-rule-2018", "vendor-contract-2024"]),
        ("chain-bureau", "Which document does the PostRight data sharing agreement cite?",
         {"document_id": "dpo-rule-2018"}, "dpo-rule-2018", ["dsa-postright-2020", "dpo-rule-2018"]),
        ("chain-scan", "A scanned copy of the 2019 register rules was filed in 2024. What is its status, and which document does it cite?",
         {"status": "draft", "cites": "sop-national-v2"}, "sop-national-v2-scan",
         ["sop-national-v2-scan", "sop-national-v2"]),
    ]


def _row(world: dict, case_id: str, question: str, expected: dict, citation_id: str, visit: list[str]) -> dict:
    keys = tuple(expected)
    return make(case_id, question, expected, "value", "chain", keys, cite(world["catalog"][citation_id]), "multi_hop", visit)

