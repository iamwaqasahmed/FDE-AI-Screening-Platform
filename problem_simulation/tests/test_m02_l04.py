"""Module 2, Lesson 4: the release, the register, and the root-image demo.

Guards the deploy release, the model register, and the root-image demo.

Earlier days must survive the write. Prose and the deploy notice must not
contain the hashes, the tokens, the national id, the watermark, or the quota.
Those values may live in the register and the log fixture. The demo may reject
a root image and accept a registered one without printing a secret. The security
interview must release the log fact. Both the filled suite and the shell suite
must pass, because the shell tests are still green on purpose.
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
from alwaha.demo.deploy import main as demo_main
from alwaha.engagement.interview import run
from alwaha.engagement.personas import load_personas
from alwaha.engagement.m02_l04 import gold
from alwaha.paths import M02_L04_APP, M02_L04_DEPLOY, M02_L04_ROOT, M02_L04_TEMPLATES, M02_L04_TESTS, M02_L04_WORK
from alwaha.release.m01_l02 import write_m01_l02
from alwaha.release.m01_l03 import write_m01_l03
from alwaha.release.m01_l04 import write_m01_l04
from alwaha.release.m01_l05 import write_m01_l05
from alwaha.release.fingerprint import fingerprint
from alwaha.release.m02_l01 import write_m02_l01
from alwaha.release.m02_l02 import write_m02_l02
from alwaha.release.m02_l03 import write_m02_l03
from alwaha.release.m02_l04 import write_m02_l04
from alwaha.release.write import write_release

# Security-officer script. The last turn is the one that should release the log fact.
_CISO = [
    "Is the security review booked at the end?",
    "Which go-live checklist does gate G4 use?",
    "Is patient data in the integration engine log since that change?",
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


def _prose(pack: Path) -> str:
    """Join the markdown and the manifest files in a pack.

    Secrets are forbidden in prose even when a fixture file is allowed to hold them.
    """
    chunks = []
    for path in pack.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".yaml", ".yml"}:
            chunks.append(path.read_text(encoding="utf-8"))
    return "\n".join(chunks)


def _secrets(hidden: dict, canary: str) -> list[str]:
    """The hidden values this day's prose must not print: the three image hashes, both
    tokens, the national id, and the watermark.
    """
    return [
        hidden["approved_hash"],
        hidden["previous_hash"],
        hidden["lookalike_hash"],
        hidden["dev_token"],
        hidden["prod_token"],
        hidden["national_id"],
        canary,
    ]


class ReleaseTests(unittest.TestCase):
    """Catches a pack that rewrites an earlier day or that prints a deploy secret in prose."""
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
            third = root / "m02_l03"
            write_m02_l03(profile, third, truth)
            # Fingerprints of the earlier packs, including the three week-2 days, plus their gold files.
            before = (
                tuple(fingerprint(pack) for pack in packs),
                fingerprint(week2),
                fingerprint(second),
                fingerprint(third),
                (truth / "personas.json").read_bytes(),
                (truth / "m02_l01_gold.json").read_bytes(),
                (truth / "m02_l02_gold.json").read_bytes(),
                (truth / "m02_l03_gold.json").read_bytes(),
            )
            # Write this lesson twice. The two results must agree, and the earlier lessons must stay as they were.
            first = write_m02_l04(profile, root / "m02_l04", truth)
            again = write_m02_l04(profile, root / "m02_l04", truth)
            self.assertEqual(first, again)
            self.assertEqual(
                before,
                (
                    tuple(fingerprint(pack) for pack in packs),
                    fingerprint(week2),
                    fingerprint(second),
                    fingerprint(third),
                    (truth / "personas.json").read_bytes(),
                    (truth / "m02_l01_gold.json").read_bytes(),
                    (truth / "m02_l02_gold.json").read_bytes(),
                    (truth / "m02_l03_gold.json").read_bytes(),
                ),
            )
            # This day's gold stays on the hidden side.
            self.assertTrue((truth / "m02_l04_gold.json").is_file())
            self.assertFalse((root / "m02_l04" / "m02_l04_gold.json").exists())

    def test_profiles_differ_by_canary(self) -> None:
        """Fails when either watermark is missing, repeated, or shared, or when the
        fingerprints match.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_m02_l04(practice, root / "practice", root / "practice-truth")
            write_m02_l04(small, root / "small", root / "small-truth")
            self.assertEqual(_canary_count(root / "practice", practice.canary()), 1)
            self.assertEqual(_canary_count(root / "small", small.canary()), 1)
            self.assertNotEqual(fingerprint(root / "practice"), fingerprint(root / "small"))

    def test_notice_keeps_the_secrets_out(self) -> None:
        """Fails when prose or the notice contains a secret or the quota, when the register
        loses the approved hash, when the log fixture loses the national id, or when
        the watermark is not exactly once in the pack and absent from the gold file.
        """
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            write_m02_l04(profile, pack, root / "truth")
            # The hidden gold must match the generator and must not contain the watermark.
            hidden = json.loads((root / "truth" / "m02_l04_gold.json").read_text(encoding="utf-8"))
            prose = _prose(pack)
            notice = (pack / "notices" / "deploy.md").read_text(encoding="utf-8")
            self.assertEqual(hidden, gold(profile))
            self.assertNotIn(profile.canary(), json.dumps(hidden))
            # Prose and the notice keep every secret out, including the quota as a standalone number.
            for secret in _secrets(hidden, profile.canary()):
                self.assertNotIn(secret, prose)
                self.assertNotIn(secret, notice)
            self.assertIsNone(re.search(rf"(?<!\d){hidden['quota']}(?!\d)", notice))
            self.assertIsNone(re.search(rf"(?<!\d){hidden['quota']}(?!\d)", prose))
            # The register keeps the approved hash, and the log fixture keeps the national id. The watermark appears once.
            self.assertIn(hidden["approved_hash"], (pack / "registry" / "models.json").read_text(encoding="utf-8"))
            self.assertIn(hidden["national_id"], (pack / "fixtures" / "log.json").read_text(encoding="utf-8"))
            self.assertEqual(_canary_count(pack, profile.canary()), 1)


