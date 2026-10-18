"""The live registry shaper. Version 3 of the API is not version 3 of the file."""

from __future__ import annotations

from serve.routers.registry_schema import v3

FILE_COLUMNS = ("DISTRICT_CODE", "FLAG_DATE", "SCHEMA_VERSION", "REGISTERED_SITE")


def api_shape() -> dict:
    shaped = v3(_sample())
    missing = [column for column in ("DISTRICT_CODE", "FLAG_DATE", "SCHEMA_VERSION") if column not in shaped]
    keeps = ["home_clinic"] if "home_clinic" in shaped else []
    return {"keeps": keeps, "missing": missing, "old_numbers": True, "shaped_keys": sorted(shaped)}


def _sample() -> dict:
    return {
        "REGISTRY_NO": "HR000001",
        "LOCAL_PID": "LP000001",
        "FORENAME": "Ada",
        "SURNAME": "North",
        "DOB": "24/09/1996",
        "SEX": "F",
        "DISTRICT": "North City",
        "HOME_CLINIC": "North City Eye Clinic",
        "FLAG": "",
        "RECORD_STATUS": "Active",
    }
