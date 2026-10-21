"""Scanned and printed result letters. Gold holds the character span of every personal detail."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.corpus.add import Extra, add_document
from simulation.world.clock import parse
from simulation.world.sites import slug
from simulation.world.staff import name

FAMILY = "patient-letters"
SAMPLE = 220
OUTCOME = {
    "R0": "Your photographs did not show changes that need a hospital appointment. We will invite you again next year.",
    "R1": "Your photographs showed small changes. These do not need a hospital appointment. We will invite you again.",
    "R2": "Your photographs showed changes that need a closer look. We have asked the hospital eye clinic to see you.",
    "R3": "Your photographs showed changes that need a closer look soon. We have asked the hospital eye clinic to see you.",
}


def build(world: dict, rng: np.random.Generator) -> None:
    sample = _sample(world, rng)
    for row in sample.itertuples(index=False):
        doc_id = f"letter-{row.event_id.lower()}"
        body = _body(row)
        pii = [{"kind": "name", "value": f"{row.forename} {row.surname}"}, {"kind": "dob", "value": row.dob},
               {"kind": "postcode", "value": row.postcode_sector}]
        if row.national:
            pii.append({"kind": "national_id", "value": row.national})
        if row.screening:
            pii.append({"kind": "screening_no", "value": row.screening})
        original = "scan" if int(row.event_id[-1]) % 3 == 0 else "pdf"
        add_document(world, doc_id, FAMILY, f"Screening result letter {row.site}", body, parse(row.letter_at),
                     row.site, Extra(original=original, pii=pii))


def _sample(world: dict, rng: np.random.Generator) -> pd.DataFrame:
    events = world["events"]
    pool = events[(events["letter_at"] != "") & events["grade"].isin(list(OUTCOME))]
    picked = pool.iloc[np.sort(rng.choice(len(pool), size=min(SAMPLE, len(pool)), replace=False))]
    ids = world["identifiers"]
    national = _first(ids[(ids["system"] == "national-spine") & (ids["relation"] == "assigned")], "national")
    screening = _first(ids[ids["system"] == "screening"], "screening")
    frame = picked[["event_id", "person_uid", "forename", "surname", "dob", "postcode_sector", "site", "letter_at", "grade"]]
    frame = frame.merge(national, on="person_uid", how="left")
    return frame.merge(screening, on="person_uid", how="left").fillna("")


def _first(ids: pd.DataFrame, column: str) -> pd.DataFrame:
    rows = ids[ids["id_value"] != ""].drop_duplicates("person_uid")
    return rows[["person_uid", "id_value"]].rename(columns={"id_value": column})


def _body(row) -> str:
    lines = [
        f"{row.forename} {row.surname}",
        f"Date of birth: {row.dob}",
        f"Postcode area: {row.postcode_sector}",
    ]
    if row.national:
        lines.append(f"National id: {row.national}")
    if row.screening:
        lines.append(f"Screening number: {row.screening}")
    lines += [
        "",
        f"Dear {row.forename} {row.surname},",
        "",
        f"Thank you for attending diabetic eye screening at {row.site}.",
        "",
        OUTCOME[row.grade],
        "",
        "If you have questions, call the screening office and quote your screening number.",
        "",
        f"{name('programme_manager')}, Screening Programme Manager",
        f"Reference: {slug(row.site)}/{row.event_id}",
    ]
    return "\n".join(lines)
