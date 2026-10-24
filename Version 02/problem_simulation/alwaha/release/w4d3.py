"""Write rel-w4d3. Earlier packs and personas.json are left where they are."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.engagement.w4d3 import gold
from alwaha.engagement.w4d3_pages import capacity, release_note
from alwaha.engagement.w4d3_rows import (
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

RELEASE = "rel-w4d3"


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _json(path: Path, payload: dict | list) -> None:
    _write(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _jsonl(path: Path, rows: list[dict]) -> None:
    body = "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows)
    _write(path, body)


def write_w4d3(profile: Profile, pack: Path, truth: Path) -> str:
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
    _write(truth / "w4d3_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    names.append("README.md")
    _write(pack / "README.md", release_note(today_rate(profile.seed), sorted(names)))
    digest = fingerprint(pack, truth / "w4d3_gold.json")
    _write(truth / "rel-w4d3-fingerprint.txt", digest + "\n")
    return digest
