"""A reference folder passes on the small build."""

from __future__ import annotations

from pathlib import Path

import pytest

from reference_enterprise.assemble import build

SMALL = Path(__file__).resolve().parents[2] / "problem_simulation" / "build" / "data-small"


@pytest.mark.skipif(not (SMALL / "truth/gold/enterprise.json").exists(), reason="build the small profile first")
def test_reference_passes(tmp_path):
    from enterprise_check.__main__ import main

    out = tmp_path / "week-02"
    build(SMALL, out)
    main(["--work", str(out), "--data", str(SMALL)])
