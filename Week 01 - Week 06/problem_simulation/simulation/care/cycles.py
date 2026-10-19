"""Annual cycles, generated from the hidden layers. Each stage lives in its own module."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.care.attendance import build_invitations
from simulation.care.breach import apply_breach
from simulation.care.grading import stamp_grading
from simulation.care.letters import stamp_letters
from simulation.care.naming import stamp_names
from simulation.care.pilot import stamp_pilot
from simulation.care.placement import stamp_photos, stamp_site
from simulation.care.referrals import stamp_referrals, stamp_truth
from simulation.care.rules import stamp_rules
from simulation.devices.quality import stamp_devices
from simulation.disease.hba1c import on_dates
from simulation.disease.state import DiseaseIndex
from simulation.ml.vendor_model import stamp_vendor


def build_events(people: pd.DataFrame, hidden: dict, rng: np.random.Generator) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Return events, invitations, and the daily grader hours."""
    base = people[people["alias_of"] == ""].reset_index(drop=True)
    invitations = build_invitations(base, hidden["hba1c"], rng)
    columns = ["person_uid", "cycle_start", "planned_date", "reminder", "sms", "dna_prev"]
    attended = invitations.loc[invitations["attended"], columns]
    events = base.merge(attended, on="person_uid", how="inner")
    events = events.sort_values(["person_uid", "cycle_start"]).reset_index(drop=True)
    stamp_site(events, rng)
    events = stamp_photos(events, rng)
    stamp_rules(events)
    stamp_devices(events, rng)
    disease = DiseaseIndex(hidden["disease"])
    stamp_truth(events, disease)
    rows = hidden["person_row"].reindex(events["person_uid"]).to_numpy()
    events["hba1c"] = on_dates(hidden["hba1c"], rows, events["photo_date"])
    hours = stamp_grading(events, rng)
    stamp_letters(events, rng)
    stamp_referrals(events, disease, rng)
    stamp_pilot(events, rng)
    stamp_vendor(events, rng)
    stamp_names(events)
    events.insert(0, "event_id", [f"E{index + 1:07d}" for index in range(len(events))])
    return apply_breach(events), invitations, hours
