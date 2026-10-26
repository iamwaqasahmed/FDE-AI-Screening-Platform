"""Write rel-w1d2.
Day 1 files are left where they are.

The pack is cleared, then the leader pages, the sample tables, the baselines, and the templates are written. Gold and the measured metrics go into the truth directory. The release note is written after the file list is known, and the fingerprint covers the pack and both truth files.
"""

from __future__ import annotations

import csv
import json
import shutil
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.paths import BASELINES_ROOT, TEMPLATES_ROOT
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset
from alwaha.samples.demand import DEMAND_FIELDS, demand_rows
from alwaha.samples.dna import DNA_FIELDS, dna_rows
from alwaha.samples.gold import gold_payload
from alwaha.samples.letters import letters_text
from alwaha.samples.measure import measure_pack
from alwaha.samples.messages import message_rows
from alwaha.samples.pages import (
    access_page,
    claim_figures,
    dashboard_page,
    register_page,
    sponsor_page,
    vendor_page,
)
from alwaha.samples.prices import PRICE_FIELDS, price_rows

RELEASE = "rel-w1d2"


def _write(path: Path, text: str) -> None:
    """Write text to the path, creating parent directories.

    A Unix newline is forced so the pack file does not depend on the machine that wrote it.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _write_csv(path: Path, fields: tuple[str, ...], rows: list[dict[str, str]]) -> None:
    """Write a CSV file with the given columns and rows.

    Parent directories are created. A key that is not a column is left out, so a sample row can carry fields this file does not publish.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _copy_tree(source: Path, destination: Path) -> None:
    """Copy a source tree onto the destination.

    Caches are skipped. A missing source stops the release so a half-built pack is not left behind.
    """
    if not source.is_dir():
        raise SystemExit(f"Missing {source}.")
    shutil.copytree(
        source,
        destination,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".pytest_cache"),
        dirs_exist_ok=True,
    )


def _release_note(files: list[str]) -> str:
    """Return the readme for this pack.

    Every pack file is listed except the readme itself, because this text is that readme. The note is from patient access and says a figure on the pages is a claim.
    """
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w1d2

From: the director of patient access
Case date: 2027-01-11

The leaders' numbers are in this pack. A figure on these pages is a claim until you measure it. The day notes are [Week 1, Day 2](../../Week%2001/Day%2002/README.md).

Files:

{listed}
"""


def write_day2(profile: Profile, pack: Path, truth: Path) -> str:
    """Return the fingerprint of the pack and its truth files.

    It writes the leader pages, the sample tables, the baselines, the templates, the approach gold, and the measured metrics. The digest is the value the caller stores for this release.
    """
    # Clear the pack and open the truth directory.
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    # Leader pages. The letters page carries this profile's marker.
    figures = claim_figures(profile.seed)
    pages = {
        "problems.md": register_page(),
        "extracts/dashboard.md": dashboard_page(figures["median"]),
        "extracts/vendor-note.md": vendor_page(figures["chats"]),
        "extracts/access-costs.md": access_page(figures["noshow"], figures["returns"], figures["empty"], figures["calls"]),
        "extracts/sponsor-ask.md": sponsor_page(figures["impact"]),
        "samples/ds-letters.md": letters_text(profile.canary(), profile.seed),
    }
    for relative, text in pages.items():
        _write(pack / relative, text)
    # Sample tables, then the baseline tree and the template tree.
    _write_csv(pack / "finance" / "prices.csv", PRICE_FIELDS, price_rows(profile.seed))
    _write_csv(pack / "samples" / "ds-dna.csv", DNA_FIELDS, dna_rows(profile.seed))
    _write_csv(pack / "samples" / "ds-messages.csv", ("message_id", "text"), message_rows(profile.seed))
    _write_csv(pack / "samples" / "ds-demand.csv", DEMAND_FIELDS, demand_rows(profile.seed))
    _copy_tree(BASELINES_ROOT, pack / "baselines")
    _copy_tree(TEMPLATES_ROOT, pack / "templates")
    # Measure the written pack, and keep each message intent beside those measurements.
    measured = measure_pack(pack)
    intents = [{"id": row["message_id"], "intent": row["intent"]} for row in message_rows(profile.seed)]
    metrics = {key: measured[key] for key in measured}
    metrics["message_intents"] = intents
    _write(truth / "approach_gold.json", json.dumps(gold_payload(), indent=2) + "\n")
    _write(truth / "sample_metrics.json", json.dumps(metrics, indent=2) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    # The note is not on disk yet, so its name is added before the note is written.
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    # Fingerprint the pack and both truth files, and store that digest.
    digest = fingerprint(pack, truth / "approach_gold.json", truth / "sample_metrics.json")
    _write(truth / "rel-w1d2-fingerprint.txt", digest + "\n")
    return digest
