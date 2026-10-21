"""The vendor model's hidden behaviour: calibration moves with firmware, and it is weaker on some subgroups."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.care.behaviour import sigmoid
from simulation.care.grading import latent_severity

REJECT_BELOW = 0.30
RETRO_FROM = "2022-01-01"
LABEL_CUTS = ((0.25, "R0"), (0.50, "R1"), (0.80, "R2"))
OLDER_PENALTY = 1.1
OPERATOR_PENALTY = 0.5


def stamp_vendor(events: pd.DataFrame, rng: np.random.Generator) -> None:
    """Score every primary-care and outreach capture from 2022. The pilot file shows only the pilot rows."""
    eligible = events["capture"].isin(["shared_folder", "outreach_laptop", "vendor_cloud"]).to_numpy()
    eligible = eligible & events["photo_date"].ge(RETRO_FROM).to_numpy()
    severity = latent_severity(events)
    age = (pd.to_datetime(events["photo_date"]) - pd.to_datetime(events["dob"])).dt.days.to_numpy() / 365.25
    referable = severity >= 2
    noise_sd = 0.55 + 1.2 * np.clip(0.6 - events["quality"].to_numpy(), 0, None)
    z = (
        2.3 * (severity - 1.5)
        + 6.0 * events["firmware_score_shift"].to_numpy()
        + 6.0 * events["model_vendor_bias"].to_numpy()
        - np.where((age >= 75) & referable, OLDER_PENALTY, 0.0)
        - np.where((events["operator"] == "PB").to_numpy() & referable, OPERATOR_PENALTY, 0.0)
        + rng.normal(0, 1, len(events)) * noise_sd
    )
    score = sigmoid(z)
    rejected = events["quality"].to_numpy() < REJECT_BELOW
    keep = eligible & ~rejected
    events["vendor_scored"] = eligible
    events["vendor_score"] = np.where(keep, score.round(3), np.nan)
    events["vendor_label"] = np.where(keep, _labels(score), "")


def _labels(score: np.ndarray) -> np.ndarray:
    out = np.full(len(score), "R3", dtype=object)
    for cut, label in reversed(LABEL_CUTS):
        out = np.where(score < cut, label, out)
    return out
