"""Write rel-m03-l04.
Earlier packs and personas.json are left where they are.

The pack is cleared, then the notices, the budgets, the score and failure slices, the calibration subset, the demand table, and the workshop files are written. Gold goes into the truth directory. The release note is added once the file list is known, and the fingerprint covers the pack and the gold file.
"""

from __future__ import annotations

import csv
import io
import json
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.engagement.m03_l04 import gold
from alwaha.engagement.m03_l04_demand import series
from alwaha.engagement.m03_l04_judge import subset
from alwaha.engagement.m03_l04_pages import CASE_DATE, ab_status, budgets, campaign, dot_vote, experiment, hidden_test, seats
from alwaha.engagement.m03_l04_rows import dev_score, failures
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-m03-l04"


def _write(path: Path, text: str) -> None:
    """Write text to the path, creating parent directories.

    A Unix newline is forced so the pack file does not depend on the machine that wrote it.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _json(path: Path, payload: dict | list) -> None:
    """Write one JSON value to the path.

    Keys are sorted and the text ends with a newline. The text writer creates parent directories.
    """
    _write(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _jsonl(path: Path, rows: list[dict]) -> None:
    """Write the rows as JSON lines.

    Each object has sorted keys and brings its own newline. No extra blank line is added after the last row.
    """
    body = "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows)
    _write(path, body)


def _csv(path: Path, rows: list[dict]) -> None:
    """Write the demand rows as CSV.

    The columns are district, year, month, and visits, in that order. The text writer stores the finished text.
    """
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=["district", "year", "month", "visits"], lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
    _write(path, buffer.getvalue())


def _release_note(files: list[str]) -> str:
    """Return the readme for this pack.

    Every pack file is listed except the readme itself, because this text is that readme. The note is from the transformation office and points at the hidden-test protocol, the campaign, and the wording experiment.
    """
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-m03-l04

From: the office of the Chief Digital and Transformation Officer
Case date: {CASE_DATE}

The hidden-test protocol, the judge-calibration subset, the eye-screening campaign, and ab-status are open. The lesson notes are [Module 3 Lesson 4](<../../Module 03/Lesson 04/Student_Copy/home.md>).

Files:

{listed}
"""


def write_m03_l04(profile: Profile, pack: Path, truth: Path) -> str:
    """Return the fingerprint of the pack and its gold.

    It writes the notices, the budgets, the score and failure slices, the calibration subset, the demand table, the dot vote, the seats, the experiment, and the gold.
    """
    # Clear the pack and open the truth directory.
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    # Notices for the hidden-test protocol, the campaign, and the wording experiment.
    _write(pack / "notices" / "hidden-test.md", hidden_test())
    _write(pack / "notices" / "campaign.md", campaign())
    _write(pack / "notices" / "ab-status.md", ab_status())
    _json(pack / "budget" / "metrics.json", budgets())
    # Score and failure slices, the calibration subset, and the demand table.
    _jsonl(pack / "slices" / "score.jsonl", dev_score())
    _jsonl(pack / "slices" / "failures.jsonl", failures())
    _jsonl(pack / "slices" / "calibration.jsonl", subset())
    _csv(pack / "demand" / "ophth.csv", series(profile.seed))
    # Workshop ranking, seats, and the experiment record, then gold.
    _json(pack / "workshop" / "dot-vote.json", dot_vote())
    _write(pack / "workshop" / "seats.md", seats())
    _json(pack / "experiment" / "ab-status.json", experiment())
    _write(truth / "m03_l04_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    # The note is not on disk yet, so its name is added before the note is written.
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    # Fingerprint the pack and the gold file, and store that digest.
    digest = fingerprint(pack, truth / "m03_l04_gold.json")
    _write(truth / "rel-m03-l04-fingerprint.txt", digest + "\n")
    return digest
