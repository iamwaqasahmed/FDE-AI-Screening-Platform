"""Day 2 of Week 3: the ruling, the quota, and the registered adapter."""

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
from alwaha.demo.gateway import main as demo_main
from alwaha.engagement.interview import run, score_turns, winning_questions
from alwaha.engagement.personas import load_personas
from alwaha.engagement.w3d2 import gold, measurement_block
from alwaha.paths import W3D2_APP, W3D2_ROOT, W3D2_TEMPLATES, W3D2_WORK
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
from alwaha.release.w3d2 import write_w3d2
from alwaha.release.write import write_release

_DPO = [
    "How should we handle patient data?",
    "What does the unsigned ruling say about the external model?",
    "Did you sign it?",
]
_FINANCE = [
    "Is there a budget line?",
    "Should we rent a GPU or buy one, and how many weeks?",
    "What is the quota and the cap?",
]
_APP = (
    "prompt.py",
    "extract.py",
    "intent.py",
    "adapter.py",
    "route.py",
    "cost.py",
    "qlora.py",
    "domain.py",
    "prefs.py",
)
_TESTS = (
    "test_prompt.py",
    "test_extract.py",
    "test_intent.py",
    "test_adapter.py",
    "test_route.py",
    "test_cost.py",
    "test_qlora.py",
    "test_domain.py",
    "test_prefs.py",
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
            write_w3d1(profile, root / "w3d1", truth)
            before = (
                tuple(fingerprint(pack) for pack in packs),
                tuple(fingerprint(pack) for pack in week2),
                fingerprint(root / "w3d1"),
                (truth / "personas.json").read_bytes(),
                (truth / "w3d1_gold.json").read_bytes(),
            )
            first = write_w3d2(profile, root / "w3d2", truth)
            again = write_w3d2(profile, root / "w3d2", truth)
            self.assertEqual(first, again)
            self.assertEqual(
                before,
                (
                    tuple(fingerprint(pack) for pack in packs),
                    tuple(fingerprint(pack) for pack in week2),
                    fingerprint(root / "w3d1"),
                    (truth / "personas.json").read_bytes(),
                    (truth / "w3d1_gold.json").read_bytes(),
                ),
            )
            self.assertTrue((truth / "w3d2_gold.json").is_file())
            self.assertFalse((root / "w3d2" / "w3d2_gold.json").exists())

    def test_profiles_differ_and_the_cap_splits_the_prices(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_w3d2(practice, root / "practice", root / "practice-truth")
            write_w3d2(small, root / "small", root / "small-truth")
            self.assertEqual(_canary_count(root / "practice", practice.canary()), 0)
            self.assertEqual(_canary_count(root / "small", small.canary()), 0)
            self.assertNotEqual(fingerprint(root / "practice"), fingerprint(root / "small"))
            for profile, folder in ((practice, "practice-truth"), (small, "small-truth")):
                hidden = json.loads((root / folder / "w3d2_gold.json").read_text(encoding="utf-8"))
                self.assertEqual(hidden, gold(profile))
                self.assertLessEqual(hidden["local_sar"], hidden["cap"]["max_sar"])
                self.assertGreater(hidden["external_sar"], hidden["cap"]["max_sar"])

    def test_prose_and_the_register_keep_the_secrets_out(self) -> None:
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            write_w3d2(profile, pack, root / "truth")
            hidden = json.loads((root / "truth" / "w3d2_gold.json").read_text(encoding="utf-8"))
            prose = _prose(pack)
            register = (pack / "registry" / "reg-models.json").read_text(encoding="utf-8")
            blob = "\n".join(path.read_text(encoding="utf-8") for path in pack.rglob("*") if path.is_file())
            self.assertNotIn(profile.canary(), prose)
            self.assertNotIn(profile.canary(), json.dumps(hidden))
            self.assertNotIn(hidden["cloud_hash"], register)
            self.assertIn(hidden["adapter_hash"], register)
            for row in hidden["held_letters"]:
                self.assertNotIn(row["item_id"], blob)
                self.assertNotIn(row["text"], blob)
            for row in hidden["held_messages"]:
                self.assertNotIn(row["message_id"], blob)
            self.assertNotIn(hidden["held_pref"]["draft"], blob)


class DemoTests(unittest.TestCase):
    def test_demo_refuses_without_printing_the_watermark(self) -> None:
        profile = load("practice")
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "practice"])
        text = stdout.getvalue()
        self.assertEqual(text.splitlines(), ["the gateway refused the prompt"])
        self.assertNotIn(profile.canary(), text)

    def test_lessons_do_not_state_the_seed_values(self) -> None:
        notes = [path.read_text(encoding="utf-8") for path in W3D2_ROOT.glob("*.md")]
        notes.extend(path.read_text(encoding="utf-8") for path in W3D2_TEMPLATES.glob("*.md"))
        lesson_text = "\n".join(notes)
        hidden = gold(load("practice"))
        small = gold(load("small"))
        self.assertNotIn(load("practice").canary(), lesson_text)
        for secret in (hidden["adapter_hash"], hidden["cloud_hash"], small["adapter_hash"], small["cloud_hash"]):
            self.assertNotIn(secret, lesson_text)
        for row in hidden["held_letters"]:
            self.assertNotIn(row["item_id"], lesson_text)

    def test_modules_differ_and_only_the_copy_passes(self) -> None:
        packet = W3D2_APP.parent
        for name in _APP:
            shell = (W3D2_APP / name).read_bytes()
            filled = (W3D2_WORK / "app" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        for name in _TESTS:
            shell = (packet / "tests" / name).read_bytes()
            filled = (W3D2_WORK / "tests" / name).read_bytes()
            self.assertEqual(shell, filled, name)
        work = _suite(W3D2_WORK)
        shell = _suite(packet)
        self.assertEqual(work.returncode, 0, work.stdout + work.stderr)
        self.assertNotEqual(shell.returncode, 0, shell.stdout + shell.stderr)

    def test_interviews_release_the_new_facts_and_keep_the_old_ones(self) -> None:
        personas = load_personas()
        for data in personas.values():
            scored = score_turns(data, run(data, winning_questions(data)))
            self.assertTrue(scored["ok"], data["id"])
        dpo = personas["dpo"]
        turns = run(dpo, _DPO)
        self.assertEqual(turns[1]["released"], ["unsigned-ruling"])
        self.assertEqual(turns[2]["released"], ["signed-ruling"])
        self.assertNotIn(str(gold(load("practice"))["quota"]["gpus"]), turns[2]["answer"])
        self.assertEqual(dpo["must_surface"], ("unsigned-ruling",))
        finance = personas["finance"]
        turns = run(finance, _FINANCE)
        self.assertEqual(turns[1]["released"], ["rent-or-buy"])
        self.assertEqual(turns[2]["released"], ["gpu-quota"])
        self.assertNotRegex(turns[2]["answer"], r"\d")
        self.assertEqual(finance["must_surface"], ("rent-or-buy", "double-benefit", "unit-prices"))
        practice = gold(load("practice"))
        memo = (W3D2_WORK / "approach.md").read_text(encoding="utf-8")
        self.assertIn(measurement_block(practice["adapter_hash"], practice["local_sar"]), memo.replace("\r\n", "\n"))


def _suite(folder: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
        cwd=folder,
        capture_output=True,
        text=True,
        check=False,
    )


if __name__ == "__main__":
    unittest.main()
