"""Latent sensitivity on the restricted cohort. The debrief quotes it. The drop does not contain it."""

from __future__ import annotations

from simulation.eval.evidence.bars import CLAIM_CUT
from simulation.ml.retrospective import scored_frame


def latent(world: dict, allowed: list[str]) -> dict:
    frame = scored_frame(world["events"])
    frame = frame[frame["site"].isin(allowed) & frame["vendor_score"].notna()]
    truth = frame["true_referable"].astype(bool)
    called = frame["vendor_score"].to_numpy() >= CLAIM_CUT
    positives = int(truth.sum())
    caught = int((called & truth.to_numpy()).sum())
    return {"sensitivity": round(caught / positives, 4) if positives else 0.0, "positives": positives, "cut": CLAIM_CUT}
