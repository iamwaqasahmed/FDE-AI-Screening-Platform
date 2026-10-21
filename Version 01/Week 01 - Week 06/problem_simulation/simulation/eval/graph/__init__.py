"""Week 4 gold: the bureau reconciliation, the graph questions, and the incident note.

`build` returns the JSON payload and the reconciliation frame. Export writes
`truth/gold/graph.json` and `truth/gold/graph_reconciliation.parquet`.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.eval.graph import (
    baselines,
    calls,
    cohort,
    cost,
    drop,
    governance,
    links,
    questions_chain,
    questions_control,
    questions_guard,
    questions_incident,
    questions_path,
    reconcile,
    text,
    truth,
)
from simulation.world.clock import iso
from simulation.world.engagement import WEEKS


def build(world: dict) -> tuple[dict, pd.DataFrame]:
    reconciled = reconcile.frame(world)
    linked = links.prepare(world, reconciled)
    cohort_items, resend = cohort.facts(world, linked)
    items = {**drop.facts(world, reconciled), **cohort_items, **governance.facts(world, linked)}
    items.update(calls.facts(world))
    items.update(cost.facts(items, resend))
    cases = (
        questions_path.cases(world, linked)
        + questions_chain.cases(world)
        + questions_incident.cases(world, items)
        + questions_control.cases(world)
        + questions_guard.cases(world)
    )
    rated = baselines.rates(world, cases)
    payload = {
        "as_of": iso(WEEKS[4]),
        "questions": cases,
        "baselines": rated,
        "items": items,
        "resend": resend,
        "truth": truth.facts(world, items, reconciled),
        "text": text.facts(items, rated),
    }
    return _plain(payload), reconciled


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
