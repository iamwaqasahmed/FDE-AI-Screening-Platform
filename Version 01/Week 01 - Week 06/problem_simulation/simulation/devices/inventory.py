"""Camera inventory with firmware history. Two upgrades change image quality and vendor calibration."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

import pandas as pd

from simulation.world.clock import FIRMWARE_MARKET, FIRMWARE_RIVER
from simulation.world.sites import CAPTURE_SITES, MARKET, RIVER_SITE, is_hospital

MODELS = {
    "Optica R2": {"quality": 0.70, "vendor_bias": 0.00},
    "Lumen 7": {"quality": 0.62, "vendor_bias": -0.06},
    "FundusPro X": {"quality": 0.74, "vendor_bias": 0.02},
}


@dataclass(frozen=True)
class Firmware:
    version: str
    installed: date
    quality_shift: float
    score_shift: float


@dataclass(frozen=True)
class Camera:
    device_id: str
    site: str
    model: str
    installed: date
    firmware: tuple[Firmware, ...]


def _site_code(site: str) -> str:
    return "".join(word[0] for word in site.split()[:3]).upper()


def _history(site: str, model: str) -> tuple[Firmware, ...]:
    base = [Firmware("2.0.4", date(2017, 1, 1), 0.0, 0.0), Firmware("2.1.0", date(2020, 8, 17), 0.0, 0.0)]
    if site == MARKET:
        base.append(Firmware("4.2.0", FIRMWARE_MARKET, -0.13, 0.09))
    elif site == RIVER_SITE:
        base.append(Firmware("3.1.0", FIRMWARE_RIVER, 0.10, -0.12))
    else:
        base.append(Firmware("2.2.1", date(2023, 11, 6), 0.0, 0.0))
    return tuple(base)


def build_cameras() -> tuple[Camera, ...]:
    cameras = []
    for site in CAPTURE_SITES:
        count = 2 if is_hospital(site) or site == RIVER_SITE else 1
        for number in range(1, count + 1):
            model = "Lumen 7" if site == RIVER_SITE else ("FundusPro X" if number == 2 else "Optica R2")
            cameras.append(
                Camera(f"CAM-{_site_code(site)}-{number:02d}", site, model, date(2016, 6, 1), _history(site, model))
            )
    return tuple(cameras)


CAMERAS = build_cameras()


def firmware_on(camera: Camera, day: str) -> Firmware:
    live = [item for item in camera.firmware if item.installed.isoformat() <= day]
    return live[-1] if live else camera.firmware[0]


def inventory_frame(lagged: bool) -> pd.DataFrame:
    """Truth when lagged is False. The handover spreadsheet lags: the hand-kept column misses an upgrade."""
    rows = []
    for camera in CAMERAS:
        history = list(camera.firmware)
        if lagged and camera.site == RIVER_SITE:
            history = history[:-1]
        latest = history[-1]
        recorded = latest.installed
        if lagged and camera.site == MARKET:
            recorded = date(recorded.year, recorded.month, 1).replace(month=min(recorded.month + 2, 12))
        rows.append(
            {
                "device_id": camera.device_id,
                "site": camera.site,
                "model": camera.model,
                "installed": camera.installed.isoformat(),
                "firmware": latest.version,
                "firmware_updated": recorded.isoformat(),
            }
        )
    return pd.DataFrame(rows)


def firmware_history_frame() -> pd.DataFrame:
    rows = [
        {"device_id": camera.device_id, "site": camera.site, "version": item.version, "installed": item.installed.isoformat()}
        for camera in CAMERAS
        for item in camera.firmware
    ]
    return pd.DataFrame(rows)
