"""Write rel-w2d5. Earlier packs and personas.json are left where they are."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.engagement.w2d5 import gold, live_slot, missed_file, nightly_file, queued_fixture
from alwaha.engagement.w2d5_pages import change_note, interface_note, schedule_spec, steer_page
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-w2d5"


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _json(path: Path, payload: dict) -> None:
    _write(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _release_note(files: list[str]) -> str:
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w2d5

From: the steering committee
Case date: 2027-01-21

Change request cr-ain asks the team to include h-ain. The day notes are [Week 2, Day 5](../../Week%2002/Day%2005/README.md).

Files:

{listed}
"""


def write_w2d5(profile: Profile, pack: Path, truth: Path) -> str:
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    _write(pack / "notices" / "cr-ain.md", change_note())
    _write(pack / "systems" / "sched-ain.md", interface_note())
    _write(pack / "steering" / "steer-w2.md", steer_page())
    _write(pack / "openapi" / "sched-ain.yaml", schedule_spec())
    _json(pack / "fixtures" / "queued.json", queued_fixture())
    _json(pack / "fixtures" / "live-slot.json", live_slot(profile))
    _json(pack / "fixtures" / "nightly.json", nightly_file(profile))
    _json(pack / "fixtures" / "missed.json", missed_file(profile))
    _write(truth / "w2d5_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    digest = fingerprint(pack, truth / "w2d5_gold.json")
    _write(truth / "rel-w2d5-fingerprint.txt", digest + "\n")
    return digest
