"""Write rel-w4d4. Earlier packs and personas.json are left where they are.

The pack is cleared, then the drill, replicas, in-flight work, outage, lead time, hospital shares, model-down file, and the two template pages are written. Gold goes to the truth directory. The release note lists the files already written plus its own name, which is added because the note is not on disk yet. The fingerprint covers the pack and the gold file.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.engagement.w4d4 import gold
from alwaha.engagement.w4d4_pages import architecture, failover, release_note
from alwaha.engagement.w4d4_rows import drill, hospitals, inflight, lead_time, model_down, outage, replicas
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-w4d4"


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


def write_w4d4(profile: Profile, pack: Path, truth: Path) -> str:
    """Write this release into pack and its gold into truth, and return the fingerprint."""
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    _json(pack / "drill" / "site-a.json", drill(profile.seed))
    _json(pack / "sites" / "replicas.json", replicas(profile))
    _jsonl(pack / "workflow" / "inflight.jsonl", inflight())
    _json(pack / "insure" / "outage.json", outage(profile.seed))
    _json(pack / "finance" / "lead-time.json", lead_time(profile.seed))
    _json(pack / "hospitals" / "shares.json", hospitals(profile.seed))
    _json(pack / "serving" / "model-down.json", model_down())
    _write(pack / "templates" / "failover.md", failover())
    _write(pack / "templates" / "architecture.md", architecture())
    _write(truth / "w4d4_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    # The note is not on disk yet, so its name is added before the note is rendered.
    names.append("README.md")
    _write(pack / "README.md", release_note(sorted(names)))
    digest = fingerprint(pack, truth / "w4d4_gold.json")
    _write(truth / "rel-w4d4-fingerprint.txt", digest + "\n")
    return digest
