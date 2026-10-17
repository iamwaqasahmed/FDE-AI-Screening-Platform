"""Named accounts keep access: their revocation or disable dates are never written."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.faults import record


def apply(frame: pd.DataFrame, rng: np.random.Generator, params: dict) -> tuple[pd.DataFrame, dict]:
    """params: accounts (ids), key (account column), clear (columns blanked), set ({column: value}), only (optional row mask column)."""
    key = params.get("key", "account_id")
    hit = frame[key].isin(list(params["accounts"]))
    only = params.get("only", "")
    if only:
        hit &= frame[only].astype(bool)
    out = frame.copy()
    cleared = {}
    for column in params.get("clear", ()):
        cleared[column] = int((hit & (out[column] != "")).sum())
        out[column] = np.where(hit, "", out[column])
    for column, value in params.get("set", {}).items():
        out[column] = np.where(hit, value, out[column])
    if only:
        out = out.drop(columns=[only])
    return out, record("stale_account", accounts=sorted(params["accounts"]), rows=int(hit.sum()), cleared=cleared)
