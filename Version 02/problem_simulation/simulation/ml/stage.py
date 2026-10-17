"""ML evidence: the vendor retrospective, adjudicated labels, true operating points, the did-not-attend table, and the judge set."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.ml.adjudication import adjudicated_sample, noise_by_grader
from simulation.ml.claims import claim_gold
from simulation.ml.dna_splits import run_baselines
from simulation.ml.dna_table import GROUP_COLUMN, dna_table, leakage_truth
from simulation.ml.judge_answers import calibration_rows
from simulation.ml.judge_facts import judge_facts
from simulation.ml.judge_rubric import rubric_text
from simulation.ml.operating import operating_points
from simulation.ml.retrospective import handover_frame, scored_frame, truth_frame


def build(world: dict, rng: np.random.Generator) -> None:
    files, gold = world["files"], world["gold"]
    scored = scored_frame(world["events"])
    files["handover/ml/vendor_retrospective.csv"] = handover_frame(scored)
    files["truth/ml/retrospective_truth.parquet"] = truth_frame(scored)
    sample = adjudicated_sample(scored, rng)
    files["handover/ml/adjudicated_labels.csv"] = sample
    noise = noise_by_grader(scored, sample)
    gold["ml_label_noise"] = noise
    points = operating_points(scored)
    files["truth/ml/operating_points.csv"] = points
    claim = claim_gold(points)
    gold["ml_vendor_claim"] = claim
    table, person_uid = dna_table(world["invitations"], world["people"], rng)
    files["handover/ml/dna_training.csv"] = table
    files["truth/ml/dna_keys.parquet"] = _key_map(table, person_uid)
    files["truth/ml/dna_leakage.json"] = leakage_truth(table)
    baselines = run_baselines(table, rng)
    gold["ml_baselines"] = baselines
    counts = {"scored": len(scored), "rejected": int(scored["vendor_score"].isna().sum()), "adjudicated": len(sample)}
    gold["ml_counts"] = counts
    rows = calibration_rows(judge_facts(points, noise, baselines, claim, counts), rng)
    files["eval/judge_calibration.jsonl"] = rows
    files["eval/judge_rubric.md"] = rubric_text()
    world["tables"]["ml_operating_points"] = points
    world["tables"]["ml_adjudicated"] = sample


def _key_map(table: pd.DataFrame, person_uid: np.ndarray) -> pd.DataFrame:
    frame = pd.DataFrame({GROUP_COLUMN: table[GROUP_COLUMN].to_numpy(), "person_uid": person_uid})
    return frame.drop_duplicates().sort_values(GROUP_COLUMN).reset_index(drop=True)
