"""Care-path invariants: breach labels, the pilot, hidden urgent codes, and the hidden mechanisms."""

from __future__ import annotations

import pandas as pd

from simulation.world.clock import BUREAU_MIGRATION_END, BUREAU_MIGRATION_START, NCEC_ADOPT, iso
from simulation.world.quotas import PILOT_IMAGES
from simulation.world.sites import NCEC


def check(world: dict, errors: list[str]) -> None:
    events = world["events"]
    labels = set(events.loc[events["breach"] != "", "breach"].unique())
    if labels != {"grader_backlog", "letter_bureau", "booking"}:
        errors.append(f"Breach labels are {sorted(labels)}")
    if events["pilot"].sum() != PILOT_IMAGES:
        errors.append(f"Pilot images {int(events['pilot'].sum())} != {PILOT_IMAGES}")
    if not events["grade_hidden"].any():
        errors.append("No grade was left only in the note text.")
    if not events["letter_duplicate"].any():
        errors.append("The letter incident week has no dispatches.")
    adopted = events[(events["site"] == NCEC) & (events["photo_date"] >= iso(NCEC_ADOPT))]
    if adopted["specialist_clause"].eq("spec-ncec").sum() != len(adopted):
        errors.append(f"{NCEC} events after adoption do not all use the local clause.")
    _hidden(events, errors)


def _hidden(events: pd.DataFrame, errors: list[str]) -> None:
    graded = events[events["grade"].isin(["R0", "R1", "R2", "R3"])]
    if graded.empty:
        errors.append("No graded events.")
        return
    missed = graded["true_referable"] & ~graded["grade"].isin(["R2", "R3"])
    if not missed.any():
        errors.append("No missed referable disease against the latent state.")
    if missed.mean() > 0.25:
        errors.append(f"Missed disease rate {missed.mean():.2f} is implausibly high.")
    letter = events[events["breach"] == "letter_bureau"]
    in_migration = letter["graded_at"].between(iso(BUREAU_MIGRATION_START), iso(BUREAU_MIGRATION_END))
    if letter.empty or in_migration.mean() < 0.3:
        errors.append("Letter-bureau breaches do not cluster in the bureau migration.")
    backlog = events[events["breach"] == "grader_backlog"]
    if backlog.empty or backlog["photo_date"].str[:4].value_counts().max() < 0.25 * len(backlog):
        errors.append("Grader-backlog breaches do not cluster in a capacity shortfall.")
    if events["grader_id"].eq("").all():
        errors.append("No grader was assigned.")
    if events.loc[events["grade"] == "U", "quality"].mean() >= events.loc[events["grade"] != "U", "quality"].mean():
        errors.append("Ungradable photographs are not lower quality.")
