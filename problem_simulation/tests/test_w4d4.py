"""Day 4 of Week 4: the site drill, the insurance outage, and rent versus buy."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from alwaha.config.profile import load
from alwaha.demo.drill import main as demo_main
from alwaha.engagement.interview import run
from alwaha.engagement.personas import load_personas
from alwaha.engagement.w4d3_rows import BACKLOG
from alwaha.engagement.w4d4 import gold
from alwaha.engagement.w4d4_rows import HOSPITALS, PURCHASE_WEEKS, replicas
from alwaha.paths import W4D4_APP, W4D4_ROOT
from alwaha.release.fingerprint import fingerprint
from alwaha.release.w4d3 import write_w4d3
from alwaha.release.w4d4 import write_w4d4

_APP = ("replicas.py", "route.py", "failover.py", "hashes.py", "breaker.py", "degrade.py", "procure.py", "hospitals.py")
_TEXT = {".md", ".py", ".yml", ".yaml", ".json", ".txt"}


def _blob(pack: Path) -> str:
    chunks = []
    for path in pack.rglob("*"):
        if path.is_file():
            chunks.append(path.read_text(encoding="utf-8"))
    return "\n".join(chunks)


def _lines(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _suite(folder: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
        cwd=folder,
        capture_output=True,
        text=True,
        check=False,
    )


class ReleaseTests(unittest.TestCase):
    def test_same_seed_matches_and_day_3_stays(self) -> None:
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            truth = root / "truth"
            write_w4d3(profile, root / "w4d3", truth)
            before = fingerprint(root / "w4d3")
            first = write_w4d4(profile, root / "w4d4", truth)
            again = write_w4d4(profile, root / "w4d4", truth)
            self.assertEqual(first, again)
            self.assertEqual(before, fingerprint(root / "w4d3"))
            self.assertTrue((truth / "w4d4_gold.json").is_file())
            self.assertFalse((root / "w4d4" / "w4d4_gold.json").exists())

    def test_profiles_differ_and_the_split_stays_out(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_w4d4(practice, root / "practice" / "pack", root / "practice-truth")
            write_w4d4(small, root / "small" / "pack", root / "small-truth")
            practice_blob = _blob(root / "practice" / "pack")
            small_blob = _blob(root / "small" / "pack")
            practice_gold = json.loads((root / "practice-truth" / "w4d4_gold.json").read_text(encoding="utf-8"))
            small_gold = json.loads((root / "small-truth" / "w4d4_gold.json").read_text(encoding="utf-8"))
            self.assertNotIn(practice.canary(), practice_blob)
            self.assertNotIn(small.canary(), small_blob)
            self.assertNotIn("w4d4_gold", practice_blob)
            for shown in (practice_gold, small_gold):
                self.assertNotIn(str(shown["local_sar"]), practice_blob if shown is practice_gold else small_blob)
                self.assertNotIn(shown["buy_arrives"], practice_blob if shown is practice_gold else small_blob)
                self.assertNotIn(shown["rent_arrives"], practice_blob if shown is practice_gold else small_blob)
                self.assertEqual(shown["route"], "rent")
                self.assertGreater(shown["buy_arrives"], shown["deadline"])
                self.assertLessEqual(shown["rent_arrives"], shown["deadline"])
                self.assertEqual(sum(shown["hospital_sar"].values()), shown["local_sar"])
                self.assertEqual(sorted(shown["hospital_sar"]), sorted(HOSPITALS))
            self.assertNotEqual(practice_gold["budget_seconds"], small_gold["budget_seconds"])
            self.assertNotEqual(practice_gold["rent_days"], small_gold["rent_days"])
            self.assertNotEqual(practice_gold["hospital_sar"], small_gold["hospital_sar"])
            self.assertNotEqual(practice_gold["lookalike_hash"], small_gold["lookalike_hash"])
            self.assertEqual(practice_gold, gold(practice))
            self.assertEqual(small_gold, gold(small))
            pack = root / "practice" / "pack"
            drill = json.loads((pack / "drill" / "site-a.json").read_text(encoding="utf-8"))
            self.assertEqual(drill["killed"], "site-a")
            self.assertGreater(drill["timeout_seconds"], drill["budget_seconds"])
            self.assertNotIn(str(drill["budget_seconds"]), (pack / "README.md").read_text(encoding="utf-8"))
            note = json.loads((pack / "finance" / "lead-time.json").read_text(encoding="utf-8"))
            self.assertEqual(note["purchase_weeks"], PURCHASE_WEEKS)
            self.assertEqual(note["deadline"], "2027-02-08")
            self.assertEqual(note["ordered_on"], "2027-02-03")
            shares = json.loads((pack / "hospitals" / "shares.json").read_text(encoding="utf-8"))
            counts = [row["referrals"] for row in shares["shares"]]
            self.assertEqual(sum(counts), BACKLOG)
            self.assertEqual(len(set(counts)), 4)
            sites = json.loads((pack / "sites" / "replicas.json").read_text(encoding="utf-8"))
            self.assertEqual(sites["sites"][0]["health"], "down")
            self.assertEqual(sites["sites"][1]["health"], "up")
            self.assertNotIn(practice_gold["lookalike_id"], [row["id"] for row in sites["sites"][0]["models"]])
            self.assertEqual(sites["sites"][1]["models"][-1]["id"], practice_gold["lookalike_id"])
            readme = (pack / "README.md").read_text(encoding="utf-8")
            self.assertIn("2027-02-03", readme)
            self.assertNotIn(practice_gold["lookalike_hash"], readme)
            self.assertNotIn(str(practice_gold["local_sar"]), readme)

    def test_the_interviews_reach_the_site_and_the_deadline(self) -> None:
        questions = W4D4_ROOT / "work" / "interviews"
        ea = run(load_personas()["ea"], _lines(questions / "ea.questions.txt"))
        released = [fact_id for turn in ea for fact_id in turn["released"]]
        self.assertEqual(released, ["site-takeover", "workflow-store", "insure-partner"])
        self.assertEqual(load_personas()["ea"]["must_surface"], ("ain-file", "hl7-pair"))
        finance = run(load_personas()["finance"], _lines(questions / "finance.questions.txt"))
        released = [fact_id for turn in finance for fact_id in turn["released"]]
        self.assertEqual(released, ["rent-or-buy", "purchase-deadline"])
        self.assertEqual(load_personas()["finance"]["must_surface"], ("rent-or-buy", "double-benefit", "unit-prices"))

    def test_demo_prints_the_failover(self) -> None:
        profile = load("practice")
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "practice"])
        text = stdout.getvalue()
        shown = gold(profile)
        self.assertEqual(text.splitlines(), ["site-a down", "site-b serving"])
        self.assertNotIn(str(shown["budget_seconds"]), text)
        self.assertNotIn(shown["lookalike_hash"], text)
        self.assertNotIn(str(shown["local_sar"]), text)
        self.assertNotIn(profile.canary(), text)

    def test_lessons_do_not_state_the_canary_or_the_split(self) -> None:
        profile = load("practice")
        shown = gold(profile)
        notes = []
        blob = []
        for path in W4D4_ROOT.rglob("*"):
            if not path.is_file() or path.suffix not in _TEXT:
                continue
            text = path.read_text(encoding="utf-8")
            blob.append(text)
            if path.suffix == ".md":
                notes.append(text)
        code = "\n".join(blob)
        prose = "\n".join(notes)
        self.assertNotIn(profile.canary(), code)
        self.assertNotIn(shown["lookalike_hash"], code)
        for row in replicas(profile)["sites"][0]["models"]:
            self.assertNotIn(row["hash"], code)
        self.assertNotIn(str(shown["local_sar"]), prose)
        self.assertNotIn(shown["buy_arrives"], prose)
        self.assertNotIn(shown["rent_arrives"], prose)
        for value in shown["hospital_sar"].values():
            self.assertIsNone(re.search(rf"(?<!\d){value}(?!\d)", prose))

    def test_modules_differ_and_both_copies_pass(self) -> None:
        for name in _APP:
            shell = (W4D4_APP / name).read_bytes()
            filled = (W4D4_ROOT / "work" / "app" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        work = _suite(W4D4_ROOT / "work")
        shell = _suite(W4D4_ROOT)
        self.assertEqual(work.returncode, 0, work.stdout + work.stderr)
        self.assertEqual(shell.returncode, 0, shell.stdout + shell.stderr)


if __name__ == "__main__":
    unittest.main()
