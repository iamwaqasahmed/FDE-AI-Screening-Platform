"""Module 1, Lesson 3 release, calendar, and the out-of-order demo.

Guards the working-day calendar, the third-day release, and the out-of-order demo.

The calendar test uses the real counter, not the test double. The release tests
write earlier days first and then this day, and they require the earlier packs
and gold files to stay put. The learner pack must match the event stream, keep
the in-force criteria distinct from the draft, and keep due dates and clause ids
out of the lesson notes. The demo may show the arrival pair and must not name
the ordering defect.
"""

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
from alwaha.paths import M01_L03_ROOT, WORKFLOW_ROOT
from alwaha.release.m01_l02 import write_m01_l02
from alwaha.release.m01_l03 import write_m01_l03
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import write_release
from alwaha.world.calendar import WORKING_DAY_COUNT, add_working_days, holiday_dates, is_working_day


class CalendarTests(unittest.TestCase):
    """Catches a counter that treats a weekend or a holiday as a working day, or that
    lands a due date on the wrong side of the weekend.
    """
    def test_friday_and_eid_are_not_working_days(self) -> None:
        """Fails when the weekend day or a holiday counts as a working day, or when the
        span that starts just before the weekend does not land on the next working day.
        """
        # Friday is closed, and so is every date on the holiday list.
        holidays = set(holiday_dates())
        friday = date(2027, 1, 15)
        self.assertEqual(friday.weekday(), 4)
        self.assertFalse(is_working_day(friday, holidays))
        for day in holiday_dates():
            self.assertFalse(is_working_day(day, holidays))
        # Count working days from the Thursday before that Friday. The due date is not a Friday.
        thursday = date(2027, 1, 14)
        self.assertEqual(thursday.weekday(), 3)
        due = add_working_days(thursday, WORKING_DAY_COUNT, holidays)
        self.assertNotEqual(due.weekday(), 4)
        self.assertEqual(due, date(2027, 1, 17))


