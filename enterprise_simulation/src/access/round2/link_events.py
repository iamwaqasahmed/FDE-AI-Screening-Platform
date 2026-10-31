"""One referral recorded on the channel, hospital, and payer logs."""

from __future__ import annotations

REF = "R2D-7"
PERSON = "p-r2d-7"
STREAM = "r2d-7"
DESK_MEMBER = "MBR-R2D-7"
HOSPITAL_MEMBER = "MRN-R2D-7"


def commands() -> list[dict]:
    """Return the January 2027 commands for referral R2D-7."""
    rows = [*_channel(), *_hospital(), *_payer()]
    return sorted(rows, key=lambda row: row["occurred_at"])


def _channel() -> list[dict]:
    return [
        _command(
            "cmd-r2d-session",
            "channel",
            "DeskSession",
            "2027-01-18T15:10:00Z",
            1,
            _fields(
                member_id=DESK_MEMBER,
                session_id="sess-r2d-7",
                phone="604-555-0148",
                postal="V6B 1A1",
                desk_region="BC",
                zone="America/Vancouver",
                channel="phone",
            ),
        ),
        _command(
            "cmd-r2d-request",
            "channel",
            "RequestAccepted",
            "2027-01-18T15:26:00Z",
            2,
            _fields(
                member_id=DESK_MEMBER,
                utterance="asking about referral R2D-7",
                handset_delivered=False,
                channel="phone",
                desk_region="BC",
            ),
        ),
        _command(
            "cmd-r2d-desk-id",
            "channel",
            "IdentifierRecorded",
            "2027-01-18T15:40:00Z",
            3,
            _fields(member_id=DESK_MEMBER, recorded_on="desk"),
        ),
        _command(
            "cmd-r2d-note",
            "channel",
            "DeskNote",
            "2027-01-22T16:45:00Z",
            4,
            _fields(
                role="clerk",
                desk_member_id=DESK_MEMBER,
                hospital_member_id=HOSPITAL_MEMBER,
                note=(
                    "Desk copy of the member id is MBR-R2D-7. "
                    "Hospital copy of the member id is MRN-R2D-7. "
                    "The two identifiers disagree."
                ),
            ),
        ),
    ]


def _hospital() -> list[dict]:
    return [
        _command(
            "cmd-r2d-referral",
            "hospital",
            "ReferralAccepted",
            "2027-01-19T17:05:00Z",
            1,
            _fields(
                member_id=HOSPITAL_MEMBER,
                site="fraser-burnaby",
                state="BC",
            ),
        ),
        _command(
            "cmd-r2d-chart",
            "hospital",
            "IdentifierRecorded",
            "2027-01-19T18:20:00Z",
            2,
            _fields(
                member_id=HOSPITAL_MEMBER,
                recorded_on="hospital",
                site="fraser-burnaby",
            ),
        ),
        _command(
            "cmd-r2d-offer",
            "hospital",
            "SlotOffered",
            "2027-01-21T22:00:00Z",
            3,
            _fields(
                site="fraser-burnaby",
                offer_id="offer-r2d-7",
                version="slot-r2d-7",
            ),
        ),
    ]


def _payer() -> list[dict]:
    return [
        _command(
            "cmd-r2d-coverage",
            "payer",
            "CoverageDecided",
            "2027-01-20T16:00:00Z",
            1,
            _fields(
                answer="yes",
                effective_from="2027-01-25T00:00:00Z",
                effective_to="2027-01-31T00:00:00Z",
                currency="CAD",
                member_region="BC",
            ),
        )
    ]


def _fields(**extra: object) -> dict:
    return {"ref": REF, "person_id": PERSON, **extra}


def _command(
    command_id: str,
    authority: str,
    event_type: str,
    occurred_at: str,
    rev: int,
    payload: dict,
) -> dict:
    return {
        "command_id": command_id,
        "authority": authority,
        "type": event_type,
        "occurred_at": occurred_at,
        "stream_id": STREAM,
        "stream_rev": rev,
        "payload": payload,
    }
