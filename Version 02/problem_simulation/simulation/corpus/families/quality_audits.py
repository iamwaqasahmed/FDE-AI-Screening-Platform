"""Quarterly grading quality audits. The spreadsheet holds per-grader agreement; the text only names the overall rate."""

from __future__ import annotations

import random

import numpy as np
import pandas as pd

from simulation.corpus.add import Extra, add_composed
from simulation.corpus.families.common import percent, pick, quarter_of, quarters
from simulation.prose import FactSpec
from simulation.prose.spec import facts
from simulation.workforce.graders import ROSTER

FAMILY = "quality-audits"
NAMES = {grader.grader_id: grader.name for grader in ROSTER}


def build(world: dict, rng: np.random.Generator) -> None:
    events = world["events"]
    second = events[events["second_grade"] != ""].copy()
    second["quarter"] = quarter_of(second["second_graded_at"])
    second["agree"] = second["second_grade"] == second["grade"]
    gold = world["gold"].setdefault("table_only_facts", [])
    for year, quarter, day in quarters():
        rows = second[second["quarter"] == f"{year}q{quarter}"]
        if len(rows) < 10:
            continue
        table, lowest = _table(rows)
        doc_id = f"quality-audit-{year}q{quarter}"
        spec = FactSpec(
            doc_id=doc_id,
            family=FAMILY,
            title=f"Grading quality audit {year} Q{quarter}",
            facts=facts(reads=len(rows), agreement=percent(int(rows["agree"].sum()), len(rows))),
            sections=("Scope", "Result"),
            length_words=140,
        )
        add_composed(world, spec, _draft, day, extra=Extra(original="xlsx", table=table))
        gold.append({"doc_id": doc_id, "lowest_grader": lowest, "table": table[1:]})


def _table(rows: pd.DataFrame) -> tuple[list[list[str]], str]:
    grouped = rows.groupby("grader_id")["agree"].agg(["size", "mean"]).sort_index()
    table = [["Grader", "Name", "Second reads", "Agreement %"]]
    for grader_id, row in grouped.iterrows():
        table.append([grader_id, NAMES.get(grader_id, "agency"), str(int(row["size"])), f"{100 * row['mean']:.1f}"])
    eligible = grouped[grouped["size"] >= 5]
    lowest = str(eligible["mean"].idxmin()) if not eligible.empty else ""
    return table, lowest


def _draft(spec: FactSpec, rng: random.Random) -> str:
    v = spec.values()
    return "\n\n".join(
        [
            "## Scope",
            pick(rng, f"The audit covered {v['reads']} second reads taken this quarter.",
                 f"A sample of {v['reads']} graded sets was read again by a second grader."),
            "## Result",
            pick(rng, f"First and second grades agreed in {v['agreement']} per cent of sets.",
                 f"Overall agreement was {v['agreement']} per cent."),
            "Per-grader results are in the attached spreadsheet and are discussed with each grader privately.",
        ]
    )
