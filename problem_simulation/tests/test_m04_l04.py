"""Module 4, Lesson 4: the site drill, the insurance outage, and rent versus buy.

Guards the site drill, the insurance outage, and the rent-versus-buy choice.

The previous surge day must survive the write. Packs must not carry a watermark,
the gold name, the local spend, or the arrival dates. Rent must be the route
that lands in time, and the hospital shares must add up to that spend. The drill
must kill one site and use a timeout longer than the budget. The readme may
show the order date and must not show the lookalike hash or the spend. The
architect and finance interviews must reach the site and the deadline. The demo
may show the failover and must not print a budget, a hash, or a spend. Both
suites must pass.
"""

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
from alwaha.engagement.m04_l03_rows import BACKLOG
from alwaha.engagement.m04_l04 import gold
from alwaha.engagement.m04_l04_rows import HOSPITALS, PURCHASE_WEEKS, replicas
from alwaha.paths import M04_L04_APP, M04_L04_ROOT, M04_L04_WORK
from alwaha.release.fingerprint import fingerprint
from alwaha.release.m04_l03 import write_m04_l03
from alwaha.release.m04_l04 import write_m04_l04

# Shell modules that must differ from the filled copy.
_APP = ("replicas.py", "route.py", "failover.py", "hashes.py", "breaker.py", "degrade.py", "procure.py", "hospitals.py")
_TEXT = {".md", ".py", ".yml", ".yaml", ".json", ".txt"}


def _blob(pack: Path) -> str:
    """Join every file in a pack so a spend figure cannot hide outside the readme.

    The release test joins each profile's pack and fails if a watermark, the gold file name, a
    spend figure, or an arrival date appears in that text.
    """
    chunks = []
    for path in pack.rglob("*"):
        if path.is_file():
            chunks.append(path.read_text(encoding="utf-8"))
    return "\n".join(chunks)


def _lines(path: Path) -> list[str]:
    """Return the non-empty lines of a question file.

    The interview runner wants the questions without blank lines or surrounding space.
    """
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _suite(folder: Path) -> subprocess.CompletedProcess[str]:
    """Run a packet's own unit tests and return the process result without raising.

    The caller runs both the filled packet and the unfinished packet, both of which are supposed
    to pass, and a run that does not exit cleanly is the failure.
    """
    return subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
        cwd=folder,
        capture_output=True,
        text=True,
        check=False,
    )


