"""Gross annual value and running cost of each opportunity, counted from the world's volumes."""

from __future__ import annotations

from simulation.economics.costs import cost
from simulation.economics.opportunities import OPPORTUNITIES, Opportunity
from simulation.economics.reminder import true_uplift


def _harm(v: dict, cause: str) -> float:
    return v["harm"][cause]["harm_gbp"]


def _reminder_gain(world: dict, v: dict) -> float:
    uplift = true_uplift(world["invitations"])
    ordered = sorted(uplift.values())
    median = (ordered[len(ordered) // 2 - 1] + ordered[len(ordered) // 2]) / 2
    phones = v["phones_by_district"]
    gained = sum(0.5 * uplift[d] * phones.get(d, 0.0) for d in uplift if uplift[d] > median)
    saved_sms = sum(phones.get(d, 0.0) * cost("sms") for d in uplift if uplift[d] < 0.01)
    return gained * cost("dna_slot") + saved_sms


GROSS = {
    "grader_triage_ai": lambda w, v: v["vendor_low_scores"] * cost("grader_read") + 0.3 * _harm(v, "grader_backlog")
    * v["primary_reads"] / max(v["primary_reads"] + v["hospital_reads"], 1.0),
    "letter_bureau_fix": lambda w, v: _harm(v, "letter_bureau") + v["duplicate_letters"] * cost("letter_reprint")
    + v["calls"].get("letter_not_received", 0.0) * cost("call"),
    "reminder_targeting": _reminder_gain,
    "identity_resolution": lambda w, v: _harm(v, "never_graded")
    + v["alias_records"] * (cost("letter") + cost("sms") + 0.3 * cost("dna_slot")),
    "dna_prediction": lambda w, v: v["dna_screening"] * cost("dna_slot"),
    "fast_track_scheduling": lambda w, v: _harm(v, "booking") + v["ophthalmology_dna"] * cost("ophthalmology_visit"),
    "call_deflection": lambda w, v: sum(v["calls"].values()) * cost("call"),
    "vendor_model_expansion": lambda w, v: v["grader_reads"] * cost("grader_read") + _harm(v, "grader_backlog"),
}

RUNNING = {
    "grader_triage_ai": lambda w, v: v["primary_reads"] * cost("vendor_read_fee"),
    "vendor_model_expansion": lambda w, v: (v["primary_reads"] + v["hospital_reads"]) * cost("vendor_read_fee"),
    "call_deflection": lambda w, v: 0.6 * v["calls"].get("letter_not_received", 0.0) * cost("call"),
}

CLAIMED = {
    "vendor_model_expansion": lambda w, v: v["grader_reads"] * cost("grader_read") + _harm(v, "grader_backlog")
    + _harm(v, "never_graded"),
}

ALLOWED = {
    "vendor_model_expansion": lambda w, v: v["primary_reads"] / max(v["primary_reads"] + v["hospital_reads"], 1.0),
}


def value_model(item: Opportunity, world: dict, v: dict) -> dict:
    gross = float(GROSS[item.key](world, v))
    running = float(RUNNING.get(item.key, lambda w, v: 0.0)(world, v))
    allowed = float(ALLOWED.get(item.key, lambda w, v: 1.0)(world, v))
    claimed = float(CLAIMED[item.key](world, v)) if item.key in CLAIMED else gross
    low, high = item.achievable
    keep = (1.0 - item.risk_discount) * allowed

    def net(share: float) -> float:
        return round(gross * share * keep - running, 0)

    return {
        "key": item.key,
        "title": item.title,
        "problem": item.problem,
        "claimed_annual_gbp": round(claimed, 0),
        "gross_annual_gbp": round(gross, 0),
        "running_cost_gbp": round(running, 0),
        "achievable": [low, high],
        "risk_discount": item.risk_discount,
        "allowed_share": round(allowed, 4),
        "net_annual_gbp": net((low + high) / 2),
        "value_range_gbp": [net(low), net(high)],
        "data_readiness": item.data_readiness,
        "regulatory_risk": item.regulatory_risk,
        "months_to_value": item.months_to_value,
        "blockers": list(item.blockers),
        "must_cite": list(item.must_cite),
    }


def value_models(world: dict, v: dict) -> list[dict]:
    return [value_model(item, world, v) for item in OPPORTUNITIES]
