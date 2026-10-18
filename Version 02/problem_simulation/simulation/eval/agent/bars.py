"""Thresholds for the Week 5 checker. The single-loop agent stays under the margin."""

from __future__ import annotations

from simulation.architecture.model_register import MODELS
from simulation.eval.evidence.bars import BUDGETS
from simulation.world.engagement import WEEKS

ITEM_BAR = 0.8
ROLE_BAR = 0.6
FACT_BAR = 0.8
ANSWER_OVERALL = 0.8
ANSWER_MARGIN = 0.3
SLICE_BAR = 0.6
STRICT_SLICES = ("veto", "injection", "approval", "resume")
BASELINE_CEILING = 0.5
COST_TOLERANCE = 0.001
WILSON_TOLERANCE = 0.01
PACE_TOLERANCE = 0.1
CLOCK_DAY_TOLERANCE = 1.0
MONEY_TOLERANCE = 1.0
WILSON_Z = 1.96
TODAY = WEEKS[5]
PERSON_QUESTIONS = 10
VETO_TASKS = 11
MULTI_HOP_INPUT = 16_000
MULTI_HOP_OUTPUT = 4_000
PERSONAL_MODELS = tuple(row[0] for row in MODELS if "official-sensitive" in row[6])
BANNED_MODEL = "M06"
SWEEP_COLUMNS = ("local_pid", "request_id", "hospital", "clause_id", "days_over")
BACKLOG_COLUMNS = ("ticket_id", "duplicate_of", "missing_criteria", "blocked_by")

__all__ = ["BUDGETS", "TODAY"]
