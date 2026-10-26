"""chk-w3-labels. A miss does not print the gold label.

This check grades the relabel function on the held-out rows. A planted token, a missing module, or a crash stops the check. Photo, blank sub-specialty, and the old guideline are separate misses. A field mismatch that those three do not already explain is reported as the old guideline.
"""

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
    """Return the relabel misses.

    Each held-out row is relabeled and compared with the expected record. A scan where gold says photo is the photo miss. An empty sub-specialty where gold has one is the blank miss. A guideline other than the current one is the old-guideline miss. The four-field view catches any other disagreement, but that disagreement uses the old-guideline message only when photo and blank did not already fire. An exception replaces those flags with the run miss.
    """
    if contains_canary(work, canary):
        return [WATERMARK]
    if not (work / "app" / "labels.py").is_file():
        return [RUN]
    try:
        module = load_module(work / "app", "labels")
        photo = blank = old = mismatch = False
        for row, expected in zip(gold["held_out"], gold["held_out_labels"]):
            got = module.relabel(row)
            # A phone photo that is still called a scan is its own miss.
            if got.get("source_type") == "scan" and expected["source_type"] == "photo":
                photo = True
            # A missing sub-specialty is read as blank. The miss fires only when gold expected one.
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
    # A field mismatch uses the old-guideline message only when the photo and blank checks did not already explain it.
    if old or (mismatch and not problems):
        problems.append(OLD)
    return problems


def _view(row: dict) -> dict:
    """Return the four fields that decide whether a relabeled row matches gold.

    Missing keys are read as empty strings so a dropped field still compares.
    """
    return {
        "guideline": row.get("guideline", ""),
        "item_id": row.get("item_id", ""),
        "source_type": row.get("source_type", ""),
        "sub_specialty": row.get("sub_specialty", ""),
    }
