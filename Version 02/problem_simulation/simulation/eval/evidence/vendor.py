"""The restricted cohort, the two references, and the operating points the model card asks for."""

from __future__ import annotations

import pandas as pd

from simulation.eval.evidence.bars import CLAIM_CUT, QUALITY_MIN
from simulation.eval.evidence.rates import clean, point, sensitivity
from simulation.ml.retrospective import handover_frame, scored_frame
from simulation.systems.resolve import ids_on
from simulation.world.clock import SNAPSHOT, iso


def cohort(world: dict, allowed: list[str]) -> tuple[pd.DataFrame, pd.DataFrame]:
    frame = clean(handover_frame(scored_frame(world["events"])))
    sample = clean(world["tables"]["ml_adjudicated"])
    kept = frame[frame["site"].isin(allowed)].reset_index(drop=True)
    joined = sample.merge(kept, on="capture_ref", how="inner")
    return kept, joined


def scope(frame: pd.DataFrame, joined: pd.DataFrame, removed: list[str]) -> dict:
    rejected = int(frame["vendor_label"].eq("").sum())
    return {"captures": int(len(frame)), "rejected": rejected, "adjudicated": int(len(joined)), "removed_sites": list(removed)}


def gap(frame: pd.DataFrame, joined: pd.DataFrame) -> dict:
    _, _, routine = sensitivity(frame, "grader_label")
    _, _, adjudicated = sensitivity(joined, "adjudicated_label")
    return {
        "cut": CLAIM_CUT,
        "rejected": int(frame["vendor_label"].eq("").sum()),
        "routine": routine,
        "adjudicated": adjudicated,
        "gap": round(adjudicated - routine, 3),
    }


def points(joined: pd.DataFrame) -> dict:
    bands = joined["age_band"].astype(str)
    quality = joined["quality_shown"]
    return {
        "all": point(joined, "adjudicated_label"),
        "age_75_plus": point(joined[bands.eq("75+")], "adjudicated_label"),
        "age_under_75": point(joined[~bands.eq("75+")], "adjudicated_label"),
        "claim_population": point(joined[(~bands.eq("75+")) & (quality >= QUALITY_MIN)], "adjudicated_label"),
        "sites": {site: point(group, "adjudicated_label") for site, group in sorted(joined.groupby("site"), key=lambda item: item[0])},
    }


def extract_frame(world: dict, allowed: list[str]) -> pd.DataFrame:
    base = scored_frame(world["events"])
    base = base[base["site"].isin(allowed)]
    local = ids_on(world["identifiers"], "local_pid", iso(SNAPSHOT))
    frame = pd.DataFrame({
        "capture_ref": base["capture_ref"].astype(str),
        "site": base["site"].astype(str),
        "capture_date": base["photo_date"].astype(str),
        "local_pid": base["person_uid"].map(local).fillna("").astype(str),
        "year_of_birth": base["dob"].astype(str).str.slice(0, 4),
    })
    return frame.sort_values("capture_ref").reset_index(drop=True)
