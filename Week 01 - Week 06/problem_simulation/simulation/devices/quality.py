"""Per-capture image quality from device, firmware, dilation, operator, and age."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.devices.inventory import CAMERAS, MODELS, firmware_on
from simulation.world.sites import RIVER_SITE, is_hospital

UNGRADABLE_BELOW = 0.48
OPERATORS = ("JT", "RS", "MK", "AW", "PB", "LN")
POOR_OPERATOR = "PB"


def stamp_devices(events: pd.DataFrame, rng: np.random.Generator) -> None:
    by_site: dict[str, list] = {}
    for camera in CAMERAS:
        by_site.setdefault(camera.site, []).append(camera)
    device, firmware, quality_shift, score_shift, model_quality, model_bias = [], [], [], [], [], []
    picks = rng.random(len(events))
    for roll, site, day in zip(picks, events["site"], events["photo_date"]):
        options = by_site[site]
        camera = options[int(roll * len(options))]
        item = firmware_on(camera, day)
        device.append(camera.device_id)
        firmware.append(item.version)
        quality_shift.append(item.quality_shift)
        score_shift.append(item.score_shift)
        model_quality.append(MODELS[camera.model]["quality"])
        model_bias.append(MODELS[camera.model]["vendor_bias"])
    events["device_id"] = device
    events["firmware"] = firmware
    events["firmware_score_shift"] = score_shift
    events["model_vendor_bias"] = model_bias
    events["operator"] = _operators(events, rng)
    dilation_rate = np.array([_dilation_rate(site) for site in events["site"]])
    events["dilated"] = rng.random(len(events)) < dilation_rate
    age = (pd.to_datetime(events["photo_date"]) - pd.to_datetime(events["dob"])).dt.days.to_numpy() / 365.25
    quality = (
        np.array(model_quality)
        + np.array(quality_shift)
        + np.where(events["dilated"], 0.10, -0.04)
        + np.where(events["operator"] == POOR_OPERATOR, -0.12, 0.0)
        - 0.004 * np.maximum(age - 60, 0)
        + rng.normal(0, 0.12, len(events))
    )
    events["quality"] = np.clip(quality, 0, 1).round(3)
    events["quality_shown"] = np.where(events["capture"] == "pacs", "", np.round(events["quality"] * 10).astype(int).astype(str))


def _operators(events: pd.DataFrame, rng: np.random.Generator) -> np.ndarray:
    site_codes = {site: index for index, site in enumerate(sorted(events["site"].unique()))}
    offset = events["site"].map(site_codes).to_numpy()
    pick = (offset + rng.integers(0, 3, len(events))) % len(OPERATORS)
    return np.array(OPERATORS, dtype=object)[pick]


def _dilation_rate(site: str) -> float:
    if is_hospital(site):
        return 0.85
    if site == RIVER_SITE:
        return 0.30
    return 0.55
