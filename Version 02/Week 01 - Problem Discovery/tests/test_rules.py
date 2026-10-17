"""Checker rules for the traps a careless reading falls into."""

from __future__ import annotations

from discovery_check.items.ranking import ranking
from discovery_check.items.sizing import backlog, eligible_people, reminder
from discovery_check.rules import integers, present

ELIGIBLE = {"eligible": {"count": 1000, "tolerance": 0.02, "registry_rows": 1200, "warehouse": 1100}}
RANKING = {
    "ranking": {
        "keys": ["identity_resolution", "letter_bureau_fix", "vendor_model_expansion"],
        "highest": "identity_resolution",
        "lowest": "vendor_model_expansion",
        "prerequisites": {
            "identity_resolution": [],
            "letter_bureau_fix": [],
            "vendor_model_expansion": ["identity_resolution"],
        },
        "blockers": {
            "identity_resolution": [],
            "letter_bureau_fix": [],
            "vendor_model_expansion": ["clinical_safety_owner"],
        },
    }
}
REMINDER = {"reminder": {"change_date": "2023-01-09", "naive": {"North City": 0.07}, "naive_tolerance": 0.03}}
BACKLOG = {"backlog": {"from": "2025-10-01", "lead": 100, "board": 40, "true": 10}}


def test_eligible_rejects_the_warehouse_and_the_raw_rows():
    assert eligible_people({"count": 1005}, ELIGIBLE)
    assert not eligible_people({"count": 1100}, ELIGIBLE)
    assert not eligible_people({"count": 1200}, ELIGIBLE)


def test_vendor_first_fails_and_a_structural_order_passes():
    good = ["identity_resolution", "letter_bureau_fix", "vendor_model_expansion"]
    assert ranking({"order": good}, RANKING)
    assert not ranking({"order": ["vendor_model_expansion", "identity_resolution", "letter_bureau_fix"]}, RANKING)


def test_reminder_rejects_the_naive_figure_as_the_effect():
    same = {"change_date": "2023-01-09", "districts": {"North City": {"naive": 0.07, "true_uplift": 0.07}}}
    smaller = {"change_date": "2023-01-09", "districts": {"North City": {"naive": 0.07, "true_uplift": 0.02}}}
    assert not reminder(same, REMINDER)
    assert reminder(smaller, REMINDER)


def test_backlog_rejects_the_board_number():
    assert not backlog({"from": "2025-10-01", "lead": 100, "board": 40, "true": 40}, BACKLOG)
    assert backlog({"from": "2025-10-01", "lead": 100, "board": 40, "true": 12}, BACKLOG)


def test_numbers_and_dates_in_prose():
    assert 5394 in integers("The eligible count we can defend is 5394.")
    assert 2026 not in integers("The freeze starts 2026-10-19.")
    assert present("Agency graders read 8,333 encounters.", "8333")
    assert present("The rota changed on 4 March 2024.", "2024-03-04")
