"""Day 5 release, steering page, and the readout demo."""

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
from alwaha.engagement.day5 import QUESTIONS
from alwaha.paths import AGENT_ROOT, DAY5_ROOT
from alwaha.release.day2 import write_day2
from alwaha.release.day3 import write_day3
from alwaha.release.day4 import write_day4
from alwaha.release.day5 import write_day5
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import write_release


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
            before = (
                tuple(fingerprint(pack) for pack in packs[:4]),
                (truth / "personas.json").read_bytes(),
                (truth / "approach_gold.json").read_bytes(),
                (truth / "events_gold.json").read_bytes(),
                (truth / "agent_gold.json").read_bytes(),
            )
            first = write_day5(profile, packs[4], truth)
            second = write_day5(profile, packs[4], truth)
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
            self.assertTrue((truth / "day5_gold.json").is_file())
            self.assertFalse((packs[4] / "day5_gold.json").exists())

    def test_profiles_differ_by_canary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_day5(practice, root / "practice", root / "practice-truth")
            write_day5(small, root / "small", root / "small-truth")
            self.assertEqual(_canary_count(root / "practice", practice.canary()), 1)
            self.assertEqual(_canary_count(root / "small", small.canary()), 1)
            self.assertNotEqual(fingerprint(root / "practice"), fingerprint(root / "small"))

    def test_pack_keeps_the_answers_out(self) -> None:
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            write_day5(profile, pack, root / "truth")
            written = [
                json.loads(line)
                for line in (pack / "scenarios" / "ds-failures.jsonl").read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
            self.assertEqual(written, scenarios(profile.canary()))
            self.assertEqual(json.loads((pack / "scenarios" / "order.json").read_text(encoding="utf-8")), list(FAILURE_ORDER))
            blob = "\n".join(path.read_text(encoding="utf-8") for path in pack.rglob("*") if path.is_file())
            self.assertNotIn("16 weeks", blob)
            self.assertNotIn("unsigned ruling", blob)
            gold = json.loads((root / "truth" / "day5_gold.json").read_text(encoding="utf-8"))
            self.assertNotIn(profile.canary(), json.dumps(gold))
            self.assertEqual([row["scenario"] for row in gold["scenarios"]], list(FAILURE_ORDER))

    def test_notes_do_not_copy_the_answers(self) -> None:
        notes = [path.read_text(encoding="utf-8") for path in DAY5_ROOT.glob("*.md")]
        notes.extend(path.read_text(encoding="utf-8") for path in (DAY5_ROOT / "templates").glob("*.md"))
        notes.extend(path.read_text(encoding="utf-8") for path in (DAY5_ROOT / "agent").glob("*.py"))
        text = "\n".join(notes)
        for secret in ("16 weeks", "unsigned ruling", "CANARY-", "slot-race"):
            self.assertNotIn(secret, text)
        self.assertEqual((DAY5_ROOT / "agent" / "model.py").read_text(encoding="utf-8"), (AGENT_ROOT / "model.py").read_text(encoding="utf-8"))


class DemoTests(unittest.TestCase):
    def test_demo_reads_the_card_and_not_the_hidden_fact(self) -> None:
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "small"])
        text = stdout.getvalue()
        card = next(row for row in PERSONAS if row["id"] == "cdo")
        lines = text.splitlines()
        self.assertEqual(lines[0], card["says_first"])
        self.assertEqual(lines[1:], [f"{index}. {question}" for index, question in enumerate(QUESTIONS, start=1)])
        lowered = text.lower()
        self.assertNotIn("16", text)
        self.assertNotIn("unsigned", lowered)
        self.assertNotIn("gpu", lowered)
        self.assertNotIn("purchase", lowered)


if __name__ == "__main__":
    unittest.main()
