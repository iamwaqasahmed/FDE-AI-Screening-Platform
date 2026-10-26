"""Write rel-w2d2.
Earlier packs and personas.json are left where they are.

The pack is cleared, then the feed notice, the topic registry, the interface documents, the channel notes, the webhook, the cancellations, and the mart extract are written. Gold goes into the truth directory. The release note is added once the file list is known, and the fingerprint covers the pack and the gold file.
"""

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
    """Write text to the path, creating parent directories.

    A Unix newline is forced so the pack file does not depend on the machine that wrote it.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _json(path: Path, payload: dict) -> None:
    """Write one JSON value to the path.

    Keys are sorted and the text ends with a newline. The text writer creates parent directories.
    """
    _write(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _jsonl(path: Path, rows: list[dict]) -> None:
    """Write the rows as JSON lines.

    Each object has sorted keys. The file ends with a newline even when there are no rows, so the terminator is always there.
    """
    lines = [json.dumps(row, sort_keys=True) for row in rows]
    _write(path, "\n".join(lines) + "\n")


def _release_note(files: list[str]) -> str:
    """Return the readme for this pack.

    Every pack file is listed except the readme itself, because this text is that readme. The note is from the enterprise architect and points at the webhooks, the messaging channel, and the feeds.
    """
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w2d2

From: the enterprise architect
Case date: 2027-01-18

Webhooks, WhatsApp, and the HL7 feeds are in this pack. The day notes are [Week 2, Day 2](../../Week%2002/Day%2002/README.md).

Files:

{listed}
"""


def write_w2d2(profile: Profile, pack: Path, truth: Path) -> str:
    """Return the fingerprint of the pack and its gold.

    It writes the feed notice, the topic registry, the interface documents, the channel notes, the webhook, the cancellations, the faults, the feed, the mart, and the gold.
    """
    # Clear the pack and open the truth directory.
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    # Feed notice, topic registry, interface documents, and channel notes.
    _write(pack / "notices" / "feeds.md", notice())
    _write(pack / "registry" / "topics.md", registry())
    _write(pack / "openapi" / "eref.yaml", eref_spec())
    _write(pack / "openapi" / "sms.yaml", sms_spec())
    _write(pack / "openapi" / "wa.yaml", wa_spec())
    _write(pack / "channels" / "wa.md", wa_note())
    _write(pack / "channels" / "dms.md", dms_note())
    # Webhook, cancellations, faults, the feed, and the mart extract.
    _json(pack / "webhooks" / "referral.submitted.json", webhook(profile))
    _jsonl(pack / "events" / "session.cancelled.jsonl", cancellations())
    _json(pack / "channels" / "sms-faults.json", faults())
    _jsonl(pack / "feeds" / "int-engine.jsonl", hl7_rows())
    _write(pack / "mart" / "waitlist.csv", mart_csv(profile))
    # Gold, after the pack files it is checked against.
    _write(truth / "w2d2_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    # The note is not on disk yet, so its name is added before the note is written.
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    # Fingerprint the pack and the gold file, and store that digest.
    digest = fingerprint(pack, truth / "w2d2_gold.json")
    _write(truth / "rel-w2d2-fingerprint.txt", digest + "\n")
    return digest
