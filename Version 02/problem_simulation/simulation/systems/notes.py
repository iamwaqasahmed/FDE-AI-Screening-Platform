"""Interface notes, the owner register, and the breast boundary page."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from simulation.systems.catalog import OWNERS, SYSTEMS


def write_interfaces(folder: Path) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    for system in SYSTEMS:
        lines = [
            f"# {system['name']}",
            "",
            f"Trust zone: {system['trust_zone']}",
            "",
            f"Interface: {system['interface']}",
            "",
            f"System of record for: {system['system_of_record_for']}",
            "",
            f"Known defect: {system['known_defect']}",
            "",
            f"Hosting: {system['hosting']}",
            "",
            f"Classification: {system['classification']}",
            "",
            f"Files: handover/{system['folder']}",
            "",
        ]
        (folder / f"{system['system_id']}.md").write_text("\n".join(lines), encoding="utf-8")


def write_owners(path: Path) -> None:
    frame = pd.DataFrame(OWNERS, columns=["role", "name"])
    frame.to_csv(path, index=False)


def write_breast(folder: Path) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    text = (
        "Breast programme\n\n"
        "This folder is not a cohort. There are no breast rows, no breast images, and no breast grades.\n"
        "A clinical answer for the breast programme cannot be produced from the eye-screening drop.\n"
    )
    (folder / "README.txt").write_text(text, encoding="utf-8")
