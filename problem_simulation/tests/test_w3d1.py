"""Day 1 of Week 3: the history, the guideline, and the fidelity card."""

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
from alwaha.demo.merge import main as demo_main
from alwaha.engagement.interview import run
from alwaha.engagement.personas import load_personas
from alwaha.engagement.w3d1 import gold
from alwaha.paths import W3D1_APP, W3D1_ROOT
from alwaha.release.day2 import write_day2
from alwaha.release.day3 import write_day3
from alwaha.release.day4 import write_day4
from alwaha.release.day5 import write_day5
from alwaha.release.fingerprint import fingerprint
from alwaha.release.w2d1 import write_w2d1
from alwaha.release.w2d2 import write_w2d2
from alwaha.release.w2d3 import write_w2d3
from alwaha.release.w2d4 import write_w2d4
from alwaha.release.w2d5 import write_w2d5
from alwaha.release.w3d1 import write_w3d1
from alwaha.release.write import write_release

_DPO = [
    "How should we handle patient data?",
    "Is the data request for the full history approved, or is it only a sample?",
]
_COORD = [
    "Is the queue the problem?",
    "What sits in the note?",
    "How do clerk labels and the guideline treat a photo?",
]
_APP = (
    "dates.py",
    "codes.py",
    "cluster.py",
    "labels.py",
    "synthetic.py",
    "scan.py",
    "pit.py",
    "budget.py",
)


def _canary_count(pack: Path, canary: str) -> int:
    total = 0
    for path in pack.rglob("*"):
        if path.is_file():
            total += path.read_text(encoding="utf-8").count(canary)
    return total


def _prose(pack: Path) -> str:
    chunks = []
    for path in pack.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".yaml", ".yml"}:
            chunks.append(path.read_text(encoding="utf-8"))
    return "\n".join(chunks)


class ReleaseTests(unittest.TestCase):
    def test_same_seed_matches_and_earlier_days_stay(self) -> None:
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            packs = [root / f"day{index}" for index in range(1, 6)]
            truth = root / "truth"
            write_release(profile, packs[0], truth)
            write_day2(profile, packs[1], truth)
            write_day3(profile, packs[2], truth)
            write_day4(profile, packs[3], truth)
            write_day5(profile, packs[4], truth)
            week2 = [root / f"w2d{index}" for index in range(1, 6)]
            write_w2d1(profile, week2[0], truth)
            write_w2d2(profile, week2[1], truth)
            write_w2d3(profile, week2[2], truth)
            write_w2d4(profile, week2[3], truth)
            write_w2d5(profile, week2[4], truth)
            before = (
                tuple(fingerprint(pack) for pack in packs),
                tuple(fingerprint(pack) for pack in week2),
                (truth / "personas.json").read_bytes(),
                (truth / "w2d5_gold.json").read_bytes(),
            )
            first = write_w3d1(profile, root / "w3d1", truth)
            again = write_w3d1(profile, root / "w3d1", truth)
            self.assertEqual(first, again)
            self.assertEqual(
                before,
                (
                    tuple(fingerprint(pack) for pack in packs),
                    tuple(fingerprint(pack) for pack in week2),
                    (truth / "personas.json").read_bytes(),
                    (truth / "w2d5_gold.json").read_bytes(),
                ),
            )
            self.assertTrue((truth / "w3d1_gold.json").is_file())
            self.assertFalse((root / "w3d1" / "w3d1_gold.json").exists())

    def test_profiles_differ_by_canary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_w3d1(practice, root / "practice", root / "practice-truth")
            write_w3d1(small, root / "small", root / "small-truth")
            self.assertEqual(_canary_count(root / "practice", practice.canary()), 1)
            self.assertEqual(_canary_count(root / "small", small.canary()), 1)
            self.assertNotEqual(fingerprint(root / "practice"), fingerprint(root / "small"))

    def test_prose_keeps_the_secrets_out(self) -> None:
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            write_w3d1(profile, pack, root / "truth")
            hidden = json.loads((root / "truth" / "w3d1_gold.json").read_text(encoding="utf-8"))
            prose = _prose(pack)
            self.assertEqual(hidden, gold(profile))
            self.assertNotIn(profile.canary(), json.dumps(hidden))
            for secret in (profile.canary(), *hidden["national_ids"], *hidden["dates"].values()):
                self.assertNotIn(secret, prose)
            self.assertEqual(_canary_count(pack, profile.canary()), 1)
            self.assertIn(profile.canary(), (pack / "letters" / "clerk.jsonl").read_text(encoding="utf-8"))


class DemoTests(unittest.TestCase):
    def test_demo_prints_two_mrns_and_one_national_id(self) -> None:
        profile = load("practice")
        hidden = gold(profile)
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "practice"])
        text = stdout.getvalue()
        shown = hidden["demo"]
        expected = [shown["mrn_mother"], shown["mrn_newborn"], shown["national_id"], "These two MRNs stay two people."]
        self.assertEqual(text.splitlines(), expected)
        self.assertNotIn(profile.canary(), text)
        for converted in hidden["dates"].values():
            self.assertNotIn(converted, text)

    def test_lessons_do_not_state_the_gregorian_date(self) -> None:
        lessons = []
        for path in W3D1_ROOT.rglob("*"):
            if not path.is_file() or "work" in path.parts:
                continue
            if path.suffix in {".md", ".py", ".yml", ".yaml"}:
                lessons.append(path.read_text(encoding="utf-8"))
        lesson_text = "\n".join(lessons)
        hidden = gold(load("small"))
        self.assertNotIn(load("small").canary(), lesson_text)
        for secret in (*hidden["national_ids"], *hidden["dates"].values()):
            self.assertNotIn(secret, lesson_text)

    def test_modules_differ_and_both_suites_pass(self) -> None:
        for name in _APP:
            shell = (W3D1_APP / name).read_bytes()
            filled = (W3D1_ROOT / "work" / "app" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        for folder in (W3D1_ROOT, W3D1_ROOT / "work"):
            completed = subprocess.run(
                [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
                cwd=folder,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)

    def test_dpo_and_coord_lead_add_no_required_fact(self) -> None:
        personas = load_personas()
        dpo = personas["dpo"]
        turns = run(dpo, _DPO)
        self.assertEqual(turns[0]["released"], [])
        self.assertEqual(turns[1]["released"], [])
        self.assertIn("full history is approved", turns[1]["answer"])
        self.assertEqual(dpo["must_surface"], ("unsigned-ruling",))
        coord = personas["coord-lead"]
        turns = run(coord, _COORD)
        self.assertEqual(turns[2]["released"], [])
        self.assertIn("phone photo", turns[2]["answer"])
        self.assertEqual(coord["must_surface"], ("shorthand", "thursday", "v4-draft"))


if __name__ == "__main__":
    unittest.main()
