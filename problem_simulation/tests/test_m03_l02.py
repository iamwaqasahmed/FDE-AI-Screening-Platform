"""Module 3, Lesson 2: the ruling, the quota, and the registered adapter.

Guards the ruling release, the spend cap, and the registered adapter.

Earlier days must survive the write. This pack carries no watermark. The local
price must sit inside the cap and the external price must sit outside it. Prose
and the register must not contain the cloud hash, the held letters, or the held
messages, while the register must contain the adapter hash. The demo may say
the gateway refused and must not print the watermark. The unfinished packet
tests must fail, and the filled copy must pass. Interviews must release the new
facts without dropping the old required ones.
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
from alwaha.demo.gateway import main as demo_main
from alwaha.engagement.interview import run, score_turns, winning_questions
from alwaha.engagement.personas import load_personas
from alwaha.engagement.m03_l02 import gold, measurement_block
from alwaha.paths import M03_L02_APP, M03_L02_ROOT, M03_L02_TEMPLATES, M03_L02_WORK
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
from alwaha.release.m03_l01 import write_m03_l01
from alwaha.release.m03_l02 import write_m03_l02
from alwaha.release.write import write_release

# Data-protection script. The second and third turns should release the unsigned ruling and then the signature.
_DPO = [
    "How should we handle patient data?",
    "What does the unsigned ruling say about the external model?",
    "Did you sign it?",
]
# Finance script. The quota turn should release the fact and should not contain a digit.
_FINANCE = [
    "Is there a budget line?",
    "Should we rent a GPU or buy one, and how many weeks?",
    "What is the quota and the cap?",
]
# Shell modules that must differ from the filled copy.
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
# Packet tests that must stay byte-identical. The shell fails because the modules are unfinished, not because the tests changed.
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
    """Count watermark hits across every file in a pack.

    This day's pack is supposed to have none.
    """
    total = 0
    for path in pack.rglob("*"):
        if path.is_file():
            total += path.read_text(encoding="utf-8").count(canary)
    return total


def _prose(pack: Path) -> str:
    """Join the markdown and the manifest files so a held letter in prose can be told
    apart from one that never shipped.
    """
    chunks = []
    for path in pack.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".yaml", ".yml"}:
            chunks.append(path.read_text(encoding="utf-8"))
    return "\n".join(chunks)


class ReleaseTests(unittest.TestCase):
    """Catches a pack that rewrites an earlier day, that leaks a held letter, or that
    puts the local and external prices on the wrong sides of the cap.
    """
    def test_same_seed_matches_and_earlier_days_stay(self) -> None:
        """Fails when a second write disagrees, when an earlier pack or the previous gold
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
            week2 = [root / f"m02l{index}" for index in range(1, 6)]
            write_m02_l01(profile, week2[0], truth)
            write_m02_l02(profile, week2[1], truth)
            write_m02_l03(profile, week2[2], truth)
            write_m02_l04(profile, week2[3], truth)
            write_m02_l05(profile, week2[4], truth)
            write_m03_l01(profile, root / "m03_l01", truth)
            # Fingerprints of the earlier packs, including yesterday, plus the previous gold.
            before = (
                tuple(fingerprint(pack) for pack in packs),
                tuple(fingerprint(pack) for pack in week2),
                fingerprint(root / "m03_l01"),
                (truth / "personas.json").read_bytes(),
                (truth / "m03_l01_gold.json").read_bytes(),
            )
            # Write this lesson twice. The two results must agree, and the earlier lessons must stay as they were.
            first = write_m03_l02(profile, root / "m03_l02", truth)
            again = write_m03_l02(profile, root / "m03_l02", truth)
            self.assertEqual(first, again)
            self.assertEqual(
                before,
                (
                    tuple(fingerprint(pack) for pack in packs),
                    tuple(fingerprint(pack) for pack in week2),
                    fingerprint(root / "m03_l01"),
                    (truth / "personas.json").read_bytes(),
                    (truth / "m03_l01_gold.json").read_bytes(),
                ),
            )
            # This day's gold stays on the hidden side.
            self.assertTrue((truth / "m03_l02_gold.json").is_file())
            self.assertFalse((root / "m03_l02" / "m03_l02_gold.json").exists())

    def test_profiles_differ_and_the_cap_splits_the_prices(self) -> None:
        """Fails when a pack contains a watermark, when the fingerprints match, or when
        either profile's local price exceeds the cap or its external price does not.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_m03_l02(practice, root / "practice", root / "practice-truth")
            write_m03_l02(small, root / "small", root / "small-truth")
            self.assertEqual(_canary_count(root / "practice", practice.canary()), 0)
            self.assertEqual(_canary_count(root / "small", small.canary()), 0)
            self.assertNotEqual(fingerprint(root / "practice"), fingerprint(root / "small"))
            for profile, folder in ((practice, "practice-truth"), (small, "small-truth")):
                hidden = json.loads((root / folder / "m03_l02_gold.json").read_text(encoding="utf-8"))
                self.assertEqual(hidden, gold(profile))
                self.assertLessEqual(hidden["local_sar"], hidden["cap"]["max_sar"])
                self.assertGreater(hidden["external_sar"], hidden["cap"]["max_sar"])

    def test_prose_and_the_register_keep_the_secrets_out(self) -> None:
        """Fails when prose or the gold file contains the watermark, when the register
        contains the cloud hash or lacks the adapter hash, or when a held letter, held
        message, or preference draft appears anywhere in the pack.
        """
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            write_m03_l02(profile, pack, root / "truth")
            # Read the gold, the prose, the register, and every learner file.
            hidden = json.loads((root / "truth" / "m03_l02_gold.json").read_text(encoding="utf-8"))
            prose = _prose(pack)
            register = (pack / "registry" / "reg-models.json").read_text(encoding="utf-8")
            blob = "\n".join(path.read_text(encoding="utf-8") for path in pack.rglob("*") if path.is_file())
            # Prose and the gold keep the watermark out. The register has the adapter hash and not the cloud hash.
            self.assertNotIn(profile.canary(), prose)
            self.assertNotIn(profile.canary(), json.dumps(hidden))
            self.assertNotIn(hidden["cloud_hash"], register)
            self.assertIn(hidden["adapter_hash"], register)
            # Held letters, held messages, and the preference draft stay out of the pack.
            for row in hidden["held_letters"]:
                self.assertNotIn(row["item_id"], blob)
                self.assertNotIn(row["text"], blob)
            for row in hidden["held_messages"]:
                self.assertNotIn(row["message_id"], blob)
            self.assertNotIn(hidden["held_pref"]["draft"], blob)


class DemoTests(unittest.TestCase):
    """Catches a demo or a lesson that prints a seed value, a module that was not
    changed, a shell suite that passes, or an interview that drops a fact.
    """
    def test_demo_refuses_without_printing_the_watermark(self) -> None:
        """Fails when the demo does not report the gateway refusal, or when it prints the
        watermark.
        """
        profile = load("practice")
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "practice"])
        text = stdout.getvalue()
        self.assertEqual(text.splitlines(), ["the gateway refused the prompt"])
        self.assertNotIn(profile.canary(), text)

    def test_lessons_do_not_state_the_seed_values(self) -> None:
        """Fails when lesson notes contain a watermark or an adapter or cloud hash, or a
        held letter id.
        """
        notes = [path.read_text(encoding="utf-8") for path in M03_L02_ROOT.glob("README.md")]
        notes.extend(path.read_text(encoding="utf-8") for path in M03_L02_TEMPLATES.glob("*.md"))
        lesson_text = "\n".join(notes)
        hidden = gold(load("practice"))
        small = gold(load("small"))
        self.assertNotIn(load("practice").canary(), lesson_text)
        for secret in (hidden["adapter_hash"], hidden["cloud_hash"], small["adapter_hash"], small["cloud_hash"]):
            self.assertNotIn(secret, lesson_text)
        for row in hidden["held_letters"]:
            self.assertNotIn(row["item_id"], lesson_text)

    def test_modules_differ_and_only_the_copy_passes(self) -> None:
        """Fails when a shell module matches the filled copy, when a packet test was
        rewritten, when the filled suite fails, or when the shell suite passes.
        """
        packet = M03_L02_APP.parent
        for name in _APP:
            shell = (M03_L02_APP / name).read_bytes()
            filled = (M03_L02_WORK / "app" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        for name in _TESTS:
            shell = (packet / "tests" / name).read_bytes()
            filled = (M03_L02_WORK / "tests" / name).read_bytes()
            self.assertEqual(shell, filled, name)
        work = _suite(M03_L02_WORK)
        shell = _suite(packet)
        self.assertEqual(work.returncode, 0, work.stdout + work.stderr)
        self.assertNotEqual(shell.returncode, 0, shell.stdout + shell.stderr)

    def test_interviews_release_the_new_facts_and_keep_the_old_ones(self) -> None:
        """Fails when a winning script no longer completes a persona, when the ruling or
        the quota facts do not surface, or when an answer contains a digit. The memo
        must still carry the measurement block for the practice adapter.
        """
        # Every persona's winning script still completes.
        personas = load_personas()
        for data in personas.values():
            scored = score_turns(data, run(data, winning_questions(data)))
            self.assertTrue(scored["ok"], data["id"])
        # The privacy officer's new turns release the ruling facts and do not state the quota count.
        dpo = personas["dpo"]
        turns = run(dpo, _DPO)
        self.assertEqual(turns[1]["released"], ["unsigned-ruling"])
        self.assertEqual(turns[2]["released"], ["signed-ruling"])
        self.assertNotIn(str(gold(load("practice"))["quota"]["gpus"]), turns[2]["answer"])
        self.assertEqual(dpo["must_surface"], ("unsigned-ruling",))
        # Finance releases the rent-or-buy and quota facts. The quota answer has no digit.
        finance = personas["finance"]
        turns = run(finance, _FINANCE)
        self.assertEqual(turns[1]["released"], ["rent-or-buy"])
        self.assertEqual(turns[2]["released"], ["gpu-quota"])
        self.assertNotRegex(turns[2]["answer"], r"\d")
        self.assertEqual(finance["must_surface"], ("rent-or-buy", "double-benefit", "unit-prices"))
        # The memo still carries the measurement block for the practice adapter.
        practice = gold(load("practice"))
        memo = (M03_L02_WORK / "approach.md").read_text(encoding="utf-8")
        self.assertIn(measurement_block(practice["adapter_hash"], practice["local_sar"]), memo.replace("\r\n", "\n"))


def _suite(folder: Path) -> subprocess.CompletedProcess[str]:
    """Run a packet's own unit tests and return the process result without raising.

    The caller decides whether a non-zero exit is the failure or the expected outcome.
    """
    return subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
        cwd=folder,
        capture_output=True,
        text=True,
        check=False,
    )


if __name__ == "__main__":
    unittest.main()
