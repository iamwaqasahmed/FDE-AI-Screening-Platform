"""Write rel-m04-l03. Earlier packs and personas.json are left where they are.

The pack is cleared, then the forecast, price, throughput, load, registry, cache, and capacity page are written. Gold is written into the truth directory. The release note is written after the file list is collected, and the note's own name is added to that list because the note is not on disk yet. The fingerprint covers the pack and the gold file, and that digest is also stored beside the gold.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.engagement.m04_l03 import gold
from alwaha.engagement.m04_l03_pages import capacity, release_note
from alwaha.engagement.m04_l03_rows import (
    candidate,
    forecast,
    load_rows,
    price_today,
    public_cache,
    registry,
    throughput,
    today_rate,
)
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-m04-l03"


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


def write_m04_l03(profile: Profile, pack: Path, truth: Path) -> str:
    """Write this release into pack and its gold into truth, and return the fingerprint."""
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    _json(pack / "forecast" / "p-forecast.json", forecast(profile))
    _json(pack / "finance" / "price-today.json", price_today(profile.seed))
    _json(pack / "serving" / "throughput.json", throughput(profile.seed))
    _jsonl(pack / "load" / "mixed.jsonl", load_rows())
    _json(pack / "registry" / "adapters.json", registry(profile))
    _json(pack / "registry" / "candidate.json", candidate(profile))
    _json(pack / "serving" / "public.json", public_cache())
    _write(pack / "templates" / "capacity.md", capacity())
    _write(truth / "m04_l03_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    # The note is not on disk yet, so its name is added before the note is rendered.
    names.append("README.md")
    _write(pack / "README.md", release_note(today_rate(profile.seed), sorted(names)))
    digest = fingerprint(pack, truth / "m04_l03_gold.json")
    _write(truth / "rel-m04-l03-fingerprint.txt", digest + "\n")
    return digest
