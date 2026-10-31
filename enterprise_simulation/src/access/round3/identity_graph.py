"""Identity links for referral R3C-1. Each observation stays in the list."""

from __future__ import annotations

REF = "R3C-1"
PERSON_A = "p-r3c-1"
PERSON_B = "p-r3c-2"
MEMBER_CHANNEL = "MBR-R3C-1"
MEMBER_PAYER = "MBR-R3C-9"
MRN = "MRN-R3C-1"
PHONE_SHARED = "604-555-2770"
PHONE_LATER = "604-555-2771"
_WINDOW_FROM = "2026-05-04T00:00:00Z"
_WINDOW_TO = "2026-08-04T00:00:00Z"
_ATTRS = (
    ("phone", "phone"),
    ("member_id", "member"),
    ("mrn", "mrn"),
)


def commands() -> list[dict]:
    """Return the 2026 identity commands for R3C-1, in time order."""
    rows = [*_channel(), *_hospital(), *_payer()]
    return sorted(rows, key=lambda row: (row["occurred_at"], row["command_id"]))


def edges(commands: list[dict]) -> list[dict]:
    """Return one edge per recorded link. Later commands do not drop earlier ones."""
    found: list[dict] = []
    for command in commands:
        found.extend(_command_edges(command))
    return found


def _channel() -> list[dict]:
    return [
        _command(
            "cmd-r3c-request",
            "channel",
            "RequestAccepted",
            "2026-04-06T15:05:00Z",
            "r3c-desk",
            1,
            {
                "ref": REF,
                "person_id": PERSON_A,
                "member_id": MEMBER_CHANNEL,
                "phone": PHONE_SHARED,
                "handset_delivered": False,
                "channel": "phone",
                "desk_region": "BC",
                "utterance": "calling about referral R3C-1",
                "same_person": [PERSON_A, MEMBER_CHANNEL],
            },
        ),
        _command(
            "cmd-r3c-member",
            "channel",
            "IdentifierRecorded",
            "2026-04-06T15:20:00Z",
            "r3c-desk",
            2,
            {
                "ref": REF,
                "person_id": PERSON_A,
                "member_id": MEMBER_CHANNEL,
                "recorded_on": "desk",
            },
        ),
        _command(
            "cmd-r3c-note",
            "channel",
            "DeskNote",
            "2026-04-22T15:30:00Z",
            "r3c-desk",
            3,
            {
                "ref": REF,
                "role": "clerk",
                "note": (
                    "cmd-r3c-phone-copy still stores phone 604-555-2770 on p-r3c-2. "
                    "cmd-r3c-split stores phone 604-555-2770 on p-r3c-1 and "
                    "phone 604-555-2771 on p-r3c-2. "
                    "The channel member id on R3C-1 is MBR-R3C-1. "
                    "The payer member id on R3C-1 is MBR-R3C-9."
                ),
            },
        ),
    ]


def _hospital() -> list[dict]:
    return [
        _command(
            "cmd-r3c-mrn",
            "hospital",
            "IdentifierRecorded",
            "2026-04-08T17:40:00Z",
            "r3c-chart",
            1,
            {
                "ref": REF,
                "person_id": PERSON_A,
                "mrn": MRN,
                "site": "fraser-burnaby",
                "state": "BC",
                "recorded_on": "hospital",
            },
        ),
        _command(
            "cmd-r3c-chart",
            "hospital",
            "ChartOpened",
            "2026-04-08T19:05:00Z",
            "r3c-chart",
            2,
            {
                "ref": REF,
                "person_id": PERSON_B,
                "site": "fraser-burnaby",
                "state": "BC",
                "note": "Chart opened for p-r3c-2. This command stores no phone.",
            },
        ),
        _command(
            "cmd-r3c-phone-copy",
            "hospital",
            "PhoneRecorded",
            "2026-04-09T16:20:00Z",
            "r3c-chart",
            3,
            {
                "ref": REF,
                "person_id": PERSON_B,
                "phone": PHONE_SHARED,
                "site": "fraser-burnaby",
                "copied_from_command_id": "cmd-r3c-request",
                "note": "Phone 604-555-2770 was copied onto person_id p-r3c-2.",
            },
        ),
        *_split(),
    ]


def _split() -> list[dict]:
    return [
        _command(
            "cmd-r3c-split",
            "hospital",
            "IdentitySplit",
            "2026-04-16T18:55:00Z",
            "r3c-chart",
            4,
            {
                "ref": REF,
                "prior_command_id": "cmd-r3c-phone-copy",
                "person_id": PERSON_A,
                "phone": PHONE_SHARED,
                "other_person_id": PERSON_B,
                "other_phone": PHONE_LATER,
                "bindings": [
                    {"person_id": PERSON_A, "phone": PHONE_SHARED},
                    {"person_id": PERSON_B, "phone": PHONE_LATER},
                ],
                "note": (
                    "This event stores phone 604-555-2770 on p-r3c-1 and "
                    "phone 604-555-2771 on p-r3c-2. "
                    "cmd-r3c-phone-copy remains in the log."
                ),
            },
        )
    ]


def _payer() -> list[dict]:
    window = {"effective_from": _WINDOW_FROM, "effective_to": _WINDOW_TO}
    return [
        _command(
            "cmd-r3c-coverage",
            "payer",
            "CoverageDecided",
            "2026-04-21T16:00:00Z",
            "r3c-payer",
            1,
            {
                "ref": REF,
                "person_id": PERSON_A,
                "member_id": MEMBER_PAYER,
                "answer": "yes",
                "currency": "CAD",
                "member_region": "BC",
                "window": window,
                **window,
            },
        )
    ]


def _command_edges(command: dict) -> list[dict]:
    payload = command.get("payload") or {}
    source = command["command_id"]
    found: list[dict] = []
    for subject in _subjects(payload):
        found.extend(_subject_edges(subject, source))
    found.extend(_pair_edge(payload, source))
    return found


def _subjects(payload: dict) -> list[dict]:
    bindings = payload.get("bindings")
    if bindings:
        return [item for item in bindings if isinstance(item, dict)]
    return [_flat(payload)]


def _flat(payload: dict) -> dict:
    return {
        key: payload[key]
        for key in ("person_id", "phone", "member_id", "mrn")
        if payload.get(key)
    }


def _subject_edges(subject: dict, source: str) -> list[dict]:
    origin = subject.get("person_id")
    if not origin:
        return []
    found = []
    for key, rel in _ATTRS:
        value = subject.get(key)
        if value:
            found.append(_edge(origin, rel, value, source))
    return found


def _pair_edge(payload: dict, source: str) -> list[dict]:
    pair = payload.get("same_person")
    if not isinstance(pair, (list, tuple)) or len(pair) != 2:
        return []
    left, right = pair
    if not left or not right:
        return []
    return [_edge(left, "same_person", right, source)]


def _edge(origin: str, rel: str, value: str, source: str) -> dict:
    return {"from": origin, "rel": rel, "to": value, "source": source}


def _command(
    command_id: str,
    authority: str,
    event_type: str,
    occurred_at: str,
    stream_id: str,
    stream_rev: int,
    payload: dict,
) -> dict:
    return {
        "command_id": command_id,
        "authority": authority,
        "type": event_type,
        "occurred_at": occurred_at,
        "stream_id": stream_id,
        "stream_rev": stream_rev,
        "payload": payload,
    }
