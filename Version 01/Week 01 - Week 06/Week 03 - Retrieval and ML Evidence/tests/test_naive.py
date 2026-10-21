"""Shortcuts that look finished and are wrong."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from evidence_check.extract import score as score_extract
from evidence_check.gold import extract, load
from evidence_check.items.cohorts import dna_leak
from evidence_check.items.corpus import policy_graph
from evidence_check.items.vendor import reference_gap

SMALL = Path(__file__).resolve().parents[2] / "problem_simulation" / "build" / "data-small"


def test_a_date_of_birth_column_fails(tmp_path: Path):
    path = tmp_path / "vendor_extract.csv"
    path.write_text("capture_ref,DOB\nVR-000001,1966-01-02\n", encoding="utf-8")
    gold = pd.DataFrame({"capture_ref": ["VR-000001"], "local_pid": ["LP1"], "year_of_birth": ["1966"], "capture_date": ["2024-01-01"]})
    assert score_extract(path, gold)["dates"] is False


@pytest.mark.skipif(not (SMALL / "truth/gold/evidence.json").exists(), reason="build the small profile first")
def test_shortcuts_fail_the_small_seed(tmp_path: Path):
    gold = load(SMALL)
    register = {"drafts": [], "withdrawn": [], "overlays": [], "stale_register": []}
    assert policy_graph(register, gold) is False
    gap = dict(gold["items"]["reference_gap"])
    assert reference_gap({"cut": gap["cut"], "rejected": gap["rejected"], "routine": gap["routine"],
                          "adjudicated": gap["routine"], "gap": 0}, gold) is False
    leak = dict(gold["items"]["dna_leak"])
    swapped = dict(leak, honest_auc=leak["random_auc"], inflation=0)
    assert dna_leak(swapped, gold) is False
    frame = extract(SMALL)
    written = tmp_path / "vendor_extract.csv"
    frame.assign(DOB="1966-01-02").to_csv(written, index=False)
    assert score_extract(written, frame)["ok"] is False
