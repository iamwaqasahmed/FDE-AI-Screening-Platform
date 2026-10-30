"""Write rel-m04-l05. Earlier packs and personas.json are left where they are.

The pack is cleared, then the connect, staff, bus, handoff, leave, warehouse, value, survey, and responsibility files are written, along with the gate, the personal file, the steering page, and the template pages. Gold goes to the truth directory. The release note lists the files already written plus its own name, which is added because the note is not on disk yet. The fingerprint covers the pack and the gold file.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.engagement.m04_l05 import gold
from alwaha.engagement.m04_l05_pages import (
    architecture_deploy,
    knowledge,
    operations,
    proposal,
    readout,
    release_note,
    retro,
    sprint,
    stage_gate,
    steer_page,
)
from alwaha.engagement.m04_l05_rows import attack, events, feed, handoffs, leave, model, raci, readiness, requests, staff
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-m04-l05"


def _write(path: Path, text: str) -> None:
    """Create the parent directory and write text with a Unix newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _json(path: Path, payload: dict | list) -> None:
    """Write one JSON value with sorted keys and a trailing newline."""
    _write(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _jsonl(path: Path, rows: list[dict]) -> None:
    """Write one JSON object per line, with sorted keys, including a trailing newline."""
    body = "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows)
    _write(path, body)


def write_m04_l05(profile: Profile, pack: Path, truth: Path) -> str:
    """Write this release into pack and its gold into truth, and return the fingerprint."""
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    _json(pack / "connect" / "requests.json", requests())
    _json(pack / "iam" / "staff.json", staff())
    _jsonl(pack / "bus" / "events.jsonl", events())
    _jsonl(pack / "cc" / "handoff.jsonl", handoffs())
    _jsonl(pack / "hr" / "leave.jsonl", leave(profile.seed))
    _jsonl(pack / "warehouse" / "feed.jsonl", feed())
    _json(pack / "value" / "model.json", model())
    _json(pack / "survey" / "readiness.json", readiness())
    _json(pack / "raci" / "assistant.json", raci())
    _write(pack / "gates" / "stage-gate.md", stage_gate())
    _json(pack / "personal" / "attack.json", attack())
    _write(pack / "steering" / "steer-m04-l05.md", steer_page())
    _write(pack / "templates" / "architecture-deploy.md", architecture_deploy())
    _write(pack / "templates" / "operations.md", operations())
    _write(pack / "templates" / "proposal.md", proposal())
    _write(pack / "templates" / "readout.md", readout())
    _write(pack / "templates" / "retro.md", retro())
    _write(pack / "templates" / "sprint.md", sprint())
    _write(pack / "templates" / "knowledge.md", knowledge())
    _write(truth / "m04_l05_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    # The note is not on disk yet, so its name is added before the note is rendered.
    names.append("README.md")
    _write(pack / "README.md", release_note(sorted(names)))
    digest = fingerprint(pack, truth / "m04_l05_gold.json")
    _write(truth / "rel-m04-l05-fingerprint.txt", digest + "\n")
    return digest
