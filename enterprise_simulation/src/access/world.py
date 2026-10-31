"""Build var/ and the student pack from the fixed history."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from access.access_audit import audit_view
from access.access_audit import commands as audit_commands
from access.history import REF, history
from access.legacy_desk import commands as legacy_commands
from access.legacy_desk import symptoms as legacy_symptoms
from access.round2.incident_overlays import overlay as incident_overlay
from access.round2.lesson_feeds import commands as feed_commands
from access.round2.lesson_feeds import feeds as lesson_feeds
from access.round3.identity_graph import commands as identity_commands
from access.round3.identity_graph import edges as identity_edges
from access.round3.seasonality import monthly_volume
from access.scenarios import names as scenario_names
from access.scenarios import overlay as scenario_overlay
from access.logs import append_all, connect, init_db
from access.paths import log_db, proj_dir, student_pack, var_dir
from access.pack_views import write_views
from access.project import load_rows, project_all

SEED = "20270110"

def _scenario_commands(name: str) -> list[dict]:
    if name in scenario_names():
        return scenario_overlay(name)
    return incident_overlay(name)

_STUDENT = """# Northline student pack

Northline Access Collaborative is already running. These files are what the
three organizations will show you. They disagree. The pack does not say which
clock a screen is allowed to use.

Read `extracts/`. The assistant screen is what the current product shows.
It is not a key. Write `prediction.txt` before a check will grade an artifact.

    python -m access init
    python -m access check --release INV-01 --binding binding.json

Other releases read the artifact named in the student README section
"Artifacts". Do not open `instructor/`.
"""

_ARTIFACTS = """
## Artifacts

| Release | File |
| --- | --- |
| INV-01 | `binding.json` with `label_roles` |
| INV-02 | `decisions.py` defining `decide(case)` |
| INV-03 | `capability.py` defining `book(call)` |
| INV-04 | `delivery.py` defining `deliver(batch)` |
| INV-05 | `citation.py` defining `cite(ask, documents)` |
| INV-06 | `score_rule.py` defining `score(rows)` |
| INV-07 | `signal.py` defining `signal(obs)` |
| INV-08 | `boundary.py` defining `boundary(item)` and `TEMPLATE` |
| INV-09 | `binding.json` and `handoff.json` |

Put `prediction.txt` in the same directory. The sentence is not scored.
"""


def reset(root: Path, scenario: str | None = None) -> None:
    """Delete generated state and write it again."""
    generated = var_dir(root)
    if generated.exists():
        shutil.rmtree(generated)
    pack = student_pack(root)
    if pack.exists():
        shutil.rmtree(pack)
    build(root, scenario)


def build(root: Path, scenario: str | None = None) -> dict:
    """Append history, project it, and write the student-visible extracts."""
    commands = history()
    if scenario:
        commands = commands + _scenario_commands(scenario)
    path = log_db(root)
    init_db(path)
    conn = connect(path)
    try:
        ids = append_all(conn, commands)
    finally:
        conn.close()
    project_all(path, proj_dir(root))
    _write_pack(root)
    manifest = {"seed": SEED, "scenario": scenario or "base", "events": ids}
    var_dir(root).mkdir(parents=True, exist_ok=True)
    (var_dir(root) / "manifest.json").write_text(
        json.dumps(manifest, indent=2),
        encoding="utf-8",
    )
    return manifest


def _write_pack(root: Path) -> None:
    pack = student_pack(root)
    extracts = pack / "extracts"
    extracts.mkdir(parents=True, exist_ok=True)
    hospital = load_rows(proj_dir(root) / "hospital.sqlite")
    channel = load_rows(proj_dir(root) / "channel.sqlite")
    payer = load_rows(proj_dir(root) / "payer.sqlite")
    (extracts / "hospital.json").write_text(json.dumps(hospital, indent=2), encoding="utf-8")
    (extracts / "channel.json").write_text(json.dumps(channel, indent=2), encoding="utf-8")
    (extracts / "payer.json").write_text(json.dumps(payer, indent=2), encoding="utf-8")
    boards = [
        {
            "ref": REF,
            "label_id": "since_you_asked",
            "label_text": "Days since you asked Northline",
            "board_name": "facility_mart",
            "board_value": 0,
            "board_as_of": "2027-01-11",
            "currency_context": "CAD member, WA site",
        },
        {
            "ref": "REF-8801",
            "label_id": "since_facility_accepted",
            "label_text": "Days since Cascade accepted the referral",
            "board_name": "facility_mart",
            "board_value": 13,
            "board_as_of": "2027-02-02",
            "currency_context": "USD",
        },
        {
            "ref": "PERMIT-12",
            "label_id": "since_lodged",
            "label_text": "Days since the application was lodged",
            "board_name": "records_counter",
            "board_value": 19,
            "board_as_of": "2027-03-20",
            "currency_context": "CAD",
        },
    ]
    (extracts / "boards.json").write_text(json.dumps(boards, indent=2), encoding="utf-8")
    write_views(pack, hospital, channel)
    (extracts / "legacy_desk.json").write_text(
        json.dumps(legacy_symptoms(legacy_commands()), indent=2),
        encoding="utf-8",
    )
    (extracts / "audit.json").write_text(
        json.dumps(audit_view(audit_commands()), indent=2),
        encoding="utf-8",
    )
    (extracts / "site_feeds.json").write_text(
        json.dumps(lesson_feeds(feed_commands()), indent=2),
        encoding="utf-8",
    )
    (extracts / "identity_graph.json").write_text(
        json.dumps(identity_edges(identity_commands()), indent=2),
        encoding="utf-8",
    )
    (extracts / "monthly_volume.json").write_text(
        json.dumps(monthly_volume(), indent=2),
        encoding="utf-8",
    )
    sponsor = {
        "from": "Northline operations director",
        "text": "Put one wait number on the patient screen before the long weekend.",
    }
    (pack / "sponsor.json").write_text(json.dumps(sponsor, indent=2), encoding="utf-8")
    (pack / "README.md").write_text(_STUDENT + _ARTIFACTS, encoding="utf-8")
    (pack / "organization.json").write_text(
        json.dumps(
            {
                "name": "Northline Access Collaborative",
                "desk": {"city": "Vancouver", "region": "BC", "timezone": "America/Vancouver"},
                "hospitals": [
                    {"id": "cascade-seattle", "region": "WA", "timezone": "America/Los_Angeles"},
                    {"id": "cedar-ridge", "region": "WA", "slot_api": False},
                    {"id": "fraser-burnaby", "region": "BC", "timezone": "America/Vancouver"},
                ],
                "payer": {"id": "harbor-coverage", "currencies": ["CAD", "USD"]},
                "office_week": "Monday through Friday",
                "note": "Clinical sites file at night, including weekends.",
            },
            indent=2,
        ),
        encoding="utf-8",
    )
