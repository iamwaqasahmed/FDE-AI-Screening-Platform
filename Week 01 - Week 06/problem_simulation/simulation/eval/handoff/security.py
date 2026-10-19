"""Four threats. A closed risk is not a closed threat, and a live threat reopens a closed risk."""

from __future__ import annotations

from simulation.world.staff import STAFF


def summary(world: dict) -> dict:
    threats = {item["threat_id"]: item for item in world["gold"]["threats"]}
    return {"threat_summary": {
        "threat_ids": ["T1", "T2", "T3", "T4"],
        "live": ["T1", "T2", "T4"],
        "service_account": threats["T2"]["account_id"],
        "excess_role": threats["T2"]["excess_role"],
        "stale_accounts": list(threats["T4"]["accounts"]),
        "reopen": "R-11",
        "stays_closed": "R-08",
    }}


def rows(world: dict) -> list[dict]:
    threats = {item["threat_id"]: item for item in world["gold"]["threats"]}
    account = threats["T2"]["account_id"]
    stale = list(threats["T4"]["accounts"])
    return [
        _row("T1", "components", list(threats["T1"]["components"]), ["ea-principles", "security-supplier-assurance", "ea-current-state"], True),
        _row("T2", "evidence", [account], ["security-authentication-standard"], True),
        _row("T3", "evidence", ["INC-0270"], ["security-logging-standard"], False),
        _row("T4", "evidence", ["INC-0262", *stale], ["security-authentication-standard"], True, any_of=[["INC-0262"], stale]),
    ]


def owners() -> list[str]:
    return sorted(person.name for person in STAFF)


def _row(threat_id: str, field: str, need: list[str], standards: list[str], live: bool, any_of: list[list[str]] | None = None) -> dict:
    return {"threat_id": threat_id, "field": field, "need": need, "any_of": any_of, "standards": standards, "live": live}
