"""The bureau traps are visible in the small build, without opening truth."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

SMALL = Path(__file__).resolve().parents[2] / "problem_simulation" / "build" / "data-small"


@pytest.mark.skipif(not (SMALL / "drops/week-4").exists(), reason="build the small profile first")
def test_losses_and_copies_sit_on_the_same_days_and_the_agreement_does_not_say_chase():
    folder = SMALL / "drops/week-4/letters"
    requests = pd.read_csv(next(folder.glob("requests_*.csv")), dtype=str)
    dispatch = pd.read_csv(next(folder.glob("dispatch_*.csv")), dtype=str)
    copies = dispatch.groupby("request_id").size()
    requests["copies"] = requests["request_id"].map(copies).fillna(0).astype(int)
    odd = requests[requests["copies"] != 1]
    assert set(odd["requested_at"]) <= set(requests["requested_at"])
    assert (requests["copies"] == 0).any()
    assert (requests["copies"] == 2).any()
    agreement = (SMALL / "corpus/data-sharing/dsa-postright-2020.md").read_text(encoding="utf-8")
    assert "chase" not in agreement.lower()
    catalogue = pd.read_csv(SMALL / "handover/architecture/data_catalogue.csv", dtype=str)
    claim = catalogue.loc[catalogue["dataset"].eq("letters_dispatch"), "definition"].iloc[0]
    assert "One row per letter." in claim
    incident = pd.read_csv(SMALL / "handover/letters/incident_2025-03.csv", dtype=str)
    assert "request_id" not in incident.columns
    assert int(incident.duplicated().sum()) > 0
