"""Write rel-w3d4. Earlier packs and personas.json are left where they are."""

from __future__ import annotations

import csv
import io
import json
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.engagement.w3d4 import gold
from alwaha.engagement.w3d4_demand import series
from alwaha.engagement.w3d4_judge import subset
from alwaha.engagement.w3d4_pages import CASE_DATE, ab_status, budgets, campaign, dot_vote, experiment, hidden_test, seats
from alwaha.engagement.w3d4_rows import dev_score, failures
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-w3d4"


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _json(path: Path, payload: dict | list) -> None:
    _write(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _jsonl(path: Path, rows: list[dict]) -> None:
    body = "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows)
    _write(path, body)


def _csv(path: Path, rows: list[dict]) -> None:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=["district", "year", "month", "visits"], lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
    _write(path, buffer.getvalue())


def _release_note(files: list[str]) -> str:
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w3d4

From: the office of the Chief Digital and Transformation Officer
Case date: {CASE_DATE}

The hidden-test protocol, the judge-calibration subset, the eye-screening campaign, and ab-status are open. The day notes are [Week 3, Day 4](../../Week%2003/Day%2004/README.md).

Files:

{listed}
"""


def write_w3d4(profile: Profile, pack: Path, truth: Path) -> str:
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    _write(pack / "notices" / "hidden-test.md", hidden_test())
    _write(pack / "notices" / "campaign.md", campaign())
    _write(pack / "notices" / "ab-status.md", ab_status())
    _json(pack / "budget" / "metrics.json", budgets())
    _jsonl(pack / "slices" / "score.jsonl", dev_score())
    _jsonl(pack / "slices" / "failures.jsonl", failures())
    _jsonl(pack / "slices" / "calibration.jsonl", subset())
    _csv(pack / "demand" / "ophth.csv", series(profile.seed))
    _json(pack / "workshop" / "dot-vote.json", dot_vote())
    _write(pack / "workshop" / "seats.md", seats())
    _json(pack / "experiment" / "ab-status.json", experiment())
    _write(truth / "w3d4_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    digest = fingerprint(pack, truth / "w3d4_gold.json")
    _write(truth / "rel-w3d4-fingerprint.txt", digest + "\n")
    return digest
