"""Module 1, Lesson 5 release, steering page, and the readout demo.

Guards the steering-day release and the readout demo.

Earlier packs and gold files must survive the write. The failure scenarios and
their order must match the generator, and the answers those scenarios are about
must stay out of the learner pack and the lesson packet. The demo may read the
sponsor's opening line and the question list, and must not reveal the hidden fact.
"""

from __future__ import annotations

import json
from contextlib import redirect_stdout
from io import StringIO
import tempfile
import unittest
from pathlib import Path

from alwaha.agent.failures import FAILURE_ORDER, scenarios
from alwaha.config.profile import load
from alwaha.demo.readout import main as demo_main
from alwaha.engagement.catalog import PERSONAS
from alwaha.engagement.m01_l05 import QUESTIONS
from alwaha.paths import AGENT_ROOT, M01_L05_ROOT
from alwaha.release.m01_l02 import write_m01_l02
from alwaha.release.m01_l03 import write_m01_l03
from alwaha.release.m01_l04 import write_m01_l04
from alwaha.release.m01_l05 import write_m01_l05
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import write_release


def _canary_count(pack: Path, canary: str) -> int:
    """Count watermark hits across every file in a pack.

    Used to require exactly one hit in each profile's pack.
    """
    total = 0
    for path in pack.rglob("*"):
        if path.is_file():
            total += path.read_text(encoding="utf-8").count(canary)
    return total


class ReleaseTests(unittest.TestCase):
    """Catches a steering pack that rewrites an earlier day or that copies an answer
    into the learner files or the lesson notes.
    """
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
            # Fingerprints of the four earlier packs, plus the gold files those days wrote.
            before = (
                tuple(fingerprint(pack) for pack in packs[:4]),
                (truth / "personas.json").read_bytes(),
                (truth / "approach_gold.json").read_bytes(),
                (truth / "events_gold.json").read_bytes(),
                (truth / "agent_gold.json").read_bytes(),
            )
            # Write this lesson twice. The two results must agree, and the earlier lessons must stay as they were.
            first = write_m01_l05(profile, packs[4], truth)
            second = write_m01_l05(profile, packs[4], truth)
            self.assertEqual(first, second)
            self.assertEqual(
                before,
                (
                    tuple(fingerprint(pack) for pack in packs[:4]),
                    (truth / "personas.json").read_bytes(),
                    (truth / "approach_gold.json").read_bytes(),
                    (truth / "events_gold.json").read_bytes(),
                    (truth / "agent_gold.json").read_bytes(),
                ),
            )
            # This day's gold stays on the hidden side.
            self.assertTrue((truth / "m01_l05_gold.json").is_file())
            self.assertFalse((packs[4] / "m01_l05_gold.json").exists())

    def test_profiles_differ_by_canary(self) -> None:
        """Fails when either watermark is missing, repeated, or shared, or when the two
        packs have the same fingerprint.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_m01_l05(practice, root / "practice", root / "practice-truth")
            write_m01_l05(small, root / "small", root / "small-truth")
            self.assertEqual(_canary_count(root / "practice", practice.canary()), 1)
            self.assertEqual(_canary_count(root / "small", small.canary()), 1)
            self.assertNotEqual(fingerprint(root / "practice"), fingerprint(root / "small"))

    def test_pack_keeps_the_answers_out(self) -> None:
        """Fails when the failure file drifts from the generator, when the order file
        drifts, or when an answer phrase appears in the learner pack. The gold file
        must list the same scenarios and must not contain the watermark.
        """
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            write_m01_l05(profile, pack, root / "truth")
            # Read the failure file and compare it, and its order, with the generator.
            written = [
                json.loads(line)
                for line in (pack / "scenarios" / "ds-failures.jsonl").read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
            self.assertEqual(written, scenarios(profile.canary()))
            self.assertEqual(json.loads((pack / "scenarios" / "order.json").read_text(encoding="utf-8")), list(FAILURE_ORDER))
            # Join every learner file. The answer phrases must not appear there.
            blob = "\n".join(path.read_text(encoding="utf-8") for path in pack.rglob("*") if path.is_file())
            self.assertNotIn("16 weeks", blob)
            self.assertNotIn("unsigned ruling", blob)
            # The hidden gold lists the same scenarios and does not contain the watermark.
            gold = json.loads((root / "truth" / "m01_l05_gold.json").read_text(encoding="utf-8"))
            self.assertNotIn(profile.canary(), json.dumps(gold))
            self.assertEqual([row["scenario"] for row in gold["scenarios"]], list(FAILURE_ORDER))

    def test_notes_do_not_copy_the_answers(self) -> None:
        """Fails when lesson notes, templates, or the packet agent contain an answer phrase
        or a watermark prefix. The packet model must still be the unfinished model, not
        a filled one.
        """
        packet = M01_L05_ROOT / "Student_Copy" / "packet"
        notes = [path.read_text(encoding="utf-8") for path in M01_L05_ROOT.glob("README.md")]
        notes.extend(path.read_text(encoding="utf-8") for path in (packet / "templates").glob("*.md"))
        notes.extend(path.read_text(encoding="utf-8") for path in (packet / "agent").glob("*.py"))
        text = "\n".join(notes)
        for secret in ("16 weeks", "unsigned ruling", "CANARY-", "slot-race"):
            self.assertNotIn(secret, text)
        self.assertEqual((packet / "agent" / "model.py").read_text(encoding="utf-8"), (AGENT_ROOT / "model.py").read_text(encoding="utf-8"))


class DemoTests(unittest.TestCase):
    """Catches a readout demo that skips the sponsor's card or that speaks the hidden fact."""
    def test_demo_reads_the_card_and_not_the_hidden_fact(self) -> None:
        """Fails when the first line is not the sponsor's opening line, when the remaining
        lines are not the question list, or when the hidden deadline or the purchase
        fact appears in the output.
        """
        # Run the readout demo and split what it prints into lines.
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "small"])
        text = stdout.getvalue()
        # The first line is the sponsor's opening line. The rest are the question list, numbered.
        card = next(row for row in PERSONAS if row["id"] == "cdo")
        lines = text.splitlines()
        self.assertEqual(lines[0], card["says_first"])
        self.assertEqual(lines[1:], [f"{index}. {question}" for index, question in enumerate(QUESTIONS, start=1)])
        # The hidden deadline and the purchase fact stay out of the output.
        lowered = text.lower()
        self.assertNotIn("16", text)
        self.assertNotIn("unsigned", lowered)
        self.assertNotIn("gpu", lowered)
        self.assertNotIn("purchase", lowered)


if __name__ == "__main__":
    unittest.main()
