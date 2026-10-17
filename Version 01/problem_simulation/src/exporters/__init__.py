"""Write the authority handover from the truth tables."""

from __future__ import annotations

from pathlib import Path

from problem_simulation.src.exporters.grader_workbook import write_grader_workbook
from problem_simulation.src.exporters.letters import write_letters
from problem_simulation.src.exporters.pacs_manifest import write_pacs_manifest
from problem_simulation.src.exporters.readme_and_dictionary import write_readme_and_dictionary
from problem_simulation.src.exporters.referrals import write_referrals
from problem_simulation.src.exporters.registry import write_registry
from problem_simulation.src.exporters.rows import screening_rows
from problem_simulation.src.exporters.shared_folder import write_shared_folder
from problem_simulation.src.exporters.vendor_scores import write_vendor_scores


def export_handover(tables: dict, cfg: dict, handover_dir: Path) -> None:
    handover_dir.mkdir(parents=True, exist_ok=True)
    print("Writing registry, manifests, and vendor scores...")
    write_registry(tables["person"], cfg, handover_dir)
    write_pacs_manifest(tables, handover_dir)
    write_shared_folder(tables, cfg, handover_dir)
    write_vendor_scores(tables, handover_dir)
    write_readme_and_dictionary(handover_dir)
    print("Building grader rows...")
    rows = screening_rows(tables)
    print("Writing grader workbook, letters, and referrals...")
    write_grader_workbook(rows, handover_dir)
    write_letters(rows, tables, cfg, handover_dir)
    write_referrals(rows, tables, handover_dir)
