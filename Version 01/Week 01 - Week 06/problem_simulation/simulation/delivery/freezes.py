"""Release and change-freeze calendar per system. Freezes come from the shared timeline."""

from __future__ import annotations

import pandas as pd

from simulation.delivery.plan import RELEASE_SYSTEMS, release_windows
from simulation.world.timeline import happenings


def freeze_calendar() -> pd.DataFrame:
    rows = [
        {"system": item.system, "kind": "freeze", "ref": item.ref, "start": item.start.isoformat(),
         "end": item.end.isoformat() if item.end else "", "note": f"{item.title}. {item.cause}. {item.effect}."}
        for item in happenings(kind="freeze")
    ]
    for system in RELEASE_SYSTEMS:
        for day in release_windows(system):
            rows.append({"system": system, "kind": "release_window", "ref": "", "start": day.isoformat(),
                         "end": day.isoformat(), "note": "Monthly release window"})
    return pd.DataFrame(rows).sort_values(["system", "start", "kind"]).reset_index(drop=True)
