"""The did-not-attend table the authority's analyst built: one row per invitation, with a feature filled in after the outcome."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.ml.keys import patient_keys

LEAKY_FEATURE = "booking_status_final"
GROUP_COLUMN = "patient_key"
TIME_COLUMN = "cycle_start"
LABEL = "did_not_attend"
NUMERIC = ("travel_burden", "age", "hba1c", "years_diagnosed", "dna_prev", "has_phone", "sms", "reminder")
CATEGORICAL = ("district", "sex", "diabetes_type", "planned_month")
STATUS_ATTENDED = (("closed_attended", 0.93), ("closed_rebooked", 0.07))
STATUS_MISSED = (("closed_no_show", 0.58), ("closed_attended", 0.04), ("closed_cancelled", 0.18), ("closed_rebooked", 0.12), ("open", 0.08))


def dna_table(invitations: pd.DataFrame, people: pd.DataFrame, rng: np.random.Generator) -> tuple[pd.DataFrame, np.ndarray]:
    """The table and, row for row, the person ids it was built from (truth only)."""
    base = people.loc[people["alias_of"] == "", ["person_uid", "sex", "diabetes_type", "diagnosis_date"]]
    frame = invitations.merge(base, on="person_uid", how="left", validate="many_to_one")
    frame = frame.sort_values(["cycle_start", "planned_date", "person_uid"]).reset_index(drop=True)
    missed = ~frame["attended"].to_numpy()
    years = (pd.to_datetime(frame["planned_date"]) - pd.to_datetime(frame["diagnosis_date"])).dt.days.to_numpy() / 365.25
    table = pd.DataFrame(
        {
            "invitation_ref": [f"INV-{number:07d}" for number in range(1, len(frame) + 1)],
            GROUP_COLUMN: patient_keys(frame["person_uid"], rng).to_numpy(),
            TIME_COLUMN: frame["cycle_start"].to_numpy(),
            "planned_date": frame["planned_date"].to_numpy(),
            "district": frame["district"].to_numpy(),
            "sex": frame["sex"].to_numpy(),
            "diabetes_type": frame["diabetes_type"].to_numpy(),
            "years_diagnosed": np.round(np.maximum(years, 0), 1),
            "travel_burden": frame["travel_burden"].to_numpy(),
            "age": frame["age"].to_numpy(),
            "hba1c": frame["hba1c"].to_numpy(),
            "has_phone": frame["has_phone"].astype(int).to_numpy(),
            "sms": frame["sms"].astype(int).to_numpy(),
            "reminder": frame["reminder"].astype(int).to_numpy(),
            "dna_prev": frame["dna_prev"].to_numpy(),
            "planned_month": frame["planned_month"].to_numpy(),
            LEAKY_FEATURE: _status(missed, rng),
            LABEL: missed.astype(int),
        }
    )
    return table, frame["person_uid"].to_numpy()


def _status(missed: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    attended_draw = _draw(STATUS_ATTENDED, rng.random(len(missed)))
    missed_draw = _draw(STATUS_MISSED, rng.random(len(missed)))
    return np.where(missed, missed_draw, attended_draw)


def _draw(options: tuple, roll: np.ndarray) -> np.ndarray:
    edges = np.cumsum([share for _, share in options])
    index = np.minimum(np.searchsorted(edges, roll, side="right"), len(options) - 1)
    return np.array([label for label, _ in options], dtype=object)[index]


def leakage_truth(table: pd.DataFrame) -> dict:
    per_person = table.groupby(GROUP_COLUMN).size()
    return {
        "leaky_feature": LEAKY_FEATURE,
        "why": "The booking status is closed after the appointment date, so it encodes whether the person attended.",
        "group_column": GROUP_COLUMN,
        "time_column": TIME_COLUMN,
        "label": LABEL,
        "rows": int(len(table)),
        "people": int(per_person.size),
        "mean_rows_per_person": round(float(per_person.mean()), 3),
        "people_with_repeat_rows": int((per_person > 1).sum()),
        "label_rate": round(float(table[LABEL].mean()), 4),
        "honest_split": "Hold out whole people and train on earlier cycles than the test cycles.",
    }
