"""Day 3 of Week 4: the surge forecast, the new external price, and the referral batch."""

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
from alwaha.engagement.w3d2 import adapter_hash
from alwaha.engagement.w4d3 import gold
from alwaha.engagement.w4d3_rows import ADAPTERS, BACKLOG, COLD_START_SECONDS, PEAK_MULTIPLE, WINDOW_HOURS, registry
from alwaha.paths import W4D3_APP, W4D3_ROOT
from alwaha.release.fingerprint import fingerprint
from alwaha.release.w4d2 import write_w4d2
from alwaha.release.w4d3 import write_w4d3

_FINANCE = [
    "Is there a budget line for the spend?",
    "Where are the SMS and label prices on the sheet?",
    "Does today's external price replace yesterday's?",
]
_BI = [
    "Did the wait dashboard improve?",
    "Is the forecast backlog the eye-screening campaign?",
]
_APP = ("adapters.py", "batch.py", "route.py", "public.py", "quota.py", "scale.py", "price.py", "capacity.py")
_TEXT = {".md", ".py", ".yml", ".yaml", ".json", ".txt"}


def _blob(pack: Path) -> str:
    chunks = []
    for path in pack.rglob("*"):
        if path.is_file():
            chunks.append(path.read_text(encoding="utf-8"))
    return "\n".join(chunks)


def _suite(folder: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
        cwd=folder,
        capture_output=True,
        text=True,
        check=False,
    )


class ReleaseTests(unittest.TestCase):
    def test_same_seed_matches_and_day_2_stays(self) -> None:
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            truth = root / "truth"
            write_w4d2(profile, root / "w4d2", truth)
            before = fingerprint(root / "w4d2")
            first = write_w4d3(profile, root / "w4d3", truth)
            again = write_w4d3(profile, root / "w4d3", truth)
            self.assertEqual(first, again)
            self.assertEqual(before, fingerprint(root / "w4d2"))
            self.assertTrue((truth / "w4d3_gold.json").is_file())
            self.assertFalse((root / "w4d3" / "w4d3_gold.json").exists())

    def test_profiles_differ_and_the_budget_stays_out(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_w4d3(practice, root / "practice" / "pack", root / "practice-truth")
            write_w4d3(small, root / "small" / "pack", root / "small-truth")
            practice_blob = _blob(root / "practice" / "pack")
            small_blob = _blob(root / "small" / "pack")
            practice_gold = json.loads((root / "practice-truth" / "w4d3_gold.json").read_text(encoding="utf-8"))
            small_gold = json.loads((root / "small-truth" / "w4d3_gold.json").read_text(encoding="utf-8"))
            self.assertNotIn(practice.canary(), practice_blob)
            self.assertNotIn(small.canary(), small_blob)
            self.assertNotIn("w4d3_gold", practice_blob)
            for key in ("budget_sar", "new_sar", "old_sar", "local_sar"):
                self.assertNotIn(str(practice_gold[key]), practice_blob)
                self.assertNotIn(str(small_gold[key]), small_blob)
            practice_sheet = (root / "practice" / "pack" / "serving" / "throughput.json").read_text(encoding="utf-8")
            small_sheet = (root / "small" / "pack" / "serving" / "throughput.json").read_text(encoding="utf-8")
            practice_price = (root / "practice" / "pack" / "finance" / "price-today.json").read_text(encoding="utf-8")
            small_price = (root / "small" / "pack" / "finance" / "price-today.json").read_text(encoding="utf-8")
            self.assertNotEqual(practice_sheet, small_sheet)
            self.assertNotEqual(practice_price, small_price)
            self.assertEqual(practice_gold, gold(practice))
            self.assertEqual(small_gold, gold(small))
            self.assertNotEqual(practice_gold["new_price"], small_gold["new_price"])
            self.assertNotEqual(practice_gold["local_batched_tps"], small_gold["local_batched_tps"])
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
            pack = root / "practice" / "pack"
            forecast = json.loads((pack / "forecast" / "p-forecast.json").read_text(encoding="utf-8"))
            self.assertEqual(forecast["id"], "p-forecast")
            self.assertEqual(forecast["backlog_referrals"], BACKLOG)
            self.assertEqual(forecast["campaign"], "eye-screening")
            sheet = json.loads(practice_sheet)
            self.assertLessEqual(sheet["chat_p95_reserved_ms"], sheet["chat_p95_budget_ms"])
            self.assertGreater(sheet["chat_p95_starved_ms"], sheet["chat_p95_budget_ms"])
            models = json.loads((pack / "registry" / "adapters.json").read_text(encoding="utf-8"))["models"]
            self.assertEqual([row["id"] for row in models], list(ADAPTERS))
            self.assertEqual(models[-1]["hash"], adapter_hash(practice))
            candidate = json.loads((pack / "registry" / "candidate.json").read_text(encoding="utf-8"))
            self.assertEqual(candidate["status"], "unregistered")
            self.assertNotIn(candidate["id"], [row["id"] for row in models])
            note = (pack / "README.md").read_text(encoding="utf-8")
            self.assertIn(str(practice_gold["new_price"]), note)
            self.assertIn("price.ext_large_per_1k", note)
            self.assertIn("2027-02-02", note)

    def test_the_interviews_reach_the_price_and_the_campaign(self) -> None:
        finance = run(load_personas()["finance"], _FINANCE)
        released = [fact_id for turn in finance for fact_id in turn["released"]]
        self.assertIn("price-today", released)
        self.assertEqual(load_personas()["finance"]["must_surface"], ("rent-or-buy", "double-benefit", "unit-prices"))
        bi = run(load_personas()["bi-lead"], _BI)
        released = [fact_id for turn in bi for fact_id in turn["released"]]
        self.assertEqual(released, ["campaign-backlog"])

    def test_demo_prints_the_missed_window(self) -> None:
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
        profile = load("practice")
        shown = gold(profile)
        notes = []
        blob = []
        for path in W4D3_ROOT.rglob("*"):
            if not path.is_file() or path.suffix not in _TEXT:
                continue
            text = path.read_text(encoding="utf-8")
            blob.append(text)
            if path.suffix == ".md":
                notes.append(text)
        code = "\n".join(blob)
        prose = "\n".join(notes)
        self.assertNotIn(profile.canary(), code)
        self.assertNotIn(shown["candidate_hash"], code)
        for row in registry(profile)["models"]:
            self.assertNotIn(row["hash"], code)
        for key in ("budget_sar", "new_sar", "old_sar", "local_sar"):
            self.assertNotIn(str(shown[key]), prose)
        for key in ("new_price", "old_price"):
            self.assertIsNone(re.search(rf"(?<!\d){shown[key]}(?!\d)", prose))

    def test_modules_differ_and_both_copies_pass(self) -> None:
        for name in _APP:
            shell = (W4D3_APP / name).read_bytes()
            filled = (W4D3_ROOT / "work" / "app" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        work = _suite(W4D3_ROOT / "work")
        shell = _suite(W4D3_ROOT)
        self.assertEqual(work.returncode, 0, work.stdout + work.stderr)
        self.assertEqual(shell.returncode, 0, shell.stdout + shell.stderr)


if __name__ == "__main__":
    unittest.main()
