"""Week 3 gold: retrieval questions, the restricted cohort, and the note a team has to write.

`build` returns the JSON payload and the vendor-extract frame. Export writes
`truth/gold/evidence.json` and `truth/gold/evidence_extract.parquet`.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.devices.inventory import inventory_frame
from simulation.eval.evidence import (
    baselines,
    claims,
    corpus,
    dna,
    drift,
    drop,
    governance,
    labels,
    overdue,
    questions_corpus,
    questions_injection,
    questions_policy,
    redaction,
    text,
    truth,
    vendor,
)
from simulation.eval.evidence.pdftext import pdf_text
from simulation.eval.evidence.rates import clean
from simulation.ml.retrospective import handover_frame, scored_frame


def build(world: dict) -> tuple[dict, pd.DataFrame]:
    cases = questions_policy.cases(world) + questions_corpus.cases(world) + questions_injection.cases(world)
    full = clean(handover_frame(scored_frame(world["events"])))
    items = {**drop.facts(world, full["site"].unique()), **corpus.facts(world), **governance.facts(world)}
    allowed = items["drop_restriction"]["allowed_sites"]
    kept, joined = vendor.cohort(world, allowed)
    items["vendor_scope"] = vendor.scope(kept, joined, items["drop_restriction"]["removed_sites"])
    items["reference_gap"] = vendor.gap(kept, joined)
    items["operating_points"] = vendor.points(joined)
    items["label_noise"] = labels.noise(kept, joined)
    items["firmware_drift"] = drift.firmware(full, inventory_frame(True), allowed)
    located = claims.locate(world["rendered"], _pdf(world))
    items["claims"] = claims.judge(items["operating_points"], located["claimed"], located["source"],
                                   located["stopped_document"], located["postmortem"], located["injection_document"])
    items["dna_leak"] = dna.scores(world["files"]["handover/ml/dna_training.csv"])
    items["overdue_pilot_scope"] = overdue.count(world, allowed)
    rated = baselines.rates(world, cases)
    payload = {
        "as_of": items["drop_restriction"]["effective"],
        "questions": cases,
        "baselines": rated,
        "items": items,
        "redaction": redaction.spans(world),
        "latent": truth.latent(world, allowed),
        "text": text.facts(items, rated),
    }
    return _plain(payload), vendor.extract_frame(world, allowed)


def _pdf(world: dict) -> bytes:
    return world["files"]["corpus/proposals/originals/proposal-retinalytics-2026.pdf"]


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
