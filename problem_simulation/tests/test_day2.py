"""Day 2 release and the four baselines.

Guards the second-day release, the sample measurements, and the four baseline scripts.

Writing this day must be stable and must leave the first day's pack and persona
file untouched. The gold approach file stays on the hidden side. The sample tests
use one small pack and the measurements taken from it. They catch a leaked label,
a family word in the learner pack, a baseline script that prints the wrong kind
of number, and a demo that names the split defect.
"""

from __future__ import annotations

import csv
import io
import json
import re
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from alwaha.build import main as build_main
from alwaha.config.profile import load
from alwaha.demo.split import main as demo_main
from alwaha.paths import BASELINES_ROOT
from alwaha.release.day2 import write_day2
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import write_release
from alwaha.samples.measure import measure_pack
from day2_memos import grab

# Method-family names that must not appear in the learner pack. The pattern matches them as whole words.
FAMILY_WORDS = ("no-model", "classical-ml", "extract", "retrieve", "agent", "forecast", "blocked")
FAMILY_PATTERN = re.compile("|".join(rf"(?<![a-z-]){re.escape(word)}(?![a-z-])" for word in FAMILY_WORDS))
# Every key the price sheet must contain. The test checks the set of keys, not a copied amount.
PRICE_KEYS = {
    "cost.slot_missed",
    "cost.return_cycle",
    "cost.coordinator_hour",
    "cost.call_minute",
    "cost.sms",
    "cost.wa_template",
    "cost.label",
    "cost.gpu_hour_rent",
    "cost.gpu_buy",
    "price.ext_large_per_1k",
    "price.local_per_1k",
    "harm.week_waiting",
}


