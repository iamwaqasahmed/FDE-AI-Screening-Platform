"""Benefits register. Agency spend avoided counts grader hours that triage time released already counts."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.world.staff import name

GRADER_RATE = 38
DOUBLE_COUNT = ("B-04", "B-08")


def _rows(rng: np.random.Generator) -> list[tuple]:
    triage_hours = int(rng.integers(1800, 2400))
    agency_hours = int(rng.integers(900, 1400))
    return [
        ("B-01", "Less call-centre time chasing overdue referrals", "call_centre_lead", "non_cashable", 14_500, "",
         "Calls about lost or late referral letters fall by a third."),
        ("B-02", "Fewer letter reprints after daily reconciliation", "programme_manager", "cashable", 6_200, "",
         "Duplicate dispatches caught before print."),
        ("B-03", "Fewer unnecessary hospital referrals", "ophthalmology_lead", "cashable", 41_000, "",
         "Adjudicated grades remove false-positive referrals."),
        ("B-04", "Grader hours released by AI triage", "lead_grader", "cashable", triage_hours * GRADER_RATE, triage_hours,
         f"{triage_hours} grader hours a year no longer spent on images the model triages out, at {GRADER_RATE} per hour."),
        ("B-05", "Faster referral for sight-threatening disease", "ophthalmology_lead", "non_cashable", 0, "",
         "Days from grade to referral fall for urgent grades."),
        ("B-06", "Lower postage through portal letters", "product_owner", "cashable", 9_800, "",
         "A fifth of results letters move to the portal."),
        ("B-07", "Fewer ungradable repeat appointments", "programme_manager", "cashable", 12_300, "",
         "Firmware monitoring catches quality drops within a month."),
        ("B-08", "Reduced agency grader spend", "finance_head", "cashable", agency_hours * GRADER_RATE, agency_hours,
         f"{agency_hours} agency grader hours a year not booked, because AI triage frees enough grader time to cover them, "
         f"at {GRADER_RATE} per hour."),
        ("B-09", "Automated board pack reporting", "bi_developer", "non_cashable", 7_400, "",
         "Analyst hours on the monthly pack fall from four days to one."),
        ("B-10", "Fewer complaints about letters", "patient_rep", "non_cashable", 3_100, "",
         "Complaints about missing letters halve."),
    ]


def benefits_frame(rng: np.random.Generator) -> pd.DataFrame:
    return pd.DataFrame(
        [{"benefit_id": bid, "benefit": title, "owner": name(owner), "type": kind, "annual_value_gbp": int(value),
          "hours": hours, "basis": basis, "start_year": 2027}
         for bid, title, owner, kind, value, hours, basis in _rows(rng)]
    )


def benefits_gold(frame: pd.DataFrame) -> dict:
    values = frame.set_index("benefit_id")["annual_value_gbp"]
    cashable = frame[frame["type"] == "cashable"]["annual_value_gbp"].sum()
    overlap = int(min(values[DOUBLE_COUNT[0]], values[DOUBLE_COUNT[1]]))
    return {
        "pair": list(DOUBLE_COUNT),
        "overlap_gbp": overlap,
        "claimed_total_gbp": int(frame["annual_value_gbp"].sum()),
        "claimed_cashable_gbp": int(cashable),
        "corrected_cashable_gbp": int(cashable - overlap),
        "reason": "Agency hours avoided are a subset of the grader hours released by triage; both are priced at the same rate.",
    }
