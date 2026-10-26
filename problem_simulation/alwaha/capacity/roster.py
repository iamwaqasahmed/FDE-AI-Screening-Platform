"""Clinicians, one home facility and one specialty each.

Every hospital is crossed with every specialty. The gender alternates with the specialty index. Leave recorded after publish is set only for the Wadi endocrinology clinician. Other clinicians leave that flag false.
"""

from __future__ import annotations

from alwaha.config.scale import site_name
from alwaha.world.catalog import HOSPITALS, SPECIALTIES
from alwaha.world.sites import SITES

_NAMES = {row["id"]: row["name"] for row in SITES}


def roster(profile) -> list[dict]:
    """Return one clinician row per hospital and specialty, using the profile's site names."""
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
                    # Only this clinician is the one whose leave lands after the sessions are published.
                    "leave_recorded_after_publish": hospital == "h-wadi" and specialty == "endo",
                }
            )
    return rows
