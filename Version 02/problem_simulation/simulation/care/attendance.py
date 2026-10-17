"""Invitations cycle by cycle. A did-not-attend in one cycle lowers the next cycle's chance."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.care.behaviour import DNA_PENALTY, calibrate_base, sigmoid, static_terms, time_terms
from simulation.disease.hba1c import on_dates
from simulation.world.clock import cycle_starts, iso
from simulation.world.quotas import ATTEND

FEATURES = ("travel_burden", "age", "hba1c", "has_phone", "sms", "reminder", "dna_prev", "planned_month")


def build_invitations(base: pd.DataFrame, hba1c: np.ndarray, rng: np.random.Generator) -> pd.DataFrame:
    rows = np.arange(len(base))
    dna_prev = np.zeros(len(base), dtype=int)
    first = pd.Series([iso(cycle_starts()[0])] * len(base))
    first_a1c = on_dates(hba1c, rows, first)
    first_age = _age(base, pd.to_datetime(first))
    static_first = static_terms(base, first_age, first_a1c)
    bases = {d: calibrate_base(static_first[base["district"].eq(d).to_numpy()], ATTEND[d]) for d in ATTEND}
    frames = []
    for cycle in cycle_starts():
        planned = pd.Series(pd.Timestamp(cycle) + pd.to_timedelta(rng.integers(0, 300, len(base)), unit="D"))
        frame = _cycle(base, rows, hba1c, cycle, planned, dna_prev, bases, rng)
        invited = frame["invited"].to_numpy()
        attended = frame["attended"].to_numpy()
        dna_prev = np.where(invited, (~attended).astype(int), dna_prev)
        frames.append(frame[frame["invited"]])
    return pd.concat(frames, ignore_index=True)


def _cycle(base, rows, hba1c, cycle, planned, dna_prev, bases, rng) -> pd.DataFrame:
    day = planned.dt.strftime("%Y-%m-%d")
    alive = (base["flag_true_on"] == "") | (base["flag_true_on"] > iso(cycle))
    invited = (base["diagnosis_date"] <= iso(cycle)) & alive
    present = ((base["flag_true_on"] == "") | (day < base["flag_true_on"])) & (
        (base["silent_move_on"] == "") | (day < base["silent_move_on"])
    )
    age = _age(base, planned)
    a1c = on_dates(hba1c, rows, day)
    has_phone = base["has_phone"].to_numpy()
    terms = time_terms(planned, has_phone, base["district"])
    static = static_terms(base, age, a1c)
    district_base = base["district"].map(bases).to_numpy()
    common = district_base + static + terms["season"] + terms["covid"] + terms["trend"] + 0.15 * terms["sms"]
    common = common + DNA_PENALTY * dna_prev
    p_with = sigmoid(common + terms["reminder_term"])
    p_without = sigmoid(common)
    attended = invited.to_numpy() & present.to_numpy() & (rng.random(len(base)) < p_with)
    return pd.DataFrame(
        {
            "person_uid": base["person_uid"].to_numpy(),
            "cycle_start": iso(cycle),
            "planned_date": day.to_numpy(),
            "district": base["district"].to_numpy(),
            "travel_burden": base["travel_burden"].to_numpy(),
            "age": age.round(1),
            "hba1c": a1c,
            "has_phone": has_phone,
            "sms": terms["sms"],
            "reminder": terms["reminder"],
            "dna_prev": dna_prev,
            "planned_month": planned.dt.month.to_numpy(),
            "p_attend": p_with.round(4),
            "p_attend_no_reminder": p_without.round(4),
            "silent_moved": ~present.to_numpy() & (base["silent_move_on"] != "").to_numpy(),
            "invited": invited.to_numpy(),
            "attended": attended,
        }
    )


def _age(base: pd.DataFrame, when) -> np.ndarray:
    born = pd.to_datetime(base["dob"])
    return (pd.to_datetime(pd.Series(when).reset_index(drop=True)) - born).dt.days.to_numpy() / 365.25
