"""Clinicians, one home facility and one specialty each."""

from __future__ import annotations

from alwaha.config.scale import site_name
from alwaha.world.catalog import HOSPITALS, SPECIALTIES
from alwaha.world.sites import SITES

_NAMES = {row["id"]: row["name"] for row in SITES}


def roster(profile) -> list[dict]:
    rows = []
    for hospital in HOSPITALS:
        for index, specialty in enumerate(SPECIALTIES):
            rows.append(
                {
                    "clinician_id": f"{hospital}-{specialty}",
                    "facility": hospital,
                    "facility_name": site_name(profile, hospital, _NAMES.get(hospital, hospital)),
                    "specialty": specialty,
                    "gender": "f" if index % 2 == 0 else "m",
                    "leave_recorded_after_publish": hospital == "h-wadi" and specialty == "endo",
                }
            )
    return rows
