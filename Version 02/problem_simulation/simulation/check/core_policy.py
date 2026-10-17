"""Clause resolution, signed headers, and the lexical traps."""

from __future__ import annotations

from datetime import date, timedelta

import pandas as pd

from simulation.eval.overlap import best_document
from simulation.eval.questions import ELIGIBILITY, FOURTEEN_DAYS, OAKRIDGE_DECEASED
from simulation.policy.apply import applicable_clause, document_applies
from simulation.policy.parse import parse_header
from simulation.world.clock import HARBOUR_ADOPT, NCEC_ADOPT, OAKRIDGE_MEMO, SNAPSHOT, iso
from simulation.world.sites import HARBOUR, NCEC, OAKRIDGE

DAY = timedelta(days=1)


def check(world: dict, errors: list[str]) -> None:
    if document_applies("sop-urgent-draft", SNAPSHOT):
        errors.append("The national draft applies at the snapshot.")
    checks = [
        (NCEC, NCEC_ADOPT - DAY, "spec-v3"),
        (NCEC, NCEC_ADOPT, "spec-ncec"),
        (HARBOUR, HARBOUR_ADOPT - DAY, "spec-v3"),
        (HARBOUR, HARBOUR_ADOPT, "spec-harbour"),
        (OAKRIDGE, OAKRIDGE_MEMO + timedelta(days=30), "elig-oakridge-memo"),
        (OAKRIDGE, date(2026, 3, 1), "elig-v3"),
    ]
    for site, on_date, clause_id in checks:
        topic = "eligibility" if clause_id.startswith("elig-") else "specialist_review"
        found = applicable_clause(site, on_date, topic)
        if found.clause_id != clause_id:
            errors.append(f"{site} on {iso(on_date)} resolved to {found.clause_id}, expected {clause_id}")
    events = world["events"]
    if events["specialist_clause"].eq("spec-draft").any():
        errors.append("A care event cites the national draft.")
    _match_stored(events, errors)


def _match_stored(events: pd.DataFrame, errors: list[str]) -> None:
    columns = ["grade_clause", "letter_clause", "specialist_clause", "eligibility_clause"]
    if events[columns].eq("").any().any():
        errors.append("A care event is missing a clause id.")
        return
    for row in events.groupby(["site", "photo_date"], as_index=False).head(1).itertuples(index=False):
        on_date = date.fromisoformat(row.photo_date)
        found = tuple(
            applicable_clause(row.site, on_date, topic).clause_id
            for topic in ("grade_turnaround", "letter_turnaround", "specialist_review", "eligibility")
        )
        stored = (row.grade_clause, row.letter_clause, row.specialist_clause, row.eligibility_clause)
        if found != stored:
            errors.append(f"{row.site} on {row.photo_date} stored {stored} but resolves to {found}")
            return


def check_headers(world: dict, errors: list[str]) -> None:
    for document_id, document in world["catalog"].items():
        parsed = parse_header(world["rendered"][document_id])
        if parsed.get("document_id") != document.document_id or parsed.get("status") != document.status:
            errors.append(f"Header mismatch for {document_id}")
            continue
        for field in ("supersedes", "cites", "applies_to", "constrains"):
            if parsed.get(field) != getattr(document, field):
                errors.append(f"Edge mismatch for {document_id} {field}")
                break
        sunset = iso(document.sunset) if document.sunset else ""
        if parsed.get("sunset") != sunset or parsed.get("effective") != iso(document.effective):
            errors.append(f"Window mismatch for {document_id}")


def check_lexical(world: dict, errors: list[str]) -> None:
    policy = {key: text for key, text in world["rendered"].items() if world["catalog"][key].clause_ids}
    expectations = {
        FOURTEEN_DAYS: "sop-urgent-draft",
        ELIGIBILITY: "sop-national-v1",
        OAKRIDGE_DECEASED: "memo-oakridge-recirculated",
    }
    for question, document_id in expectations.items():
        winner = best_document(question, policy)
        if winner != document_id:
            errors.append(f"Overlap picked {winner} for a question whose trap document is {document_id}")
    if applicable_clause(NCEC, NCEC_ADOPT + timedelta(days=290), "specialist_review").document_id == "sop-urgent-draft":
        errors.append(f"Gold specialist clause at {NCEC} is the draft.")
