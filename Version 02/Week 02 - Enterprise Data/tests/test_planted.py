"""The API's version 3 is not the file, and the reissue drops warehouse rows."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from enterprise_check.live import FILE_COLUMNS, api_shape

SMALL = Path(__file__).resolve().parents[2] / "problem_simulation" / "build" / "data-small"


def test_api_v3_omits_the_file_columns():
    shape = api_shape()
    assert "home_clinic" in shape["keeps"]
    assert "REGISTERED_SITE" not in shape["shaped_keys"]
    for column in ("DISTRICT_CODE", "FLAG_DATE", "SCHEMA_VERSION"):
        assert column in shape["missing"]
        assert column in FILE_COLUMNS


def test_reissue_join_loss_equals_the_batch():
    if not SMALL.exists():
        return
    batch = pd.read_csv(SMALL / "drops/week-2/registry/reissue_batch.csv", dtype=str)
    warehouse = pd.read_csv(SMALL / "handover/warehouse/registry_snapshot.csv", dtype=str)
    version3 = pd.read_csv(SMALL / "drops/week-2/registry/current_v3.csv", dtype=str)
    lost = warehouse["registry_no"].isin(set(batch["OLD_REGISTRY_NO"])).sum()
    assert lost == len(batch)
    assert not version3["REGISTRY_NO"].isin(set(batch["OLD_REGISTRY_NO"])).any()
