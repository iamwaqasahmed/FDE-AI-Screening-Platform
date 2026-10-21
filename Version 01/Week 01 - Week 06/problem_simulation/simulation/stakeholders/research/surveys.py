"""Staff and patient survey responses. The loudest theme is planted to differ from the costliest problem."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.economics.problems import THEMES
from simulation.world.sites import ALL_SITES, DISTRICTS

STAFF_COUNT = 60
PATIENT_COUNT = 240
STAFF_GROUPS = ("grader", "booking", "call centre", "clinic", "outreach", "hospital")
AGE_BANDS = ("18-39", "40-59", "60-74", "75+")
PATIENT_TEXT = {
    "letters": ("My result letter never came.", "I had to ring to find out my result.", "The letter arrived after the "
                "appointment it was about."),
    "travel_and_parking": ("Parking at the clinic is impossible.", "The bus takes over an hour each way."),
    "hospital_wait": ("I waited months for the hospital eye appointment.", "Nobody told me how long the hospital wait was."),
    "results_delay": ("It took a long time to hear anything after my photos.",),
    "missed_appointments": ("I missed my slot because the time did not suit me.",),
}
STAFF_TEXT = {
    "letters": ("Half my calls are people chasing letters.", "We cannot see whether the bureau sent a letter."),
    "travel_and_parking": ("Patients arrive late because of parking.", "Outreach patients travel too far."),
    "hospital_wait": ("Fast-track slots are always full.", "We have nowhere to send urgent referrals."),
    "results_delay": ("The grading queue never gets shorter.", "Some photos never seem to reach a grader."),
    "missed_appointments": ("Empty slots every afternoon.", "Reminders do not seem to change much here."),
}


def theme_weights(voiced: str, costliest: str) -> dict[str, float]:
    rest = [theme for theme in THEMES if theme not in (voiced, costliest)]
    weights = {voiced: 0.36, costliest: 0.08}
    weights.update({theme: 0.56 / len(rest) for theme in rest})
    return weights


def allocate(total: int, weights: dict[str, float], rng: np.random.Generator) -> list[str]:
    """Largest-remainder counts, then a seeded shuffle. The voiced theme always has the most responses."""
    raw = {theme: total * weight for theme, weight in weights.items()}
    counts = {theme: int(value) for theme, value in raw.items()}
    for theme in sorted(raw, key=lambda key: (counts[key] - raw[key], key))[: total - sum(counts.values())]:
        counts[theme] += 1
    labels = [theme for theme in THEMES for _ in range(counts.get(theme, 0))]
    return [labels[index] for index in rng.permutation(len(labels))]


def staff_survey(voiced: str, costliest: str, rng: np.random.Generator) -> pd.DataFrame:
    themes = allocate(STAFF_COUNT, theme_weights(voiced, costliest), rng)
    rows = []
    for index, theme in enumerate(themes, start=1):
        options = STAFF_TEXT[theme]
        rows.append({"respondent_id": f"S{index:03d}", "staff_group": STAFF_GROUPS[int(rng.integers(0, len(STAFF_GROUPS)))],
                     "site": ALL_SITES[int(rng.integers(0, len(ALL_SITES)))], "top_problem": theme,
                     "severity_1_to_5": int(rng.integers(3, 6)), "comment": options[int(rng.integers(0, len(options)))]})
    return pd.DataFrame(rows)


def patient_survey(voiced: str, costliest: str, rng: np.random.Generator) -> pd.DataFrame:
    themes = allocate(PATIENT_COUNT, theme_weights(voiced, costliest), rng)
    rows = []
    for index, theme in enumerate(themes, start=1):
        options = PATIENT_TEXT[theme]
        rows.append({"respondent_id": f"R{index:04d}", "district": DISTRICTS[int(rng.integers(0, len(DISTRICTS)))],
                     "age_band": AGE_BANDS[int(rng.integers(0, len(AGE_BANDS)))],
                     "satisfaction_1_to_5": int(rng.integers(1, 5)), "theme": theme,
                     "comment": options[int(rng.integers(0, len(options)))]})
    return pd.DataFrame(rows)


def voice_counts(staff: pd.DataFrame, patients: pd.DataFrame) -> dict[str, int]:
    counts = staff["top_problem"].value_counts().add(patients["theme"].value_counts(), fill_value=0)
    return {theme: int(counts.get(theme, 0)) for theme in THEMES}
