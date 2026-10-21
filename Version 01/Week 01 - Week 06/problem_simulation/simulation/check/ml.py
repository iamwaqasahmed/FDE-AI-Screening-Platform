"""ML evidence invariants: no person ids, real subgroup gaps, a leak that inflates AUC, and a balanced judge set."""

from __future__ import annotations

import re
from collections import Counter

import pandas as pd

from simulation.ml.claims import material_gap
from simulation.ml.operating import lookup

UID = re.compile(r"\bP\d{7}\b")
HANDOVER_FILES = ("handover/ml/vendor_retrospective.csv", "handover/ml/adjudicated_labels.csv", "handover/ml/dna_training.csv")
GAP_SUBGROUPS = ("age_75_plus", "river_3.1.0_after_upgrade")


def check_no_person_ids(world: dict, errors: list[str]) -> None:
    for path in HANDOVER_FILES:
        frame = world["files"].get(path)
        if not isinstance(frame, pd.DataFrame):
            errors.append(f"{path} is missing.")
            continue
        if "person_uid" in frame.columns:
            errors.append(f"{path} has a person_uid column.")
        text_columns = frame.select_dtypes(exclude="number")
        if any(text_columns[column].astype(str).str.contains(UID).any() for column in text_columns.columns):
            errors.append(f"{path} contains a person id.")


def check_retrospective(world: dict, errors: list[str]) -> None:
    frame = world["files"]["handover/ml/vendor_retrospective.csv"]
    truth = world["files"]["truth/ml/retrospective_truth.parquet"]
    if len(frame) != int(world["events"]["vendor_scored"].sum()) or len(truth) != len(frame):
        errors.append("The retrospective set does not hold every vendor-scored capture.")
    if frame["capture_ref"].duplicated().any():
        errors.append("Retrospective capture references repeat.")
    if not truth["disagreement_reason"].str.startswith("vendor_wrong").any() or not truth["disagreement_reason"].eq("grader_wrong").any():
        errors.append("The retrospective has no vendor-wrong or no grader-wrong disagreements.")


def check_operating_points(world: dict, errors: list[str]) -> None:
    points = world["tables"]["ml_operating_points"]
    for subgroup in GAP_SUBGROUPS:
        if not material_gap(points, subgroup):
            errors.append(f"Vendor sensitivity for {subgroup} is not materially below the whole set.")
    if lookup(points, "all", reference="grader_label") >= lookup(points, "all") - 0.05:
        errors.append("Sensitivity against the grader label does not differ from sensitivity against latent disease.")
    claim = world["gold"]["ml_vendor_claim"]
    if claim["holds_overall"] or not claim["holds_on"]:
        errors.append("The vendor claim should fail overall and hold on at least one subgroup.")


def check_labels(world: dict, errors: list[str]) -> None:
    sample = world["tables"]["ml_adjudicated"]
    share = len(sample) / max(len(world["files"]["handover/ml/vendor_retrospective.csv"]), 1)
    if not 0.03 <= share <= 0.07:
        errors.append(f"Adjudicated share {share:.3f} is not about five per cent.")
    if sample["routine_label"].eq(sample["adjudicated_label"]).all():
        errors.append("Adjudicated labels never differ from routine grades.")


def check_leakage(world: dict, errors: list[str]) -> None:
    result = world["gold"]["ml_baselines"]
    if result["random_split_with_leak_auc"] <= result["honest_split_without_leak_auc"] + 0.1:
        errors.append("The leaky random-split AUC is not well above the honest AUC.")
    leakage = world["files"]["truth/ml/dna_leakage.json"]
    if leakage["mean_rows_per_person"] <= 1.5:
        errors.append("The did-not-attend table does not repeat people, so a random split cannot leak.")


def check_judge_set(world: dict, errors: list[str]) -> None:
    rows = world["files"]["eval/judge_calibration.jsonl"]
    scores = Counter(row["label"]["score"] for row in rows)
    if len(rows) < 150:
        errors.append(f"Judge calibration set has only {len(rows)} rows.")
    for level in range(1, 6):
        if scores[level] < 0.08 * len(rows):
            errors.append(f"Judge calibration score {level} has {scores[level]} rows.")
    passes = sum(row["label"]["pass"] for row in rows)
    if not 0.25 <= passes / max(len(rows), 1) <= 0.6:
        errors.append(f"Judge calibration pass share {passes / max(len(rows), 1):.2f} is unbalanced.")


CHECKS = [
    ("ml_no_person_ids", check_no_person_ids),
    ("ml_retrospective", check_retrospective),
    ("ml_operating_points", check_operating_points),
    ("ml_labels", check_labels),
    ("ml_leakage", check_leakage),
    ("ml_judge_set", check_judge_set),
]
