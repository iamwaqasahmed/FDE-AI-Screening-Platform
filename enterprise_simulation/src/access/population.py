"""Two years of synthetic operations. The graded references are not in this list."""

from __future__ import annotations

import random
from datetime import datetime, timedelta, timezone


def population(seed: int = 20270110, count: int = 240) -> list[dict]:
    """Return deterministic historical commands from January 2025 through 2026."""
    rng = random.Random(seed)
    start = datetime(2025, 1, 6, 15, 0, tzinfo=timezone.utc)
    commands: list[dict] = []
    shared_phone = "604-555-0144"
    shared_twins = "604-555-0199"
    reused_mrn = "MRN-44190"
    for index in range(count):
        ref = f"HX-{index:04d}"
        when = start + timedelta(days=index * 3, hours=rng.randint(0, 10))
        region = "BC" if index % 3 == 0 else "WA"
        relation = None
        household = None
        if index in (7, 8):
            region = "BC"
            phone = shared_phone
            relation = "mother" if index == 7 else "newborn"
            household = "hh-newborn"
        elif index in (12, 13):
            region = "BC"
            phone = shared_twins
            relation = "twin"
            household = "hh-twins"
        else:
            prefix = "604" if region == "BC" else "206"
            phone = f"{prefix}-555-{1000 + (index % 8000):04d}"
        currency = "CAD" if region == "BC" else "USD"
        person = f"p-{index:04d}"
        mrn = reused_mrn if index in (20, 21) else f"MRN-{100000 + index}"
        commands.append(
            {
                "command_id": f"cmd-hx-req-{index}",
                "authority": "channel",
                "type": "RequestAccepted",
                "occurred_at": when.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "stream_id": ref,
                "stream_rev": 1,
                "payload": {
                    "ref": ref,
                    "person_id": person,
                    "phone": phone,
                    "mrn": mrn,
                    "household": household,
                    "relation": relation,
                    "handset_delivered": index % 11 != 0,
                    "channel": "phone" if index % 2 == 0 else "web",
                    "desk_region": region,
                    "utterance": "please check the referral",
                },
            }
        )
        if index % 10 == 0:
            continue
        accepted = when + timedelta(days=rng.randint(0, 4), hours=2)
        commands.append(
            {
                "command_id": f"cmd-hx-acc-{index}",
                "authority": "hospital",
                "type": "ReferralAccepted",
                "occurred_at": accepted.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "stream_id": ref,
                "stream_rev": 1,
                "payload": {
                    "ref": ref,
                    "person_id": person,
                    "site": "cascade-seattle" if region == "WA" else "fraser-burnaby",
                    "state": region,
                    "mrn": mrn,
                },
            }
        )
        if index == 21:
            commands.append(
                {
                    "command_id": "cmd-hx-mrn-pointer",
                    "authority": "hospital",
                    "type": "MrnPointer",
                    "occurred_at": (accepted + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "stream_id": "mrn-44190",
                    "stream_rev": 1,
                    "payload": {
                        "mrn": reused_mrn,
                        "from_person": "p-0020",
                        "to_person": "p-0021",
                        "ref": ref,
                    },
                }
            )
        if index % 7 == 0:
            continue
        answer = "no" if index % 17 == 0 else "yes"
        commands.append(
            {
                "command_id": f"cmd-hx-cov-{index}",
                "authority": "payer",
                "type": "CoverageDecided",
                "occurred_at": (accepted + timedelta(days=rng.randint(0, 6))).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "stream_id": ref,
                "stream_rev": 1,
                "payload": {
                    "ref": ref,
                    "answer": answer,
                    "effective_from": (accepted + timedelta(days=3)).strftime("%Y-%m-%dT00:00:00Z"),
                    "effective_to": (accepted + timedelta(days=90)).strftime("%Y-%m-%dT00:00:00Z"),
                    "currency": currency,
                    "member_region": region,
                },
            }
        )
        if index % 5 != 0:
            continue
        filed = accepted + timedelta(days=2)
        file_id = f"cedar-{filed.strftime('%Y-%m-%d')}-{index}"
        commands.append(
            {
                "command_id": f"cmd-hx-file-{index}",
                "authority": "hospital",
                "type": "SlotFiled",
                "occurred_at": filed.strftime("%Y-%m-%dT21:00:00Z"),
                "stream_id": ref,
                "stream_rev": 2,
                "payload": {
                    "ref": ref,
                    "site": "cedar-ridge",
                    "file_id": file_id,
                    "clinic": "ENDO-CLN",
                    "booking_date": filed.strftime("%Y-%m-%d"),
                    "state": "WA",
                },
            }
        )
        if index % 15 == 0:
            commands.append(
                {
                    "command_id": f"cmd-hx-file-again-{index}",
                    "authority": "hospital",
                    "type": "SlotFiled",
                    "occurred_at": (filed + timedelta(days=1)).strftime("%Y-%m-%dT21:00:00Z"),
                    "stream_id": ref,
                    "stream_rev": 3,
                    "payload": {
                        "ref": ref,
                        "site": "cedar-ridge",
                        "file_id": file_id,
                        "clinic": "ENDO-CLN",
                        "booking_date": filed.strftime("%Y-%m-%d"),
                        "state": "WA",
                        "replay": True,
                    },
                }
            )
    return commands
