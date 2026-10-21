"""Every clause in the policy calculus. A clause belongs to exactly one document."""

from __future__ import annotations

from simulation.policy import frames as f
from simulation.policy import notes_text as n
from simulation.policy.types import Clause


def _clause(
    clause_id: str,
    topic: str,
    document_id: str,
    frames: tuple[str, ...],
    days: int | None = None,
    grade: str = "",
    include_deceased: bool = False,
) -> Clause:
    return Clause(clause_id, topic, document_id, days, grade, include_deceased, frames)


def _national() -> list[Clause]:
    return [
        _clause("elig-v1", "eligibility", "sop-national-v1", f.ELIGIBILITY_V1),
        _clause("elig-v2", "eligibility", "sop-national-v2", f.REGISTER_V2),
        _clause("elig-v3", "eligibility", "sop-national-v3", f.REGISTER_V3),
        _clause("cover-v1", "coverage_window", "sop-national-v1", f.ELIGIBILITY_V1, days=365),
        _clause("cover-v2", "coverage_window", "sop-national-v2", f.REGISTER_V2, days=730),
        _clause("cover-v3", "coverage_window", "sop-national-v3", f.REGISTER_V3, days=730),
        _clause("done-v1", "completed_screen", "sop-national-v1", f.ELIGIBILITY_V1),
        _clause("done-v2", "completed_screen", "sop-national-v2", f.REGISTER_V2),
        _clause("done-v3", "completed_screen", "sop-national-v3", f.REGISTER_V3),
        _clause("grade-v1", "grade_turnaround", "sop-national-v1", f.GRADE_V1, days=21),
        _clause("grade-v2", "grade_turnaround", "sop-national-v2", f.GRADE_V2, days=14),
        _clause("grade-v3", "grade_turnaround", "sop-national-v3", f.GRADE_V3, days=10),
        _clause("letter-v1", "letter_turnaround", "sop-national-v1", f.LETTER_V1, days=14),
        _clause("letter-v2", "letter_turnaround", "sop-national-v2", f.LETTER_V2, days=7),
        _clause("letter-v3", "letter_turnaround", "sop-national-v3", f.LETTER_V3, days=5),
        _clause("spec-v1", "specialist_review", "sop-national-v1", f.SPEC_NONE),
        _clause("spec-v2", "specialist_review", "sop-national-v2", f.SPEC_NONE),
        _clause("spec-v3", "specialist_review", "sop-national-v3", f.SPEC_NONE),
        _clause("recall-routine-v3", "recall", "sop-national-v3", f.RECALL_ROUTINE, days=365, grade="R0"),
        _clause("recall-r1-v3", "recall", "sop-national-v3", f.RECALL_ROUTINE, days=365, grade="R1"),
        _clause("recall-u-v3", "recall", "sop-national-v3", f.RECALL_U, days=90, grade="U"),
        _clause("spec-draft", "specialist_review", "sop-urgent-draft", f.DRAFT_14, days=14),
    ]


def _local() -> list[Clause]:
    return [
        _clause("spec-ncec", "specialist_review", "site-sop-ncec-2024", f.NCEC_FAST, days=14),
        _clause("spec-harbour", "specialist_review", "site-sop-harbour-2025", f.HARBOUR_FAST, days=14),
        _clause("recall-u-hill", "recall", "site-sop-hill-2022", f.RECALL_U_HILL, days=60, grade="U"),
        _clause("elig-oakridge-memo", "eligibility", "memo-oakridge-2024", f.OAKRIDGE_INCLUDE, include_deceased=True),
        _clause("elig-oakridge-echo", "eligibility", "memo-oakridge-recirculated", f.OAKRIDGE_REPEAT, include_deceased=True),
        _clause("minutes-withdraw", "withdrawal", "minutes-2024-11", f.MINUTES),
    ]


def _governance() -> list[Clause]:
    return [
        _clause("letter-body", "letter_content", "dpo-rule-2018", f.LETTER_BODY),
        _clause("images-stay", "image_export", "dpo-rule-2018", f.IMAGES_STAY),
        _clause("grader-signs", "grader_signs", "dpo-rule-2018", f.GRADER_SIGNS),
        _clause("vendor-not-sor", "vendor_score", "vendor-contract-2024", f.VENDOR_NOT_SOR),
        _clause("vendor-receive", "vendor_receive", "dpia-vendor-2024", f.VENDOR_RECEIVE),
        _clause("pilot-stop", "pilot_start", "owner-governance", f.PILOT_STOP),
        _clause("grade-list", "grade_code", "grade-codes", f.GRADE_LIST),
        _clause("confidence-rule", "identity_confidence", "data-quality-note", n.quality_frames()),
        _clause("retention-rule", "retention", "retention-rule", n.retention_frames()),
        _clause("district-names", "district_names", "district-circular-2022", n.district_frames()),
        _clause("letter-incident", "letter_incident", "incident-letter-2025", n.incident_frames()),
        _clause("letter-result", "letter_template", "letter-template-result", n.result_letter()),
        _clause("letter-recall", "letter_template", "letter-template-recall", n.recall_letter()),
        _clause("breast-out", "breast_scope", "breast-memo", f.BREAST),
    ]


def build_clauses() -> dict[str, Clause]:
    rows = _national() + _local() + _governance()
    return {row.clause_id: row for row in rows}
