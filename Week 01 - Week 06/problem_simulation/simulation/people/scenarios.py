"""Planted people scenarios beyond aliases: twins, silent movers, and households."""

from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd

from simulation.world.clock import iso
from simulation.world.quotas import SILENT_MOVERS, TWIN_PAIRS

SILENT_FIRST = date(2019, 3, 1)
SILENT_LAST = date(2026, 6, 1)


def mark_twins(people: pd.DataFrame) -> None:
    """Pairs with the same surname, date of birth, and postcode sector. Different people."""
    pool = people.index[(people["district"] == "East City") & (people["flag"] == "") & (people["scenario"] == "")].to_numpy()
    rows = pool[: TWIN_PAIRS * 2]
    for start in range(0, len(rows) - 1, 2):
        left, right = rows[start], rows[start + 1]
        for column in ("surname", "dob", "postcode_sector", "home_site", "diagnosis_date"):
            people.at[right, column] = people.at[left, column]
        if people.at[right, "forename"] == people.at[left, "forename"]:
            people.at[right, "forename"] = people.at[right, "forename"] + "a"
        people.loc[[left, right], "scenario"] = "twin"
        people.loc[[left, right], "household"] = f"H-T{start // 2:04d}"


def mark_silent_movers(people: pd.DataFrame, rng: np.random.Generator) -> None:
    """People who left the area and told no one. The register keeps them, so the rule still counts them."""
    people["silent_move_on"] = ""
    pool = people.index[(people["flag"] == "") & (people["scenario"] == "") & (people["reuse_role"] == "")].to_numpy()
    chosen = rng.choice(pool, size=min(SILENT_MOVERS, len(pool)), replace=False)
    span = (SILENT_LAST - SILENT_FIRST).days
    for row_id in chosen:
        people.at[row_id, "silent_move_on"] = iso(SILENT_FIRST + timedelta(days=int(rng.integers(0, span))))


def assign_households(people: pd.DataFrame, rng: np.random.Generator) -> None:
    """Some people share a household, and with it a landline or family mobile."""
    if "household" not in people:
        people["household"] = ""
    labels = people["household"].to_numpy(dtype=object).copy()
    postcode = people["postcode_sector"].to_numpy(dtype=object).copy()
    number = 0
    for district in sorted(people["district"].unique()):
        open_rows = np.flatnonzero((people["district"] == district).to_numpy() & (labels == ""))
        order = rng.permutation(open_rows)
        sizes = rng.choice([1, 1, 1, 2, 2, 3], size=len(order))
        cursor = 0
        while cursor < len(order):
            members = order[cursor : cursor + int(sizes[cursor])]
            postcode[members] = postcode[members[0]]
            labels[members] = f"H{number:06d}"
            number += 1
            cursor += len(members)
    people["household"] = labels
    people["postcode_sector"] = postcode
    people["has_phone"] = rng.random(len(people)) >= 0.15
