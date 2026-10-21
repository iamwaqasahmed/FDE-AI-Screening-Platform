"""The eight opportunities: what each claims to fix, how much of it is achievable, and what stands in the way."""

from __future__ import annotations

from dataclasses import dataclass

from simulation.world.clock import BUREAU_MIGRATION_START, INCIDENT_START, REMINDER_CHANGE, ROTA_CHANGE
from simulation.world.engagement import DPO_RESTRICTION


@dataclass(frozen=True)
class Opportunity:
    key: str
    title: str
    problem: str
    achievable: tuple[float, float]
    risk_discount: float
    data_readiness: float
    regulatory_risk: str
    months_to_value: int
    blockers: tuple[str, ...]
    must_cite: tuple[str, ...]


OPPORTUNITIES = (
    Opportunity("grader_triage_ai", "Vendor score to order the primary-care grading queue", "results_delay",
                (0.3, 0.6), 0.3, 0.6, "medium", 9, ("clinical_safety_owner",),
                ("vendor scores exist only for primary-care and outreach captures",
                 f"one grader's accuracy fell after the rota change on {ROTA_CHANGE.isoformat()}")),
    Opportunity("letter_bureau_fix", "Reconcile bureau dispatches and reissue lost letters", "letters",
                (0.6, 0.8), 0.05, 0.8, "low", 4, (),
                (f"the bureau platform migration from {BUREAU_MIGRATION_START.isoformat()} slowed dispatch",
                 f"the duplicate week from {INCIDENT_START.isoformat()} lost letters")),
    Opportunity("reminder_targeting", "Target SMS reminders by district uplift", "missed_appointments",
                (0.4, 0.7), 0.1, 0.5, "low", 6, (),
                (f"the reminder change on {REMINDER_CHANGE.isoformat()} had no control group",
                 "the true uplift differs by district and the naive before-and-after overstates it")),
    Opportunity("identity_resolution", "Resolve people across registry, PACS, lab, and booking ids", "missed_appointments",
                (0.2, 0.4), 0.05, 0.4, "medium", 5, (),
                ("photographs that never reached a grader cluster in Hill Counties and River Districts",
                 "rows are not people: aliases, false merges, and reused registry numbers",
                 "the 2023 merge batch was reversed in 2025")),
    Opportunity("dna_prediction", "Predict did-not-attend to offer earlier contact", "missed_appointments",
                (0.1, 0.2), 0.2, 0.4, "medium", 8, (),
                ("the analyst's table has a feature populated after the outcome",
                 "previous did-not-attend history splits across alias records")),
    Opportunity("fast_track_scheduling", "Schedule fast-track ophthalmology slots", "hospital_wait",
                (0.05, 0.15), 0.1, 0.6, "low", 4, ("consultant_vacancy",),
                ("fast-track clinic slots were cut during the consultant vacancy",
                 "the bottleneck is clinic capacity, not slot allocation")),
    Opportunity("call_deflection", "Self-service answers for contact-centre calls", "letters",
                (0.15, 0.3), 0.1, 0.7, "low", 5, (),
                ("most avoidable calls are about letters that never arrived",
                 "fixing the bureau removes the calls that deflection would count")),
    Opportunity("vendor_model_expansion", "Vendor model grading at every site", "results_delay",
                (0.6, 0.9), 0.6, 0.5, "high", 18, ("clinical_safety_owner", "dpo_restriction"),
                (f"the DPO restriction from {DPO_RESTRICTION.isoformat()} keeps hospital studies away from the vendor",
                 "the vendor model is weaker for people aged 75 and over",
                 "the pilot stays stopped until a clinical safety owner is named")),
)

BY_KEY = {item.key: item for item in OPPORTUNITIES}

BLOCKERS = {
    "clinical_safety_owner": "No clinical safety owner is named, so the pilot stays stopped",
    "dpo_restriction": "The DPO restricts the vendor to primary-care captures and bans a field",
    "consultant_vacancy": "The consultant vacancy cut fast-track capacity; scheduling cannot add slots",
}
