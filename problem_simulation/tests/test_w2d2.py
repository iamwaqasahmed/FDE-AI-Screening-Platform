"""Day 2 of Week 2: the release, the feeds, and the HL7 demo."""

from __future__ import annotations

import json
from contextlib import redirect_stdout
from io import StringIO
import tempfile
import unittest
from pathlib import Path

from alwaha.config.profile import load
from alwaha.demo.hl7 import main as demo_main
from alwaha.engagement.interview import run
from alwaha.engagement.personas import load_personas
from alwaha.engagement.w2d2 import CLOCK, DROPPED, EXTRA, gold, webhook
from alwaha.paths import W2D2_APP, W2D2_ROOT, W2D2_TEMPLATES, W2D2_WORK
from alwaha.release.day2 import write_day2
from alwaha.release.day3 import write_day3
from alwaha.release.day4 import write_day4
from alwaha.release.day5 import write_day5
from alwaha.release.fingerprint import fingerprint
from alwaha.release.w2d1 import write_w2d1
from alwaha.release.w2d2 import write_w2d2
from alwaha.release.write import write_release

_EA = [
    "What is the API strategy?",
    "Do h-nakhl and h-safra still send HL7, and is h-wadi on the private cloud?",
    "Does eref push a webhook subscription now?",
    "Who owns the referral.submitted contract?",
    "Which zone is the integration engine in?",
]
_ACCESS = [
    "No-shows dominate the cost. What does the ledger say?",
    "What share of contact-center calls ask for a referral status?",
    "How is a cancelled visit told by SMS?",
    "Is WhatsApp a new channel, and does a reply survive the session window?",
    "Is the mart wait figure the number you trust at the desk?",
]
_DAY1 = [
    "What is the API strategy?",
    "Do h-nakhl and h-safra still send HL7, and is h-wadi on the private cloud?",
    "Where is the FHIR version notice?",
]


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
            write_day5(profile, packs[4], truth)
            week2 = root / "week2"
            write_w2d1(profile, week2, truth)
            before = (
                tuple(fingerprint(pack) for pack in packs),
                fingerprint(week2),
                (truth / "personas.json").read_bytes(),
                (truth / "approach_gold.json").read_bytes(),
                (truth / "events_gold.json").read_bytes(),
                (truth / "agent_gold.json").read_bytes(),
                (truth / "day5_gold.json").read_bytes(),
                (truth / "w2d1_gold.json").read_bytes(),
            )
            first = write_w2d2(profile, root / "w2d2", truth)
            second = write_w2d2(profile, root / "w2d2", truth)
            self.assertEqual(first, second)
            self.assertEqual(
                before,
                (
                    tuple(fingerprint(pack) for pack in packs),
                    fingerprint(week2),
                    (truth / "personas.json").read_bytes(),
                    (truth / "approach_gold.json").read_bytes(),
                    (truth / "events_gold.json").read_bytes(),
                    (truth / "agent_gold.json").read_bytes(),
                    (truth / "day5_gold.json").read_bytes(),
                    (truth / "w2d1_gold.json").read_bytes(),
                ),
            )
            self.assertTrue((truth / "w2d2_gold.json").is_file())
            self.assertFalse((root / "w2d2" / "w2d2_gold.json").exists())

    def test_profiles_differ_by_canary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_w2d2(practice, root / "practice", root / "practice-truth")
            write_w2d2(small, root / "small", root / "small-truth")
            self.assertEqual(_canary_count(root / "practice", practice.canary()), 1)
            self.assertEqual(_canary_count(root / "small", small.canary()), 1)
            self.assertNotEqual(fingerprint(root / "practice"), fingerprint(root / "small"))

    def test_pack_keeps_the_dropped_field_out(self) -> None:
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            write_w2d2(profile, pack, root / "truth")
            blob = "\n".join(path.read_text(encoding="utf-8") for path in pack.rglob("*") if path.is_file())
            self.assertNotIn(DROPPED, blob)
            self.assertIn(EXTRA, blob)
            self.assertIn(CLOCK, blob)
            written = json.loads((pack / "webhooks" / "referral.submitted.json").read_text(encoding="utf-8"))
            self.assertEqual(written, webhook(profile))
            hidden = json.loads((root / "truth" / "w2d2_gold.json").read_text(encoding="utf-8"))
            self.assertEqual(hidden, gold(profile))
            self.assertEqual(hidden["dropped_field"], DROPPED)
            self.assertNotIn(profile.canary(), json.dumps(hidden))
            lines = [
                json.loads(line)
                for line in (pack / "events" / "session.cancelled.jsonl").read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
            self.assertEqual(len(lines), 3)
            self.assertEqual(lines[0]["event_id"], lines[1]["event_id"])


class DemoTests(unittest.TestCase):
    def test_demo_shows_order_and_not_the_dropped_field(self) -> None:
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "practice"])
        text = stdout.getvalue()
        self.assertEqual(
            text.splitlines(),
            ["file order: sequence 1 stands", "sequence order: sequence 2 stands"],
        )
        for secret in (DROPPED, EXTRA, "thyroid", "ZSS"):
            self.assertNotIn(secret, text)

    def test_notes_do_not_name_the_hidden_fields(self) -> None:
        notes = [path.read_text(encoding="utf-8") for path in W2D2_ROOT.glob("*.md")]
        notes.extend(path.read_text(encoding="utf-8") for path in W2D2_TEMPLATES.glob("*.md"))
        lesson_text = "\n".join(notes)
        for secret in (DROPPED, EXTRA, CLOCK, "thyroid", "ZSS", "CANARY-", "sub-specialty"):
            self.assertNotIn(secret, lesson_text)

    def test_only_the_trap_modules_differ(self) -> None:
        traps = {"intake.py", "cancel.py", "mart.py"}
        for source in W2D2_APP.glob("*.py"):
            copy = W2D2_WORK / "app" / source.name
            if source.name in traps:
                self.assertNotEqual(source.read_bytes(), copy.read_bytes(), source.name)
            else:
                self.assertEqual(source.read_bytes(), copy.read_bytes(), source.name)

    def test_day1_questions_still_land(self) -> None:
        turns = run(load_personas()["ea"], _DAY1)
        self.assertIn("private cloud", turns[1]["answer"])
        self.assertIn("hl7-pair", turns[1]["released"])
        self.assertIn("notices/fhir-v2.md", turns[2]["answer"])
        self.assertEqual(turns[2]["released"], [])

    def test_new_questions_release_no_week1_facts(self) -> None:
        personas = load_personas()
        ea = run(personas["ea"], _EA)
        self.assertEqual(ea[2]["released"], [])
        self.assertIn("pushes", ea[2]["answer"])
        self.assertIn("owned by eref", ea[3]["answer"])
        self.assertEqual(ea[3]["released"], [])
        self.assertIn("zone-hospital", ea[4]["answer"])
        access = run(personas["access-mgr"], _ACCESS)
        self.assertEqual(access[0]["released"], [])
        self.assertIn("reason-mix", access[1]["released"])
        self.assertIn("SMS", access[2]["answer"])
        self.assertEqual(access[2]["released"], [])
        self.assertIn("session window", access[3]["answer"])
        self.assertIn("desk", access[4]["answer"])
        self.assertEqual(personas["ea"]["must_surface"], ("ain-file", "hl7-pair"))
        self.assertEqual(personas["access-mgr"]["must_surface"], ("returns-and-slots", "reason-mix"))


if __name__ == "__main__":
    unittest.main()
