"""The fifteen flows. Each denied flow cites a document that denies it."""

from __future__ import annotations

import pandas as pd

from simulation.eval.handoff.bars import FLOW_COLUMNS
from simulation.eval.handoff.flows import ROWS


def frame() -> pd.DataFrame:
    rows = [
        {"flow_id": f"F-{index:02d}", "source": source, "target": target, "data": data, "allowed": allowed, "rule": accepted[0]}
        for index, (source, target, data, allowed, accepted) in enumerate(ROWS, start=1)
    ]
    return pd.DataFrame(rows, columns=list(FLOW_COLUMNS))