class ReleaseTests(unittest.TestCase):
    """Catches a second-day pack that is unstable, that rewrites the first day, or that
    publishes the approach gold beside the samples.
    """
    def test_same_seed_matches_and_day1_stays(self) -> None:
        """Fails when a second write disagrees with the first, when the first day's pack or
        persona file changes, or when the approach gold is missing from the hidden side
        or present in the learner pack.
        """
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            day1, day2, truth = root / "day1", root / "day2", root / "truth"
            write_release(profile, day1, truth)
            before_pack = fingerprint(day1)
            before_personas = (truth / "personas.json").read_bytes()
            first = write_day2(profile, day2, truth)
            second = write_day2(profile, day2, truth)
            self.assertEqual(first, second)
            self.assertEqual(fingerprint(day1), before_pack)
            self.assertEqual((truth / "personas.json").read_bytes(), before_personas)
            self.assertTrue((truth / "approach_gold.json").is_file())
            self.assertFalse((day2 / "approach_gold.json").exists())

    def test_profiles_differ(self) -> None:
        """Fails when practice and small write the same fingerprint, or when the practice
        watermark shows up in the small letter sample.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice = write_day2(load("practice"), root / "practice", root / "practice-truth")
            small = write_day2(load("small"), root / "small", root / "small-truth")
            self.assertNotEqual(practice, small)
            practice_letter = (root / "practice" / "samples" / "ds-letters.md").read_text(encoding="utf-8")
            small_letter = (root / "small" / "samples" / "ds-letters.md").read_text(encoding="utf-8")
            self.assertIn(load("practice").canary(), practice_letter)
            self.assertNotIn(load("practice").canary(), small_letter)

    def test_unknown_release_exits(self) -> None:
        """Fails when the build command accepts a release name it does not know."""
        with self.assertRaises(SystemExit):
            build_main(["--release", "rel-nope"])


class SampleTests(unittest.TestCase):
    """Catches a sample pack whose measurements, labels, prices, or baseline output drifted.

    The fixture is one small second-day pack plus the measurement dict taken from it.
    Prices, the no-show page, and the leader pages are read from that pack. The
    baseline scripts are the ones shipped for learners, run against those samples.
    """
    def setUp(self) -> None:
        """Write a temporary small pack and measure it.

        Later tests read both the files and the measurement dict, so a change in either
        place is visible here.
        """
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        write_day2(self.profile, self.pack, self.truth)
        self.measured = measure_pack(self.pack)

    def tearDown(self) -> None:
        """Delete the temporary pack."""
        self.tmp.cleanup()

    def test_dna_split_and_hidden_column(self) -> None:
        """Fails when the person-level no-show figure collapses into the row-level figure,
        when the hidden final-status column disagrees with the attendance flag, or when
        the learner baseline script can see that column.
        """
        self.assertEqual(self.measured["p-dna"], "0.0000")
        self.assertEqual(self.measured["dna_row"], "0.7692")
        self.assertGreater(int(self.measured["dna_shared"]), 0)
        self.assertLess(float(self.measured["p-forecast"]), float(self.measured["demand_mean"]))
        with (self.pack / "samples" / "ds-dna.csv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertIn("appointment_status_final", rows[0])
        for row in rows:
            expected = "dna" if row["did_not_attend"] == "1" else "seen"
            self.assertEqual(row["appointment_status_final"], expected)
        script = (BASELINES_ROOT / "dna.py").read_text(encoding="utf-8")
        self.assertNotIn("appointment_status_final", script)

    def test_messages_hide_intent_and_miss_a_status(self) -> None:
        """Fails when the message sample still has an intent column, or when every status
        message is obvious from its wording.

        The hidden intent list is what makes a missed status detectable. The learner
        file must not carry that column.
        """
        raw = json.loads((self.truth / "sample_metrics.json").read_text(encoding="utf-8"))
        intents = {row["id"]: row["intent"] for row in raw["message_intents"]}
        with (self.pack / "samples" / "ds-messages.csv").open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            self.assertNotIn("intent", reader.fieldnames or [])
            missed = [row for row in reader if intents[row["message_id"]] == "status" and "status" not in row["text"].lower()]
        self.assertTrue(missed)

    def test_prices_and_leader_pages(self) -> None:
        """Fails when the price sheet is missing a key, when the external or purchase price
        is not the more expensive of its pair, when the leader pages lose the booking
        date or the vendor's containment claim, or when a family word or a planted rate
        leaks into any learner file.
        """
        with (self.pack / "finance" / "prices.csv").open(encoding="utf-8", newline="") as handle:
            prices = {row["key"]: int(row["sar"]) for row in csv.DictReader(handle)}
        self.assertEqual(set(prices), PRICE_KEYS)
        self.assertGreater(prices["price.ext_large_per_1k"], prices["price.local_per_1k"])
        self.assertGreater(prices["cost.gpu_buy"], prices["cost.gpu_hour_rent"])
        access = self.pack / "extracts" / "access-costs.md"
        self.assertGreater(int(grab(access, r"no-shows \| (\d+)")), int(grab(access, r"returned referrals \| (\d+)")))
        dashboard = (self.pack / "extracts" / "dashboard.md").read_text(encoding="utf-8")
        vendor = (self.pack / "extracts" / "vendor-note.md").read_text(encoding="utf-8")
        self.assertIn("booking_date", dashboard)
        self.assertIn("not the Al-Waha Health Cluster", vendor)
        self.assertIn("70 percent", vendor)
        for path in self.pack.rglob("*"):
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            for rate in ("27%", "18%", "22%", "58%", "9%"):
                self.assertNotIn(rate, text)
            self.assertIsNone(FAMILY_PATTERN.search(text.lower()), path.as_posix())

    def test_cli_prints_the_baseline(self) -> None:
        """Fails when a baseline script prints a different figure, or a different method
        name, than the measurement of the pack it was given.
        """
        samples = self.pack / "samples"
        cases = (
            (["dna.py", str(samples / "ds-dna.csv"), "--split", "person"], f"person {self.measured['p-dna']}"),
            (["messages.py", str(samples / "ds-messages.csv")], f"keyword {self.measured['p-status']}"),
            (["letters.py", str(samples / "ds-letters.md")], f"filled {self.measured['p-bounce']}"),
        )
        for args, expected in cases:
            completed = _run(args)
            self.assertEqual(completed.stdout.strip(), expected)
        demand = _run(["demand.py", str(samples / "ds-demand.csv")])
        self.assertIn(f"seasonal {self.measured['p-forecast']}", demand.stdout)
        self.assertIn(f"mean {self.measured['demand_mean']}", demand.stdout)

    def test_demo_does_not_name_the_split_defect(self) -> None:
        """Fails when the demo names the leak or the hidden column, or when the row figure
        is not the larger of the two splits it prints.
        """
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "small"])
        text = stdout.getvalue()
        self.assertNotIn("leak", text.lower())
        self.assertNotIn("appointment_status", text)
        lines = dict(line.split() for line in text.splitlines())
        self.assertGreater(float(lines["row"]), float(lines["person"]))
        self.assertGreater(int(lines["shared"]), 0)


def _run(args: list[str]) -> subprocess.CompletedProcess[str]:
    """Run one baseline script and capture its text.

    A non-zero exit fails the case. The caller compares the text with the measurement.
    """
    return subprocess.run(
        [sys.executable, str(BASELINES_ROOT / args[0]), *args[1:]],
        check=True,
        capture_output=True,
        text=True,
    )


if __name__ == "__main__":
    unittest.main()
