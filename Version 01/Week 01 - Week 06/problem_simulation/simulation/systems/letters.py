"""Letter bureau: a 90-day dispatch file, the incident file, and JSON samples."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from simulation.systems.resolve import ids_on
from simulation.world.clock import SNAPSHOT, detail_start, iso


def write_letters(events: pd.DataFrame, identifiers: pd.DataFrame, folder: Path) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    recent = iso(detail_start())
    local_pid = ids_on(identifiers, "local_pid", iso(SNAPSHOT))
    sent = events[events["letter_at"] != ""].copy()
    sent["local_pid"] = sent["person_uid"].map(local_pid).fillna("")
    _table(sent[sent["letter_at"] >= recent], folder / "dispatch_90d.csv", duplicate=False)
    incident = sent[sent["letter_duplicate"]]
    _table(incident, folder / "incident_2025-03.csv", duplicate=True)
    samples = folder / "samples"
    samples.mkdir(exist_ok=True)
    for row in incident.head(8).itertuples(index=False):
        for copy in (1, 2):
            payload = {
                "request_id": f"LB-{row.event_id}-{copy}",
                "local_pid": row.local_pid,
                "template": "result",
                "sent_at": row.letter_at,
                "site": row.site,
            }
            (samples / f"{row.event_id}-{copy}.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def _table(frame: pd.DataFrame, path: Path, duplicate: bool) -> None:
    rows = frame[["local_pid", "letter_at", "site"]].copy()
    rows["template"] = "result"
    if duplicate:
        rows = pd.concat([rows, rows.copy()], ignore_index=True)
    rows.to_csv(path, index=False)
