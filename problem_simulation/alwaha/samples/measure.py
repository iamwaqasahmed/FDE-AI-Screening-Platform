"""Recompute the four printed baselines from a rel-m01-l02 pack.

The pack's sample files are scored with the participant baseline modules. The result maps each problem id to the figure that baseline prints, and also keeps the row-split accuracy, the shared-person count, and the mean demand error.
"""

from __future__ import annotations

from pathlib import Path

from alwaha.samples.script import load_baseline


def measure_pack(pack: Path) -> dict[str, str | int]:
    """Return the baseline figures for the sample files under this pack.

    p-dna is the person split. dna_row is the row split. dna_shared is how many people cross that row split. p-status is the keyword share. p-bounce is the filled-letter count. p-forecast is the seasonal error, and demand_mean is the earlier-average error.
    """
    # Load the four baseline modules that score the sample files.
    dna = load_baseline("dna.py")
    messages = load_baseline("messages.py")
    letters = load_baseline("letters.py")
    demand = load_baseline("demand.py")
    # Read the sample tables and the letter file from this pack.
    dna_rows = dna.load_rows(pack / "samples" / "ds-dna.csv")
    message_rows = messages.load_rows(pack / "samples" / "ds-messages.csv")
    letter_text = (pack / "samples" / "ds-letters.md").read_text(encoding="utf-8")
    demand_rows = demand.load_rows(pack / "samples" / "ds-demand.csv")
    # Person split, keyword share, filled letters, seasonal error, and the three extra figures.
    return {
        "p-dna": dna.show(dna.score(dna_rows, "person")),
        "p-status": messages.show(messages.rate(message_rows)),
        "p-bounce": str(letters.filled(letter_text)),
        "p-forecast": demand.show(demand.seasonal(demand_rows)),
        "dna_row": dna.show(dna.score(dna_rows, "row")),
        "dna_shared": dna.shared(dna_rows),
        "demand_mean": demand.show(demand.mean_error(demand_rows)),
    }
