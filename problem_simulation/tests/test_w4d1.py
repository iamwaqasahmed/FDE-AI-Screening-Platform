"""Day 1 of Week 4: the attack window, the breach clock, and the first requests."""

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
from alwaha.demo.letter import main as demo_main
from alwaha.engagement.interview import run
from alwaha.engagement.personas import load_personas
from alwaha.engagement.w4d1 import gold
from alwaha.engagement.w4d1_rows import CASE_AT
from alwaha.paths import W4D1_APP, W4D1_ROOT, W4D1_WORK
from alwaha.release.fingerprint import fingerprint
from alwaha.release.w3d5 import write_w3d5
from alwaha.release.w4d1 import write_w4d1

_CISO = [
    "How does a security review happen?",
    "What checklist does the security office use at go-live?",
    "What is in the integration engine log since the change?",
]
_APP = ("guard.py", "output.py", "supply.py", "redact.py", "limit.py", "access.py", "erase.py", "fair.py")


def _blob(pack: Path) -> str:
    chunks = []
    for path in pack.rglob("*"):
        if path.is_file():
            chunks.append(path.read_text(encoding="utf-8"))
    return "\n".join(chunks)


def _suite(folder: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
        cwd=folder,
        capture_output=True,
        text=True,
        check=False,
    )


class ReleaseTests(unittest.TestCase):
    def test_same_seed_matches_and_day_5_stays(self) -> None:
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            truth = root / "truth"
            write_w3d5(profile, root / "w3d5", truth)
            before = fingerprint(root / "w3d5")
            first = write_w4d1(profile, root / "w4d1", truth)
            again = write_w4d1(profile, root / "w4d1", truth)
            self.assertEqual(first, again)
            self.assertEqual(before, fingerprint(root / "w3d5"))
            self.assertTrue((truth / "w4d1_gold.json").is_file())
            self.assertFalse((root / "w4d1" / "w4d1_gold.json").exists())

    def test_profiles_differ_and_the_canary_stays_out(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_w4d1(practice, root / "practice" / "pack", root / "practice-truth")
            write_w4d1(small, root / "small" / "pack", root / "small-truth")
            practice_blob = _blob(root / "practice" / "pack")
            small_blob = _blob(root / "small" / "pack")
            self.assertNotIn(practice.canary(), practice_blob)
            self.assertNotIn(small.canary(), small_blob)
            self.assertNotIn("hid-prompt", practice_blob)
            self.assertNotIn("circ-hours-old", practice_blob)
            self.assertNotEqual(
                (root / "practice" / "pack" / "fairness" / "outcomes.jsonl").read_text(encoding="utf-8"),
                (root / "small" / "pack" / "fairness" / "outcomes.jsonl").read_text(encoding="utf-8"),
            )
            self.assertEqual(
                (root / "practice" / "pack" / "fairness" / "bound.json").read_text(encoding="utf-8"),
                (root / "small" / "pack" / "fairness" / "bound.json").read_text(encoding="utf-8"),
            )
            practice_gold = json.loads((root / "practice-truth" / "w4d1_gold.json").read_text(encoding="utf-8"))
            small_gold = json.loads((root / "small-truth" / "w4d1_gold.json").read_text(encoding="utf-8"))
            self.assertEqual(practice_gold, gold(practice))
            self.assertEqual(small_gold, gold(small))
            self.assertNotEqual(practice_gold["fairness"], small_gold["fairness"])
            self.assertLessEqual(practice_gold["fairness"]["gap"], practice_gold["bound"])
            self.assertLessEqual(small_gold["fairness"]["gap"], small_gold["bound"])
            self.assertGreater(practice_gold["fairness"]["gap"], 0)
            self.assertIn(CASE_AT, (root / "practice" / "pack" / "notices" / "phi-logs.md").read_text(encoding="utf-8"))
            dev = (root / "practice" / "pack" / "attacks" / "dev.jsonl").read_text(encoding="utf-8")
            self.assertIn("atk-direct", dev)
            self.assertNotIn("atk-prompt", dev)

    def test_the_interview_reaches_the_checklist_and_the_log(self) -> None:
        turns = run(load_personas()["ciso"], _CISO)
        released = [fact_id for turn in turns for fact_id in turn["released"]]
        self.assertEqual(released, ["checklist", "engine-log"])

    def test_demo_prints_the_unguarded_booking(self) -> None:
        profile = load("practice")
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "practice"])
        text = stdout.getvalue()
        self.assertEqual(text.splitlines(), ["atk-indirect", "the letter booked a slot"])
        self.assertNotIn("ignore", text)
        self.assertNotIn(profile.canary(), text)

    def test_lessons_do_not_state_the_canary(self) -> None:
        lessons = []
        for path in W4D1_ROOT.rglob("*"):
            if path.is_file() and path.suffix in {".md", ".py", ".yml", ".yaml", ".json", ".txt"}:
                lessons.append(path.read_text(encoding="utf-8"))
        self.assertNotIn(load("practice").canary(), "\n".join(lessons))

    def test_modules_differ_and_both_copies_pass(self) -> None:
        for name in _APP:
            shell = (W4D1_APP / name).read_bytes()
            filled = (W4D1_WORK / "app" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        work = _suite(W4D1_WORK)
        shell = _suite(W4D1_APP.parent)
        self.assertEqual(work.returncode, 0, work.stdout + work.stderr)
        self.assertEqual(shell.returncode, 0, shell.stdout + shell.stderr)


if __name__ == "__main__":
    unittest.main()
