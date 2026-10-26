"""Write rel-w1d3.
Earlier packs are left where they are.

The writer stops if a template tree is missing, then clears the pack and writes the calendar, the policy, the criteria, the event stream, and the workflow. Gold goes into the truth directory. The release note is added once the file list is known, and the fingerprint covers the pack and the gold file.
"""

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
    """Write text to the path, creating parent directories.

    A Unix newline is forced so the pack file does not depend on the machine that wrote it.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _write_csv(path: Path, fields: tuple[str, ...], rows: list[dict[str, str]]) -> None:
    """Write a CSV file with the given columns and rows.

    Parent directories are created. The open-referral table and the clinic table use this so their headers stay in the given order.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _copy_tree(source: Path, destination: Path) -> None:
    """Copy a source tree onto the destination.

    Caches are skipped. A missing source stops the release so a half-built pack is not left behind.
    """
    if not source.is_dir():
        raise SystemExit(f"Missing {source}.")
    shutil.copytree(
        source,
        destination,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".pytest_cache"),
        dirs_exist_ok=True,
    )


def _release_note(files: list[str]) -> str:
    """Return the readme for this pack.

    Every pack file is listed except the readme itself, because this text is that readme. The note is from the enterprise architect and points at the event stream, the policy, and the calendar.
    """
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w1d3

From: the enterprise architect
Case date: 2027-01-12

The event stream, the SLA policy, and the business calendar are in this pack. The day notes are [Week 1, Day 3](../../Week%2001/Day%2003/README.md).

Files:

{listed}
"""


def write_day3(profile: Profile, pack: Path, truth: Path) -> str:
    """Return the fingerprint of the pack and the events gold.

    It writes the calendar, the policy, the criteria pages, the event stream, the faults, the open referrals, the clinics, the contract, the interface files, the workflow tree, and the templates. A missing template stops the release before anything is replaced.
    """
    # Stop before replacing anything when a template tree is missing.
    if not WORKFLOW_ROOT.is_dir() or not DAY3_TEMPLATES.is_dir():
        raise SystemExit("Day 3 template is missing.")
    # Clear the pack and open the truth directory.
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    _write(pack / "calendar" / "business-calendar.json", json.dumps(calendar_document(), indent=2, sort_keys=True) + "\n")
    _write(pack / "policy" / "pol-sla.md", policy_page())
    for doc in criteria_docs():
        _write(pack / "criteria" / f"{doc['doc_id']}.md", render_criteria(doc))
    # Event stream, faults, open referrals, and clinics.
    lines = [json.dumps(row, sort_keys=True) for row in events(profile.canary())]
    _write(pack / "events" / "intake.jsonl", "\n".join(lines) + "\n")
    _write(pack / "events" / "faults.json", json.dumps(faults(), indent=2, sort_keys=True) + "\n")
    _write_csv(pack / "events" / "open-referrals.csv", OPEN_FIELDS, open_referrals())
    _write_csv(pack / "catalog" / "clinics.csv", CLINIC_FIELDS, clinics())
    _write(pack / "contracts" / "referral.submitted.md", contract_page())
    _write(pack / "openapi" / "eref.yaml", eref_spec())
    _write(pack / "openapi" / "his-wadi.yaml", his_wadi_spec())
    # Workflow, templates, and gold.
    _copy_tree(WORKFLOW_ROOT, pack / "workflow")
    _copy_tree(DAY3_TEMPLATES, pack / "templates")
    _write(truth / "events_gold.json", json.dumps(payload(profile.canary()), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    # The note is not on disk yet, so its name is added before the note is written.
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    # Fingerprint the pack and the gold file, and store that digest.
    digest = fingerprint(pack, truth / "events_gold.json")
    _write(truth / "rel-w1d3-fingerprint.txt", digest + "\n")
    return digest
