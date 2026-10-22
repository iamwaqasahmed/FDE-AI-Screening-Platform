"""Day 2 release and the four baselines."""

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

FAMILY_WORDS = ("no-model", "classical-ml", "extract", "retrieve", "agent", "forecast", "blocked")
FAMILY_PATTERN = re.compile("|".join(rf"(?<![a-z-]){re.escape(word)}(?![a-z-])" for word in FAMILY_WORDS))
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
    def test_same_seed_matches_and_day1_stays(self) -> None:
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
        with self.assertRaises(SystemExit):
            build_main(["--release", "rel-nope"])


class SampleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        write_day2(self.profile, self.pack, self.truth)
        self.measured = measure_pack(self.pack)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_dna_split_and_hidden_column(self) -> None:
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
        raw = json.loads((self.truth / "sample_metrics.json").read_text(encoding="utf-8"))
        intents = {row["id"]: row["intent"] for row in raw["message_intents"]}
        with (self.pack / "samples" / "ds-messages.csv").open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            self.assertNotIn("intent", reader.fieldnames or [])
            missed = [row for row in reader if intents[row["message_id"]] == "status" and "status" not in row["text"].lower()]
        self.assertTrue(missed)

    def test_prices_and_leader_pages(self) -> None:
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
    return subprocess.run(
        [sys.executable, str(BASELINES_ROOT / args[0]), *args[1:]],
        check=True,
        capture_output=True,
        text=True,
    )


if __name__ == "__main__":
    unittest.main()
