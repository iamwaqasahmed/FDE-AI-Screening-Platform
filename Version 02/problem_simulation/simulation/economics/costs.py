"""Unit costs in pounds and teaching harm weights. The weights are not clinical."""

from __future__ import annotations

import pandas as pd

UNIT_COSTS = {
    "grader_read": (9.50, "One primary or secondary grade of one encounter"),
    "grader_hour": (38.00, "One employed grader hour"),
    "agency_grader_hour": (62.00, "One agency grader hour, from January 2025"),
    "letter": (1.10, "One printed and posted result letter"),
    "letter_reprint": (1.60, "One reissued letter after a loss or duplicate"),
    "sms": (0.04, "One SMS invitation or reminder"),
    "screening_appointment": (46.00, "One booked screening slot"),
    "dna_slot": (46.00, "One screening slot lost to a did-not-attend"),
    "outreach_day": (1450.00, "One outreach van day"),
    "ophthalmology_visit": (140.00, "One hospital ophthalmology appointment"),
    "call": (6.80, "One handled contact-centre call"),
    "vendor_read_fee": (2.10, "Vendor fee per scored image under the pilot contract"),
}

HARM_WEIGHTS = {0: 0.0, 1: 0.1, 2: 1.0, 3: 4.0}
PROGRESSION_POINTS = 12.0
HARM_UNIT_GBP = 250.0


def cost(name: str) -> float:
    return UNIT_COSTS[name][0]


def unit_costs_frame() -> pd.DataFrame:
    rows = [{"item": key, "unit_cost_gbp": value, "definition": text} for key, (value, text) in UNIT_COSTS.items()]
    return pd.DataFrame(rows)


def harm_weights_frame() -> pd.DataFrame:
    rows = [{"true_level": level, "harm_points_per_week": weight} for level, weight in HARM_WEIGHTS.items()]
    rows.append({"true_level": "progressed_in_delay", "harm_points_per_week": PROGRESSION_POINTS})
    frame = pd.DataFrame(rows)
    frame["gbp_per_point"] = HARM_UNIT_GBP
    frame["note"] = "Teaching weight, not a clinical weight"
    return frame
