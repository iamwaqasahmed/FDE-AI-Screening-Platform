"""Regenerate the Hartland screening world into data/."""

from __future__ import annotations

import shutil
from pathlib import Path

import numpy as np
import pandas as pd

from problem_simulation.src.config_loader import PKG_ROOT, REPO_ROOT, load_config
from problem_simulation.src.eval_cases import write_eval
from problem_simulation.src.events import build_events
from problem_simulation.src.exporters import export_handover
from problem_simulation.src.outcomes import assign_outcomes
from problem_simulation.src.pilot import add_pilot
from problem_simulation.src.population import build_population
from problem_simulation.src.truth import write_truth
from problem_simulation.src.validate import validate


def main() -> None:
    cfg = load_config()
    rng = np.random.default_rng(cfg["seed"])
    print("Building population...")
    people = build_population(cfg, rng)
    print("Stamping outcomes...")
    people = assign_outcomes(people, cfg, rng)
    print("Building visits and letters...")
    tables = build_events(people, cfg, rng)
    print("Building pilot scores...")
    tables = add_pilot(tables, cfg, rng)
    data_root = REPO_ROOT / "data"
    print("Writing truth...")
    write_truth(tables, data_root / "truth")
    export_handover(tables, cfg, data_root / "handover")
    print("Copying corpus...")
    _copy_corpus(cfg, data_root / "corpus")
    print("Writing eval cases...")
    write_eval(tables, cfg, data_root / "eval")
    validate(REPO_ROOT)


def _copy_corpus(cfg: dict, dest: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    source = PKG_ROOT / "corpus"
    rows = []
    for doc in cfg["corpus"]:
        text = (source / doc["filename"]).read_text(encoding="utf-8")
        (dest / doc["filename"]).write_text(text, encoding="utf-8")
        rows.append(doc)
    pd.DataFrame(rows).to_csv(dest / "manifest.csv", index=False)


if __name__ == "__main__":
    main()
