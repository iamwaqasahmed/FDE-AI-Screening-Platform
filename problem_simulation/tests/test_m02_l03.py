"""Module 2, Lesson 3: the release, the clock, and the receipt demo.

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
from alwaha.engagement.m02_l03 import OLD_DELAY_SECONDS, SWITCH, gold
from alwaha.paths import M02_L03_APP, M02_L03_ROOT, M02_L03_TEMPLATES, M02_L03_TESTS, M02_L03_WORK
from alwaha.release.m01_l02 import write_m01_l02
from alwaha.release.m01_l03 import write_m01_l03
from alwaha.release.m01_l04 import write_m01_l04
from alwaha.release.m01_l05 import write_m01_l05
from alwaha.release.fingerprint import fingerprint
from alwaha.release.m02_l01 import write_m02_l01
from alwaha.release.m02_l02 import write_m02_l02
from alwaha.release.m02_l03 import write_m02_l03
from alwaha.release.write import write_release

# Patient-representative script. The last turn is the one that should release the caregiver fact.
_REP = [
    "Why does the phone line still not answer?",
    "Are the daytime slots in Ramadan the ones his mother misses?",
    "Does a caregiver in the family book for her?",
]


def _canary_count(pack: Path, canary: str) -> int:
    """Count watermark hits across every file in a pack.

    The release tests write a pack for a profile and fail when that profile's watermark is
    missing or repeated.
    """
    total = 0
    for path in pack.rglob("*"):
        if path.is_file():
            total += path.read_text(encoding="utf-8").count(canary)
    return total


class ReleaseTests(unittest.TestCase):
    """Catches a pack that rewrites an earlier day or that publishes the old delay."""
    def test_same_seed_matches_and_earlier_days_stay(self) -> None:
        """Fails when a second write disagrees, when an earlier pack or gold file changes,
        or when this lesson's gold is missing from the hidden side or present in the pack.
        """
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            packs = [root / f"m01l{index}" for index in range(1, 6)]
            truth = root / "truth"
            write_release(profile, packs[0], truth)
            write_m01_l02(profile, packs[1], truth)
            write_m01_l03(profile, packs[2], truth)
            write_m01_l04(profile, packs[3], truth)
            write_m01_l05(profile, packs[4], truth)
            week2 = root / "week2"
            write_m02_l01(profile, week2, truth)
            second = root / "m02_l02"
            write_m02_l02(profile, second, truth)
            # Fingerprints of the earlier packs, including the two week-2 days, plus their gold files.
            before = (
                tuple(fingerprint(pack) for pack in packs),
                fingerprint(week2),
                fingerprint(second),
                (truth / "personas.json").read_bytes(),
                (truth / "m02_l01_gold.json").read_bytes(),
                (truth / "m02_l02_gold.json").read_bytes(),
            )
            # Write this lesson twice. The two results must agree, and the earlier lessons must stay as they were.
            first = write_m02_l03(profile, root / "m02_l03", truth)
            again = write_m02_l03(profile, root / "m02_l03", truth)
            self.assertEqual(first, again)
            self.assertEqual(
                before,
                (
                    tuple(fingerprint(pack) for pack in packs),
                    fingerprint(week2),
                    fingerprint(second),
                    (truth / "personas.json").read_bytes(),
                    (truth / "m02_l01_gold.json").read_bytes(),
                    (truth / "m02_l02_gold.json").read_bytes(),
                ),
            )
            # This day's gold stays on the hidden side.
            self.assertTrue((truth / "m02_l03_gold.json").is_file())
            self.assertFalse((root / "m02_l03" / "m02_l03_gold.json").exists())

    def test_profiles_differ_by_canary(self) -> None:
        """Fails when either watermark is missing, repeated, or shared, or when the
        fingerprints match.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_m02_l03(practice, root / "practice", root / "practice-truth")
            write_m02_l03(small, root / "small", root / "small-truth")
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
            write_m02_l03(profile, pack, root / "truth")
            # Join every learner file, and load the hidden gold.
            blob = "\n".join(path.read_text(encoding="utf-8") for path in pack.rglob("*") if path.is_file())
            hidden = json.loads((root / "truth" / "m02_l03_gold.json").read_text(encoding="utf-8"))
            # The gold matches the generator. The old delay and the hidden due times stay out of the pack.
            self.assertEqual(hidden, gold(profile))
            self.assertNotIn(str(OLD_DELAY_SECONDS), blob)
            self.assertNotIn(str(hidden["cases"][0]["due"]), blob)
            self.assertNotIn(str(hidden["cases"][1]["due"]), blob)
            self.assertIn(SWITCH, blob)
            # The watermark is absent from the gold and appears once in the pack.
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
        notes = [path.read_text(encoding="utf-8") for path in M02_L03_ROOT.glob("README.md")]
        notes.extend(path.read_text(encoding="utf-8") for path in M02_L03_TEMPLATES.glob("*.md"))
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
        # Every app module and every packet test differs between the shell and the filled copy.
        for source in M02_L03_APP.glob("*.py"):
            copy = M02_L03_WORK / "app" / source.name
            self.assertNotEqual(source.read_bytes(), copy.read_bytes(), source.name)
        for name in ("test_calendar.py", "test_schema.py", "test_receipt.py", "test_journey.py"):
            shell = (M02_L03_TESTS / name).read_bytes()
            filled = (M02_L03_WORK / "tests" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        # The workflow file is the same, because this day does not change the pipeline.
        shell_ci = (M02_L03_ROOT / "packet" / ".github" / "workflows" / "ci.yml").read_bytes()
        filled_ci = (M02_L03_WORK / ".github" / "workflows" / "ci.yml").read_bytes()
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
        """Fails when the filled packet's own unit tests do not pass.

        The test runs that packet's unit tests from the filled work tree and fails if the run
        does not exit cleanly.
        """
        completed = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
            cwd=M02_L03_WORK,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)


if __name__ == "__main__":
    unittest.main()
