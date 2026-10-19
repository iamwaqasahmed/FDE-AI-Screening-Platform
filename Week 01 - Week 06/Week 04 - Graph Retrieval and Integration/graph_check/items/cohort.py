"""Who was chased, who was not reached, and the re-send."""

from __future__ import annotations

from course.checks.rules import close, same_set
from simulation.eval.graph.bars import CLOCK_DAY_TOLERANCE, PEOPLE_TOLERANCE

CONTACT = ("chased", "seen", "deceased", "moved", "bound", "once", "twice", "lost")
RESEND = ("resend", "hold_seen", "hold_deceased", "hold_moved")


def contact_status(answer: dict, gold: dict) -> bool:
    row = gold["items"]["contact_status"]
    return all(answer.get(key) == row[key] for key in CONTACT)


def chase_lost_people(answer: dict, gold: dict) -> bool:
    row = gold["items"]["chase_lost_people"]
    return (
        answer.get("local_ids") == row["local_ids"]
        and answer.get("is_upper_bound") is True
        and close(answer.get("people"), row["people"], PEOPLE_TOLERANCE)
    )


def pilot_scope_lost(answer: dict, gold: dict) -> bool:
    row = gold["items"]["pilot_scope_lost"]
    return answer.get("local_ids") == row["local_ids"] and answer.get("is_upper_bound") is True


def clock_breaches(answer: dict, gold: dict) -> bool:
    row = gold["items"]["clock_breaches"]
    return (
        answer.get("with_clock") == row["with_clock"]
        and same_set(answer.get("clause_ids", []), row["clause_ids"])
        and close(answer.get("median_days_over"), row["median_days_over"], CLOCK_DAY_TOLERANCE, relative=False)
    )


def resend_summary(answer: dict, gold: dict) -> bool:
    row = gold["items"]["resend_summary"]
    return answer.get("key") == row["key"] and all(answer.get(key) == row[key] for key in RESEND)
