"""Write one profile's world under build/<profile>/world."""

from __future__ import annotations

import shutil
from pathlib import Path

from alwaha.behavior.staff import styles
from alwaha.capacity.roster import roster
from alwaha.capacity.sessions import sessions
from alwaha.capacity.travel import nightly, travel
from alwaha.care.flow import bookings, breaches, referrals
from alwaha.config.scale import volume_rows
from alwaha.corpus.address import render_markdown
from alwaha.corpus.documents import documents
from alwaha.corpus.render import kind_for, write_original
from alwaha.datasets.splits import dna, letters, messages, redteam, retrieve
from alwaha.datasets.volume import write_streams
from alwaha.demand.need import needs
from alwaha.people.population import build_people
from alwaha.people.store import write_json, write_jsonl
from alwaha.release.fingerprint import fingerprint
from alwaha.systems.all import faults


def write_world(profile, root: Path, stream_rows: int | None = None) -> str:
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True)
    people = build_people(profile)
    need_rows = needs(profile, people)
    referral_rows = referrals(need_rows)
    booking_rows = bookings(profile, people, referral_rows)
    write_jsonl(root / "people" / "people.jsonl", people)
    write_jsonl(root / "demand" / "needs.jsonl", need_rows)
    write_jsonl(root / "capacity" / "roster.jsonl", roster(profile))
    write_jsonl(root / "capacity" / "sessions.jsonl", sessions(profile))
    write_jsonl(root / "capacity" / "ain.jsonl", nightly(profile))
    write_jsonl(root / "capacity" / "travel.jsonl", travel(profile))
    write_jsonl(root / "behavior" / "staff.jsonl", styles(profile))
    write_jsonl(root / "care" / "referrals.jsonl", referral_rows)
    write_jsonl(root / "care" / "bookings.jsonl", booking_rows)
    write_jsonl(root / "care" / "breaches.jsonl", breaches(referral_rows))
    for fault in faults(profile):
        write_json(root / "systems" / f"{fault['export']}.json", fault)
    _corpus(root, documents(profile))
    write_jsonl(root / "datasets" / "ds-letters.jsonl", letters(profile))
    write_jsonl(root / "datasets" / "ds-messages.jsonl", messages(profile))
    write_jsonl(root / "datasets" / "ds-dna.jsonl", dna(profile, booking_rows))
    write_jsonl(root / "datasets" / "ds-retrieve.jsonl", retrieve(profile))
    write_jsonl(root / "datasets" / "ds-redteam.jsonl", redteam(profile))
    count = volume_rows(profile) if stream_rows is None else stream_rows
    if count:
        write_streams(root, count)
    return fingerprint(root)


def _corpus(root: Path, specs: list[dict]) -> None:
    folder = root / "corpus"
    folder.mkdir(parents=True)
    for index, spec in enumerate(specs):
        body = spec["body"]
        markdown = render_markdown(spec, body)
        (folder / f"{spec['doc_id']}.md").write_text(markdown, encoding="utf-8")
        kind = kind_for(index)
        write_original(folder / f"{spec['doc_id']}.{kind}", kind, body)
