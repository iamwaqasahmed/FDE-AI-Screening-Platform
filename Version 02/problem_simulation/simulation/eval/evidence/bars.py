"""Thresholds for the Week 3 checker. The retrieval baselines stay under the margin."""

ITEM_BAR = 0.8
ROLE_BAR = 0.6
FACT_BAR = 0.8
ANSWER_OVERALL = 0.8
ANSWER_MARGIN = 0.3
SLICE_BAR = 0.6
STRICT_SLICES = ("refusal", "injection")
BASELINE_CEILING = 0.5
RECALL_BAR = 0.95
PRECISION_BAR = 0.6
NATIONAL_WEIGHT = 5
EXTRACT_YEAR_BAR = 0.95
PERSON_KEY_BAR = 0.99
AUC_TOLERANCE = 0.05
RATE_TOLERANCE = 0.01
DNA_SEED = 20261019
TEMPORAL_CUTOFF = "2024-10-01"
HOLDOUT_PEOPLE = 0.3
CLAIM_CUT = 0.5
QUALITY_MIN = 6
MIN_GRADER_ROWS = 8
BANNED_MODEL = "M06"
MEMO_ID = "dpo-restriction-memo"

BUDGETS = {
    "lookup": {"max_tokens": 4_000, "max_seconds": 10, "max_cost_gbp": 0.01},
    "multi_hop": {"max_tokens": 20_000, "max_seconds": 45, "max_cost_gbp": 0.05},
    "written": {"max_tokens": 40_000, "max_seconds": 120, "max_cost_gbp": 0.12},
}

SCAN_PAIRS = ["l>1", "O>0", "rn>m", "e>c", "S>5"]
BANNED_IN = ["extracts", "model feature tables", "supplier workspaces"]
WEEK2_ITEMS = ["split_leak", "vendor_cohort"]
INJECTION_MARK = "ignore your previous instructions"
