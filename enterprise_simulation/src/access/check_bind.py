"""Grade a binding. Miss text does not include the sealed authority or event."""

from __future__ import annotations

import json
from pathlib import Path

from access.sealed import PROMISES


def grade(binding_path: Path, *, check_prediction: bool = True) -> list[str]:
    """Return miss sentences. An empty list is satisfactory."""
    from access.checks.common import require_prediction

    if check_prediction:
        missing = require_prediction(binding_path)
        if missing:
            return missing
    if not binding_path.is_file():
        return ["the binding file is missing"]
    try:
        raw = json.loads(binding_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return ["the binding file is not JSON"]
    if isinstance(raw, dict):
        raw.pop("pass", None)
    labels = raw.get("label_roles") if isinstance(raw, dict) else None
    if not isinstance(labels, dict):
        return ["the binding does not map a label to an authority"]
    problems: list[str] = []
    for label_id, promise in PROMISES.items():
        got = labels.get(label_id)
        if not isinstance(got, dict):
            problems.append(f"the label {label_id} has no authority")
            continue
        if got.get("authority") != promise["authority"] or got.get("event") != promise["event"]:
            problems.append(
                f"the label {label_id} does not cite the series its text promises"
            )
    return problems
