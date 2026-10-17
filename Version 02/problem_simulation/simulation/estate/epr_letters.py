"""EPR clinic letters as text. The seen date is in the letter even when the referral message left it blank."""

from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd

from simulation.config import active
from simulation.corpus.add import pii_spans
from simulation.estate.common import TRUTH
from simulation.systems.mrn import MrnIndex
from simulation.systems.ophthalmology import shown_referral
from simulation.world.sites import is_hospital
from simulation.world.staff import name

BLANK_SHARE = 0.7
FINDINGS = ("Examination findings are recorded in the hospital record.", "Visual acuity was measured and discussed with the patient.",
            "Imaging was reviewed in clinic with the patient.")
PLANS = ("The clinic will arrange further review.", "Follow-up will be booked by the clinic.", "Discharged back to the screening programme.")


def build_epr_letters(world: dict, rng: np.random.Generator) -> pd.DataFrame:
    chosen = _sample(world, rng)
    rows, spans = [], []
    for index, row in enumerate(chosen.itertuples(index=False), start=1):
        letter_id = f"EPR-{index:06d}"
        body = _letter(row, rng)
        path = f"handover/epr_letters/{letter_id}.txt"
        world["files"][path] = body
        values = {"name": f"{row.forename} {row.surname}", "dob": _dob(row.dob), "mrn": row.mrn}
        spans.extend({"letter_id": letter_id, "file": path, **span} for span in pii_spans(body, values))
        rows.append({"letter_id": letter_id, "file": path, "event_id": row.event_id, "person_uid": row.person_uid,
                     "mrn": row.mrn, "site": row.site, "seen_at": row.seen_at, "message_blank": bool(row.blank)})
    world["gold"].setdefault("pii_epr", []).extend(spans)
    truth = pd.DataFrame(rows)
    world["files"][f"{TRUTH}/epr_letters.parquet"] = truth
    return truth


def _sample(world: dict, rng: np.random.Generator) -> pd.DataFrame:
    events = world["events"]
    pool = events[(events["seen_at"] != "") & events["site"].map(is_hospital)].sort_values("event_id").copy()
    index = MrnIndex(world["identifiers"])
    pool["mrn"] = [index.get(row.person_uid, row.site, row.photo_date) for row in pool.itertuples(index=False)]
    pool = pool[pool["mrn"] != ""]
    pool["blank"] = [shown_referral(row)[1] == "" for row in pool.itertuples(index=False)]
    total = min(len(pool), active().count(200))
    blank, filled = pool[pool["blank"]], pool[~pool["blank"]]
    take_blank = min(len(blank), int(round(total * BLANK_SHARE)))
    take_filled = min(len(filled), total - take_blank)
    parts = [frame.iloc[np.sort(rng.choice(len(frame), take, replace=False))] for frame, take in ((blank, take_blank), (filled, take_filled)) if take]
    return pd.concat(parts).sort_values(["seen_at", "event_id"]) if parts else pool.iloc[:0]


def _letter(row, rng: np.random.Generator) -> str:
    typed = date.fromisoformat(row.seen_at) + timedelta(days=int(rng.integers(2, 11)))
    seen_text = seen_texts(row.seen_at)[0 if rng.random() < 0.6 else 1]
    consultant = name("ophthalmology_lead") if rng.random() < 0.5 else name("clinical_director")
    full = f"{row.forename} {row.surname}"
    grade = row.grade or "a referable grade"
    return (
        f"{row.site} - Ophthalmology Outpatients\nClinic letter\n\nTyped: {typed:%d/%m/%Y}\n\n"
        f"Patient: {full}\nDate of birth: {_dob(row.dob)}\nHospital number: {row.mrn}\n\n"
        f"Dear colleague,\n\nI saw {full} in clinic on {seen_text}, following referral from the diabetic eye screening "
        f"programme ({grade} at screening). {FINDINGS[int(rng.integers(0, len(FINDINGS)))]}\n\n"
        f"{PLANS[int(rng.integers(0, len(PLANS)))]}\n\nYours sincerely,\n\n{consultant}\nConsultant Ophthalmologist\n"
    )


def _dob(value: str) -> str:
    return f"{value[8:10]}/{value[5:7]}/{value[:4]}"


def seen_texts(seen_at: str) -> tuple[str, str]:
    seen = date.fromisoformat(seen_at)
    return f"{seen.day} {seen:%B %Y}", f"{seen:%d/%m/%Y}"
