"""Vendor scores for the 400-image primary-care pilot."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def write_vendor_scores(tables: dict[str, pd.DataFrame], handover_dir: Path) -> None:
    vendor = tables["vendor_score"]
    export = pd.DataFrame(
        {
            "FILE_NAME": vendor["file_name"],
            "GRADER_LABEL": vendor["grader_label"],
            "MODEL_LABEL": vendor["model_label"],
            "MODEL_SCORE": vendor["model_score"],
        }
    )
    export.to_csv(handover_dir / "vendor_scores.csv", index=False)
