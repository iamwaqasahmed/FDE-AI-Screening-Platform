"""Day 4 of Week 3: the benchmark, the campaign, and the judge."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from alwaha.config.profile import load
from alwaha.demo.judge import main as demo_main
from alwaha.engagement.interview import run
from alwaha.engagement.personas import load_personas
from alwaha.engagement.w3d4 import gold
from alwaha.engagement.w3d4_judge import HELD_DOC, HELD_SPAN
from alwaha.paths import W3D4_APP, W3D4_ROOT, W3D4_TEMPLATES, W3D4_WORK
from alwaha.release.fingerprint import fingerprint
from alwaha.release.w3d3 import write_w3d3
from alwaha.release.w3d4 import write_w3d4

_CDO = [
    "When does the board want the service live?",
    "Is an eye-screening campaign coming, and does the session plan still use last year's months?",
]
_APP = (
    "score.py",
    "forecast.py",
    "failures.py",
    "judge.py",
    "intervals.py",
    "experiment.py",
    "gate.py",
)
_TESTS = (
    "test_score.py",
    "test_forecast.py",
    "test_failures.py",
    "test_judge.py",
    "test_intervals.py",
    "test_experiment.py",
    "test_gate.py",
)
_TYPES = ("hallucination", "retrieval", "reasoning", "workflow")


def _blob(pack: Path) -> str:
    chunks = []
    for path in pack.rglob("*"):
        if path.is_file():
            chunks.append(path.read_text(encoding="utf-8"))
    return "\n".join(chunks)


def _canary_count(pack: Path, canary: str) -> int:
    total = 0
    for path in pack.rglob("*"):
        if path.is_file():
            total += path.read_text(encoding="utf-8").count(canary)
    return total


class ReleaseTests(unittest.TestCase):
    def test_same_seed_matches_and_day_3_stays(self) -> None:
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            truth = root / "truth"
            write_w3d3(profile, root / "w3d3", truth)
            before = fingerprint(root / "w3d3")
            first = write_w3d4(profile, root / "w3d4", truth)
            again = write_w3d4(profile, root / "w3d4", truth)
            self.assertEqual(first, again)
            self.assertEqual(before, fingerprint(root / "w3d3"))
            self.assertTrue((truth / "w3d4_gold.json").is_file())
            self.assertFalse((root / "w3d4" / "w3d4_gold.json").exists())

    def test_profiles_differ_and_the_canary_stays_out(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_w3d4(practice, root / "practice" / "pack", root / "practice-truth")
            write_w3d4(small, root / "small" / "pack", root / "small-truth")
            self.assertEqual(_canary_count(root / "practice" / "pack", practice.canary()), 0)
            self.assertEqual(_canary_count(root / "small" / "pack", small.canary()), 0)
            self.assertNotEqual(fingerprint(root / "practice" / "pack"), fingerprint(root / "small" / "pack"))
            practice_gold = json.loads((root / "practice-truth" / "w3d4_gold.json").read_text(encoding="utf-8"))
            small_gold = json.loads((root / "small-truth" / "w3d4_gold.json").read_text(encoding="utf-8"))
            self.assertEqual(practice_gold, gold(practice))
            self.assertEqual(small_gold, gold(small))
            self.assertNotEqual(practice_gold["later_visits"], small_gold["later_visits"])

    def test_the_pack_keeps_labels_and_the_effect_out(self) -> None:
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            write_w3d4(profile, pack, root / "truth")
            hidden = json.loads((root / "truth" / "w3d4_gold.json").read_text(encoding="utf-8"))
            blob = _blob(pack)
            note = (pack / "notices" / "campaign.md").read_text(encoding="utf-8")
            self.assertIn(hidden["case_date"], note)
            for row in hidden["later_visits"]:
                self.assertNotIn(str(row["visits"]), note)
            self.assertNotIn("winner", (pack / "notices" / "ab-status.md").read_text(encoding="utf-8"))
            self.assertNotIn('"label"', (pack / "slices" / "score.jsonl").read_text(encoding="utf-8"))
            failure_text = (pack / "slices" / "failures.jsonl").read_text(encoding="utf-8")
            for name in _TYPES:
                self.assertNotIn(name, failure_text)
            held = hidden["calibration_held"][0]
            self.assertNotIn(held["answer"], blob)
            self.assertNotIn(HELD_SPAN, blob)
            self.assertNotIn(HELD_DOC, blob)
            self.assertNotIn(profile.canary(), blob)
            self.assertGreaterEqual(hidden["metrics"]["extraction"], hidden["budgets"]["extraction"])
            self.assertEqual(hidden["ab_status"]["winner"], "clause")
            self.assertEqual(hidden["ab_status"]["peek_winner"], "short")


class DemoTests(unittest.TestCase):
    def test_demo_names_the_miss_and_not_the_item(self) -> None:
        profile = load("practice")
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "practice"])
        text = stdout.getvalue()
        hidden = gold(profile)
        self.assertEqual(
            text.splitlines(),
            ["the judge marked the citation correct", "the citation is not the in-force document"],
        )
        held = hidden["calibration_held"][0]
        self.assertNotIn(held["answer"], text)
        self.assertNotIn(held["span"], text)
        self.assertNotIn(held["doc_id"], text)
        self.assertNotIn(profile.canary(), text)

    def test_lessons_do_not_state_the_held_item(self) -> None:
        notes = [path.read_text(encoding="utf-8") for path in W3D4_ROOT.glob("*.md")]
        notes.extend(path.read_text(encoding="utf-8") for path in W3D4_TEMPLATES.glob("*.md"))
        lesson_text = "\n".join(notes)
        hidden = gold(load("practice"))
        held = hidden["calibration_held"][0]
        self.assertNotIn(load("practice").canary(), lesson_text)
        self.assertNotIn(held["answer"], lesson_text)
        self.assertNotIn(held["span"], lesson_text)

    def test_modules_differ_and_only_the_copy_passes(self) -> None:
        packet = W3D4_APP.parent
        for name in _APP:
            shell = (W3D4_APP / name).read_bytes()
            filled = (W3D4_WORK / "app" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        for name in _TESTS:
            shell = (packet / "tests" / name).read_bytes()
            filled = (W3D4_WORK / "tests" / name).read_bytes()
            self.assertEqual(shell, filled, name)
        shell_ci = (packet / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
        work_ci = (W3D4_WORK / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
        self.assertIn("# evaluation-gate:", shell_ci)
        self.assertIn("\n  evaluation-gate:\n", work_ci)
        work = _suite(W3D4_WORK)
        shell = _suite(packet)
        self.assertEqual(work.returncode, 0, work.stdout + work.stderr)
        self.assertNotEqual(shell.returncode, 0, shell.stdout + shell.stderr)

    def test_the_campaign_question_is_not_a_week_1_fact(self) -> None:
        personas = load_personas()
        turns = run(personas["cdo"], _CDO)
        self.assertEqual(turns[1]["released"], ["eye-campaign"])
        self.assertFalse(any(char.isdigit() for char in turns[1]["answer"]))
        self.assertEqual(personas["cdo"]["must_surface"], ("gpu-lead-time",))


def _suite(folder: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
        cwd=folder,
        capture_output=True,
        text=True,
        check=False,
    )


if __name__ == "__main__":
    unittest.main()