class DemoTests(unittest.TestCase):
    """Catches a demo or a lesson that prints a secret, a trap file that was not
    changed, or a packet suite that does not pass.
    """
    def test_demo_rejects_root_without_the_hash(self) -> None:
        """Fails when the demo does not reject the root image and accept the registered
        one, or when it prints a secret or the quota.
        """
        profile = load("practice")
        hidden = gold(profile)
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "practice"])
        text = stdout.getvalue()
        self.assertEqual(text.splitlines(), ["root image: rejected", "registered image: accepted"])
        for secret in _secrets(hidden, profile.canary()):
            self.assertNotIn(secret, text)
        self.assertNotIn(str(hidden["quota"]), text)

    def test_notes_do_not_name_the_secrets(self) -> None:
        """Fails when lesson notes or templates contain a secret or the quota.

        The test reads every lesson note and template and fails if a deploy secret appears, or
        if the quota appears as a number standing alone.
        """
        notes = [path.read_text(encoding="utf-8") for path in M02_L04_ROOT.glob("README.md")]
        notes.extend(path.read_text(encoding="utf-8") for path in M02_L04_TEMPLATES.glob("*.md"))
        lesson_text = "\n".join(notes)
        profile = load("small")
        hidden = gold(profile)
        for secret in _secrets(hidden, profile.canary()):
            self.assertNotIn(secret, lesson_text)
        self.assertIsNone(re.search(rf"(?<!\d){hidden['quota']}(?!\d)", lesson_text))

    def test_only_the_trap_modules_differ(self) -> None:
        """Fails when an app module, a packet test, the image file, the manifest, or the
        pipeline is identical in the shell and the filled copy. This day changes all
        of them.
        """
        # Every app module, packet test, image, manifest, and pipeline differs between the shell and the filled copy.
        for source in M02_L04_APP.glob("*.py"):
            copy = M02_L04_WORK / "app" / source.name
            self.assertNotEqual(source.read_bytes(), copy.read_bytes(), source.name)
        for name in ("test_admit.py", "test_health.py", "test_router.py", "test_secrets.py"):
            shell = (M02_L04_TESTS / name).read_bytes()
            filled = (M02_L04_WORK / "tests" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        # The image, the manifest, and the pipeline are traps too. Each one differs.
        self.assertNotEqual(
            (M02_L04_DEPLOY / "Dockerfile").read_bytes(),
            (M02_L04_WORK / "deploy" / "Dockerfile").read_bytes(),
        )
        self.assertNotEqual(
            (M02_L04_DEPLOY / "deployment.yaml").read_bytes(),
            (M02_L04_WORK / "deploy" / "deployment.yaml").read_bytes(),
        )
        shell_ci = M02_L04_ROOT / "Student_Copy" / "packet" / ".github" / "workflows" / "ci.yml"
        self.assertNotEqual(
            shell_ci.read_bytes(),
            (M02_L04_WORK / ".github" / "workflows" / "ci.yml").read_bytes(),
        )

    def test_ciso_releases_the_log(self) -> None:
        """Fails when the review question releases a fact too early, or when the checklist
        and the engine-log facts do not surface. The log answer must name the change.
        """
        turns = run(load_personas()["ciso"], _CISO)
        self.assertEqual(turns[0]["released"], [])
        self.assertIn("review", turns[0]["answer"].lower())
        self.assertEqual(turns[1]["released"], ["checklist"])
        self.assertIn("checklist", turns[1]["answer"].lower())
        self.assertEqual(turns[2]["released"], ["engine-log"])
        self.assertIn("CHG-2025-118", turns[2]["answer"])

    def test_filled_suite_passes(self) -> None:
        """Fails when the filled packet's own unit tests do not pass.

        The test runs that packet's unit tests from the filled work tree and fails if the run
        does not exit cleanly.
        """
        completed = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
            cwd=M02_L04_WORK,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)

    def test_shell_suite_passes(self) -> None:
        """Fails when the unfinished packet's own unit tests do not pass.

        Those tests are still green. The traps are caught by the deploy checker, not
        by the shell suite.
        """
        completed = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
            cwd=M02_L04_ROOT / "Student_Copy" / "packet",
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)


if __name__ == "__main__":
    unittest.main()
