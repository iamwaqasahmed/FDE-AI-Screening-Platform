"""Write the research CSVs and summary documents, and record which theme is loudest and which is costliest."""

from __future__ import annotations

from datetime import timedelta

import numpy as np
import pandas as pd

from simulation.corpus.add import add_document
from simulation.stakeholders.queries import summary_for
from simulation.stakeholders.research.calls import call_gold, call_reasons
from simulation.stakeholders.research.observations import add_observations
from simulation.stakeholders.research.surveys import patient_survey, staff_survey, voice_counts
from simulation.world.engagement import KICKOFF

PUBLIC = "engagement/research"


def _summary_doc(world: dict, doc_id: str, title: str, frame: pd.DataFrame, column: str, intro: str) -> str:
    counts = frame[column].value_counts().sort_index()
    lines = [intro, "", "| Theme | Responses |", "|---|---|"]
    lines += [f"| {theme.replace('_', ' ')} | {count} |" for theme, count in counts.items()]
    lines += ["", "Themes were coded from free text by the discovery team. Counts are mentions, not costs."]
    add_document(world, doc_id, "research", title, "\n".join(lines), KICKOFF + timedelta(days=1))
    return doc_id


def _calls_doc(world: dict, calls: pd.DataFrame) -> str:
    yearly = calls.assign(year=calls["month"].str.slice(0, 4)).pivot_table(index="year", columns="reason", values="calls",
                                                                          aggfunc="sum")
    lines = ["Call-centre reason codes by year. Agents often log letter calls as general queries, so the coded "
             "reason undercounts some causes.", "", "| Year | " + " | ".join(c.replace("_", " ") for c in yearly.columns) + " |",
             "|---|" + "---|" * len(yearly.columns)]
    lines += [f"| {year} | " + " | ".join(str(int(v)) for v in row) + " |" for year, row in yearly.iterrows()]
    add_document(world, "research-call-reasons", "research", "Call reasons over time", "\n".join(lines),
                 KICKOFF + timedelta(days=1))
    return "research-call-reasons"


def build_research(world: dict, rng: np.random.Generator) -> dict:
    summary = summary_for(world)
    voiced, costliest = summary["most_voiced_problem"], summary["costliest_problem"]
    staff = staff_survey(voiced, costliest, rng)
    patients = patient_survey(voiced, costliest, rng)
    calls = call_reasons(world, rng)
    world["files"][f"{PUBLIC}/staff_survey.csv"] = staff
    world["files"][f"{PUBLIC}/patient_survey.csv"] = patients
    world["files"][f"{PUBLIC}/call_reasons.csv"] = calls
    docs = [
        _summary_doc(world, "research-staff-survey", "Staff survey summary", staff, "top_problem",
                     "Staff were asked for the one problem that costs the service most."),
        _summary_doc(world, "research-patient-survey", "Patient survey summary", patients, "theme",
                     "Patients were asked what they would most like the service to fix."),
        _calls_doc(world, calls),
        *add_observations(world),
    ]
    counts = voice_counts(staff, patients)
    gold = {
        "most_voiced": max(sorted(counts), key=lambda theme: counts[theme]),
        "voice_counts": counts,
        "costliest": costliest,
        "problem_costs_gbp_per_year": summary["problem_costs"],
        "calls": call_gold(calls),
        "documents": docs,
    }
    world.setdefault("gold", {})["research"] = gold
    return gold
