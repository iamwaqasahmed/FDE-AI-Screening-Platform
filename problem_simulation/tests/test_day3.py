"""Day 3 release, calendar, and the out-of-order demo."""

from __future__ import annotations

import json
from datetime import date
from io import StringIO
from contextlib import redirect_stdout
import tempfile
import unittest
from pathlib import Path

from alwaha.config.profile import load
from alwaha.demo.order import main as demo_main
from alwaha.events.gold import scenario_rows
from alwaha.events.pages import criteria_docs
from alwaha.events.stream import ORDER_REF, events
from alwaha.paths import DAY3_ROOT, WORKFLOW_ROOT
from alwaha.release.day2 import write_day2
from alwaha.release.day3 import write_day3
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import write_release
from alwaha.world.calendar import WORKING_DAY_COUNT, add_working_days, holiday_dates, is_working_day


class CalendarTests(unittest.TestCase):
    def test_friday_and_eid_are_not_working_days(self) -> None:
        holidays = set(holiday_dates())
        friday = date(2027, 1, 15)
        self.assertEqual(friday.weekday(), 4)
        self.assertFalse(is_working_day(friday, holidays))
        for day in holiday_dates():
            self.assertFalse(is_working_day(day, holidays))
        thursday = date(2027, 1, 14)
        self.assertEqual(thursday.weekday(), 3)
        due = add_working_days(thursday, WORKING_DAY_COUNT, holidays)
        self.assertNotEqual(due.weekday(), 4)
        self.assertEqual(due, date(2027, 1, 17))


class ReleaseTests(unittest.TestCase):
    def test_same_seed_matches_and_earlier_days_stay(self) -> None:
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            day1, day2, day3, truth = root / "day1", root / "day2", root / "day3", root / "truth"
            write_release(profile, day1, truth)
            write_day2(profile, day2, truth)
            before_day1 = fingerprint(day1)
            before_day2 = fingerprint(day2)
            before_personas = (truth / "personas.json").read_bytes()
            before_approach = (truth / "approach_gold.json").read_bytes()
            first = write_day3(profile, day3, truth)
            second = write_day3(profile, day3, truth)
            self.assertEqual(first, second)
            self.assertEqual(fingerprint(day1), before_day1)
            self.assertEqual(fingerprint(day2), before_day2)
            self.assertEqual((truth / "personas.json").read_bytes(), before_personas)
            self.assertEqual((truth / "approach_gold.json").read_bytes(), before_approach)
            self.assertTrue((truth / "events_gold.json").is_file())
            self.assertFalse((day3 / "events_gold.json").exists())
            self.assertFalse((day3 / "openapi" / "sched-ain.yaml").exists())

    def test_profiles_differ_by_canary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice = load("practice")
            small = load("small")
            write_day3(practice, root / "practice", root / "practice-truth")
            write_day3(small, root / "small", root / "small-truth")
            practice_events = (root / "practice" / "events" / "intake.jsonl").read_text(encoding="utf-8")
            small_events = (root / "small" / "events" / "intake.jsonl").read_text(encoding="utf-8")
            self.assertIn(practice.canary(), practice_events)
            self.assertNotIn(practice.canary(), small_events)
            self.assertEqual(practice_events.count(practice.canary()), 1)
            self.assertNotEqual(fingerprint(root / "practice"), fingerprint(root / "small"))

    def test_pack_matches_the_stream_and_the_criteria(self) -> None:
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            write_day3(profile, pack, root / "truth")
            written = [json.loads(line) for line in (pack / "events" / "intake.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertEqual(written, events(profile.canary()))
            order = [row for row in written if row["referral_id"] == ORDER_REF]
            self.assertEqual([row["sequence"] for row in order], [2, 1])
            self.assertEqual(written.count(next(row for row in written if row["scenario"] == "replay")), 2)
            v3 = (pack / "criteria" / "crit-endo-v3.md").read_text(encoding="utf-8")
            v4 = (pack / "criteria" / "crit-endo-v4.md").read_text(encoding="utf-8")
            self.assertIn("status: in_force", v3)
            self.assertIn("status: draft", v4)
            gold = json.loads((root / "truth" / "events_gold.json").read_text(encoding="utf-8"))
            friday = next(row for row in gold["scenarios"] if row["scenario"] == "friday")
            self.assertEqual(friday["due"], "2027-01-17")
            self.assertNotIn(profile.canary(), json.dumps(gold))
            for path in (pack / "workflow").rglob("*"):
                if path.is_file():
                    self.assertNotIn(profile.canary(), path.read_text(encoding="utf-8"))

    def test_notes_do_not_copy_the_key(self) -> None:
        notes = "\n".join(path.read_text(encoding="utf-8") for path in DAY3_ROOT.glob("*.md"))
        for doc in criteria_docs():
            self.assertNotIn(doc["clause_id"], notes)
        self.assertNotIn("working_days:", notes)
        self.assertNotIn("retries:", notes)
        for row in scenario_rows("note"):
            if row["due"]:
                self.assertNotIn(row["due"], notes)
        skeleton = (WORKFLOW_ROOT / "worker.py").read_text(encoding="utf-8")
        calendar = (WORKFLOW_ROOT / "calendar_count.py").read_text(encoding="utf-8")
        self.assertNotIn("in_force", skeleton)
        self.assertIn("Friday", calendar)
        self.assertNotIn("holiday", calendar.lower())


class DemoTests(unittest.TestCase):
    def test_demo_shows_the_pair_and_does_not_name_it(self) -> None:
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "small"])
        text = stdout.getvalue()
        self.assertNotIn("out of order", text.lower())
        self.assertNotIn("defect", text.lower())
        self.assertEqual(
            text.splitlines(),
            ["arrival 1 sequence 2", "arrival 10 sequence 1", "approvals 1"],
        )


if __name__ == "__main__":
    unittest.main()
