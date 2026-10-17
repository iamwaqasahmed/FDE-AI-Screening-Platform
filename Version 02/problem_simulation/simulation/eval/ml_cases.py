"""ML evidence questions: true operating points, the vendor claim, label noise, and the did-not-attend leak."""

from __future__ import annotations

import math

from simulation.eval.case_format import make_case
from simulation.ml.judge_facts import MIN_GRADER_ROWS, SUBGROUP_NAMES
from simulation.ml.operating import lookup

ROLES = ("ml", "data_science")
VENDOR_SURFACES = ("ml", "vendor", "devices", "grader")
DNA_SURFACES = ("ml", "behaviour")


def cases(world: dict) -> list[dict]:
    points = world["tables"]["ml_operating_points"]
    gold = world["gold"]
    return (
        _operating(points)
        + _periods(points)
        + _claim(gold["ml_vendor_claim"], points)
        + _noise(gold["ml_label_noise"])
        + _dna(gold["ml_baselines"], world["files"]["truth/ml/dna_leakage.json"])
        + _counts(gold["ml_counts"], world["files"]["truth/ml/retrospective_truth.parquet"])
    )


def _ask(case_id: str, question: str, expected: dict, outcome: str = "solution", budget: str = "analysis", surfaces=VENDOR_SURFACES, kind: str = "value") -> dict:
    sources = ("handover/ml/vendor_retrospective.csv",) if surfaces is VENDOR_SURFACES else ("handover/ml/dna_training.csv",)
    return make_case(f"ml-{case_id}", question, expected, outcome=outcome, roles=ROLES, surfaces=surfaces, budget=budget, sources=sources, kind=kind)


def _rate(value: float) -> dict:
    return {"value": round(value, 4), "tolerance": 0.02}


def _operating(points) -> list[dict]:
    out = []
    for key, label in SUBGROUP_NAMES.items():
        value = lookup(points, key)
        if not math.isnan(value):
            out.append(_ask(f"sens-true-{key}", f"Against latent disease, what is the vendor's sensitivity at the R2 cut for {label}?", _rate(value)))
    for key in ("all", "age_75_plus", "river_3.1.0_after_upgrade"):
        value = lookup(points, key, reference="grader_label")
        if not math.isnan(value):
            out.append(_ask(f"sens-grader-{key}", f"Using the routine grader label as reference, what is the vendor's sensitivity at the R2 cut for {SUBGROUP_NAMES[key]}?", _rate(value)))
    out.append(_ask("spec-true-all", "Against latent disease, what is the vendor's specificity at the R2 cut on all scored captures?", _rate(lookup(points, "all", metric="specificity"))))
    market = points[(points["subgroup"] == "market_4.2.0_after_upgrade") & (points["reference"] == "true_referable")]["n"].max()
    out.append(_ask("market-scored", "How many vendor-scored captures come from Market Eye Clinic on firmware 4.2.0 after its upgrade?", {"value": int(market), "tolerance": 0}, outcome="discovery", budget="multi_hop"))
    return out


def _periods(points) -> list[dict]:
    years = sorted(name.split(":")[1] for name in points["subgroup"].unique() if name.startswith("period:"))
    return [
        _ask(f"sens-period-{year}", f"Against latent disease, what is the vendor's sensitivity at the R2 cut for captures in {year}?", _rate(lookup(points, f"period:{year}")))
        for year in years
        if not math.isnan(lookup(points, f"period:{year}"))
    ]


def _claim(claim: dict, points) -> list[dict]:
    return [
        _ask("claim-overall", f"The vendor claims sensitivity {claim['claimed']:.2f}. Does that hold against latent disease on all scored captures?",
             {"value": claim["holds_overall"], "true_sensitivity": round(claim["true_sensitivity_all"], 4), "tolerance": 0.02}, outcome="discovery"),
        _ask("claim-subgroups", f"On which subgroups does the vendor's sensitivity reach the claimed {claim['claimed']:.2f}?",
             {"value": claim["holds_on"]}, outcome="discovery", kind="set"),
        _ask("claim-gap-grader", "How far below the latent-disease sensitivity is the sensitivity measured against the routine grader label?",
             _rate(claim["true_sensitivity_all"] - claim["grader_sensitivity_all"]), outcome="discovery"),
        _ask("firmware-drift", "By how much does vendor sensitivity at River Outreach fall after the 3.1.0 firmware upgrade?",
             _rate(lookup(points, "river_before_upgrade") - lookup(points, "river_3.1.0_after_upgrade"))),
    ]


