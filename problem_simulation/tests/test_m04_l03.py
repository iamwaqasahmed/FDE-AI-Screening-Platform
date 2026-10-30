"""Module 4, Lesson 3: the surge forecast, the new external price, and the referral batch.

Guards the surge release, the new external price, and the referral batch.

The previous incident day must survive the write. Spend figures must stay out
of the learner pack, while the readme may name today's price and the price key.
Profiles must differ in throughput and in price. The new price must be the
higher one, the external rate must beat the batched local rate, and the batched
rate must beat the unbatched rate and fit the window. The unregistered candidate
must stay out of the adapter list. The finance and warehouse interviews must
reach the price and the campaign. The demo may show the missed window and must
not print the price or the backlog. Both suites must pass.
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
from alwaha.demo.cold import main as demo_main
from alwaha.engagement.interview import run
from alwaha.engagement.personas import load_personas
from alwaha.engagement.m03_l02 import adapter_hash
from alwaha.engagement.m04_l03 import gold
from alwaha.engagement.m04_l03_rows import ADAPTERS, BACKLOG, COLD_START_SECONDS, PEAK_MULTIPLE, WINDOW_HOURS, registry
from alwaha.paths import M04_L03_APP, M04_L03_ROOT, M04_L03_WORK
from alwaha.release.fingerprint import fingerprint
from alwaha.release.m04_l02 import write_m04_l02
from alwaha.release.m04_l03 import write_m04_l03

# Finance script. One of these turns should release today's price.
_FINANCE = [
    "Is there a budget line for the spend?",
    "Where are the SMS and label prices on the sheet?",
    "Does today's external price replace yesterday's?",
]
# Warehouse-lead script. The forecast turn should release the campaign backlog.
_BI = [
    "Did the wait dashboard improve?",
    "Is the forecast backlog the eye-screening campaign?",
]
# Shell modules that must differ from the filled copy.
_APP = ("adapters.py", "batch.py", "route.py", "public.py", "quota.py", "scale.py", "price.py", "capacity.py")
_TEXT = {".md", ".py", ".yml", ".yaml", ".json", ".txt"}


def _blob(pack: Path) -> str:
    """Join every file in a pack so a spend figure cannot hide outside the readme.

    The release test joins each profile's pack and fails if a watermark, the gold file name, or
    a spend figure appears in that text.
    """
    chunks = []
    for path in pack.rglob("*"):
        if path.is_file():
            chunks.append(path.read_text(encoding="utf-8"))
    return "\n".join(chunks)


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
    """Catches a pack that rewrites the previous day, leaks a spend figure, or serves
    an unregistered adapter.
    """
    def test_same_seed_matches_and_day_2_stays(self) -> None:
        """Fails when a second write disagrees, when the previous pack changes, or when
        this day's gold is missing from the hidden side or present in the pack.
        """
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            truth = root / "truth"
            write_m04_l02(profile, root / "m04_l02", truth)
            before = fingerprint(root / "m04_l02")
            first = write_m04_l03(profile, root / "m04_l03", truth)
            again = write_m04_l03(profile, root / "m04_l03", truth)
            self.assertEqual(first, again)
            self.assertEqual(before, fingerprint(root / "m04_l02"))
            self.assertTrue((truth / "m04_l03_gold.json").is_file())
            self.assertFalse((root / "m04_l03" / "m04_l03_gold.json").exists())

    def test_profiles_differ_and_the_budget_stays_out(self) -> None:
        """Fails when a spend figure leaks into a pack, when the two profiles match, or
        when the serving rules disagree with the gold file. The forecast must be the
        eye-screening backlog, chat latency must stay inside its budget only when it
        is reserved, and the candidate must be unregistered.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_m04_l03(practice, root / "practice" / "pack", root / "practice-truth")
            write_m04_l03(small, root / "small" / "pack", root / "small-truth")
            # Join each pack and load each gold file.
            practice_blob = _blob(root / "practice" / "pack")
            small_blob = _blob(root / "small" / "pack")
            practice_gold = json.loads((root / "practice-truth" / "m04_l03_gold.json").read_text(encoding="utf-8"))
            small_gold = json.loads((root / "small-truth" / "m04_l03_gold.json").read_text(encoding="utf-8"))
            # Watermarks, the gold file name, and the spend figures stay out of the packs.
            self.assertNotIn(practice.canary(), practice_blob)
            self.assertNotIn(small.canary(), small_blob)
            self.assertNotIn("m04_l03_gold", practice_blob)
            for key in ("budget_sar", "new_sar", "old_sar", "local_sar"):
                self.assertNotIn(str(practice_gold[key]), practice_blob)
                self.assertNotIn(str(small_gold[key]), small_blob)
            # Throughput sheets and today's prices differ across profiles.
            practice_sheet = (root / "practice" / "pack" / "serving" / "throughput.json").read_text(encoding="utf-8")
            small_sheet = (root / "small" / "pack" / "serving" / "throughput.json").read_text(encoding="utf-8")
            practice_price = (root / "practice" / "pack" / "finance" / "price-today.json").read_text(encoding="utf-8")
            small_price = (root / "small" / "pack" / "finance" / "price-today.json").read_text(encoding="utf-8")
            self.assertNotEqual(practice_sheet, small_sheet)
            self.assertNotEqual(practice_price, small_price)
            # Both gold files match the generator, and the profiles do not share a price or a batched rate.
            self.assertEqual(practice_gold, gold(practice))
            self.assertEqual(small_gold, gold(small))
            self.assertNotEqual(practice_gold["new_price"], small_gold["new_price"])
            self.assertNotEqual(practice_gold["local_batched_tps"], small_gold["local_batched_tps"])
            # The new price is higher. The external rate beats the batched local rate, which beats the unbatched rate.
            for shown in (practice_gold, small_gold):
                self.assertGreater(shown["new_price"], shown["old_price"])
                self.assertGreater(shown["ext_large_tps"], shown["local_batched_tps"])
                self.assertGreater(shown["local_batched_tps"], shown["local_unbatched_tps"])
                self.assertGreater(shown["new_sar"], shown["budget_sar"])
                self.assertEqual(shown["old_sar"], shown["budget_sar"])
                self.assertLessEqual(shown["local_sar"], shown["budget_sar"])
                self.assertGreater(shown["hours_unbatched"], WINDOW_HOURS)
                self.assertLessEqual(shown["hours"], WINDOW_HOURS)
                self.assertEqual(shown["backlog"], BACKLOG)
                self.assertEqual(shown["window_hours"], WINDOW_HOURS)
                self.assertEqual(shown["peak_multiple"], PEAK_MULTIPLE)
                self.assertEqual(shown["cold_start_seconds"], COLD_START_SECONDS)
                self.assertEqual(shown["adapters"], list(ADAPTERS))
            # The forecast is the eye-screening backlog.
            pack = root / "practice" / "pack"
            forecast = json.loads((pack / "forecast" / "p-forecast.json").read_text(encoding="utf-8"))
            self.assertEqual(forecast["id"], "p-forecast")
            self.assertEqual(forecast["backlog_referrals"], BACKLOG)
            self.assertEqual(forecast["campaign"], "eye-screening")
            # Reserved chat stays inside its budget. Starved chat does not.
            sheet = json.loads(practice_sheet)
            self.assertLessEqual(sheet["chat_p95_reserved_ms"], sheet["chat_p95_budget_ms"])
            self.assertGreater(sheet["chat_p95_starved_ms"], sheet["chat_p95_budget_ms"])
            # The last adapter is the approved hash. The candidate is unregistered and not in that list.
            models = json.loads((pack / "registry" / "adapters.json").read_text(encoding="utf-8"))["models"]
            self.assertEqual([row["id"] for row in models], list(ADAPTERS))
            self.assertEqual(models[-1]["hash"], adapter_hash(practice))
            candidate = json.loads((pack / "registry" / "candidate.json").read_text(encoding="utf-8"))
            self.assertEqual(candidate["status"], "unregistered")
            self.assertNotIn(candidate["id"], [row["id"] for row in models])
            # The readme names today's price, the price key, and the price date.
            note = (pack / "README.md").read_text(encoding="utf-8")
            self.assertIn(str(practice_gold["new_price"]), note)
            self.assertIn("price.ext_large_per_1k", note)
            self.assertIn("2027-02-02", note)

    def test_the_interviews_reach_the_price_and_the_campaign(self) -> None:
        """Fails when finance does not release today's price, when that persona's required
        facts changed, or when the warehouse lead does not release the campaign backlog.
        """
        finance = run(load_personas()["finance"], _FINANCE)
        released = [fact_id for turn in finance for fact_id in turn["released"]]
        self.assertIn("price-today", released)
        self.assertEqual(load_personas()["finance"]["must_surface"], ("rent-or-buy", "double-benefit", "unit-prices"))
        bi = run(load_personas()["bi-lead"], _BI)
        released = [fact_id for turn in bi for fact_id in turn["released"]]
        self.assertEqual(released, ["campaign-backlog"])

    def test_demo_prints_the_missed_window(self) -> None:
        """Fails when the demo does not show the window and the cold start, or when it
        prints the new price, the backlog, or the watermark.
        """
        profile = load("practice")
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "practice"])
        text = stdout.getvalue()
        shown = gold(profile)["demo"]
        self.assertEqual(text.splitlines(), [shown["window"], shown["cold"]])
        self.assertNotIn(str(gold(profile)["new_price"]), text)
        self.assertNotIn(str(gold(profile)["backlog"]), text)
        self.assertNotIn(profile.canary(), text)

    def test_lessons_do_not_state_the_canary_or_the_price(self) -> None:
        """Fails when a lesson or packet source contains the watermark or a model hash, or
        when a lesson page contains a spend figure or a bare price.
        """
        # Skip the release fixtures. Keep lesson pages apart from the other sources.
        release_trees = (
            M04_L03_ROOT / "packet" / "release",
            M04_L03_ROOT.parent / "Solution_Copy" / "sources",
        )
        profile = load("practice")
        shown = gold(profile)
        notes = []
        blob = []
        for path in M04_L03_ROOT.rglob("*"):
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
        self.assertNotIn(shown["candidate_hash"], code)
        for row in registry(profile)["models"]:
            self.assertNotIn(row["hash"], code)
        # Lesson pages must not contain a spend figure or a bare price.
        for key in ("budget_sar", "new_sar", "old_sar", "local_sar"):
            self.assertNotIn(str(shown[key]), prose)
        for key in ("new_price", "old_price"):
            self.assertIsNone(re.search(rf"(?<!\d){shown[key]}(?!\d)", prose))

    def test_modules_differ_and_both_copies_pass(self) -> None:
        """Fails when a shell module matches the filled copy, or when either suite fails.

        The test compares every shell module with the filled copy and runs both packet suites,
        and fails if any module matches or either suite does not exit cleanly.
        """
        for name in _APP:
            shell = (M04_L03_APP / name).read_bytes()
            filled = (M04_L03_WORK / "app" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        work = _suite(M04_L03_WORK)
        shell = _suite(M04_L03_APP.parent)
        self.assertEqual(work.returncode, 0, work.stdout + work.stderr)
        self.assertEqual(shell.returncode, 0, shell.stdout + shell.stderr)


if __name__ == "__main__":
    unittest.main()
