"""rel-w3d4 gold. Held-out labels, the campaign lift, and the experiment effect stay here."""

from __future__ import annotations

from alwaha.config.profile import Profile
from alwaha.engagement.w3d4_demand import FIT_YEAR, LATER_MONTHS, LATER_YEAR, series, window
from alwaha.engagement.w3d4_judge import FLUENT_WRONG, full_set, held, subset
from alwaha.engagement.w3d4_pages import CASE_DATE, budgets, experiment
from alwaha.engagement.w3d4_rows import failure_types, held_score
from alwaha.engagement.w3d4_rules import citation_accuracy, extraction_f1, journey_pass, report

_PEEK = "contained"


def gold(profile: Profile) -> dict:
    rows = series(profile.seed)
    scored = held_score()
    protocol = experiment()
    effect = report(protocol)
    peek = report({**protocol, "metric": _PEEK})
    return {
        "ab_status": {
            "metric": effect["metric"],
            "peek": _PEEK,
            "peek_winner": peek["winner"],
            "winner": effect["winner"],
        },
        "budgets": budgets(),
        "calibration": full_set(),
        "calibration_held": held(),
        "case_date": CASE_DATE,
        "demo": next(item["item_id"] for item in subset() if item["item_id"] == FLUENT_WRONG and item["fluent"] and not item["pass"]),
        "failures": failure_types(),
        "fit_window": {"months": list(LATER_MONTHS), "year": FIT_YEAR},
        "held_score": scored,
        "later_visits": window(rows, LATER_YEAR, LATER_MONTHS),
        "later_window": {"months": list(LATER_MONTHS), "year": LATER_YEAR},
        "metrics": {
            "citation": citation_accuracy(scored["citation"]),
            "extraction": extraction_f1(scored["extraction"]),
            "journey": journey_pass(scored["journey"]),
        },
    }
