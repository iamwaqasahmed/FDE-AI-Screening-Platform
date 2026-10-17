"""Keys the ML handover uses instead of person ids, and the shared bands and referable rules."""

from __future__ import annotations

import numpy as np
import pandas as pd

AGE_BANDS = ((0, "<40"), (40, "40-59"), (60, "60-74"), (75, "75+"))
REFERABLE_CODES = ("R2", "R3")
GRADED_CODES = ("R0", "R1", "R2", "R3")


def age_at(events: pd.DataFrame) -> np.ndarray:
    return (pd.to_datetime(events["photo_date"]) - pd.to_datetime(events["dob"])).dt.days.to_numpy() / 365.25


def age_band(age: np.ndarray) -> np.ndarray:
    out = np.full(len(age), AGE_BANDS[0][1], dtype=object)
    for low, label in AGE_BANDS[1:]:
        out = np.where(age >= low, label, out)
    return out


def capture_refs(frame: pd.DataFrame) -> pd.Series:
    """One stable reference per capture. File names repeat for same-name, same-day people."""
    order = frame.sort_values(["photo_date", "file_name", "event_id"]).index
    refs = pd.Series([f"VR-{number:06d}" for number in range(1, len(order) + 1)], index=order)
    return refs.reindex(frame.index)


def patient_keys(person_uid: pd.Series, rng: np.random.Generator) -> pd.Series:
    """A pseudonymous key per person, shuffled so it does not follow registration order."""
    people = np.array(sorted(person_uid.unique()), dtype=object)
    numbers = rng.permutation(len(people)) + 1
    lookup = dict(zip(people, [f"PK-{number:06d}" for number in numbers]))
    return person_uid.map(lookup)


def grader_referable(grade: pd.Series) -> np.ndarray:
    return grade.isin(list(REFERABLE_CODES)).to_numpy()


def is_graded(grade: pd.Series) -> np.ndarray:
    return grade.isin(list(GRADED_CODES)).to_numpy()
