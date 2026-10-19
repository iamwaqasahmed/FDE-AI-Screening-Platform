"""Registry record shapes for schema versions 1, 2, and 3."""

from __future__ import annotations

from datetime import date, datetime, timedelta

from serve.versions import VersionPolicy
from simulation.world.engagement import REGISTRY_SCHEMA_V3, WEEKS

V3_WEEK = min(number for number, start in WEEKS.items() if start >= REGISTRY_SCHEMA_V3)
POLICY = VersionPolicy(default="2", versions=("1", "2", "3"), published_week={"3": V3_WEEK})
SPREADSHEET_EPOCH = date(1899, 12, 30)


def v1(row: dict) -> dict:
    return {"REG_NO": row["REGISTRY_NO"], "SURNAME": row["SURNAME"], "DOB": row["DOB"], "STATUS": row["RECORD_STATUS"]}


def v2(row: dict) -> dict:
    return dict(row)


def iso_birth_date(value: str) -> str | None:
    text = (value or "").strip()
    if text.isdigit():
        return (SPREADSHEET_EPOCH + timedelta(days=int(text))).isoformat()
    for pattern in ("%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(text, pattern).date().isoformat()
        except ValueError:
            continue
    return None


def v3(row: dict) -> dict:
    return {
        "registry_no": row["REGISTRY_NO"],
        "local_pid": row["LOCAL_PID"],
        "forename": row["FORENAME"],
        "surname": row["SURNAME"],
        "date_of_birth": iso_birth_date(row["DOB"]),
        "date_of_birth_as_supplied": row["DOB"],
        "sex": row["SEX"],
        "district": row["DISTRICT"],
        "home_clinic": row["HOME_CLINIC"],
        "flags": [flag for flag in row["FLAG"].split(";") if flag],
        "record_status": row["RECORD_STATUS"].lower(),
    }


SHAPERS = {"1": v1, "2": v2, "3": v3}
