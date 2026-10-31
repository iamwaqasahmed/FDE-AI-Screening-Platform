"""Dispatch a release to its checker."""

from __future__ import annotations

from pathlib import Path

from access.check_bind import grade
from access.checks.boundary import grade_boundary
from access.checks.capability import grade_capability
from access.checks.cite import grade_cite
from access.checks.common import require_prediction
from access.checks.decisions import grade_decisions
from access.checks.delivery import grade_delivery
from access.checks.handoff import grade_handoff
from access.checks.score import grade_score
from access.checks.signal import grade_signal

RELEASES = (
    "INV-01",
    "INV-02",
    "INV-03",
    "INV-04",
    "INV-05",
    "INV-06",
    "INV-07",
    "INV-08",
    "INV-09",
)


def grade_release(
    release: str,
    root: Path,
    binding: Path | None = None,
    artifact: Path | None = None,
) -> list[str]:
    if release not in RELEASES:
        return [f"unknown release {release}"]
    anchor = binding if release in ("INV-01", "INV-09") else artifact
    if anchor is None:
        return ["the artifact file is missing"]
    missing = require_prediction(anchor)
    if missing:
        return missing
    if release == "INV-01":
        return grade(binding, check_prediction=False) if binding else ["the artifact file is missing"]
    if release == "INV-02":
        return grade_decisions(artifact)  # type: ignore[arg-type]
    if release == "INV-03":
        return grade_capability(artifact)  # type: ignore[arg-type]
    if release == "INV-04":
        return grade_delivery(artifact)  # type: ignore[arg-type]
    if release == "INV-05":
        return grade_cite(artifact, root)  # type: ignore[arg-type]
    if release == "INV-06":
        return grade_score(artifact)  # type: ignore[arg-type]
    if release == "INV-07":
        return grade_signal(artifact)  # type: ignore[arg-type]
    if release == "INV-08":
        return grade_boundary(artifact)  # type: ignore[arg-type]
    if binding is None or artifact is None:
        return ["the artifact file is missing"]
    return grade(binding, check_prediction=False) + grade_handoff(artifact)
