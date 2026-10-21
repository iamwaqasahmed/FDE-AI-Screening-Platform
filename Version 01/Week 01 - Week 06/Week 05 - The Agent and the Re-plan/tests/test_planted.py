"""The week 5 drop keeps the traps visible on the small build."""

from __future__ import annotations

from pathlib import Path

import pytest

SMALL = Path(__file__).resolve().parents[2] / "problem_simulation" / "build" / "data-small"
pytestmark = pytest.mark.skipif(not (SMALL / "drops/week-5/delivery_assumptions.md").exists(), reason="small build is not present")


def test_the_second_site_is_a_hospital_and_the_memo_states_no_date():
    scope = (SMALL / "drops/week-5/scope_change_cdo.md").read_text(encoding="utf-8")
    assumptions = (SMALL / "drops/week-5/delivery_assumptions.md").read_text(encoding="utf-8")
    assert "hospital" in scope.lower()
    assert "2027-02-01" in scope
    assert "2027-03-29" not in assumptions
    assert "2 weeks" in assumptions and "3 weeks" in assumptions and "4 weeks" in assumptions


def test_the_contract_is_not_a_direct_award_and_gate_3_is_early():
    import pandas as pd
    routes = pd.read_csv(SMALL / "handover/delivery/procurement_routes.csv")
    direct = routes.set_index("route").loc["direct_award", "max_value_gbp"]
    roadmap = pd.read_csv(SMALL / "handover/delivery/roadmap.csv").set_index("item_id")
    gates = pd.read_csv(SMALL / "handover/delivery/funding_gates.csv").set_index("gate")
    assert int(roadmap.at["RM-02", "estimated_value_gbp"]) > int(direct)
    assert str(gates.at["G3", "gate_date"]) < "2027-03-01"


def test_the_closed_risk_has_no_mitigation_and_the_discovery_token_is_read_only():
    import pandas as pd
    import yaml
    risks = pd.read_csv(SMALL / "handover/delivery/risk_register.csv").fillna("")
    bare = risks[(risks["risk_id"] == "R-07")]
    assert bare.iloc[0]["status"] == "Closed" and bare.iloc[0]["mitigation"] == ""
    tokens = yaml.safe_load((SMALL.parents[1] / "serve" / "tokens.yaml").read_text(encoding="utf-8"))["tokens"]
    discovery = next(row for row in tokens if row["client"] == "discovery-team")
    writers = [row["client"] for row in tokens if any(scope.endswith(":write") for scope in row["scopes"])]
    assert all(scope.endswith(":read") for scope in discovery["scopes"])
    assert len(writers) >= 2


def test_the_tracker_has_no_duplicate_column():
    header = (SMALL / "handover/delivery/tracker.csv").read_text(encoding="utf-8").splitlines()[0]
    assert "duplicate_of" not in header
