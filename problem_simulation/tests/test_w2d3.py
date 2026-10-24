"""Day 3 of Week 2: the release, the clock, and the receipt demo."""

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
from alwaha.demo.receipt import main as demo_main
from alwaha.engagement.interview import run
from alwaha.engagement.personas import load_personas
from alwaha.engagement.w2d3 import OLD_DELAY_SECONDS, SWITCH, gold
from alwaha.paths import W2D3_APP, W2D3_ROOT
from alwaha.release.day2 import write_day2
from alwaha.release.day3 import write_day3
from alwaha.release.day4 import write_day4
from alwaha.release.day5 import write_day5
from alwaha.release.fingerprint import fingerprint
from alwaha.release.w2d1 import write_w2d1
from alwaha.release.w2d2 import write_w2d2
from alwaha.release.w2d3 import write_w2d3
from alwaha.release.write import write_release

_REP = [
    "Why does the phone line still not answer?",
    "Are the daytime slots in Ramadan the ones his mother misses?",
    "Does a caregiver in the family book for her?",
]


def _canary_count(pack: Path, canary: str) -> int:
    total = 0
    for path in pack.rglob("*"):
        if path.is_file():
            total += path.read_text(encoding="utf-8").count(canary)
    return total


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
            week2 = root / "week2"
            write_w2d1(profile, week2, truth)
            second = root / "w2d2"
            write_w2d2(profile, second, truth)
            before = (
                tuple(fingerprint(pack) for pack in packs),
                fingerprint(week2),
                fingerprint(second),
                (truth / "personas.json").read_bytes(),
                (truth / "w2d1_gold.json").read_bytes(),
                (truth / "w2d2_gold.json").read_bytes(),
            )
            first = write_w2d3(profile, root / "w2d3", truth)
            again = write_w2d3(profile, root / "w2d3", truth)
            self.assertEqual(first, again)
            self.assertEqual(
                before,
                (
                    tuple(fingerprint(pack) for pack in packs),
                    fingerprint(week2),
                    fingerprint(second),
                    (truth / "personas.json").read_bytes(),
                    (truth / "w2d1_gold.json").read_bytes(),
                    (truth / "w2d2_gold.json").read_bytes(),
                ),
            )
            self.assertTrue((truth / "w2d3_gold.json").is_file())
            self.assertFalse((root / "w2d3" / "w2d3_gold.json").exists())

    def test_profiles_differ_by_canary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_w2d3(practice, root / "practice", root / "practice-truth")
            write_w2d3(small, root / "small", root / "small-truth")
            self.assertEqual(_canary_count(root / "practice", practice.canary()), 1)
            self.assertEqual(_canary_count(root / "small", small.canary()), 1)
            self.assertNotEqual(fingerprint(root / "practice"), fingerprint(root / "small"))

    def test_pack_keeps_the_old_delay_out(self) -> None:
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            write_w2d3(profile, pack, root / "truth")
            blob = "\n".join(path.read_text(encoding="utf-8") for path in pack.rglob("*") if path.is_file())
            hidden = json.loads((root / "truth" / "w2d3_gold.json").read_text(encoding="utf-8"))
            self.assertEqual(hidden, gold(profile))
            self.assertNotIn(str(OLD_DELAY_SECONDS), blob)
            self.assertNotIn(str(hidden["cases"][0]["due"]), blob)
            self.assertNotIn(str(hidden["cases"][1]["due"]), blob)
            self.assertIn(SWITCH, blob)
            self.assertNotIn(profile.canary(), json.dumps(hidden))
            self.assertEqual(_canary_count(pack, profile.canary()), 1)


class DemoTests(unittest.TestCase):
    def test_demo_goes_red_without_the_delay(self) -> None:
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "practice"])
        text = stdout.getvalue()
        self.assertEqual(text.splitlines(), ["switch off: passed", "switch on: failed"])
        for secret in (str(OLD_DELAY_SECONDS), "pending", "due", SWITCH, "CANARY-"):
            self.assertNotIn(secret, text)

    def test_notes_do_not_name_the_hidden_delay(self) -> None:
        lessons = []
        for path in W2D3_ROOT.rglob("*.md"):
            if "work" in path.parts:
                continue
            lessons.append(path.read_text(encoding="utf-8"))
        lesson_text = "\n".join(lessons)
        profile = load("small")
        hidden = gold(profile)
        for secret in (str(OLD_DELAY_SECONDS), hidden["cases"][0]["due"], hidden["cases"][1]["due"], "CANARY-"):
            self.assertNotIn(secret, lesson_text)

    def test_only_the_trap_modules_differ(self) -> None:
        for source in W2D3_APP.glob("*.py"):
            copy = W2D3_ROOT / "work" / "app" / source.name
            self.assertNotEqual(source.read_bytes(), copy.read_bytes(), source.name)
        for name in ("test_calendar.py", "test_schema.py", "test_receipt.py", "test_journey.py"):
            shell = (W2D3_ROOT / "tests" / name).read_bytes()
            filled = (W2D3_ROOT / "work" / "tests" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        shell_ci = (W2D3_ROOT / ".github" / "workflows" / "ci.yml").read_bytes()
        filled_ci = (W2D3_ROOT / "work" / ".github" / "workflows" / "ci.yml").read_bytes()
        self.assertEqual(shell_ci, filled_ci)

    def test_patient_rep_releases_the_caregiver(self) -> None:
        turns = run(load_personas()["patient-rep"], _REP)
        self.assertEqual(turns[0]["released"], [])
        self.assertIn("phone line", turns[0]["answer"])
        self.assertEqual(turns[1]["released"], ["ramadan-day"])
        self.assertIn("Ramadan", turns[1]["answer"])
        self.assertEqual(turns[2]["released"], ["caregiver"])
        self.assertIn("caregiver", turns[2]["answer"].lower())

    def test_filled_suite_passes(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
            cwd=W2D3_ROOT / "work",
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)


if __name__ == "__main__":
    unittest.main()
