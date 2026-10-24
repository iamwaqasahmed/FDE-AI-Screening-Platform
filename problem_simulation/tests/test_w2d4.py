"""Day 4 of Week 2: the release, the register, and the root-image demo."""

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
from alwaha.paths import W2D4_APP, W2D4_ROOT
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

_CISO = [
    "Is the security review booked at the end?",
    "Which go-live checklist does gate G4 use?",
    "Is patient data in the integration engine log since that change?",
]


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


def _secrets(hidden: dict, canary: str) -> list[str]:
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
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_w2d4(practice, root / "practice", root / "practice-truth")
            write_w2d4(small, root / "small", root / "small-truth")
            self.assertEqual(_canary_count(root / "practice", practice.canary()), 1)
            self.assertEqual(_canary_count(root / "small", small.canary()), 1)
            self.assertNotEqual(fingerprint(root / "practice"), fingerprint(root / "small"))

    def test_notice_keeps_the_secrets_out(self) -> None:
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
    def test_demo_rejects_root_without_the_hash(self) -> None:
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
        lessons = []
        for path in W2D4_ROOT.rglob("*"):
            if not path.is_file() or "work" in path.parts:
                continue
            if path.suffix in {".md", ".py", ".yml", ".yaml"}:
                lessons.append(path.read_text(encoding="utf-8"))
        lesson_text = "\n".join(lessons)
        profile = load("small")
        hidden = gold(profile)
        for secret in _secrets(hidden, profile.canary()):
            self.assertNotIn(secret, lesson_text)
        self.assertIsNone(re.search(rf"(?<!\d){hidden['quota']}(?!\d)", lesson_text))

    def test_only_the_trap_modules_differ(self) -> None:
        for source in W2D4_APP.glob("*.py"):
            copy = W2D4_ROOT / "work" / "app" / source.name
            self.assertNotEqual(source.read_bytes(), copy.read_bytes(), source.name)
        for name in ("test_admit.py", "test_health.py", "test_router.py", "test_secrets.py"):
            shell = (W2D4_ROOT / "tests" / name).read_bytes()
            filled = (W2D4_ROOT / "work" / "tests" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        self.assertNotEqual(
            (W2D4_ROOT / "deploy" / "Dockerfile").read_bytes(),
            (W2D4_ROOT / "work" / "deploy" / "Dockerfile").read_bytes(),
        )
        self.assertNotEqual(
            (W2D4_ROOT / "deploy" / "deployment.yaml").read_bytes(),
            (W2D4_ROOT / "work" / "deploy" / "deployment.yaml").read_bytes(),
        )
        self.assertNotEqual(
            (W2D4_ROOT / ".github" / "workflows" / "ci.yml").read_bytes(),
            (W2D4_ROOT / "work" / ".github" / "workflows" / "ci.yml").read_bytes(),
        )

    def test_ciso_releases_the_log(self) -> None:
        turns = run(load_personas()["ciso"], _CISO)
        self.assertEqual(turns[0]["released"], [])
        self.assertIn("review", turns[0]["answer"].lower())
        self.assertEqual(turns[1]["released"], ["checklist"])
        self.assertIn("checklist", turns[1]["answer"].lower())
        self.assertEqual(turns[2]["released"], ["engine-log"])
        self.assertIn("CHG-2025-118", turns[2]["answer"])

    def test_filled_suite_passes(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
            cwd=W2D4_ROOT / "work",
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)

    def test_shell_suite_passes(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
            cwd=W2D4_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)


if __name__ == "__main__":
    unittest.main()
