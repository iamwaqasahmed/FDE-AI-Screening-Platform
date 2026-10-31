"""Finance board for one ledger ref. The list opens on that board."""

from __future__ import annotations

REF = "R3F-LEDGER"
AMOUNT = 18420
BOOK = "hospital-finance"
SITE = "cascade-seattle"
COPY = "cascade-copy"
PERSON = "p-r3f-ledger"
MEMBER = "MBR-R3F-14"


def commands() -> list[dict]:
    """Return the ledger commands. The first row is the finance board."""
    return [
        _board(),
        _finance_note(),
        _desk_note(),
        _payer(),
        _copy(),
        _posted(),
        _asked(),
        _member(),
        _site(),
    ]


def _board() -> dict:
    return _command(
        "cmd-r3f-board",
        "hospital",
        "BoardPrinted",
        "2027-01-21T15:00:00Z",
        "r3f-board",
        1,
        {
            "ref": REF,
            "board": "finance",
            "amount": AMOUNT,
            "currency": "USD",
            "source": COPY,
        },
    )


def _finance_note() -> dict:
    return _command(
        "cmd-r3f-finance-note",
        "channel",
        "DeskNote",
        "2027-01-22T16:25:00Z",
        "r3f-desk",
        1,
        {
            "ref": REF,
            "role": "finance",
            "note": (
                f"The hospital board is {AMOUNT} dollars short of the payer figure. "
                "They subtracted as if both were the same unit."
            ),
        },
    )


def _desk_note() -> dict:
    return _command(
        "cmd-r3f-desk-note",
        "channel",
        "DeskNote",
        "2027-01-22T18:10:00Z",
        "r3f-desk",
        2,
        {
            "ref": REF,
            "role": "desk",
            "note": "The payer row was not on the copy the board used.",
        },
    )


def _payer() -> dict:
    return _command(
        "cmd-r3f-payer",
        "payer",
        "CoverageDecided",
        "2027-01-20T16:00:00Z",
        "r3f-payer",
        1,
        {
            "ref": REF,
            "answer": "yes",
            "amount": AMOUNT,
            "currency": "CAD",
            "member_region": "BC",
            "effective_from": "2027-02-01",
            "effective_to": "2027-05-01",
            "recorded_on": "2027-01-22",
        },
    )


def _copy() -> dict:
    return _command(
        "cmd-r3f-copy",
        "hospital",
        "CopyHeld",
        "2027-01-21T14:20:00Z",
        "r3f-copy",
        1,
        {
            "ref": REF,
            "source": COPY,
            "lines": [
                {
                    "amount": AMOUNT,
                    "currency": "USD",
                    "book": BOOK,
                }
            ],
        },
    )


def _posted() -> dict:
    return _command(
        "cmd-r3f-posted",
        "hospital",
        "AmountPosted",
        "2027-01-20T19:00:00Z",
        "r3f-book",
        1,
        {
            "ref": REF,
            "amount": AMOUNT,
            "currency": "USD",
            "book": BOOK,
            "site": SITE,
        },
    )


def _asked() -> dict:
    return _command(
        "cmd-r3f-asked",
        "channel",
        "BoardRequested",
        "2027-01-21T13:40:00Z",
        "r3f-ask",
        1,
        {
            "ref": REF,
            "board": "finance",
            "role": "finance",
        },
    )


def _member() -> dict:
    return _command(
        "cmd-r3f-member",
        "channel",
        "MemberRecorded",
        "2027-01-20T15:40:00Z",
        "r3f-member",
        1,
        {
            "ref": REF,
            "person_id": PERSON,
            "member_id": MEMBER,
            "member_region": "BC",
        },
    )


def _site() -> dict:
    return _command(
        "cmd-r3f-site",
        "hospital",
        "SiteRecorded",
        "2027-01-20T15:10:00Z",
        "r3f-site",
        1,
        {
            "ref": REF,
            "site": SITE,
            "state": "WA",
        },
    )


def _command(
    command_id: str,
    authority: str,
    event_type: str,
    occurred_at: str,
    stream_id: str,
    rev: int,
    payload: dict,
) -> dict:
    return {
        "command_id": command_id,
        "authority": authority,
        "type": event_type,
        "occurred_at": occurred_at,
        "stream_id": stream_id,
        "stream_rev": rev,
        "payload": payload,
    }
