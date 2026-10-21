"""HbA1c lab feed keyed by lab patient id. Percent before the analyser change, mmol/mol after; some units blank."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.disease.hba1c import YEARS
from simulation.estate.common import TRUTH, base_people, id_map, log_fault
from simulation.faults import blank_field, unit_change
from simulation.world.clock import HISTORY_START, LAB_UNIT_CHANGE, SNAPSHOT

COLUMNS = ["result_id", "lab_pid", "test_code", "sample_date", "reported_at", "value", "unit"]
COVERAGE = 0.75


def to_percent(mmol: np.ndarray) -> np.ndarray:
    return mmol / 10.929 + 2.15


def to_mmol(percent: np.ndarray) -> np.ndarray:
    return 10.929 * (percent - 2.15)


def build_lab(world: dict, rng: np.random.Generator) -> pd.DataFrame:
    results = _results(world, rng)
    feed, change = unit_change.apply(results, rng, {
        "date": "sample_date", "value": "value", "unit": "unit", "change_on": LAB_UNIT_CHANGE,
        "before_unit": "%", "after_unit": "mmol/mol", "to_before": to_percent, "decimals": 1,
    })
    feed, blank = blank_field.apply(feed, rng, {"column": "unit", "share": 0.05, "key": "result_id"})
    log_fault(world, "lab", change)
    log_fault(world, "lab", blank)
    world["files"]["handover/lab/hba1c_results.csv"] = feed[COLUMNS]
    truth = results.assign(unit_shown=feed["unit"].to_numpy(), value_shown=feed["value"].to_numpy())
    world["files"][f"{TRUTH}/lab_hba1c.parquet"] = truth.rename(columns={"value": "hba1c_mmol_mol"})
    return truth


def _results(world: dict, rng: np.random.Generator) -> pd.DataFrame:
    people = base_people(world)
    rows = world["hidden"]["person_row"].reindex(people["person_uid"]).to_numpy()
    values = world["hidden"]["hba1c"]
    lab_pid = people["person_uid"].map(id_map(world["identifiers"], "lab_pid")).fillna("").to_numpy()
    person_index, year_index = np.meshgrid(np.arange(len(people)), np.arange(len(YEARS)), indexing="ij")
    person_index, year_index = person_index.ravel(), year_index.ravel()
    keep = (rng.random(len(person_index)) < COVERAGE) & (lab_pid[person_index] != "")
    person_index, year_index = person_index[keep], year_index[keep]
    sample = _sample_dates(np.array(YEARS)[year_index], rng)
    inside = (sample >= pd.Timestamp(HISTORY_START)) & (sample < pd.Timestamp(SNAPSHOT))
    frame = pd.DataFrame({
        "person_uid": people["person_uid"].to_numpy()[person_index],
        "lab_pid": lab_pid[person_index],
        "test_code": "HBA1C",
        "sample_date": sample.dt.strftime("%Y-%m-%d"),
        "reported_at": (sample + pd.to_timedelta(rng.integers(1, 6, len(sample)), unit="D")).dt.strftime("%Y-%m-%d"),
        "value": values[rows[person_index], year_index].astype(float),
        "unit": "mmol/mol",
    }).loc[inside.to_numpy()]
    frame = frame.sort_values(["sample_date", "lab_pid"]).reset_index(drop=True)
    frame.insert(0, "result_id", [f"LR{index:08d}" for index in range(1, len(frame) + 1)])
    return frame


def _sample_dates(years: np.ndarray, rng: np.random.Generator) -> pd.Series:
    starts = pd.to_datetime(pd.Series(years.astype(str)), format="%Y")
    return starts + pd.to_timedelta(rng.integers(0, 365, len(years)), unit="D")
