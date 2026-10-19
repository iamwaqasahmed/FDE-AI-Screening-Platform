"""The vendor pilot cohort: primary-care captures from the vendor start date, sent to the vendor cloud."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.world.clock import VENDOR_START, iso
from simulation.world.quotas import PILOT_IMAGES


def stamp_pilot(events: pd.DataFrame, rng: np.random.Generator) -> None:
    pool = events.index[
        events["capture"].eq("shared_folder")
        & events["cohort"].eq("completed")
        & events["photo_date"].ge(iso(VENDOR_START))
    ].to_numpy()
    chosen = rng.choice(pool, size=min(PILOT_IMAGES, len(pool)), replace=False) if len(pool) else []
    events["pilot"] = False
    events.loc[chosen, "pilot"] = True
    events.loc[chosen, "capture"] = "vendor_cloud"
