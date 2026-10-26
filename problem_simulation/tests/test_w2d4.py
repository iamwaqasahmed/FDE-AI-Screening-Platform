"""Day 4 of Week 2: the release, the register, and the root-image demo.

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
from alwaha.engagement.w2d4 import gold
from alwaha.paths import W2D4_APP, W2D4_DEPLOY, W2D4_ROOT, W2D4_TEMPLATES, W2D4_TESTS, W2D4_WORK
from alwaha.release.day2 import write_day2
from alwaha.release.day3 import write_day3
from alwaha.release.day4 import write_day4
from alwaha.release.day5 import write_day5
from alwaha.release.fingerprint import fingerprint
from alwaha.release.w2d1 import write_w2d1
from alwaha.release.w2d2 import write_w2d2
from alwaha.release.w2d3 import write_w2d3
from alwaha.release.w2d4 import write_w2d4
from alwaha.release.write import write_release

# Security-officer script. The last turn is the one that should release the log fact.
_CISO = [
    "Is the security review booked at the end?",
    "Which go-live checklist does gate G4 use?",
    "Is patient data in the integration engine log since that change?",
]


def _canary_count(pack: Path, canary: str) -> int:
    """Count watermark hits across every file in a pack."""
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
            third = root / "w2d3"
            write_w2d3(profile, third, truth)
            before = (
                tuple(fingerprint(pack) for pack in packs),
                fingerprint(week2),
                fingerprint(second),
                fingerprint(third),
                (truth / "personas.json").read_bytes(),
                (truth / "w2d1_gold.json").read_bytes(),
                (truth / "w2d2_gold.json").read_bytes(),
                (truth / "w2d3_gold.json").read_bytes(),
            )
            first = write_w2d4(profile, root / "w2d4", truth)
            again = write_w2d4(profile, root / "w2d4", truth)
            self.assertEqual(first, again)
            self.assertEqual(
                before,
                (
                    tuple(fingerprint(pack) for pack in packs),
                    fingerprint(week2),
                    fingerprint(second),
                    fingerprint(third),
                    (truth / "personas.json").read_bytes(),
                    (truth / "w2d1_gold.json").read_bytes(),
                    (truth / "w2d2_gold.json").read_bytes(),
                    (truth / "w2d3_gold.json").read_bytes(),
                ),
            )
            self.assertTrue((truth / "w2d4_gold.json").is_file())
            self.assertFalse((root / "w2d4" / "w2d4_gold.json").exists())

    def test_profiles_differ_by_canary(self) -> None:
        """Fails when either watermark is missing, repeated, or shared, or when the
        fingerprints match.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_w2d4(practice, root / "practice", root / "practice-truth")
            write_w2d4(small, root / "small", root / "small-truth")
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
            write_w2d4(profile, pack, root / "truth")
            hidden = json.loads((root / "truth" / "w2d4_gold.json").read_text(encoding="utf-8"))
            prose = _prose(pack)
            notice = (pack / "notices" / "deploy.md").read_text(encoding="utf-8")
            self.assertEqual(hidden, gold(profile))
            self.assertNotIn(profile.canary(), json.dumps(hidden))
            for secret in _secrets(hidden, profile.canary()):
                self.assertNotIn(secret, prose)
                self.assertNotIn(secret, notice)
            self.assertIsNone(re.search(rf"(?<!\d){hidden['quota']}(?!\d)", notice))
            self.assertIsNone(re.search(rf"(?<!\d){hidden['quota']}(?!\d)", prose))
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
        """Fails when lesson notes or templates contain a secret or the quota."""
        notes = [path.read_text(encoding="utf-8") for path in W2D4_ROOT.glob("*.md")]
        notes.extend(path.read_text(encoding="utf-8") for path in W2D4_TEMPLATES.glob("*.md"))
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
        for source in W2D4_APP.glob("*.py"):
            copy = W2D4_WORK / "app" / source.name
            self.assertNotEqual(source.read_bytes(), copy.read_bytes(), source.name)
        for name in ("test_admit.py", "test_health.py", "test_router.py", "test_secrets.py"):
            shell = (W2D4_TESTS / name).read_bytes()
            filled = (W2D4_WORK / "tests" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        self.assertNotEqual(
            (W2D4_DEPLOY / "Dockerfile").read_bytes(),
            (W2D4_WORK / "deploy" / "Dockerfile").read_bytes(),
        )
        self.assertNotEqual(
            (W2D4_DEPLOY / "deployment.yaml").read_bytes(),
            (W2D4_WORK / "deploy" / "deployment.yaml").read_bytes(),
        )
        shell_ci = W2D4_ROOT / "Student_Copy" / "packet" / ".github" / "workflows" / "ci.yml"
        self.assertNotEqual(
            shell_ci.read_bytes(),
            (W2D4_WORK / ".github" / "workflows" / "ci.yml").read_bytes(),
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
        """Fails when the filled packet's own unit tests do not pass."""
        completed = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
            cwd=W2D4_WORK,
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
            cwd=W2D4_ROOT / "Student_Copy" / "packet",
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)


if __name__ == "__main__":
    unittest.main()
