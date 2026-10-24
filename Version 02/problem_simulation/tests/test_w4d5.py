"""Day 5 of Week 4: the three connections and the rehearsal proposal."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from alwaha.config.profile import load
from alwaha.demo.benefit import main as demo_main
from alwaha.engagement.interview import run
from alwaha.engagement.personas import load_personas
from alwaha.engagement.w4d5 import gold
from alwaha.engagement.w4d5_rows import attack
from alwaha.paths import W4D5_APP, W4D5_ROOT
from alwaha.release.fingerprint import fingerprint
from alwaha.release.w4d4 import write_w4d4
from alwaha.release.w4d5 import write_w4d5

_APP = ("signin.py", "bus.py", "handoff.py", "leave.py", "warehouse.py", "rank.py", "gates.py", "personal.py")
_ANSWER = "count the same calls"
_TEXT = {".md", ".py", ".yml", ".yaml", ".json", ".txt"}


def _blob(pack: Path) -> str:
    chunks = []
    for path in pack.rglob("*"):
        if path.is_file():
            chunks.append(path.read_text(encoding="utf-8"))
    return "\n".join(chunks)


def _lines(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _bare(text: str, number: int) -> bool:
    return re.search(rf"(?<!\d){number}(?!\d)", text) is not None


def _suite(folder: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
        cwd=folder,
        capture_output=True,
        text=True,
        check=False,
    )


class ReleaseTests(unittest.TestCase):
    def test_same_seed_matches_and_day_4_stays(self) -> None:
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            truth = root / "truth"
            write_w4d4(profile, root / "w4d4", truth)
            before = fingerprint(root / "w4d4")
            first = write_w4d5(profile, root / "w4d5", truth)
            again = write_w4d5(profile, root / "w4d5", truth)
            self.assertEqual(first, again)
            self.assertEqual(before, fingerprint(root / "w4d4"))
            self.assertTrue((truth / "w4d5_gold.json").is_file())
            self.assertFalse((root / "w4d5" / "w4d5_gold.json").exists())

    def test_profiles_differ_and_the_counts_stay_out(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_w4d5(practice, root / "practice" / "pack", root / "practice-truth")
            write_w4d5(small, root / "small" / "pack", root / "small-truth")
            practice_blob = _blob(root / "practice" / "pack")
            small_blob = _blob(root / "small" / "pack")
            practice_gold = json.loads((root / "practice-truth" / "w4d5_gold.json").read_text(encoding="utf-8"))
            small_gold = json.loads((root / "small-truth" / "w4d5_gold.json").read_text(encoding="utf-8"))
            self.assertNotIn(practice.canary(), practice_blob)
            self.assertNotIn(small.canary(), small_blob)
            self.assertNotIn("w4d5_gold", practice_blob)
            self.assertNotIn(_ANSWER, practice_blob)
            self.assertFalse(_bare(practice_blob, practice_gold["leave_lag"]))
            self.assertFalse(_bare(practice_blob, practice_gold["phone_only"]))
            self.assertFalse(_bare(small_blob, small_gold["leave_lag"]))
            self.assertFalse(_bare(small_blob, small_gold["phone_only"]))
            self.assertNotEqual(practice_gold["leave_lag"], small_gold["leave_lag"])
            self.assertNotEqual(practice_gold["phone_only"], small_gold["phone_only"])
            self.assertEqual(practice_gold["event"], "session.cancelled")
            self.assertEqual(practice_gold["clock"], "referred_at")
            self.assertEqual(practice_gold, gold(practice))
            self.assertEqual(small_gold, gold(small))
            pack = root / "practice" / "pack"
            model = json.loads((pack / "value" / "model.json").read_text(encoding="utf-8"))
            blocked = [row["id"] for row in model["problems"] if row["blockers"]]
            self.assertEqual(blocked, ["p-triage"])
            self.assertNotIn("sar", practice_blob.lower())
            readme = (pack / "README.md").read_text(encoding="utf-8")
            self.assertIn("2027-02-04", readme)
            self.assertNotIn(attack()["text"], readme)
            self.assertNotIn(str(practice_gold["leave_lag"]), readme)
            self.assertNotIn(str(practice_gold["phone_only"]), readme)

    def test_the_interviews_reach_the_summary_and_the_leave(self) -> None:
        questions = W4D5_ROOT / "work" / "interviews"
        access = run(load_personas()["access-mgr"], _lines(questions / "access-mgr.questions.txt"))
        released = [fact_id for turn in access for fact_id in turn["released"]]
        self.assertEqual(released, ["reason-mix", "handoff-summary"])
        self.assertEqual(load_personas()["access-mgr"]["must_surface"], ("returns-and-slots", "reason-mix"))
        ea = run(load_personas()["ea"], _lines(questions / "ea.questions.txt"))
        released = [fact_id for turn in ea for fact_id in turn["released"]]
        self.assertEqual(released, ["late-leave", "warehouse-bi"])
        self.assertEqual(load_personas()["ea"]["must_surface"], ("ain-file", "hl7-pair"))

    def test_demo_prints_the_question(self) -> None:
        profile = load("practice")
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "practice"])
        text = stdout.getvalue()
        shown = gold(profile)
        self.assertEqual(text.splitlines(), [shown["demo"]["question"]])
        self.assertNotIn(_ANSWER, text)
        self.assertNotIn(str(shown["leave_lag"]), text)
        self.assertNotIn(str(shown["phone_only"]), text)
        self.assertNotIn(attack()["text"], text)
        self.assertNotIn(profile.canary(), text)

    def test_lessons_do_not_state_the_canary_or_the_counts(self) -> None:
        profile = load("practice")
        shown = gold(profile)
        prose = []
        code = []
        for path in W4D5_ROOT.rglob("*"):
            if not path.is_file() or path.suffix not in _TEXT:
                continue
            text = path.read_text(encoding="utf-8")
            code.append(text)
            if path.suffix == ".md":
                prose.append(text)
        notes = "\n".join(prose)
        blob = "\n".join(code)
        self.assertNotIn(profile.canary(), blob)
        self.assertNotIn(attack()["text"], notes)
        self.assertFalse(_bare(notes, shown["leave_lag"]))
        self.assertFalse(_bare(notes, shown["phone_only"]))

    def test_modules_differ_and_both_copies_pass(self) -> None:
        for name in _APP:
            shell = (W4D5_APP / name).read_bytes()
            filled = (W4D5_ROOT / "work" / "app" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        work = _suite(W4D5_ROOT / "work")
        shell = _suite(W4D5_ROOT)
        self.assertEqual(work.returncode, 0, work.stdout + work.stderr)
        self.assertEqual(shell.returncode, 0, shell.stdout + shell.stderr)


if __name__ == "__main__":
    unittest.main()
