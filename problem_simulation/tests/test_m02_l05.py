"""Module 2, Lesson 5: the release, the change request, and the steering card.

Guards the change-request release and the steering card.

Earlier days, including the deploy day, must survive the write. Prose must not
contain the clinic code, the previous code, or the watermark, while the nightly
fixture must still contain the code. The change notice must not say that a
nightly file exists. The demo may print the card and the questions and must not
mention the file. The new trap modules must differ, and the smoke modules carried
forward from the deploy day must not.
"""

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
from alwaha.engagement.m02_l05 import CARD, QUESTIONS, gold
from alwaha.paths import M02_L05_APP, M02_L05_DEPLOY, M02_L05_ROOT, M02_L05_TEMPLATES, M02_L05_TESTS, M02_L05_WORK
from alwaha.release.m01_l02 import write_m01_l02
from alwaha.release.m01_l03 import write_m01_l03
from alwaha.release.m01_l04 import write_m01_l04
from alwaha.release.m01_l05 import write_m01_l05
from alwaha.release.fingerprint import fingerprint
from alwaha.release.m02_l01 import write_m02_l01
from alwaha.release.m02_l02 import write_m02_l02
from alwaha.release.m02_l03 import write_m02_l03
from alwaha.release.m02_l04 import write_m02_l04
from alwaha.release.m02_l05 import write_m02_l05
from alwaha.release.write import write_release

# Architect script. The middle turn should release the nightly-file fact and the last turn should not release a new one.
_EA = [
    "Do we have an API strategy?",
    "Does Ain publish a nightly schedule file?",
    "What does a missed night leave, and whose clinic codes are on it?",
]
# Deploy modules and tests that must stay identical. The new queue modules are checked on their own.
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
    """Count watermark hits across every file in a pack.

    The release tests write a pack for a profile and fail when that profile's watermark is
    missing or repeated.
    """
    total = 0
    for path in pack.rglob("*"):
        if path.is_file():
            total += path.read_text(encoding="utf-8").count(canary)
    return total


def _prose(pack: Path) -> str:
    """Join the markdown and the manifest files so a secret in prose can be told apart
    from the same secret in a fixture.
    """
    chunks = []
    for path in pack.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".yaml", ".yml"}:
            chunks.append(path.read_text(encoding="utf-8"))
    return "\n".join(chunks)


class ReleaseTests(unittest.TestCase):
    """Catches a pack that rewrites an earlier day or that names the clinic code in prose."""
    def test_same_seed_matches_and_earlier_days_stay(self) -> None:
        """Fails when a second write disagrees, when an earlier pack or the deploy gold
        changes, or when this lesson's gold is missing from the hidden side or present in
        the pack.
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
            week2 = [root / f"m02l{index}" for index in range(1, 5)]
            write_m02_l01(profile, week2[0], truth)
            write_m02_l02(profile, week2[1], truth)
            write_m02_l03(profile, week2[2], truth)
            write_m02_l04(profile, week2[3], truth)
            # Fingerprints of the earlier packs, including the four week-2 days, plus the deploy gold.
            before = (
                tuple(fingerprint(pack) for pack in packs),
                tuple(fingerprint(pack) for pack in week2),
                (truth / "personas.json").read_bytes(),
                (truth / "m02_l04_gold.json").read_bytes(),
            )
            # Write this lesson twice. The two results must agree, and the earlier lessons must stay as they were.
            first = write_m02_l05(profile, root / "m02_l05", truth)
            again = write_m02_l05(profile, root / "m02_l05", truth)
            self.assertEqual(first, again)
            self.assertEqual(
                before,
                (
                    tuple(fingerprint(pack) for pack in packs),
                    tuple(fingerprint(pack) for pack in week2),
                    (truth / "personas.json").read_bytes(),
                    (truth / "m02_l04_gold.json").read_bytes(),
                ),
            )
            # This day's gold stays on the hidden side.
            self.assertTrue((truth / "m02_l05_gold.json").is_file())
            self.assertFalse((root / "m02_l05" / "m02_l05_gold.json").exists())

    def test_profiles_differ_by_canary(self) -> None:
        """Fails when either watermark is missing, repeated, or shared, or when the
        fingerprints match.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_m02_l05(practice, root / "practice", root / "practice-truth")
            write_m02_l05(small, root / "small", root / "small-truth")
            self.assertEqual(_canary_count(root / "practice", practice.canary()), 1)
            self.assertEqual(_canary_count(root / "small", small.canary()), 1)
            self.assertNotEqual(fingerprint(root / "practice"), fingerprint(root / "small"))

    def test_notice_keeps_the_clinic_code_out(self) -> None:
        """Fails when prose contains a clinic code or the watermark, when the nightly
        fixture loses the code, or when the change notice mentions a nightly file.
        """
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            write_m02_l05(profile, pack, root / "truth")
            # The hidden gold matches the generator. Prose does not contain the clinic codes or the watermark.
            hidden = json.loads((root / "truth" / "m02_l05_gold.json").read_text(encoding="utf-8"))
            prose = _prose(pack)
            self.assertEqual(hidden, gold(profile))
            self.assertNotIn(profile.canary(), json.dumps(hidden))
            for secret in (hidden["clinic_code"], hidden["previous_code"], profile.canary()):
                self.assertNotIn(secret, prose)
            # The nightly fixture keeps the clinic code. The change notice does not mention a nightly file.
            nightly = (pack / "fixtures" / "nightly.json").read_text(encoding="utf-8")
            self.assertIn(hidden["clinic_code"], nightly)
            self.assertEqual(_canary_count(pack, profile.canary()), 1)
            self.assertIsNone(re.search(r"nightly", (pack / "notices" / "cr-ain.md").read_text(encoding="utf-8"), re.I))


