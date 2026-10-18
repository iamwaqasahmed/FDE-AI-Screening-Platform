"""Proposal terms, the did-not-attend split, and the pilot-scope upper bound."""

from __future__ import annotations

from course.checks.rules import as_int, close
from simulation.eval.evidence.bars import AUC_TOLERANCE


def proposal_terms(answer: dict, gold: dict) -> bool:
    row = gold["items"]["proposal_terms"]
    return all(answer.get(key) == row[key] for key in ("hospital_studies", "no_local_evaluation", "injection"))


def dna_leak(answer: dict, gold: dict) -> bool:
    row = gold["items"]["dna_leak"]
    texts = ("leaky_feature", "group_column", "temporal_cutoff")
    if any(answer.get(key) != row[key] for key in texts) or as_int(answer.get("seed")) != row["seed"]:
        return False
    if answer.get("has_dob") is not False or answer.get("age_is_derived") is not True:
        return False
    return all(close(answer.get(key), row[key], AUC_TOLERANCE, relative=False) for key in ("random_auc", "honest_auc", "inflation"))


def overdue_pilot_scope(answer: dict, gold: dict) -> bool:
    row = gold["items"]["overdue_pilot_scope"]
    if answer.get("is_upper_bound") is not True:
        return False
    return close(answer.get("upper_bound"), row["upper_bound"], 0.02)
