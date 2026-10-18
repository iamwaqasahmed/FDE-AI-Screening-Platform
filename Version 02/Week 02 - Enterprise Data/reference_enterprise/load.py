"""Read the handover, the corpus headers, and the week-2 drop. Never opens truth or eval."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

POLICY = "corpus/policy"
DROP = "drops/week-2/registry"


def read_csv(data: Path, relative: str) -> pd.DataFrame:
    return pd.read_csv(data / relative, dtype=str).fillna("")


def v3(data: Path) -> pd.DataFrame:
    return read_csv(data, f"{DROP}/current_v3.csv")


def reissue(data: Path) -> pd.DataFrame:
    return read_csv(data, f"{DROP}/reissue_batch.csv")


def current(data: Path) -> pd.DataFrame:
    return read_csv(data, "handover/registry/current.csv")


def warehouse(data: Path) -> pd.DataFrame:
    return read_csv(data, "handover/warehouse/registry_snapshot.csv")


def pacs(data: Path) -> pd.DataFrame:
    frames = [pd.read_csv(path, dtype=str).fillna("") for path in sorted((data / "handover/pacs").glob("*.csv"))]
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()


def messages(data: Path) -> pd.DataFrame:
    frame = pd.read_csv(data / "handover/ophthalmology/messages.pipe", sep="|", dtype=str).fillna("")
    frame.columns = ["ref", "mrn", "local_pid", "referred", "booked", "seen", "grade"]
    return frame


def documents(data: Path) -> list[dict]:
    found = []
    for path in sorted((data / POLICY).glob("*.md")):
        text = path.read_text(encoding="utf-8")
        header, body = _split(text)
        header["body"] = body
        header["path"] = path.name
        found.append(header)
    return found


def _split(text: str) -> tuple[dict, str]:
    meta: dict[str, str] = {}
    applies: list[str] = []
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("#"):
            return {**meta, "applies_to": applies}, "\n".join(lines[index:])
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if key.strip() == "applies_to" and value:
            applies.append(value)
        else:
            meta[key.strip()] = value
    return {**meta, "applies_to": applies}, ""
