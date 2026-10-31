"""Instructor-only expectations still used by the checkers."""

from __future__ import annotations

DECISION_OWNERS = {
    "dec-clinical": "clinician",
    "dec-route": "human",
    "dec-cover": "payer",
    "dec-slot": "hospital-file",
}

SPONSOR_FEATURE = "refused"
SCORE_DECISION = "no-call"
SIGNAL_PAGE = "served-document"
RESTRICTED_NAMES = frozenset({"letter", "national-id", "quotation", "wage"})