class DemoTests(unittest.TestCase):
    """Catches a demo or a lesson that reveals the clinic code, a trap module that was
    not changed, or a smoke module that was changed by mistake.
    """
    def test_demo_prints_the_card_without_the_file_sentence(self) -> None:
        """Fails when the demo is not the steering card followed by the questions, or when
        it mentions the nightly file, the clinic code, or the watermark.
        """
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
        """Fails when lesson notes or templates contain either clinic code.

        The test reads every lesson note and template and fails if either clinic code appears in
        that prose.
        """
        notes = [path.read_text(encoding="utf-8") for path in M02_L05_ROOT.glob("README.md")]
        notes.extend(path.read_text(encoding="utf-8") for path in M02_L05_TEMPLATES.glob("*.md"))
        lesson_text = "\n".join(notes)
        hidden = gold(load("small"))
        self.assertNotIn(hidden["clinic_code"], lesson_text)
        self.assertNotIn(hidden["previous_code"], lesson_text)

    def test_only_the_trap_modules_differ(self) -> None:
        """Fails when a new queue module matches the shell, or when a smoke module or the
        image file differs from the filled deploy copy. Only the new modules are traps.
        """
        # The new queue modules differ between the shell and the filled copy.
        for name in ("queue.py", "file_ain.py", "notify.py", "contract.py"):
            shell = (M02_L05_APP / name).read_bytes()
            filled = (M02_L05_WORK / "app" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        # Smoke modules and the image file stay the same. They are not traps on this day.
        for name in _SMOKE:
            if name in {"admit.py", "health.py", "router.py", "secrets.py"}:
                shell = (M02_L05_APP / name).read_bytes()
                filled = (M02_L05_WORK / "app" / name).read_bytes()
            else:
                shell = (M02_L05_TESTS / name).read_bytes()
                filled = (M02_L05_WORK / "tests" / name).read_bytes()
            self.assertEqual(shell, filled, name)
        self.assertEqual(
            (M02_L05_DEPLOY / "Dockerfile").read_bytes(),
            (M02_L05_WORK / "deploy" / "Dockerfile").read_bytes(),
        )

    def test_ea_confirms_the_missed_night(self) -> None:
        """Fails when the strategy question releases a fact, when the nightly-file fact
        does not surface, or when the missed-night turn releases a new fact. The
        architect's required-fact list must stay the one from the first week.
        """
        persona = load_personas()["ea"]
        turns = run(persona, _EA)
        self.assertEqual(turns[0]["released"], [])
        self.assertEqual(turns[1]["released"], ["ain-file"])
        self.assertIn("nightly file", turns[1]["answer"])
        self.assertEqual(turns[2]["released"], [])
        self.assertIn("missed night", turns[2]["answer"].lower())
        self.assertEqual(persona["must_surface"], ("ain-file", "hl7-pair"))

    def test_filled_suite_passes(self) -> None:
        """Fails when the filled packet's own unit tests do not pass.

        The test runs that packet's unit tests from the filled work tree and fails if the run
        does not exit cleanly.
        """
        completed = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
            cwd=M02_L05_WORK,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)

    def test_shell_suite_passes(self) -> None:
        """Fails when the unfinished packet's own unit tests do not pass.

        The test runs the unfinished packet's unit tests from the student copy, which are still
        supposed to pass, and fails if the run does not exit cleanly.
        """
        completed = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
            cwd=M02_L05_ROOT / "packet",
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)


if __name__ == "__main__":
    unittest.main()
