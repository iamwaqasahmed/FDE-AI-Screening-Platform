"""Write rel-w1d3. Earlier packs are left where they are."""

from __future__ import annotations

import csv
import json
import shutil
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.events.gold import payload
from alwaha.events.pages import contract_page, criteria_docs, eref_spec, his_wadi_spec, policy_page, render_criteria
from alwaha.events.stream import clinics, events, faults, open_referrals
from alwaha.paths import DAY3_TEMPLATES, WORKFLOW_ROOT
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset
from alwaha.world.calendar import calendar_document

RELEASE = "rel-w1d3"
OPEN_FIELDS = ("patient_key", "specialty_id", "referral_id")
CLINIC_FIELDS = ("facility_id", "specialty_id", "clinic")


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _write_csv(path: Path, fields: tuple[str, ...], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _copy_tree(source: Path, destination: Path) -> None:
    if not source.is_dir():
        raise SystemExit(f"Missing {source}.")
    shutil.copytree(
        source,
        destination,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".pytest_cache"),
        dirs_exist_ok=True,
    )


def _release_note(files: list[str]) -> str:
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w1d3

From: the enterprise architect
Case date: 2027-01-12

The event stream, the SLA policy, and the business calendar are in this pack. The day notes are [Week 1, Day 3](../../Week%2001/Day%2003/README.md).

Files:

{listed}
"""


def write_day3(profile: Profile, pack: Path, truth: Path) -> str:
    if not WORKFLOW_ROOT.is_dir() or not DAY3_TEMPLATES.is_dir():
        raise SystemExit("Day 3 template is missing.")
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    _write(pack / "calendar" / "business-calendar.json", json.dumps(calendar_document(), indent=2, sort_keys=True) + "\n")
    _write(pack / "policy" / "pol-sla.md", policy_page())
    for doc in criteria_docs():
        _write(pack / "criteria" / f"{doc['doc_id']}.md", render_criteria(doc))
    lines = [json.dumps(row, sort_keys=True) for row in events(profile.canary())]
    _write(pack / "events" / "intake.jsonl", "\n".join(lines) + "\n")
    _write(pack / "events" / "faults.json", json.dumps(faults(), indent=2, sort_keys=True) + "\n")
    _write_csv(pack / "events" / "open-referrals.csv", OPEN_FIELDS, open_referrals())
    _write_csv(pack / "catalog" / "clinics.csv", CLINIC_FIELDS, clinics())
    _write(pack / "contracts" / "referral.submitted.md", contract_page())
    _write(pack / "openapi" / "eref.yaml", eref_spec())
    _write(pack / "openapi" / "his-wadi.yaml", his_wadi_spec())
    _copy_tree(WORKFLOW_ROOT, pack / "workflow")
    _copy_tree(DAY3_TEMPLATES, pack / "templates")
    _write(truth / "events_gold.json", json.dumps(payload(profile.canary()), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    digest = fingerprint(pack, truth / "events_gold.json")
    _write(truth / "rel-w1d3-fingerprint.txt", digest + "\n")
    return digest
