"""The vendor retrospective set: every scored capture, the signed grade, and why vendor and grader disagree."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.care.grading import latent_severity
from simulation.devices.quality import POOR_OPERATOR
from simulation.ml.keys import age_at, age_band, capture_refs, grader_referable, is_graded
from simulation.ml.vendor_model import LABEL_CUTS

REFER_CUT = LABEL_CUTS[1][0]
HANDOVER_COLUMNS = {
    "capture_ref": "capture_ref",
    "file_name": "file_name",
    "photo_date": "capture_date",
    "site": "site",
    "device_id": "device_id",
    "firmware": "firmware",
    "operator": "operator_code",
    "quality_shown": "quality_shown",
    "age_band": "age_band",
    "vendor_score": "vendor_score",
    "vendor_label": "vendor_label",
    "grade": "grader_label",
    "grader_initials": "grader_initials",
}


def scored_frame(events: pd.DataFrame) -> pd.DataFrame:
    """Every vendor-scored capture with the derived columns the other ML modules share."""
    frame = events[events["vendor_scored"]].copy()
    frame["capture_ref"] = capture_refs(frame)
    frame["age"] = age_at(frame)
    frame["age_band"] = age_band(frame["age"].to_numpy())
    frame["severity"] = latent_severity(frame)
    frame["vendor_referable"] = frame["vendor_score"].to_numpy() >= REFER_CUT
    frame["grader_referable"] = grader_referable(frame["grade"])
    frame["has_grader_label"] = is_graded(frame["grade"])
    return frame.sort_values("capture_ref").reset_index(drop=True)


def handover_frame(scored: pd.DataFrame) -> pd.DataFrame:
    frame = scored[list(HANDOVER_COLUMNS)].rename(columns=HANDOVER_COLUMNS)
    return frame.assign(vendor_score=scored["vendor_score"].round(3).astype(object).where(scored["vendor_score"].notna(), ""))


def truth_frame(scored: pd.DataFrame) -> pd.DataFrame:
    frame = scored[["capture_ref", "event_id", "person_uid", "file_name", "grader_id", "quality", "true_level", "true_macula", "true_referable"]].copy()
    frame["severity"] = scored["severity"]
    frame["vendor_referable"] = scored["vendor_referable"]
    frame["grader_referable"] = scored["grader_referable"]
    frame["vendor_error_cause"] = vendor_cause(scored)
    frame["grader_error_cause"] = grader_cause(scored)
    frame["disagreement_reason"] = disagreement_reason(scored, frame["vendor_error_cause"].to_numpy())
    return frame


def vendor_cause(scored: pd.DataFrame) -> np.ndarray:
    truth = scored["true_referable"].to_numpy()
    called = scored["vendor_referable"].to_numpy()
    missed, over = truth & ~called, ~truth & called
    shift = scored["firmware_score_shift"].to_numpy()
    low_quality = scored["quality"].to_numpy() < 0.6
    borderline = (scored["severity"].to_numpy() > 1) & (scored["severity"].to_numpy() <= 2)
    miss_causes = [
        (scored["age"].to_numpy() >= 75, "age_75_plus_penalty"),
        ((scored["operator"] == POOR_OPERATOR).to_numpy(), "operator_penalty"),
        (shift < 0, "firmware_shift_down"),
        (scored["model_vendor_bias"].to_numpy() < 0, "device_bias"),
        (low_quality, "low_quality"),
        (borderline, "borderline_severity"),
    ]
    over_causes = [(shift > 0, "firmware_shift_up"), (low_quality, "low_quality"), (scored["severity"].to_numpy() >= 1, "borderline_severity")]
    out = np.where(missed | over, "model_noise", "").astype(object)
    out = _apply(out, missed, miss_causes)
    out = _apply(out, over, over_causes)
    return np.where(scored["vendor_score"].isna().to_numpy(), "rejected_quality", out)


def _apply(out: np.ndarray, rows: np.ndarray, causes: list) -> np.ndarray:
    for mask, label in reversed(causes):
        out = np.where(rows & mask, label, out)
    return out


def grader_cause(scored: pd.DataFrame) -> np.ndarray:
    truth = scored["true_referable"].to_numpy()
    called = scored["grader_referable"].to_numpy()
    grade = scored["grade"].to_numpy()
    out = np.where(truth & ~called, "grader_miss", np.where(~truth & called, "grader_over_call", "")).astype(object)
    out = np.where(grade == "U", "ungradable", out)
    return np.where(grade == "", "not_graded", out)


def disagreement_reason(scored: pd.DataFrame, cause: np.ndarray) -> np.ndarray:
    vendor = scored["vendor_referable"].to_numpy()
    grader = scored["grader_referable"].to_numpy()
    truth = scored["true_referable"].to_numpy()
    out = np.where(vendor == grader, "agree", np.where(vendor == truth, "grader_wrong", "vendor_wrong:")).astype(object)
    out = np.where(out == "vendor_wrong:", "vendor_wrong:" + cause.astype(str), out)
    out = np.where(scored["grade"].to_numpy() == "U", "grader_ungradable", out)
    out = np.where(scored["grade"].to_numpy() == "", "no_grader_label", out)
    return np.where(scored["vendor_score"].isna().to_numpy(), "vendor_rejected", out)