def _noise(noise: list[dict]) -> list[dict]:
    graders = [row for row in noise if row["grader"] not in ("all_routine", "adjudicated") and row["n"] >= MIN_GRADER_ROWS]
    out = [
        _ask(f"noise-{row['grader']}", f"On the retrospective set, what share of grader {row['grader']}'s referable calls disagree with latent disease?", _rate(row["noise_rate"]), budget="analysis")
        for row in graders
    ]
    over = max(graders, key=lambda row: (row["over_call_rate"], row["grader"]))
    miss = max(graders, key=lambda row: (row["miss_rate"], row["grader"]))
    lead = next(row for row in noise if row["grader"] == "adjudicated")
    routine = next(row for row in noise if row["grader"] == "all_routine")
    return out + [
        _ask("noise-most-over-call", "Which grader over-calls referable disease most often against latent disease?", {"value": over["grader"]}),
        _ask("noise-most-miss", "Which grader misses referable disease most often against latent disease?", {"value": miss["grader"]}),
        _ask("noise-adjudicated", "What share of the lead grader's adjudicated referable calls disagree with latent disease?", _rate(lead["noise_rate"])),
        _ask("noise-routine", "What share of routine referable calls on the retrospective set disagree with latent disease?", _rate(routine["noise_rate"])),
        _ask("noise-routine-vs-adjudicated", "In the adjudicated sample, how often does the routine referable call differ from the adjudicated one?", _rate(lead["routine_vs_adjudicated_disagreement"]), budget="multi_hop"),
    ]


def _dna_ask(case_id: str, question: str, expected: dict, budget: str = "analysis") -> dict:
    return _ask(case_id, question, expected, budget=budget, surfaces=DNA_SURFACES)


def _dna(baselines: dict, leakage: dict) -> list[dict]:
    return [
        _dna_ask("dna-leaky-feature", "Which column in the did-not-attend table is only known after the outcome?", {"value": leakage["leaky_feature"]}, "multi_hop"),
        _dna_ask("dna-group-column", "Which column must a split group on so the same person is not in train and test?", {"value": leakage["group_column"]}, "multi_hop"),
        _dna_ask("dna-leaky-auc", "What AUC does a logistic baseline reach on a random row split using every column?", _rate(baselines["random_split_with_leak_auc"])),
        _dna_ask("dna-honest-auc", "What AUC does a logistic baseline reach with people held out, a temporal split, and no post-outcome column?", _rate(baselines["honest_split_without_leak_auc"])),
        _dna_ask("dna-inflation", "How much does the leaky random split inflate AUC over the honest baseline?", _rate(baselines["leak_inflation"])),
        _dna_ask("dna-people-overlap", "On a random row split, what share of test people also appear in training?", _rate(baselines["random_test_people_also_in_train"])),
        _dna_ask("dna-rows-per-person", "How many invitation rows does the did-not-attend table hold per person on average?", {"value": leakage["mean_rows_per_person"], "tolerance": 0.05}, "multi_hop"),
    ]


def _counts(counts: dict, truth) -> list[dict]:
    wrong = truth.loc[truth["disagreement_reason"].str.startswith("vendor_wrong:"), "disagreement_reason"].str.split(":").str[1]
    top = wrong.value_counts().sort_index().sort_values(ascending=False, kind="stable").index[0] if len(wrong) else ""
    return [
        _ask("count-scored", "How many captures are in the vendor retrospective set?", {"value": counts["scored"], "tolerance": 0}, outcome="discovery", budget="lookup"),
        _ask("count-rejected", "How many retrospective captures did the vendor reject for image quality?", {"value": counts["rejected"], "tolerance": 0}, outcome="discovery", budget="lookup"),
        _ask("count-adjudicated", "How many captures did the lead grader adjudicate?", {"value": counts["adjudicated"], "tolerance": 0}, outcome="discovery", budget="lookup"),
        _ask("top-vendor-miss-cause", "When the vendor disagrees with the grader and the vendor is wrong, what is the most common cause?", {"value": top}, outcome="discovery"),
    ]
