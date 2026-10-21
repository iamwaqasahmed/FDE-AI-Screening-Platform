"""Estate stage: the fault library, the volume stream, the checks, and the eval cases on the cached small world."""

from __future__ import annotations

import os

os.environ.setdefault("HARTLAND_PROFILE", "small")

from datetime import date

import numpy as np
import pandas as pd
import pytest

from simulation.check.estate import CHECKS, check_access, check_sms
from simulation.estate import volume
from simulation.estate.booking import COLUMNS, build_booking
from simulation.estate.sms import KEYS
from simulation.faults import duplicate, last_state_only, out_of_order, recode, stale_account, unit_change

RNG = np.random.default_rng(7)


@pytest.fixture(scope="module")
def world() -> dict:
    from simulation.devkit import with_stages

    return with_stages("simulation.corpus.stage", "simulation.estate.stage")


def test_last_state_only_keeps_latest():
    frame = pd.DataFrame({"key": ["a", "a", "b"], "seq": [0, 1, 0], "status": ["booked", "dna", "booked"]})
    out, entry = last_state_only.apply(frame, RNG, {"key": "key", "order": "seq"})
    assert out["status"].tolist() == ["dna", "booked"] and entry["history_lost"] == 1


def test_duplicate_and_out_of_order():
    times = pd.Series(pd.date_range("2024-01-01", periods=200, freq="min"))
    frame = pd.DataFrame({"id": range(200), "sent": times, "_arrival": times})
    dup, entry = duplicate.apply(frame, np.random.default_rng(1), {"share": 0.1, "key": "id", "shift": "_arrival"})
    assert len(dup) == 200 + entry["rows"] and entry["rows"] > 0
    ordered, record = out_of_order.apply(dup, RNG, {"arrival": "_arrival", "event": "sent", "drop": True})
    assert "_arrival" not in ordered.columns and record["inverted_share"] > 0


def test_unit_change_and_recode():
    frame = pd.DataFrame({"day": ["2021-03-31", "2021-04-01"], "value": [53.0, 53.0], "unit": ["", ""]})
    out, _ = unit_change.apply(frame, RNG, {"date": "day", "value": "value", "unit": "unit", "change_on": date(2021, 4, 1),
                                            "before_unit": "%", "after_unit": "mmol/mol", "to_before": lambda v: v / 10.929 + 2.15})
    assert out["unit"].tolist() == ["%", "mmol/mol"] and out["value"].tolist() == [7.0, 53.0]
    ledger = pd.DataFrame({"cc": ["A", "A"], "start": ["2022-04-01", "2023-04-01"]})
    coded, _ = recode.apply(ledger, RNG, {"column": "cc", "mapping": {"A": "B"}, "date": "start", "from_on": date(2023, 4, 1)})
    assert coded["cc"].tolist() == ["A", "B"]


def test_stale_account_clears_revocation():
    roles = pd.DataFrame({"account_id": ["u1", "u2"], "revoked_at": ["2024-06-01", "2024-06-01"]})
    out, entry = stale_account.apply(roles, RNG, {"accounts": ["u1"], "clear": ["revoked_at"]})
    assert out["revoked_at"].tolist() == ["", "2024-06-01"] and entry["cleared"]["revoked_at"] == 1


def test_volume_stream_partitions():
    files, faults = volume.sms_stream(np.array(["BK1", "BK2"]), np.random.default_rng(3), date(2025, 1, 1), rows=4_000)
    assert files and all(path.startswith("handover/sms/stream/year=") for path in files)
    assert sum(len(frame) for frame in files.values()) > 4_000 * 0.9 and {entry["fault"] for entry in faults} == {"duplicate", "out_of_order"}


def test_exact_columns(world):
    assert list(world["files"]["handover/booking/appointments.csv"].columns) == COLUMNS
    assert list(world["files"]["handover/sms/receipts.jsonl"].columns) == KEYS


def test_checks_pass(world):
    errors: list[str] = []
    for _, check in CHECKS:
        check(world, errors)
    assert errors == []


def test_checks_catch_removed_defects(world):
    broken = dict(world, files=dict(world["files"]), gold=dict(world["gold"]))
    receipts = broken["files"]["handover/sms/receipts.jsonl"]
    broken["files"]["handover/sms/receipts.jsonl"] = receipts.drop_duplicates().sort_values("sent_at")
    broken["gold"]["inappropriate_access"] = []
    errors: list[str] = []
    check_sms(broken, errors)
    check_access(broken, errors)
    assert len(errors) >= 3


def test_booking_is_deterministic(world):
    first = build_booking(dict(world, files={}), np.random.default_rng(5))
    second = build_booking(dict(world, files={}), np.random.default_rng(5))
    assert first.equals(second)


def test_cases(world):
    from simulation.eval.estate_cases import cases

    items = cases(world)
    outcomes = {item["tags"]["outcome"] for item in items}
    assert len(items) >= 40 and outcomes == {"enterprise_data", "architecture", "solution"}
    assert len({item["case_id"] for item in items}) == len(items)
    assert all(item["case_id"].startswith("estate-") and item["sources"] for item in items)
