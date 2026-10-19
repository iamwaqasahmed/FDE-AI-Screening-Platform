"""True operating points of the vendor at its cut points, by subgroup, against latent disease and against the grader."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.devices.quality import POOR_OPERATOR
from simulation.ml.vendor_model import LABEL_CUTS
from simulation.world.clock import FIRMWARE_MARKET, FIRMWARE_RIVER, iso
from simulation.world.sites import MARKET, RIVER_SITE

CUTS = tuple(cut for cut, _ in LABEL_CUTS)
REFERENCES = ("true_referable", "grader_label")


def subgroups(scored: pd.DataFrame) -> dict[str, np.ndarray]:
    day = scored["photo_date"].to_numpy()
    site = scored["site"].to_numpy()
    groups = {
        "all": np.ones(len(scored), dtype=bool),
        "age_75_plus": scored["age"].to_numpy() >= 75,
        "age_under_75": scored["age"].to_numpy() < 75,
        f"operator_{POOR_OPERATOR}": (scored["operator"] == POOR_OPERATOR).to_numpy(),
        "operator_other": (scored["operator"] != POOR_OPERATOR).to_numpy(),
        "market_4.2.0_after_upgrade": (site == MARKET) & (scored["firmware"] == "4.2.0").to_numpy() & (day >= iso(FIRMWARE_MARKET)),
        "river_before_upgrade": (site == RIVER_SITE) & (day < iso(FIRMWARE_RIVER)),
        "river_3.1.0_after_upgrade": (site == RIVER_SITE) & (scored["firmware"] == "3.1.0").to_numpy() & (day >= iso(FIRMWARE_RIVER)),
        "favourable": favourable(scored),
    }
    for value in sorted(scored["site"].unique()):
        groups[f"site:{value}"] = site == value
    for year in sorted(scored["photo_date"].str[:4].unique()):
        groups[f"period:{year}"] = scored["photo_date"].str[:4].to_numpy() == year
    return groups


def favourable(scored: pd.DataFrame) -> np.ndarray:
    """Captures with none of the penalties: under 75, a trained operator, no downward firmware shift, good quality."""
    return (
        (scored["age"].to_numpy() < 75)
        & (scored["operator"] != POOR_OPERATOR).to_numpy()
        & (scored["firmware_score_shift"].to_numpy() >= 0)
        & (scored["model_vendor_bias"].to_numpy() >= 0)
        & (scored["quality"].to_numpy() >= 0.6)
    )


def operating_points(scored: pd.DataFrame) -> pd.DataFrame:
    score = scored["vendor_score"].to_numpy()
    usable = ~np.isnan(score)
    references = {"true_referable": (scored["true_referable"].to_numpy(), usable), "grader_label": (scored["grader_referable"].to_numpy(), usable & scored["has_grader_label"].to_numpy())}
    rows = []
    for name, mask in subgroups(scored).items():
        for reference, (label, valid) in references.items():
            for cut in CUTS:
                rows.append(_point(name, reference, cut, score, label, mask & valid, int((mask & ~usable).sum())))
    return pd.DataFrame(rows)


def _point(subgroup: str, reference: str, cut: float, score: np.ndarray, label: np.ndarray, mask: np.ndarray, rejected: int) -> dict:
    called = np.where(mask, score >= cut, False)
    truth = label & mask
    positives, negatives = int(truth.sum()), int((mask & ~label).sum())
    true_pos, true_neg = int((called & truth).sum()), int((~called & mask & ~label).sum())
    flagged = int(called.sum())
    return {
        "subgroup": subgroup,
        "reference": reference,
        "cut": cut,
        "n": int(mask.sum()),
        "rejected": rejected,
        "positives": positives,
        "sensitivity": round(true_pos / positives, 4) if positives else np.nan,
        "specificity": round(true_neg / negatives, 4) if negatives else np.nan,
        "ppv": round(true_pos / flagged, 4) if flagged else np.nan,
    }


def lookup(points: pd.DataFrame, subgroup: str, reference: str = "true_referable", cut: float = CUTS[1], metric: str = "sensitivity") -> float:
    row = points[(points["subgroup"] == subgroup) & (points["reference"] == reference) & (points["cut"] == cut)]
    return float(row[metric].iloc[0]) if len(row) else float("nan")