class ReleaseTests(unittest.TestCase):
    """Catches a third-day pack that drifts, that rewrites an earlier day, or that
    leaks the event gold, the watermark, or the criteria key into the learner side.
    """
    def test_same_seed_matches_and_earlier_days_stay(self) -> None:
        """Fails when a second write disagrees, when an earlier pack or gold file changes,
        or when the event gold is missing from the hidden side or present in the pack.
        The scheduling spec that belongs to a later day must not appear yet.
        """
        # Write the two earlier days first, and remember their fingerprints and gold files.
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            m01_l01, m01_l02, m01_l03, truth = root / "m01_l01", root / "m01_l02", root / "m01_l03", root / "truth"
            write_release(profile, m01_l01, truth)
            write_m01_l02(profile, m01_l02, truth)
            before_m01_l01 = fingerprint(m01_l01)
            before_m01_l02 = fingerprint(m01_l02)
            before_personas = (truth / "personas.json").read_bytes()
            before_approach = (truth / "approach_gold.json").read_bytes()
            # Write this day twice into the same directories.
            first = write_m01_l03(profile, m01_l03, truth)
            second = write_m01_l03(profile, m01_l03, truth)
            # The two writes agree, and neither earlier pack nor its gold files changed.
            self.assertEqual(first, second)
            self.assertEqual(fingerprint(m01_l01), before_m01_l01)
            self.assertEqual(fingerprint(m01_l02), before_m01_l02)
            self.assertEqual((truth / "personas.json").read_bytes(), before_personas)
            self.assertEqual((truth / "approach_gold.json").read_bytes(), before_approach)
            # This day's gold stays hidden. The later day's scheduling spec is not in the pack yet.
            self.assertTrue((truth / "events_gold.json").is_file())
            self.assertFalse((m01_l03 / "events_gold.json").exists())
            self.assertFalse((m01_l03 / "openapi" / "sched-ain.yaml").exists())

    def test_profiles_differ_by_canary(self) -> None:
        """Fails when the practice watermark is missing, repeated, or shared with the small
        pack, or when the two packs share a fingerprint.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice = load("practice")
            small = load("small")
            write_m01_l03(practice, root / "practice", root / "practice-truth")
            write_m01_l03(small, root / "small", root / "small-truth")
            practice_events = (root / "practice" / "events" / "intake.jsonl").read_text(encoding="utf-8")
            small_events = (root / "small" / "events" / "intake.jsonl").read_text(encoding="utf-8")
            self.assertIn(practice.canary(), practice_events)
            self.assertNotIn(practice.canary(), small_events)
            self.assertEqual(practice_events.count(practice.canary()), 1)
            self.assertNotEqual(fingerprint(root / "practice"), fingerprint(root / "small"))

    def test_pack_matches_the_stream_and_the_criteria(self) -> None:
        """Fails when the written event file drifts from the stream, when the out-of-order
        pair or the replay is flattened, when the draft criteria looks in force, or when
        the watermark appears in the gold file or the workflow pages.
        """
        # Write the small pack and read the event file back as rows.
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            write_m01_l03(profile, pack, root / "truth")
            written = [json.loads(line) for line in (pack / "events" / "intake.jsonl").read_text(encoding="utf-8").splitlines()]
            # The file is the stream. The out-of-order pair stays reversed, and the replay appears twice.
            self.assertEqual(written, events(profile.canary()))
            order = [row for row in written if row["referral_id"] == ORDER_REF]
            self.assertEqual([row["sequence"] for row in order], [2, 1])
            self.assertEqual(written.count(next(row for row in written if row["scenario"] == "replay")), 2)
            # The older criteria page is in force. The newer page is still a draft.
            v3 = (pack / "criteria" / "crit-endo-v3.md").read_text(encoding="utf-8")
            v4 = (pack / "criteria" / "crit-endo-v4.md").read_text(encoding="utf-8")
            self.assertIn("status: in_force", v3)
            self.assertIn("status: draft", v4)
            # The Friday due date is in the hidden gold. The watermark is not in that gold.
            gold = json.loads((root / "truth" / "events_gold.json").read_text(encoding="utf-8"))
            friday = next(row for row in gold["scenarios"] if row["scenario"] == "friday")
            self.assertEqual(friday["due"], "2027-01-17")
            self.assertNotIn(profile.canary(), json.dumps(gold))
            # Workflow pages must not carry the watermark either.
            for path in (pack / "workflow").rglob("*"):
                if path.is_file():
                    self.assertNotIn(profile.canary(), path.read_text(encoding="utf-8"))

    def test_notes_do_not_copy_the_key(self) -> None:
        """Fails when lesson notes contain a clause id, the working-day setting, the retry
        setting, or a due date. Also fails when the unfinished worker already knows
        which document is in force, or when the unfinished calendar already knows about
        holidays.
        """
        # Read every lesson note for this day as one string.
        notes = "\n".join(path.read_text(encoding="utf-8") for path in M01_L03_ROOT.glob("README.md"))
        # Clause ids, the working-day setting, the retry setting, and due dates stay out of the notes.
        for doc in criteria_docs():
            self.assertNotIn(doc["clause_id"], notes)
        self.assertNotIn("working_days:", notes)
        self.assertNotIn("retries:", notes)
        for row in scenario_rows("note"):
            if row["due"]:
                self.assertNotIn(row["due"], notes)
        # The unfinished worker does not already know which document is in force.
        skeleton = (WORKFLOW_ROOT / "worker.py").read_text(encoding="utf-8")
        calendar = (WORKFLOW_ROOT / "calendar_count.py").read_text(encoding="utf-8")
        self.assertNotIn("in_force", skeleton)
        # The unfinished calendar still names Friday and does not know about holidays.
        self.assertIn("Friday", calendar)
        self.assertNotIn("holiday", calendar.lower())


class DemoTests(unittest.TestCase):
    """Catches a demo that names the ordering defect or that hides the two arrivals."""
    def test_demo_shows_the_pair_and_does_not_name_it(self) -> None:
        """Fails when the demo's lines are not the two arrivals and the single approval,
        or when it uses the words that would tell the learner the defect's name.
        """
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
