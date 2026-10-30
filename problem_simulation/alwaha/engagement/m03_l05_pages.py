"""Participant pages for rel-m03-l05.
The requirement-to-gate map stays out.

These strings are the rehearsal brief, the steering questions, the role cards, and the stage-gate list. role_cards writes one section per seat from the catalog and leaves hidden interview answers off the page. The gate page lists the gates and names the risk-tier gate.
"""

from __future__ import annotations

from alwaha.engagement.catalog import PERSONAS

CASE_DATE = "2027-01-28"
SEATS = ("cdo", "access-mgr", "phc-lead", "dpo")
QUESTIONS = (
    "What did the second run change?",
    "What will the client requirements include, and what is a non-goal?",
    "Which stage gate applies, and what is the risk tier?",
    "What does the improvement cost, in labels or GPU hours?",
    "What will you not copy from the sponsor sentence?",
)


def rehearsal() -> str:
    return f"""# Rehearsal brief

Steering asks for the client requirements. The file is rcp/requirements.md. A list that repeats the sponsor sentence is not a brief.

The price sheet and the annotation budget are in this pack. The second run is scored on slices/before.jsonl. Labels stay on the grading service.

Case date: {CASE_DATE}.
"""


def steer_page() -> str:
    """Return the steering page for this pack.

    The committee is named and the questions are numbered in the stored order so the file matches that list.
    """
    numbered = "\n".join(f"{index}. {text}" for index, text in enumerate(QUESTIONS, start=1))
    return f"""# steer-m03-l05

The steering committee asks these questions. The committee is cdo, med-dir, dpo, ciso, and finance.

{numbered}
"""


def role_cards() -> str:
    """Return the workshop role cards.

    Each seat is shown with its name, role, opening line, and goals. Hidden interview answers stay out of the page.
    """
    # Index the catalog so each seat can be looked up by id.
    by_id = {row["id"]: row for row in PERSONAS}
    parts = ["# Role cards", "", "ws-access seats. Hidden answers stay in the interview.", ""]
    # One section per seat: the heading, the name and role, the opening line, and the goals.
    for seat in SEATS:
        row = by_id[seat]
        parts.append(f"## {seat}")
        parts.append("")
        parts.append(f"{row['name']}, {row['role']}.")
        parts.append("")
        parts.append(row["says_first"])
        parts.append("")
        parts.append(" ".join(row["goals"]))
        parts.append("")
    return "\n".join(parts).rstrip() + "\n"


def stage_gate() -> str:
    return """# pol-stage-gate

Six gates:

- G0 intake
- G1 risk tier
- G2 DPIA
- G3 pilot approval
- G4 go-live
- G5 post-launch review

G1 is the risk tier.
"""
