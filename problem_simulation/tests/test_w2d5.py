"""Day 5 of Week 2: the release, the change request, and the steering card."""

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
from alwaha.demo.ain import main as demo_main
from alwaha.engagement.interview import run
from alwaha.engagement.personas import load_personas
from alwaha.engagement.w2d5 import CARD, QUESTIONS, gold
from alwaha.paths import W2D5_APP, W2D5_ROOT
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
from alwaha.release.write import write_release

_EA = [
    "Do we have an API strategy?",
    "Does Ain publish a nightly schedule file?",
    "What does a missed night leave, and whose clinic codes are on it?",
]
_SMOKE = (
    "admit.py",
    "health.py",
    "router.py",
    "secrets.py",
    "test_admit.py",
    "test_health.py",
    "test_router.py",
    "test_secrets.py",
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
            week2 = [root / f"w2d{index}" for index in range(1, 5)]
            write_w2d1(profile, week2[0], truth)
            write_w2d2(profile, week2[1], truth)
            write_w2d3(profile, week2[2], truth)
            write_w2d4(profile, week2[3], truth)
            before = (
                tuple(fingerprint(pack) for pack in packs),
                tuple(fingerprint(pack) for pack in week2),
                (truth / "personas.json").read_bytes(),
                (truth / "w2d4_gold.json").read_bytes(),
            )
            first = write_w2d5(profile, root / "w2d5", truth)
            again = write_w2d5(profile, root / "w2d5", truth)
            self.assertEqual(first, again)
            self.assertEqual(
                before,
                (
                    tuple(fingerprint(pack) for pack in packs),
                    tuple(fingerprint(pack) for pack in week2),
                    (truth / "personas.json").read_bytes(),
                    (truth / "w2d4_gold.json").read_bytes(),
                ),
            )
            self.assertTrue((truth / "w2d5_gold.json").is_file())
            self.assertFalse((root / "w2d5" / "w2d5_gold.json").exists())

    def test_profiles_differ_by_canary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_w2d5(practice, root / "practice", root / "practice-truth")
            write_w2d5(small, root / "small", root / "small-truth")
            self.assertEqual(_canary_count(root / "practice", practice.canary()), 1)
            self.assertEqual(_canary_count(root / "small", small.canary()), 1)
            self.assertNotEqual(fingerprint(root / "practice"), fingerprint(root / "small"))

    def test_notice_keeps_the_clinic_code_out(self) -> None:
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            write_w2d5(profile, pack, root / "truth")
            hidden = json.loads((root / "truth" / "w2d5_gold.json").read_text(encoding="utf-8"))
            prose = _prose(pack)
            self.assertEqual(hidden, gold(profile))
            self.assertNotIn(profile.canary(), json.dumps(hidden))
            for secret in (hidden["clinic_code"], hidden["previous_code"], profile.canary()):
                self.assertNotIn(secret, prose)
            nightly = (pack / "fixtures" / "nightly.json").read_text(encoding="utf-8")
            self.assertIn(hidden["clinic_code"], nightly)
            self.assertEqual(_canary_count(pack, profile.canary()), 1)
            self.assertIsNone(re.search(r"nightly", (pack / "notices" / "cr-ain.md").read_text(encoding="utf-8"), re.I))


class DemoTests(unittest.TestCase):
    def test_demo_prints_the_card_without_the_file_sentence(self) -> None:
        profile = load("practice")
        hidden = gold(profile)
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "practice"])
        text = stdout.getvalue()
        expected = [CARD, *[f"{index}. {question}" for index, question in enumerate(QUESTIONS, start=1)]]
        self.assertEqual(text.splitlines(), expected)
        self.assertNotIn("nightly", text.lower())
        self.assertNotIn(hidden["clinic_code"], text)
        self.assertNotIn(profile.canary(), text)

    def test_lessons_do_not_name_the_clinic_code(self) -> None:
        lessons = []
        for path in W2D5_ROOT.rglob("*"):
            if not path.is_file() or "work" in path.parts:
                continue
            if path.suffix in {".md", ".py", ".yml", ".yaml"}:
                lessons.append(path.read_text(encoding="utf-8"))
        lesson_text = "\n".join(lessons)
        hidden = gold(load("small"))
        self.assertNotIn(hidden["clinic_code"], lesson_text)
        self.assertNotIn(hidden["previous_code"], lesson_text)

    def test_only_the_trap_modules_differ(self) -> None:
        for name in ("queue.py", "file_ain.py", "notify.py", "contract.py"):
            shell = (W2D5_APP / name).read_bytes()
            filled = (W2D5_ROOT / "work" / "app" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        for name in _SMOKE:
            folder = "app" if name.endswith(".py") and not name.startswith("test_") else "tests"
            if name in {"admit.py", "health.py", "router.py", "secrets.py"}:
                folder = "app"
            shell = (W2D5_ROOT / folder / name).read_bytes()
            filled = (W2D5_ROOT / "work" / folder / name).read_bytes()
            self.assertEqual(shell, filled, name)
        self.assertEqual(
            (W2D5_ROOT / "deploy" / "Dockerfile").read_bytes(),
            (W2D5_ROOT / "work" / "deploy" / "Dockerfile").read_bytes(),
        )

    def test_ea_confirms_the_missed_night(self) -> None:
        persona = load_personas()["ea"]
        turns = run(persona, _EA)
        self.assertEqual(turns[0]["released"], [])
        self.assertEqual(turns[1]["released"], ["ain-file"])
        self.assertIn("nightly file", turns[1]["answer"])
        self.assertEqual(turns[2]["released"], [])
        self.assertIn("missed night", turns[2]["answer"].lower())
        self.assertEqual(persona["must_surface"], ("ain-file", "hl7-pair"))

    def test_filled_suite_passes(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
            cwd=W2D5_ROOT / "work",
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)

    def test_shell_suite_passes(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
            cwd=W2D5_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)


if __name__ == "__main__":
    unittest.main()
