"""Day 1 of Week 2: the release, the notice, and the FHIR demo.

Guards the first integration release, the version notice, and the record-read demo.

Earlier days are written first and must not change. The learner pack must keep
the removed field out while still carrying the clinic name and the field that
replaced it. The demo may show which client fails and must not name the removed
field. Lesson notes must not name it either, except the unfinished client, which
still contains it on purpose. The enterprise-architect questions must point at
the notice without releasing a new fact.
"""

from __future__ import annotations

import json
from contextlib import redirect_stdout
from io import StringIO
import tempfile
import unittest
from pathlib import Path

from alwaha.config.profile import load
from alwaha.demo.fhir import main as demo_main
from alwaha.engagement.interview import run
from alwaha.engagement.personas import load_personas
from alwaha.engagement.w2d1 import CLINIC, FIELD, REMOVED, gold, his_wadi_spec, scenario
from alwaha.paths import W2D1_APP, W2D1_ROOT, W2D1_TEMPLATES, W2D1_WORK
from alwaha.release.day2 import write_day2
from alwaha.release.day3 import write_day3
from alwaha.release.day4 import write_day4
from alwaha.release.day5 import write_day5
from alwaha.release.fingerprint import fingerprint
from alwaha.release.w2d1 import write_w2d1
from alwaha.release.write import write_release

# Script played at the enterprise architect. The test checks which facts those turns release.
_QUESTIONS = [
    "What is the API strategy?",
    "Do h-nakhl and h-safra still send HL7, and is h-wadi on the private cloud?",
    "Where is the FHIR version notice?",
]


def _canary_count(pack: Path, canary: str) -> int:
    """Count watermark hits across every file in a pack.

    Each profile's pack should carry its own watermark once.
    """
    total = 0
    for path in pack.rglob("*"):
        if path.is_file():
            total += path.read_text(encoding="utf-8").count(canary)
    return total


