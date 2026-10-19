"""The facts the judge calibration answers are written about, each taken from the ML gold."""

from __future__ import annotations

import math
from dataclasses import dataclass

import pandas as pd

from simulation.ml.claims import CLAIM
from simulation.ml.operating import lookup
from simulation.systems.catalog import OWNERS

MAX_FACTS = 25
MIN_GRADER_ROWS = 50
SUBGROUP_NAMES = {
    "all": "all scored captures",
    "age_75_plus": "people aged 75 and over",
    "age_under_75": "people under 75",
    "operator_PB": "captures taken by operator PB",
    "river_before_upgrade": "River Outreach before the firmware upgrade",
    "river_3.1.0_after_upgrade": "River Outreach on firmware 3.1.0",
    "favourable": "the favourable subgroup (under 75, trained operator, no firmware penalty, good quality)",
}


@dataclass(frozen=True)
class Fact:
    fact_id: str
    category: str
    question: str
    kind: str
    value: object
    secondary_label: str
    secondary: object
    caveat: str
    source: str
    overclaim: str
    wrong_text: str = ""
    secondary_wrong_text: str = ""


def judge_facts(points: pd.DataFrame, noise: list[dict], baselines: dict, claim: dict, counts: dict) -> list[Fact]:
    facts = _operating(points) + _noise(noise) + _baselines(baselines) + _discovery(claim, counts) + _governance()
    return facts[:MAX_FACTS]


def _operating(points: pd.DataFrame) -> list[Fact]:
    facts = []
    for key, label in SUBGROUP_NAMES.items():
        value, spec = lookup(points, key), lookup(points, key, metric="specificity")
        if math.isnan(value) or math.isnan(spec):
            continue
        grader = lookup(points, key, reference="grader_label")
        facts.append(Fact(
            f"op-{key}", "ml", f"What is the vendor's sensitivity at its referable cut against latent disease for {label}?",
            "rate", value, "specificity", spec,
            f"this is against latent disease; against the routine grader label it reads {grader:.2f}, which understates the vendor",
            "truth/ml/operating_points.csv", f"so the vendor can replace the grader for {label}",
        ))
    grader_all = lookup(points, "all", reference="grader_label")
    facts.append(Fact(
        "op-grader-all", "ml", "What sensitivity does the vendor show when the routine grader label is used as the reference?",
        "rate", grader_all, "specificity against the grader", lookup(points, "all", reference="grader_label", metric="specificity"),
        "the grader label is noisy, so this understates the vendor against latent disease",
        "handover/ml/vendor_retrospective.csv", "so the vendor is clearly worse than the graders",
    ))
    return facts


def _noise(noise: list[dict]) -> list[Fact]:
    facts = []
    for row in noise:
        if row["n"] < MIN_GRADER_ROWS or row["grader"] == "all_routine":
            continue
        who = "the lead adjudication" if row["grader"] == "adjudicated" else f"grader {row['grader']}"
        facts.append(Fact(
            f"noise-{row['grader']}", "ml", f"What share of referable calls by {who} disagree with latent disease on the retrospective set?",
            "rate", row["noise_rate"], "miss rate", row["miss_rate"],
            "it is measured only on vendor-scored captures and a single grade is not ground truth",
            "truth/gold/ml_label_noise.jsonl", f"so {who} should be excluded from all labels",
        ))
    return facts


def _baselines(baselines: dict) -> list[Fact]:
    return [
        Fact("dna-leaky-auc", "ml", "What AUC does the analyst's random split reach with every column in the did-not-attend table?",
             "auc", baselines["random_split_with_leak_auc"], "honest AUC", baselines["honest_split_without_leak_auc"],
             f"it is inflated by {baselines['leaky_feature']}, which is filled in after the outcome",
             "truth/gold/ml_baselines.json", "so the model is ready to target reminders"),
        Fact("dna-honest-auc", "ml", "What AUC does a did-not-attend baseline reach with people held out and a temporal split?",
             "auc", baselines["honest_split_without_leak_auc"], "random-split AUC with all columns", baselines["random_split_with_leak_auc"],
             "it excludes the post-outcome booking status and keeps each person on one side of the split",
             "truth/gold/ml_baselines.json", "so attendance is essentially predictable"),
        Fact("dna-leaky-feature", "ml", "Which column in the did-not-attend table leaks the outcome?",
             "text", baselines["leaky_feature"], "grouping column", baselines["group_column"],
             "the same person appears in many rows, so a random split also leaks people",
             "truth/ml/dna_leakage.json", "so dropping it makes the table leakage-free",
             wrong_text="dna_prev", secondary_wrong_text="invitation_ref"),
    ]


def _discovery(claim: dict, counts: dict) -> list[Fact]:
    holds = "yes" if claim["holds_overall"] else "no"
    return [
        Fact("claim-holds", "discovery", f"Does the vendor's claimed sensitivity of {claim['claimed']:.2f} hold across the programme?",
             "text", holds, "true sensitivity overall", f"{claim['true_sensitivity_all']:.2f}",
             f"it only holds on a subgroup such as the favourable captures ({claim['favourable_sensitivity']:.2f})",
             "truth/ml/operating_points.csv", "so the vendor contract can be signed on the claim",
             wrong_text="no" if holds == "yes" else "yes", secondary_wrong_text=f"{claim['claimed']:.2f}"),
        Fact("count-scored", "discovery", "How many captures are in the vendor retrospective set?",
             "count", counts["scored"], "rejected for quality", counts["rejected"],
             "the set covers primary care and outreach only, not hospital PACS captures",
             "handover/ml/vendor_retrospective.csv", "so the vendor has been validated on every site"),
    ]


def _governance() -> list[Fact]:
    owner = dict(OWNERS)["clinical_safety_owner"] or "blank"
    return [
        Fact("pilot-restart", "governance", "Can the vendor pilot restart now?",
             "text", "no", "clinical safety owner", owner,
             "the pilot stays stopped until a clinical safety owner is named in handover/owners.csv",
             "handover/owners.csv", "so restarting only needs the vendor's sign-off",
             wrong_text="yes", secondary_wrong_text="A. Okonkwo"),
    ]
