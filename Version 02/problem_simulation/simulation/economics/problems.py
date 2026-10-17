"""Annual cost of each problem theme that staff and patients complain about."""

from __future__ import annotations

from simulation.economics.costs import cost

THEMES = ("results_delay", "letters", "hospital_wait", "missed_appointments", "travel_and_parking")
SALIENCE = ("letters", "travel_and_parking", "hospital_wait", "results_delay", "missed_appointments")


def problem_costs(v: dict) -> dict[str, float]:
    harm = v["harm"]
    calls = v["calls"]
    return {
        "results_delay": round(harm["grader_backlog"]["harm_gbp"] + harm["never_graded"]["harm_gbp"] + calls.get("results_query", 0.0) * cost("call"), 0),
        "letters": round(harm["letter_bureau"]["harm_gbp"] + v["duplicate_letters"] * cost("letter_reprint")
                         + calls.get("letter_not_received", 0.0) * cost("call"), 0),
        "hospital_wait": round(harm["booking"]["harm_gbp"] + v["ophthalmology_dna"] * cost("ophthalmology_visit")
                               + calls.get("hospital_appointment", 0.0) * cost("call"), 0),
        "missed_appointments": round(v["dna_screening"] * cost("dna_slot") + calls.get("reschedule", 0.0) * cost("call"), 0),
        "travel_and_parking": round(calls.get("travel_and_parking", 0.0) * cost("call"), 0),
    }


def costliest(costs: dict[str, float]) -> str:
    return max(sorted(costs), key=lambda theme: costs[theme])


def most_voiced(costs: dict[str, float]) -> str:
    """The loudest theme is the most salient one that is not the costliest."""
    top = costliest(costs)
    return next(theme for theme in SALIENCE if theme != top)
