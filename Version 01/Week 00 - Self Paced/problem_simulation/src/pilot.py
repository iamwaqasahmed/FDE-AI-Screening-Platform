"""Pilot scores and the hospital evaluation set."""

from __future__ import annotations

import numpy as np
import pandas as pd

FLIP = {"R0": "R2", "R1": "R3", "R2": "R0", "R3": "R1"}


def add_pilot(tables: dict[str, pd.DataFrame], cfg: dict, rng: np.random.Generator) -> dict[str, pd.DataFrame]:
    images = tables["image"]
    ungradable = images[(images["camera_class"] == "primary") & (images["grade"] == "U")]
    readable = images[(images["camera_class"] == "primary") & (images["grade"].isin(list(FLIP)))]
    take_u = cfg["pilot"]["ungradable"]
    take_g = cfg["pilot"]["images"] - take_u
    if len(ungradable) < take_u or len(readable) < take_g:
        raise ValueError("Not enough primary-care images for the pilot.")
    chosen_u = ungradable.sample(n=take_u, random_state=cfg["seed"])
    chosen_g = readable.sample(n=take_g, random_state=cfg["seed"] + 1)
    chosen = pd.concat([chosen_u, chosen_g], ignore_index=True)
    flip_idx = rng.choice(take_g, size=cfg["pilot"]["disagreements"], replace=False)
    labels = chosen_g["grade"].tolist()
    model = labels.copy()
    for offset in flip_idx:
        model[int(offset)] = FLIP[labels[int(offset)]]
    vendor = pd.DataFrame(
        {
            "image_id": chosen["image_id"].tolist(),
            "person_uid": chosen["person_uid"].tolist(),
            "file_name": chosen["file_name"].tolist(),
            "grader_label": chosen_u["grade"].tolist() + labels,
            "model_label": [""] * take_u + model,
            "model_score": [np.nan] * take_u + [0.62 if model[i] != labels[i] else 0.91 for i in range(take_g)],
        }
    )
    images.loc[images["image_id"].isin(chosen["image_id"]), "is_pilot"] = True
    tables["image"] = images
    tables["vendor_score"] = vendor
    tables["hospital_eval"] = _hospital_eval(cfg)
    return tables


def _hospital_eval(cfg: dict) -> pd.DataFrame:
    spec = cfg["hospital_eval"]
    referable = spec["referable"]
    true_positives = spec["true_positives"]
    false_negatives = referable - true_positives
    other = spec["images"] - referable
    false_positives = spec["false_positives"]
    true_negatives = other - false_positives
    rows = []
    rows += [("R2", True, "R2", True)] * true_positives
    rows += [("R2", True, "R0", False)] * false_negatives
    rows += [("R0", False, "R2", True)] * false_positives
    rows += [("R0", False, "R0", False)] * true_negatives
    if len(rows) != spec["images"]:
        raise ValueError("Hospital evaluation rows do not match the configured image count.")
    frame = pd.DataFrame(rows, columns=["grader_label", "referable", "model_label", "model_positive"])
    frame.insert(0, "image_id", [f"HE{i + 1:04d}" for i in range(len(frame))])
    frame.insert(1, "person_uid", "")
    return frame