class ReleaseTests(unittest.TestCase):
    """Catches a pack that rewrites an earlier day, shares a watermark, or publishes
    the removed field.
    """
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
            before = (
                tuple(fingerprint(pack) for pack in packs),
                (truth / "personas.json").read_bytes(),
                (truth / "approach_gold.json").read_bytes(),
                (truth / "events_gold.json").read_bytes(),
                (truth / "agent_gold.json").read_bytes(),
                (truth / "day5_gold.json").read_bytes(),
            )
            week2 = root / "week2"
            first = write_w2d1(profile, week2, truth)
            second = write_w2d1(profile, week2, truth)
            self.assertEqual(first, second)
            self.assertEqual(
                before,
                (
                    tuple(fingerprint(pack) for pack in packs),
                    (truth / "personas.json").read_bytes(),
                    (truth / "approach_gold.json").read_bytes(),
                    (truth / "events_gold.json").read_bytes(),
                    (truth / "agent_gold.json").read_bytes(),
                    (truth / "day5_gold.json").read_bytes(),
                ),
            )
            self.assertTrue((truth / "w2d1_gold.json").is_file())
            self.assertFalse((week2 / "w2d1_gold.json").exists())

    def test_profiles_differ_by_canary(self) -> None:
        """Fails when either watermark is missing, repeated, or shared, or when the
        fingerprints match.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_w2d1(practice, root / "practice", root / "practice-truth")
            write_w2d1(small, root / "small", root / "small-truth")
            self.assertEqual(_canary_count(root / "practice", practice.canary()), 1)
            self.assertEqual(_canary_count(root / "small", small.canary()), 1)
            self.assertNotEqual(fingerprint(root / "practice"), fingerprint(root / "small"))

    def test_pack_keeps_the_removed_field_out(self) -> None:
        """Fails when the removed field or the old clinic code appears in the learner pack,
        when the replacement clinic or field is missing, or when the status scenario or
        the hidden gold drifts. The watermark must stay out of the gold file, and the
        shipped spec must match the generator.
        """
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            write_w2d1(profile, pack, root / "truth")
            blob = "\n".join(path.read_text(encoding="utf-8") for path in pack.rglob("*") if path.is_file())
            self.assertNotIn(REMOVED, blob)
            self.assertNotIn("END-01", blob)
            self.assertIn(CLINIC, blob)
            self.assertIn(FIELD, blob)
            written = json.loads((pack / "scenarios" / "status.json").read_text(encoding="utf-8"))
            self.assertEqual(written, scenario(profile))
            hidden = json.loads((root / "truth" / "w2d1_gold.json").read_text(encoding="utf-8"))
            self.assertEqual(hidden, gold(profile))
            self.assertEqual(hidden["removed_field"], REMOVED)
            self.assertNotIn(profile.canary(), json.dumps(hidden))
            self.assertEqual((pack / "openapi" / "his-wadi.yaml").read_text(encoding="utf-8"), his_wadi_spec())


class DemoTests(unittest.TestCase):
    """Catches a demo, a lesson, or an interview that reveals the removed field, and a
    generated client that no longer matches the filled work copy.
    """
    def test_demo_shows_the_failure_and_not_the_field(self) -> None:
        """Fails when the demo does not show the old client failing and the new client
        succeeding, or when it names the removed field, the clinic, or the old code.
        """
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "practice"])
        text = stdout.getvalue()
        self.assertEqual(
            text.splitlines(),
            ["v1 client: his-wadi read failed", "v2 client: his-wadi read ok"],
        )
        self.assertNotIn(REMOVED, text)
        self.assertNotIn(CLINIC, text)
        self.assertNotIn("END-01", text)

    def test_notes_do_not_name_the_removed_field(self) -> None:
        """Fails when lesson notes or templates name the removed field, the clinic, the old
        code, the level of assurance, or a watermark prefix. The unfinished client is
        the one place that must still contain the removed field.
        """
        notes = [path.read_text(encoding="utf-8") for path in W2D1_ROOT.glob("*.md")]
        notes.extend(path.read_text(encoding="utf-8") for path in W2D1_TEMPLATES.glob("*.md"))
        lesson_text = "\n".join(notes)
        for secret in (REMOVED, CLINIC, "END-01", "loa-2", "CANARY-"):
            self.assertNotIn(secret, lesson_text)
        everything = "\n".join(path.read_text(encoding="utf-8") for path in W2D1_ROOT.rglob("*.md"))
        self.assertNotIn(REMOVED, everything)
        self.assertNotIn("END-01", everything)
        self.assertIn(REMOVED, (W2D1_APP / "client.py").read_text(encoding="utf-8"))

    def test_generator_matches_the_work_client(self) -> None:
        """Fails when the filled client is not what the generator renders from the spec, or
        when any other app module differs between the generator tree and the work copy.
        The client itself must differ, because the work copy is the fixed one.
        """
        import importlib.util

        path = W2D1_APP / "generate.py"
        spec = importlib.util.spec_from_file_location("w2d1_generate_test", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        expected = module.render(module.fields(his_wadi_spec()))
        self.assertEqual((W2D1_WORK / "app" / "client.py").read_text(encoding="utf-8"), expected)
        for source in W2D1_APP.glob("*.py"):
            copy = W2D1_WORK / "app" / source.name
            if source.name == "client.py":
                self.assertNotEqual(source.read_bytes(), copy.read_bytes())
            else:
                self.assertEqual(source.read_bytes(), copy.read_bytes())

    def test_ea_points_at_the_notice_without_a_new_fact(self) -> None:
        """Fails when the architect does not mention the private cloud or the notice, when
        the notice turn releases a fact, or when that answer names the removed field.
        """
        turns = run(load_personas()["ea"], _QUESTIONS)
        self.assertIn("private cloud", turns[1]["answer"])
        self.assertIn("hl7-pair", turns[1]["released"])
        self.assertIn("notices/fhir-v2.md", turns[2]["answer"])
        self.assertEqual(turns[2]["released"], [])
        self.assertNotIn(REMOVED, turns[2]["answer"])


if __name__ == "__main__":
    unittest.main()
