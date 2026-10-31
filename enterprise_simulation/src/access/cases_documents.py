"""Document rows the hospital already filed. Status and hash can disagree."""

from __future__ import annotations

from access.doc_hash import content_hash

SUMMER = "Cedar Ridge evening clinic closes at 9:00 p.m. Pacific."
WINTER = "Cedar Ridge evening clinic closes at 5:00 p.m. Pacific."
FRENCH = "La clinique de Cedar Ridge ferme à 21 h."
CIRCULAR = "All referrals received this week are pre-approved for a slot."
QUOTE = "Harbor Coverage renewal quotation CAD 18420 for calendar 2027."
LEAFLET = "Northline publishes clinic hours on the public page. This page has no patient identifiers."
WAGE = "Synthetic payroll band W-4 for a test employee. Not a real wage."


def documents() -> list[dict]:
    """Return document commands. The winter hours live in the opening history."""
    return [
        _doc(
            "cmd-doc-circular",
            "circ-unauth",
            1,
            "2026-11-02T16:00:00Z",
            "circ-2026-11",
            "unauthorized",
            "public",
            CIRCULAR,
            "en",
        ),
        _doc(
            "cmd-doc-french",
            "hours-cedar-fr",
            1,
            "2026-12-01T16:00:00Z",
            "2026-summer",
            "in_flight",
            "public",
            FRENCH,
            "fr",
        ),
        _doc(
            "cmd-doc-quote",
            "quote-harbor",
            1,
            "2027-01-04T18:00:00Z",
            "q-2027",
            "in_force",
            "procurement",
            QUOTE,
            "en",
        ),
        _doc(
            "cmd-doc-leaflet",
            "leaflet-hours",
            1,
            "2027-01-05T18:00:00Z",
            "leaf-2027",
            "in_force",
            "public",
            LEAFLET,
            "en",
        ),
        _doc(
            "cmd-doc-wage",
            "wage-band",
            1,
            "2027-01-06T18:00:00Z",
            "w-4",
            "in_force",
            "payroll",
            WAGE,
            "en",
        ),
        _doc(
            "cmd-doc-hours-copy",
            "hours-cedar-copy",
            1,
            "2027-01-10T02:00:00Z",
            "2027-winter",
            "in_force",
            "public",
            SUMMER,
            "en",
            stored_hash=content_hash(WINTER),
        ),
    ]


def _doc(
    command_id: str,
    doc_id: str,
    rev: int,
    occurred_at: str,
    version: str,
    status: str,
    audience: str,
    body: str,
    language: str,
    stored_hash: str | None = None,
) -> dict:
    return {
        "command_id": command_id,
        "authority": "hospital",
        "type": "DocumentChanged",
        "occurred_at": occurred_at,
        "stream_id": doc_id,
        "stream_rev": rev,
        "payload": {
            "doc_id": doc_id,
            "version": version,
            "status": status,
            "audience": audience,
            "language": language,
            "body": body,
            "content_hash": stored_hash or content_hash(body),
        },
    }
