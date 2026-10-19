"""A lead-grader adjudicated sample of the retrospective set, and the label noise each grader carries."""

from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd

from simulation.care.grading import CODES
from simulation.devices.quality import UNGRADABLE_BELOW
from simulation.ml.keys import grader_referable, is_graded
from simulation.workforce.graders import LEAD, ROSTER, sigma_on
from simulation.world.clock import SNAPSHOT

SAMPLE_SHARE = 0.05


def adjudicated_sample(scored: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    """The lead re-reads about one in twenty routinely graded captures, blind to the routine grade."""
    pool = scored[scored["grade"].ne("").to_numpy()]
    count = max(int(round(SAMPLE_SHARE * len(scored))), 1)
    picked = pool.iloc[np.sort(rng.choice(len(pool), size=min(count, len(pool)), replace=False))]
    days = [_review_day(value, int(offset)) for value, offset in zip(picked["graded_at"], rng.integers(7, 42, len(picked)))]
    labels = lead_read(picked, days, rng)
    return pd.DataFrame(
        {
            "capture_ref": picked["capture_ref"].to_numpy(),
            "file_name": picked["file_name"].to_numpy(),
            "routine_label": picked["grade"].to_numpy(),
            "routine_grader": picked["grader_initials"].to_numpy(),
            "adjudicated_label": labels,
            "adjudicator": LEAD.initials,
            "adjudicated_at": [day.isoformat() for day in days],
        }
    )


def _review_day(graded_at: str, offset: int) -> date:
    return min(date.fromisoformat(graded_at) + timedelta(days=offset), SNAPSHOT - timedelta(days=1))


def lead_read(rows: pd.DataFrame, days: list[date], rng: np.random.Generator) -> np.ndarray:
    sigma = np.array([sigma_on(LEAD, day, 0.0) for day in days])
    quality = rows["quality"].to_numpy()
    blur = 1 + 1.5 * np.clip(0.6 - quality, 0, None)
    reading = rows["severity"].to_numpy() + LEAD.bias + rng.normal(0, 1, len(rows)) * sigma * blur
    codes = CODES[np.clip(np.rint(reading), 0, 3).astype(int)]
    return np.where(quality < UNGRADABLE_BELOW, "U", codes)


def noise_by_grader(scored: pd.DataFrame, sample: pd.DataFrame) -> list[dict]:
    """Referable-call error against latent disease for every grader, plus the adjudicated sample as one row."""
    graded = scored[is_graded(scored["grade"])]
    names = {grader.initials: grader.name for grader in ROSTER}
    rows = [_noise_row(initials, names.get(initials, ""), group["true_referable"].to_numpy(), grader_referable(group["grade"]))
            for initials, group in graded.groupby("grader_initials", sort=True)]
    rows.append(_noise_row("all_routine", "", graded["true_referable"].to_numpy(), grader_referable(graded["grade"])))
    truth = scored.set_index("capture_ref")["true_referable"]
    usable = sample[is_graded(sample["adjudicated_label"])]
    rows.append(_noise_row("adjudicated", LEAD.name, truth.loc[usable["capture_ref"]].to_numpy(), grader_referable(usable["adjudicated_label"])))
    both = sample[is_graded(sample["adjudicated_label"]) & is_graded(sample["routine_label"])]
    rows[-1]["routine_vs_adjudicated_disagreement"] = round(float(np.mean(grader_referable(both["routine_label"]) != grader_referable(both["adjudicated_label"]))), 4) if len(both) else 0.0
    return rows


def _noise_row(initials: str, name: str, truth: np.ndarray, called: np.ndarray) -> dict:
    positives, negatives = int(truth.sum()), int((~truth).sum())
    return {
        "grader": initials,
        "name": name,
        "n": int(len(truth)),
        "noise_rate": round(float(np.mean(truth != called)), 4) if len(truth) else 0.0,
        "miss_rate": round(float(np.sum(truth & ~called) / positives), 4) if positives else 0.0,
        "over_call_rate": round(float(np.sum(~truth & called) / negatives), 4) if negatives else 0.0,
    }
