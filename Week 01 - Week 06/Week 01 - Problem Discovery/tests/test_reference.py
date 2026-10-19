"""The reference folder passes, and the planted naive readings fail."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SMALL = ROOT / "problem_simulation" / "build" / "data-small"
GOLD = SMALL / "truth" / "gold" / "discovery.json"


def test_reference_passes_and_naive_readings_fail(tmp_path):
    if not GOLD.exists():
        import pytest

        pytest.skip("small build has no discovery gold")
    env = os.environ.copy()
    env["HARTLAND_PROFILE"] = "small"
    _run("reference_discovery", "--data", str(SMALL), "--out", str(tmp_path), "--profile", "small", env=env)
    _run("discovery_check", "--work", str(tmp_path), "--data", str(SMALL), env=env)
    _spoil(tmp_path)
    failed = subprocess.run(
        [sys.executable, "-m", "course", "discovery_check", "--work", str(tmp_path), "--data", str(SMALL), "--rerun"],
        cwd=ROOT,
        env=env,
        check=False,
        capture_output=True,
        text=True,
    )
    assert failed.returncode != 0
    assert "eligible_people" in failed.stdout
    assert "ranking" in failed.stdout
    assert "backlog" in failed.stdout
    assert "reminder" in failed.stdout


def _run(*args, env):
    subprocess.run([sys.executable, "-m", "course", *args], cwd=ROOT, env=env, check=True)


def _spoil(folder: Path) -> None:
    path = folder / "findings.json"
    findings = json.loads(path.read_text(encoding="utf-8"))
    gold = json.loads(GOLD.read_text(encoding="utf-8"))
    items = findings["items"]
    items["eligible_people"]["count"] = gold["eligible"]["warehouse"]
    order = items["ranking"]["order"]
    items["ranking"]["order"] = ["vendor_model_expansion", *[key for key in order if key != "vendor_model_expansion"]]
    items["backlog"]["true"] = items["backlog"]["board"]
    for row in items["reminder"]["districts"].values():
        row["true_uplift"] = row["naive"]
    path.write_text(json.dumps(findings, indent=2) + "\n", encoding="utf-8")
