"""Day 3 of Week 2: the release, the clock, and the receipt demo.

Guards the receipt-clock release and the switch demo.

Earlier integration days must survive the write. The learner pack must mention
the switch and must not contain the old delay or either hidden due time. The
demo may show the switch turning a pass into a failure and must not print the
delay. The patient-representative script must release the caregiver fact. The
filled packet's own tests must pass.
"""

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
from alwaha.paths import W2D3_APP, W2D3_ROOT, W2D3_TEMPLATES, W2D3_TESTS, W2D3_WORK
from alwaha.release.day2 import write_day2
from alwaha.release.day3 import write_day3
from alwaha.release.day4 import write_day4
from alwaha.release.day5 import write_day5
from alwaha.release.fingerprint import fingerprint
from alwaha.release.w2d1 import write_w2d1
from alwaha.release.w2d2 import write_w2d2
from alwaha.release.w2d3 import write_w2d3
from alwaha.release.write import write_release

# Patient-representative script. The last turn is the one that should release the caregiver fact.
_REP = [
    "Why does the phone line still not answer?",
    "Are the daytime slots in Ramadan the ones his mother misses?",
    "Does a caregiver in the family book for her?",
]


def _canary_count(pack: Path, canary: str) -> int:
    """Count watermark hits across every file in a pack."""
    total = 0
    for path in pack.rglob("*"):
        if path.is_file():
            total += path.read_text(encoding="utf-8").count(canary)
    return total


class ReleaseTests(unittest.TestCase):
    """Catches a pack that rewrites an earlier day or that publishes the old delay."""
    def test_same_seed_matches_and_earlier_days_stay(self) -> None:
        """Fails when a second write disagrees, when an earlier pack or gold file changes,
        or when this day's gold is missing from the hidden side or present in the pack.
        """
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
        """Fails when either watermark is missing, repeated, or shared, or when the
        fingerprints match.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_w2d3(practice, root / "practice", root / "practice-truth")
            write_w2d3(small, root / "small", root / "small-truth")
            self.assertEqual(_canary_count(root / "practice", practice.canary()), 1)
            self.assertEqual(_canary_count(root / "small", small.canary()), 1)
            self.assertNotEqual(fingerprint(root / "practice"), fingerprint(root / "small"))

    def test_pack_keeps_the_old_delay_out(self) -> None:
        """Fails when the gold drifts, when the old delay or a hidden due time appears in
        the learner pack, when the switch name is missing, or when the watermark is not
        exactly once in the pack and absent from the gold file.
        """
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
    """Catches a demo or a lesson that reveals the delay, a module that was not
    actually fixed, or a filled test suite that does not pass.
    """
    def test_demo_goes_red_without_the_delay(self) -> None:
        """Fails when the demo does not show the switch turning a pass into a failure, or
        when it prints the delay, a due time, the switch name, or a watermark prefix.
        """
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "practice"])
        text = stdout.getvalue()
        self.assertEqual(text.splitlines(), ["switch off: passed", "switch on: failed"])
        for secret in (str(OLD_DELAY_SECONDS), "pending", "due", SWITCH, "CANARY-"):
            self.assertNotIn(secret, text)

    def test_notes_do_not_name_the_hidden_delay(self) -> None:
        """Fails when lesson notes contain the old delay, a hidden due time, or a watermark
        prefix.
        """
        notes = [path.read_text(encoding="utf-8") for path in W2D3_ROOT.glob("*.md")]
        notes.extend(path.read_text(encoding="utf-8") for path in W2D3_TEMPLATES.glob("*.md"))
        lesson_text = "\n".join(notes)
        profile = load("small")
        hidden = gold(profile)
        for secret in (str(OLD_DELAY_SECONDS), hidden["cases"][0]["due"], hidden["cases"][1]["due"], "CANARY-"):
            self.assertNotIn(secret, lesson_text)

    def test_only_the_trap_modules_differ(self) -> None:
        """Fails when an app module or a packet test is identical in the shell and the
        filled copy. The workflow file must stay the same, because this day does not
        change the pipeline.
        """
        for source in W2D3_APP.glob("*.py"):
            copy = W2D3_WORK / "app" / source.name
            self.assertNotEqual(source.read_bytes(), copy.read_bytes(), source.name)
        for name in ("test_calendar.py", "test_schema.py", "test_receipt.py", "test_journey.py"):
            shell = (W2D3_TESTS / name).read_bytes()
            filled = (W2D3_WORK / "tests" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        shell_ci = (W2D3_ROOT / "Student_Copy" / "packet" / ".github" / "workflows" / "ci.yml").read_bytes()
        filled_ci = (W2D3_WORK / ".github" / "workflows" / "ci.yml").read_bytes()
        self.assertEqual(shell_ci, filled_ci)

    def test_patient_rep_releases_the_caregiver(self) -> None:
        """Fails when the phone-line turn releases a fact, or when the Ramadan and
        caregiver turns do not release the facts they exist to release.
        """
        turns = run(load_personas()["patient-rep"], _REP)
        self.assertEqual(turns[0]["released"], [])
        self.assertIn("phone line", turns[0]["answer"])
        self.assertEqual(turns[1]["released"], ["ramadan-day"])
        self.assertIn("Ramadan", turns[1]["answer"])
        self.assertEqual(turns[2]["released"], ["caregiver"])
        self.assertIn("caregiver", turns[2]["answer"].lower())

    def test_filled_suite_passes(self) -> None:
        """Fails when the filled packet's own unit tests do not pass."""
        completed = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
            cwd=W2D3_WORK,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)


if __name__ == "__main__":
    unittest.main()
