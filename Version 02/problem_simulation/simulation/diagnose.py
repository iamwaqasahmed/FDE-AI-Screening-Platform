"""Print the shape of a built world's truth: breaches, lags, grades, attendance. For tuning, not teaching."""

from __future__ import annotations

import sys

import pandas as pd

from simulation.paths import TRUTH


def main() -> None:
    events = pd.read_parquet(TRUTH / "event.parquet")
    print("events", len(events))
    print(events.groupby(events["photo_date"].str[:4])["breach"].value_counts().unstack(fill_value=0))
    print(events.groupby(events["photo_date"].str[:4])["grade_lag"].mean().round(1))
    print(events["grade"].value_counts(normalize=True).round(3))
    graded = events[events["grade"].isin(["R0", "R1", "R2", "R3"])]
    missed = graded["true_referable"] & ~graded["grade"].isin(["R2", "R3"])
    false_pos = ~graded["true_referable"] & graded["grade"].isin(["R2", "R3"])
    print("missed", round(missed.mean(), 3), "false referral", round(false_pos.mean(), 3))
    print("true level mix", events["true_level"].value_counts(normalize=True).sort_index().round(3).to_dict())
    print("fast track", int(events["fast_track"].sum()), "progressed", int(events["progressed_in_delay"].sum()))
    letter = events[events["breach"] == "letter_bureau"]
    print("letter breaches", len(letter), "in migration", int(letter["letter_in_migration"].sum()))
    if len(sys.argv) > 1:
        print(events[sys.argv[1:]].describe(include="all"))


if __name__ == "__main__":
    main()
