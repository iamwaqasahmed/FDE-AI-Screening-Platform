"""Week 5 gold: the re-plan, the public line, and the tasks an agent has to walk.

`build` returns the JSON payload, the backlog frame, and the sweep frame.
Export writes `truth/gold/agent.json`, `agent_backlog.parquet`, and `agent_sweep.parquet`.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.eval.agent import (
    backlog,
    baselines,
    business,
    governance,
    questions_approval,
    questions_control,
    questions_injection,
    questions_person,
    questions_plan,
    questions_resume,
    questions_scope,
    questions_veto,
    replan,
    sweep,
    text,
    truth,
)
from simulation.eval.agent.bars import SWEEP_COLUMNS, TODAY
from simulation.eval.graph import cohort, links, reconcile
from simulation.world.clock import iso


def build(world: dict) -> tuple[dict, pd.DataFrame, pd.DataFrame]:
    linked = links.prepare(world, reconcile.frame(world))
    cohort_items, _resend = cohort.facts(world, linked)
    items, backlog_frame = _items(world, linked)
    cases = _cases(world, items, linked, cohort_items)
    items["veto_evidence"] = _evidence(cases)
    rated = baselines.rates(world, cases)
    payload = {
        "as_of": iso(TODAY),
        "questions": cases,
        "baselines": rated,
        "items": items,
        "truth": truth.facts(world, items),
        "text": text.facts(items, rated, _counts(world, items, cohort_items)),
    }
    return _plain(payload), backlog_frame, _published(linked)


def _items(world: dict, linked: dict) -> tuple[dict, pd.DataFrame]:
    items: dict = {}
    items.update(replan.facts(world))
    backlog_items, frame = backlog.facts(world)
    items.update(backlog_items)
    items.update(business.facts(world))
    items.update(governance.facts(world))
    sweep_items, _frame = sweep.facts(linked)
    items.update(sweep_items)
    return items, frame


def _cases(world: dict, items: dict, linked: dict, cohort_items: dict) -> list[dict]:
    pilot_count = cohort_items["pilot_scope_lost"]["local_ids"]
    return (
        questions_plan.cases(items)
        + questions_person.cases(world, linked["chase"])
        + questions_scope.cases(items, pilot_count)
        + questions_veto.cases(world)
        + questions_approval.cases(world, items, cohort_items["resend_summary"])
        + questions_injection.cases(world)
        + questions_resume.cases(world, _sweep_frame(linked))
        + questions_control.cases(world)
    )


def _sweep_frame(linked: dict):
    _summary, frame = sweep.facts(linked)
    return frame


def _evidence(cases: list[dict]) -> dict:
    veto = [case for case in cases if case["slice"] == "veto"]
    families = {case["expected"]["reason"] for case in veto}
    return {"stop_tasks": len(veto), "families": len(families), "wilson_lower": truth.wilson(len(veto), len(veto))}


def _counts(world: dict, items: dict, cohort_items: dict) -> dict:
    hidden = world["gold"].get("integration", {}).get("overdue_chase_letters_lost", 0)
    return {
        "lost_in_bound": items["sweep_summary"]["rows"],
        "pilot_lost": cohort_items["pilot_scope_lost"]["local_ids"],
        "hidden_lost": hidden,
    }


def _published(linked: dict) -> pd.DataFrame:
    _summary, frame = sweep.facts(linked)
    return frame[list(SWEEP_COLUMNS)].reset_index(drop=True)


def _plain(value):
    if isinstance(value, dict):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(item) for item in value]
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.floating,)):
        return round(float(value), 4)
    if isinstance(value, np.bool_):
        return bool(value)
    return value
