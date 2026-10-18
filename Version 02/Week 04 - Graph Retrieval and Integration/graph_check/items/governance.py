"""The precedent, the agreement, the catalogue, and the header edges."""

from __future__ import annotations

from course.checks.rules import same_set

PRECEDENT = ("ref", "start", "end", "notice", "record", "second_copies")
AGREEMENT = (
    "document_id", "cited", "covers_chase", "retention_days", "evidence_deadline", "region", "zone",
    "dob_crosses", "needs_dpo_decision",
)
WINDOW = ("freeze", "start", "end", "next_window", "last_before", "first_after", "resend_needs_release")
EDGES = ("supersedes", "cites", "applies_to", "constrains", "documents")
CATALOGUE = ("dataset", "grain_claim", "grain_holds", "upstream", "verified", "requests_catalogued")


def precedent(answer: dict, gold: dict) -> bool:
    row = gold["items"]["precedent"]
    flags = answer.get("notice_says_lost") is True and answer.get("record_says_lost") is False and answer.get("has_request_id") is False
    return flags and all(answer.get(key) == row[key] for key in PRECEDENT)


def catalogue_lineage(answer: dict, gold: dict) -> bool:
    row = gold["items"]["catalogue_lineage"]
    return all(answer.get(key) == row[key] for key in CATALOGUE)


def bureau_agreement(answer: dict, gold: dict) -> bool:
    row = gold["items"]["bureau_agreement"]
    covered = same_set(answer.get("letters_covered", []), row["letters_covered"])
    return covered and all(answer.get(key) == row[key] for key in AGREEMENT)


def resend_window(answer: dict, gold: dict) -> bool:
    row = gold["items"]["resend_window"]
    return all(answer.get(key) == row[key] for key in WINDOW)


def header_edges(answer: dict, gold: dict) -> bool:
    row = gold["items"]["header_edges"]
    return all(answer.get(key) == row[key] for key in EDGES)


def referral_sites(answer: dict, gold: dict) -> bool:
    row = gold["items"]["referral_sites"]
    return (
        same_set(answer.get("hospitals", []), row["hospitals"])
        and answer.get("blank_mrn") == row["blank_mrn"]
        and answer.get("ambiguous") == row["ambiguous"]
    )
