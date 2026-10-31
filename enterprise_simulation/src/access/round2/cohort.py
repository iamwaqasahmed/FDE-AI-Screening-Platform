"""Round-2 cohort. Region, site, phone, and coverage follow the index."""

from __future__ import annotations

import random
from datetime import datetime, timedelta, timezone

_START = datetime(2025, 2, 2, tzinfo=timezone.utc)
_SHARED_INDEXES = (21, 22)
_SHARED_PHONE = "604-555-2144"
_PERSON_PREFIX = "p-r2b-"
_AUTHORITIES = ("channel", "hospital", "payer")
_ANSWERS = ("yes", "no", "timeout")


def cohort(seed: int = 20270110, count: int = 48) -> list[dict]:
    """Return channel, hospital, and payer commands for `count` indexes."""
    return _build(seed, count, ref_prefix="R2B-", command_prefix="cmd-r2b-")


def workload(seed: int = 20270110, count: int = 400) -> list[dict]:
    """Return the same index rules with workload ref and command prefixes."""
    return _build(seed, count, ref_prefix="R2BW-", command_prefix="cmd-r2bw-")


def summarize(commands: list[dict]) -> dict:
    """Count authorities, coverage answers, and BC rows on a 206 phone."""
    by_authority = {name: 0 for name in _AUTHORITIES}
    by_answer = {name: 0 for name in _ANSWERS}
    phones = _phones_by_ref(commands)
    bc_with_206_phone = 0
    for command in commands:
        _tally(by_authority, command.get("authority"))
        payload = command.get("payload") or {}
        if command.get("type") == "CoverageDecided":
            _tally(by_answer, payload.get("answer"))
        if _bc_uses_206(command, phones):
            bc_with_206_phone += 1
    return {
        "by_authority": by_authority,
        "by_answer": by_answer,
        "bc_with_206_phone": bc_with_206_phone,
    }


def _build(seed: int, count: int, ref_prefix: str, command_prefix: str) -> list[dict]:
    rng = random.Random(seed)
    rows: list[dict] = []
    for index in range(count):
        rows.extend(_index_rows(index, rng, ref_prefix, command_prefix))
    return rows


def _index_rows(
    index: int,
    rng: random.Random,
    ref_prefix: str,
    command_prefix: str,
) -> list[dict]:
    requested, accepted, decided = _moments(index, rng)
    profile = _profile(index)
    ref = f"{ref_prefix}{index:04d}"
    rows = [
        _command(
            _command_id(command_prefix, index, "request"),
            "channel",
            "RequestAccepted",
            requested,
            ref,
            _request_payload(ref, profile),
        )
    ]
    if profile["open"]:
        return rows
    rows.append(
        _command(
            _command_id(command_prefix, index, "referral"),
            "hospital",
            "ReferralAccepted",
            accepted,
            ref,
            _hospital_payload(ref, profile),
        )
    )
    rows.append(
        _command(
            _command_id(command_prefix, index, "coverage"),
            "payer",
            "CoverageDecided",
            decided,
            ref,
            _coverage_payload(ref, profile, accepted),
        )
    )
    return rows


def _profile(index: int) -> dict:
    region = _region(index)
    return {
        "region": region,
        "currency": "CAD" if region == "BC" else "USD",
        "phone": _phone(index, region),
        "person_id": f"{_PERSON_PREFIX}{index:04d}",
        "site": _site(region),
        "open": index % 5 == 0,
        "answer": _answer(index),
    }


def _region(index: int) -> str:
    if index in _SHARED_INDEXES or index % 3 == 0:
        return "BC"
    return "WA"


def _site(region: str) -> str:
    if region == "BC":
        return "fraser-burnaby"
    return "cascade-seattle"


def _answer(index: int) -> str | None:
    if index % 5 == 0:
        return None
    if index % 11 == 0:
        return "no"
    if index % 13 == 0:
        return "timeout"
    return "yes"


def _phone(index: int, region: str) -> str:
    if index in _SHARED_INDEXES:
        return _SHARED_PHONE
    if region == "BC":
        return f"604-555-{_bc_suffix(index):04d}"
    return f"206-555-{3000 + (index % 1000):04d}"


def _bc_suffix(index: int) -> int:
    """Stay inside 2000-2999 and leave 2144 for the shared handset."""
    suffix = 2000 + (index % 999)
    if suffix >= 2144:
        suffix += 1
    return suffix


def _moments(index: int, rng: random.Random) -> tuple[datetime, datetime, datetime]:
    requested = _START + timedelta(
        days=4 * index,
        hours=rng.randint(8, 16),
        minutes=rng.randint(0, 59),
    )
    accepted = requested + timedelta(hours=2)
    decided = accepted + timedelta(hours=2)
    return requested, accepted, decided


def _stamp(moment: datetime) -> str:
    return moment.strftime("%Y-%m-%dT%H:%M:%SZ")


def _command_id(prefix: str, index: int, suffix: str) -> str:
    return f"{prefix}{index}-{suffix}"


def _command(
    command_id: str,
    authority: str,
    event_type: str,
    when: datetime,
    ref: str,
    payload: dict,
) -> dict:
    return {
        "command_id": command_id,
        "authority": authority,
        "type": event_type,
        "occurred_at": _stamp(when),
        "stream_id": ref,
        "stream_rev": 1,
        "payload": payload,
    }


def _request_payload(ref: str, profile: dict) -> dict:
    return {
        "ref": ref,
        "person_id": profile["person_id"],
        "phone": profile["phone"],
        "member_region": profile["region"],
    }


def _hospital_payload(ref: str, profile: dict) -> dict:
    return {
        "ref": ref,
        "person_id": profile["person_id"],
        "site": profile["site"],
        "member_region": profile["region"],
    }


def _coverage_payload(ref: str, profile: dict, accepted: datetime) -> dict:
    payload = {
        "ref": ref,
        "person_id": profile["person_id"],
        "answer": profile["answer"],
        "member_region": profile["region"],
        "currency": profile["currency"],
    }
    if profile["answer"] != "timeout":
        payload["effective_from"] = _stamp(accepted + timedelta(days=3))
    return payload


def _phones_by_ref(commands: list[dict]) -> dict[str, str]:
    found: dict[str, str] = {}
    for command in commands:
        payload = command.get("payload") or {}
        phone = payload.get("phone")
        ref = payload.get("ref") or command.get("stream_id")
        if phone and ref:
            found[str(ref)] = str(phone)
    return found


def _tally(counts: dict, key: object) -> None:
    if isinstance(key, str) and key:
        counts[key] = counts.get(key, 0) + 1


def _bc_uses_206(command: dict, phones: dict[str, str]) -> bool:
    payload = command.get("payload") or {}
    if payload.get("member_region") != "BC":
        return False
    phone = payload.get("phone")
    if not phone:
        ref = payload.get("ref") or command.get("stream_id")
        phone = phones.get(str(ref), "")
    return str(phone).startswith("206")