class ReleaseTests(unittest.TestCase):
    """Catches a pack that rewrites the previous day, leaks the buy-versus-rent dates,
    or places the lookalike on the surviving site.
    """
    def test_same_seed_matches_and_day_3_stays(self) -> None:
        """Fails when a second write disagrees, when the previous pack changes, or when
        this day's gold is missing from the hidden side or present in the pack.
        """
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            truth = root / "truth"
            write_m04_l03(profile, root / "m04_l03", truth)
            before = fingerprint(root / "m04_l03")
            first = write_m04_l04(profile, root / "m04_l04", truth)
            again = write_m04_l04(profile, root / "m04_l04", truth)
            self.assertEqual(first, again)
            self.assertEqual(before, fingerprint(root / "m04_l03"))
            self.assertTrue((truth / "m04_l04_gold.json").is_file())
            self.assertFalse((root / "m04_l04" / "m04_l04_gold.json").exists())

    def test_profiles_differ_and_the_split_stays_out(self) -> None:
        """Fails when a spend or an arrival date leaks, when rent is not the route that
        meets the deadline, or when the hospital shares do not add up. The two profiles
        must differ in budget, rental length, shares, and lookalike. The killed site
        must not list the lookalike, and the site that stays up must.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_m04_l04(practice, root / "practice" / "pack", root / "practice-truth")
            write_m04_l04(small, root / "small" / "pack", root / "small-truth")
            # Join each pack and load each gold file.
            practice_blob = _blob(root / "practice" / "pack")
            small_blob = _blob(root / "small" / "pack")
            practice_gold = json.loads((root / "practice-truth" / "m04_l04_gold.json").read_text(encoding="utf-8"))
            small_gold = json.loads((root / "small-truth" / "m04_l04_gold.json").read_text(encoding="utf-8"))
            # Watermarks and the gold file name stay out of the packs.
            self.assertNotIn(practice.canary(), practice_blob)
            self.assertNotIn(small.canary(), small_blob)
            self.assertNotIn("m04_l04_gold", practice_blob)
            # Spend and arrival dates stay out. Rent meets the deadline. Buying does not. Shares add up.
            for shown in (practice_gold, small_gold):
                self.assertNotIn(str(shown["local_sar"]), practice_blob if shown is practice_gold else small_blob)
                self.assertNotIn(shown["buy_arrives"], practice_blob if shown is practice_gold else small_blob)
                self.assertNotIn(shown["rent_arrives"], practice_blob if shown is practice_gold else small_blob)
                self.assertEqual(shown["route"], "rent")
                self.assertGreater(shown["buy_arrives"], shown["deadline"])
                self.assertLessEqual(shown["rent_arrives"], shown["deadline"])
                self.assertEqual(sum(shown["hospital_sar"].values()), shown["local_sar"])
                self.assertEqual(sorted(shown["hospital_sar"]), sorted(HOSPITALS))
            # The profiles differ in budget, rental length, shares, and lookalike. Both gold files match the generator.
            self.assertNotEqual(practice_gold["budget_seconds"], small_gold["budget_seconds"])
            self.assertNotEqual(practice_gold["rent_days"], small_gold["rent_days"])
            self.assertNotEqual(practice_gold["hospital_sar"], small_gold["hospital_sar"])
            self.assertNotEqual(practice_gold["lookalike_hash"], small_gold["lookalike_hash"])
            self.assertEqual(practice_gold, gold(practice))
            self.assertEqual(small_gold, gold(small))
            # The killed site is over its timeout budget, and that budget is not in the readme.
            pack = root / "practice" / "pack"
            drill = json.loads((pack / "drill" / "site-a.json").read_text(encoding="utf-8"))
            self.assertEqual(drill["killed"], "site-a")
            self.assertGreater(drill["timeout_seconds"], drill["budget_seconds"])
            self.assertNotIn(str(drill["budget_seconds"]), (pack / "README.md").read_text(encoding="utf-8"))
            # The lead-time note names the purchase length, the deadline, and the order date.
            note = json.loads((pack / "finance" / "lead-time.json").read_text(encoding="utf-8"))
            self.assertEqual(note["purchase_weeks"], PURCHASE_WEEKS)
            self.assertEqual(note["deadline"], "2027-02-08")
            self.assertEqual(note["ordered_on"], "2027-02-03")
            # The four hospital counts add up to the backlog and are not all the same.
            shares = json.loads((pack / "hospitals" / "shares.json").read_text(encoding="utf-8"))
            counts = [row["referrals"] for row in shares["shares"]]
            self.assertEqual(sum(counts), BACKLOG)
            self.assertEqual(len(set(counts)), 4)
            # The killed site is down and does not list the lookalike. The site that stays up does.
            sites = json.loads((pack / "sites" / "replicas.json").read_text(encoding="utf-8"))
            self.assertEqual(sites["sites"][0]["health"], "down")
            self.assertEqual(sites["sites"][1]["health"], "up")
            self.assertNotIn(practice_gold["lookalike_id"], [row["id"] for row in sites["sites"][0]["models"]])
            self.assertEqual(sites["sites"][1]["models"][-1]["id"], practice_gold["lookalike_id"])
            # The readme names the order date and does not name the lookalike hash or the spend.
            readme = (pack / "README.md").read_text(encoding="utf-8")
            self.assertIn("2027-02-03", readme)
            self.assertNotIn(practice_gold["lookalike_hash"], readme)
            self.assertNotIn(str(practice_gold["local_sar"]), readme)

    def test_the_interviews_reach_the_site_and_the_deadline(self) -> None:
        """Fails when the architect script does not release the site, the workflow store,
        and the insurance partner, or when finance does not release the rent-or-buy
        choice and the purchase deadline. The required-fact lists must stay as they were.
        """
        questions = M04_L04_ROOT / "Student_Copy" / "packet" / "interviews"
        ea = run(load_personas()["ea"], _lines(questions / "ea.questions.txt"))
        released = [fact_id for turn in ea for fact_id in turn["released"]]
        self.assertEqual(released, ["site-takeover", "workflow-store", "insure-partner"])
        self.assertEqual(load_personas()["ea"]["must_surface"], ("ain-file", "hl7-pair"))
        finance = run(load_personas()["finance"], _lines(questions / "finance.questions.txt"))
        released = [fact_id for turn in finance for fact_id in turn["released"]]
        self.assertEqual(released, ["rent-or-buy", "purchase-deadline"])
        self.assertEqual(load_personas()["finance"]["must_surface"], ("rent-or-buy", "double-benefit", "unit-prices"))

    def test_demo_prints_the_failover(self) -> None:
        """Fails when the demo does not show the killed site down and the other site
        serving, or when it prints the budget, the lookalike hash, the spend, or the
        watermark.
        """
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
        """Fails when a lesson or packet source contains the watermark or a model hash, or
        when a lesson page contains the spend, an arrival date, or a hospital share.
        """
        # Skip the release fixtures. Keep lesson pages apart from the other sources.
        release_trees = (
            M04_L04_ROOT / "Student_Copy" / "packet" / "release",
            M04_L04_ROOT / "Solution_Copy" / "sources",
        )
        profile = load("practice")
        shown = gold(profile)
        notes = []
        blob = []
        for path in M04_L04_ROOT.rglob("*"):
            if any(path.is_relative_to(root) for root in release_trees):
                continue
            if not path.is_file() or path.suffix not in _TEXT:
                continue
            text = path.read_text(encoding="utf-8")
            blob.append(text)
            if path.suffix == ".md":
                notes.append(text)
        code = "\n".join(blob)
        prose = "\n".join(notes)
        # Sources must not contain the watermark or a model hash.
        self.assertNotIn(profile.canary(), code)
        self.assertNotIn(shown["lookalike_hash"], code)
        for row in replicas(profile)["sites"][0]["models"]:
            self.assertNotIn(row["hash"], code)
        # Lesson pages must not contain the spend, an arrival date, or a hospital share.
        self.assertNotIn(str(shown["local_sar"]), prose)
        self.assertNotIn(shown["buy_arrives"], prose)
        self.assertNotIn(shown["rent_arrives"], prose)
        for value in shown["hospital_sar"].values():
            self.assertIsNone(re.search(rf"(?<!\d){value}(?!\d)", prose))

    def test_modules_differ_and_both_copies_pass(self) -> None:
        """Fails when a shell module matches the filled copy, or when either suite fails.

        The test compares every shell module with the filled copy and runs both packet suites,
        and fails if any module matches or either suite does not exit cleanly.
        """
        for name in _APP:
            shell = (M04_L04_APP / name).read_bytes()
            filled = (M04_L04_WORK / "app" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        work = _suite(M04_L04_WORK)
        shell = _suite(M04_L04_APP.parent)
        self.assertEqual(work.returncode, 0, work.stdout + work.stderr)
        self.assertEqual(shell.returncode, 0, shell.stdout + shell.stderr)


if __name__ == "__main__":
    unittest.main()
