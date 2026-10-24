"""chk-w3-labels. A miss does not print the gold label."""

from __future__ import annotations

from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import load_module
from alwaha.check.tables import contains_canary

PHOTO = "a phone photo is still a scan"
BLANK = "a sub-specialty is still blank"
OLD = "the sample still follows ann-v1"
RUN = "the relabel did not run"


def labels_problems(work: Path, gold: dict, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return [WATERMARK]
    if not (work / "app" / "labels.py").is_file():
        return [RUN]
    try:
        module = load_module(work / "app", "labels")
        photo = blank = old = mismatch = False
        for row, expected in zip(gold["held_out"], gold["held_out_labels"]):
            got = module.relabel(row)
            if got.get("source_type") == "scan" and expected["source_type"] == "photo":
                photo = True
            if got.get("sub_specialty", "") == "" and expected["sub_specialty"]:
                blank = True
            if got.get("guideline") != "ann-v2":
                old = True
            if _view(got) != _view(expected):
                mismatch = True
    except Exception:
        return [RUN]
    problems = []
    if photo:
        problems.append(PHOTO)
    if blank:
        problems.append(BLANK)
    if old or (mismatch and not problems):
        problems.append(OLD)
    return problems


def _view(row: dict) -> dict:
    return {
        "guideline": row.get("guideline", ""),
        "item_id": row.get("item_id", ""),
        "source_type": row.get("source_type", ""),
        "sub_specialty": row.get("sub_specialty", ""),
    }
