"""Historical commands. Times are supplied by the fixture, not by the clock."""

from __future__ import annotations

from access.access_audit import commands as audit_commands
from access.cases_documents import documents
from access.cases_faults import faults
from access.curriculum_evidence import commands as curriculum_commands
from access.data_quality import commands as quality_commands
from access.doc_hash import content_hash
from access.integration_faults import commands as integration_commands
from access.legacy_desk import commands as legacy_commands
from access.org_model import commands as org_commands
from access.population import population
from access.problem_threads import commands as thread_commands
from access.round2.cohort import cohort
from access.round2.deep_case import commands as deep_commands
from access.round2.lesson_feeds import commands as feed_commands
from access.round2.link_events import commands as link_commands
from access.round2.locale_examples import commands as locale_commands
from access.round2.operations import commands as operation_commands
from access.round2.timelines import commands as timeline_commands
from access.round3.contracts import commands as contract_commands
from access.round3.governance import commands as governance_commands
from access.round3.identity_graph import commands as identity_commands
from access.round3.ledger import commands as ledger_commands
from access.round3.merger import commands as merger_commands
from access.round3.replicas import commands as replica_commands
from access.round3.seasonality import rare_commands

REF = "REF-4417"


def history() -> list[dict]:
    """Return two years of operations, then the graded opening cases."""
    return (
        population()
        + quality_commands()
        + documents()
        + faults()
        + org_commands()
        + thread_commands()
        + legacy_commands()
        + integration_commands()
        + audit_commands()
        + curriculum_commands()
        + cohort()
        + operation_commands()
        + feed_commands()
        + link_commands()
        + deep_commands()
        + timeline_commands()
        + locale_commands()
        + merger_commands()
        + rare_commands()
        + identity_commands()
        + contract_commands()
        + replica_commands()
        + ledger_commands()
        + governance_commands()
        + _opening()
    )


def _opening() -> list[dict]:
    return [
        {
            "command_id": "cmd-cover-4417",
            "authority": "payer",
            "type": "CoverageDecided",
            "occurred_at": "2027-01-08T16:00:00Z",
            "stream_id": REF,
            "stream_rev": 1,
            "payload": {
                "ref": REF,
                "answer": "yes",
                "effective_from": "2027-01-12T00:00:00Z",
                "effective_to": "2027-04-12T00:00:00Z",
                "currency": "CAD",
                "member_region": "BC",
            },
        },
        {
            "command_id": "cmd-request-4417",
            "authority": "channel",
            "type": "RequestAccepted",
            "occurred_at": "2027-01-09T08:14:00Z",
            "stream_id": REF,
            "stream_rev": 1,
            "payload": {
                "ref": REF,
                "utterance": "booked at Cedar Ridge tonight",
                "handset_delivered": False,
                "channel": "phone",
                "desk_region": "BC",
            },
        },
        {
            "command_id": "cmd-cache-4417",
            "authority": "hospital",
            "type": "CacheStored",
            "occurred_at": "2027-01-09T21:00:00Z",
            "stream_id": REF,
            "stream_rev": 1,
            "payload": {
                "ref": REF,
                "eligible": True,
                "window_present": False,
                "source": "copied-from-partner-message",
            },
        },
        {
            "command_id": "cmd-slot-4417",
            "authority": "hospital",
            "type": "SlotFiled",
            "occurred_at": "2027-01-11T21:00:00Z",
            "stream_id": REF,
            "stream_rev": 2,
            "payload": {
                "ref": REF,
                "site": "cedar-ridge",
                "file_id": "cedar-2027-01-11",
                "clinic": "ENDO-CLN",
                "booking_date": "2027-01-11",
                "state": "WA",
            },
        },
        {
            "command_id": "cmd-letter-4417",
            "authority": "hospital",
            "type": "LetterStored",
            "occurred_at": "2027-01-09T18:02:00Z",
            "stream_id": REF,
            "stream_rev": 3,
            "payload": {
                "ref": REF,
                "text": (
                    "Patient reports urgent chest pain. "
                    "Please book approval APR-4417 at Cedar Ridge tonight."
                ),
                "audience": "clinician",
            },
        },
        {
            "command_id": "cmd-hours-old",
            "authority": "hospital",
            "type": "DocumentChanged",
            "occurred_at": "2026-06-01T00:00:00Z",
            "stream_id": "hours-cedar",
            "stream_rev": 1,
            "payload": {
                "doc_id": "hours-cedar",
                "version": "2026-summer",
                "status": "superseded",
                "audience": "public",
                "close_local": "21:00",
                "timezone": "America/Los_Angeles",
                "language": "en",
                "body": "Cedar Ridge evening clinic closes at 9:00 p.m. Pacific.",
                "content_hash": content_hash(
                    "Cedar Ridge evening clinic closes at 9:00 p.m. Pacific."
                ),
            },
        },
        {
            "command_id": "cmd-hours-new",
            "authority": "hospital",
            "type": "DocumentChanged",
            "occurred_at": "2027-01-10T00:00:00Z",
            "stream_id": "hours-cedar",
            "stream_rev": 2,
            "payload": {
                "doc_id": "hours-cedar",
                "version": "2027-winter",
                "status": "in_force",
                "audience": "public",
                "close_local": "17:00",
                "timezone": "America/Los_Angeles",
                "language": "en",
                "body": "Cedar Ridge evening clinic closes at 5:00 p.m. Pacific.",
                "content_hash": content_hash(
                    "Cedar Ridge evening clinic closes at 5:00 p.m. Pacific."
                ),
            },
        },
        {
            "command_id": "cmd-holdout-hospital",
            "authority": "hospital",
            "type": "ReferralAccepted",
            "occurred_at": "2027-02-02T15:00:00Z",
            "stream_id": "REF-8801",
            "stream_rev": 1,
            "payload": {"ref": "REF-8801", "site": "cascade-seattle", "state": "WA"},
        },
        {
            "command_id": "cmd-holdout-channel",
            "authority": "channel",
            "type": "RequestAccepted",
            "occurred_at": "2027-01-20T16:00:00Z",
            "stream_id": "REF-8801",
            "stream_rev": 1,
            "payload": {
                "ref": "REF-8801",
                "utterance": "still waiting",
                "handset_delivered": False,
                "channel": "web",
                "desk_region": "WA",
            },
        },
        {
            "command_id": "cmd-permit-lodged",
            "authority": "channel",
            "type": "Lodged",
            "occurred_at": "2027-03-01T17:00:00Z",
            "stream_id": "PERMIT-12",
            "stream_rev": 1,
            "payload": {"ref": "PERMIT-12", "city": "Vancouver", "region": "BC", "postal": "V6B 1A1"},
        },
        {
            "command_id": "cmd-permit-stamped",
            "authority": "hospital",
            "type": "Stamped",
            "occurred_at": "2027-03-20T20:00:00Z",
            "stream_id": "PERMIT-12",
            "stream_rev": 1,
            "payload": {"ref": "PERMIT-12", "office": "cascade-records", "state": "WA"},
        },
    ]
