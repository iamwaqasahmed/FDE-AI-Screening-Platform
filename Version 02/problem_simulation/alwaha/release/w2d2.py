"""Write rel-w2d2. Earlier packs and personas.json are left where they are."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.engagement.w2d2 import cancellations, faults, gold, hl7_rows, mart_csv, webhook
from alwaha.engagement.w2d2_pages import dms_note, eref_spec, notice, registry, sms_spec, wa_note, wa_spec
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-w2d2"


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _json(path: Path, payload: dict) -> None:
    _write(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _jsonl(path: Path, rows: list[dict]) -> None:
    lines = [json.dumps(row, sort_keys=True) for row in rows]
    _write(path, "\n".join(lines) + "\n")


def _release_note(files: list[str]) -> str:
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w2d2

From: the enterprise architect
Case date: 2027-01-18

Webhooks, WhatsApp, and the HL7 feeds are in this pack. The day notes are [Week 2, Day 2](../../Week%2002/Day%2002/README.md).

Files:

{listed}
"""


def write_w2d2(profile: Profile, pack: Path, truth: Path) -> str:
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    _write(pack / "notices" / "feeds.md", notice())
    _write(pack / "registry" / "topics.md", registry())
    _write(pack / "openapi" / "eref.yaml", eref_spec())
    _write(pack / "openapi" / "sms.yaml", sms_spec())
    _write(pack / "openapi" / "wa.yaml", wa_spec())
    _write(pack / "channels" / "wa.md", wa_note())
    _write(pack / "channels" / "dms.md", dms_note())
    _json(pack / "webhooks" / "referral.submitted.json", webhook(profile))
    _jsonl(pack / "events" / "session.cancelled.jsonl", cancellations())
    _json(pack / "channels" / "sms-faults.json", faults())
    _jsonl(pack / "feeds" / "int-engine.jsonl", hl7_rows())
    _write(pack / "mart" / "waitlist.csv", mart_csv(profile))
    _write(truth / "w2d2_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    digest = fingerprint(pack, truth / "w2d2_gold.json")
    _write(truth / "rel-w2d2-fingerprint.txt", digest + "\n")
    return digest
