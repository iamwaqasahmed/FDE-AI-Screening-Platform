"""The reference folder passes the checker on the small build."""

from __future__ import annotations

from pathlib import Path

import pytest

from handoff_check.__main__ import main as check
from reference_handoff.assemble import build

SMALL = Path(__file__).resolve().parents[2] / "problem_simulation" / "build" / "data-small"
pytestmark = pytest.mark.skipif(not (SMALL / "truth/gold/handoff.json").exists(), reason="small handoff gold is not present")


def test_reference_passes(tmp_path):
    build(SMALL, tmp_path)
    check(["--work", str(tmp_path), "--data", str(SMALL)])


def test_reference_rerun_passes(tmp_path):
    build(SMALL, tmp_path)
    check(["--work", str(tmp_path), "--data", str(SMALL), "--rerun"])
