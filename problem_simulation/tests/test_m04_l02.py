"""Module 4, Lesson 2: the replay, the Ramadan-hours circular, and shadow-extract.

Guards the incident release, the hours circular, and the trace demo.

The previous attack day must survive the write. Packs must not carry a
watermark, the gold name, or the override rate, while the alert time may appear.
The new hours must match the document-changed event, and the old hours must not
appear in the pack. The security and patient-representative interviews must
reach the replay and the old hours. The demo may print the trace fields and
must not print the hidden detail. Lesson sources must not contain the watermark,
either hash, or that detail. Both suites must pass.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from alwaha.config.profile import load
from alwaha.demo.trace import main as demo_main
from alwaha.engagement.interview import run
from alwaha.engagement.personas import load_personas
from alwaha.engagement.m02_l04 import approved_hash
from alwaha.engagement.m04_l02 import gold
from alwaha.engagement.m04_l02_rows import ALERT_AT, DETAIL, FIRST_ERROR, shadow_hash
from alwaha.engagement.m04_l02_rules import within_slo
from alwaha.paths import M04_L02_APP, M04_L02_ROOT, M04_L02_WORK
from alwaha.release.fingerprint import fingerprint
from alwaha.release.m04_l01 import write_m04_l01
from alwaha.release.m04_l02 import write_m04_l02

# Security script. Both turns should release a fact: the replay, then the blind dashboard.
_CISO = [
    "What does the incident replay already contain?",
    "Why does a CPU dashboard miss the tool failures?",
]
# Patient-representative script. The hours turn should release the old-hours fact.
_REP = [
    "Why does the phone line still not answer?",
    "Which clinic hours is she still offered after the circular?",
]
# Shell modules that must differ from the filled copy.
_APP = ("spans.py", "dashboard.py", "meter.py", "cache.py", "drift.py", "override.py", "shadow.py")


def _blob(pack: Path) -> str:
    """Join every file in a pack so an override rate cannot hide in one fixture.

    The release test joins each profile's pack and fails if that text contains a watermark, the
    gold file name, the override rate, or the old hours.
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
    """Catches a pack that rewrites the previous day, prints the override rate, or
    leaves the old clinic hours in the learner files.
    """
    def test_same_seed_matches_and_day_1_stays(self) -> None:
        """Fails when a second write disagrees, when the previous pack changes, or when
        this day's gold is missing from the hidden side or present in the pack.
        """
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            truth = root / "truth"
            write_m04_l01(profile, root / "m04_l01", truth)
            before = fingerprint(root / "m04_l01")
            first = write_m04_l02(profile, root / "m04_l02", truth)
            again = write_m04_l02(profile, root / "m04_l02", truth)
            self.assertEqual(first, again)
            self.assertEqual(before, fingerprint(root / "m04_l01"))
            self.assertTrue((truth / "m04_l02_gold.json").is_file())
            self.assertFalse((root / "m04_l02" / "m04_l02_gold.json").exists())

    def test_profiles_differ_and_the_rate_stays_out(self) -> None:
        """Fails when a pack contains a watermark, the gold name, or the override rate,
        when the gateway meters match across profiles, or when the alert is not inside
        the response window. The new hours must equal the document event, and the old
        hours must stay out of the pack.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_m04_l02(practice, root / "practice" / "pack", root / "practice-truth")
            write_m04_l02(small, root / "small" / "pack", root / "small-truth")
            # Join each pack and load each gold file.
            practice_blob = _blob(root / "practice" / "pack")
            small_blob = _blob(root / "small" / "pack")
            practice_gold = json.loads((root / "practice-truth" / "m04_l02_gold.json").read_text(encoding="utf-8"))
            small_gold = json.loads((root / "small-truth" / "m04_l02_gold.json").read_text(encoding="utf-8"))
            # Watermarks, the gold file name, and the override rate stay out of the packs.
            self.assertNotIn(practice.canary(), practice_blob)
            self.assertNotIn(small.canary(), small_blob)
            self.assertNotIn("m04_l02_gold", practice_blob)
            self.assertNotIn(f"{practice_gold['override']:.6f}", practice_blob)
            self.assertNotIn(f"{small_gold['override']:.6f}", small_blob)
            # Gateway meters differ. Both gold files match the generator, and their costs and rates differ.
            self.assertNotEqual(
                (root / "practice" / "pack" / "meter" / "gateway.jsonl").read_text(encoding="utf-8"),
                (root / "small" / "pack" / "meter" / "gateway.jsonl").read_text(encoding="utf-8"),
            )
            self.assertEqual(practice_gold, gold(practice))
            self.assertEqual(small_gold, gold(small))
            self.assertNotEqual(practice_gold["cost"], small_gold["cost"])
            self.assertNotEqual(practice_gold["override"], small_gold["override"])
            # The alert is the named time, and it falls inside the response window.
            self.assertEqual(practice_gold["alert_at"], ALERT_AT)
            self.assertEqual(practice_gold["first_error"], FIRST_ERROR)
            self.assertEqual(practice_gold["board"]["alert_at"], ALERT_AT)
            self.assertTrue(within_slo(FIRST_ERROR, ALERT_AT))
            self.assertIn(ALERT_AT, practice_blob)
            # The new hours equal the document event. The old hours stay out of the pack.
            self.assertIn("circ-ramadan-hours", (root / "practice" / "pack" / "README.md").read_text(encoding="utf-8"))
            self.assertEqual(
                practice_gold["new_hours"],
                json.loads((root / "practice" / "pack" / "events" / "document-changed.json").read_text(encoding="utf-8"))["body"],
            )
            self.assertNotIn(practice_gold["old_hours"], practice_blob)

    def test_the_interviews_reach_the_replay_and_the_old_hours(self) -> None:
        """Fails when the security script does not release the replay and the blind
        dashboard, or when the patient representative does not release the old hours.
        """
        ciso = run(load_personas()["ciso"], _CISO)
        released = [fact_id for turn in ciso for fact_id in turn["released"]]
        self.assertEqual(released, ["replay-alert", "cpu-blind"])
        rep = run(load_personas()["patient-rep"], _REP)
        released = [fact_id for turn in rep for fact_id in turn["released"]]
        self.assertEqual(released, ["old-hours"])

    def test_demo_prints_the_trace_fields(self) -> None:
        """Fails when the demo does not print the tool, the hash, and the token count from
        the gold demo, or when it prints the hidden detail or the watermark.
        """
        profile = load("practice")
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "practice"])
        text = stdout.getvalue()
        shown = gold(profile)["demo"]
        self.assertEqual(text.splitlines(), [shown["tool"], shown["hash"], shown["tokens"]])
        self.assertNotIn(DETAIL, text)
        self.assertNotIn(profile.canary(), text)

    def test_lessons_do_not_state_the_canary_or_the_hash(self) -> None:
        """Fails when a lesson or packet source, other than the release fixtures, contains
        the watermark, either hash, or the hidden trace detail.
        """
        # Lesson and packet sources, skipping the release fixtures.
        release_trees = (
            M04_L02_ROOT / "Student_Copy" / "packet" / "release",
            M04_L02_ROOT / "Solution_Copy" / "sources",
        )
        lessons = []
        for path in M04_L02_ROOT.rglob("*"):
            if any(path.is_relative_to(root) for root in release_trees):
                continue
            if path.is_file() and path.suffix in {".md", ".py", ".yml", ".yaml", ".json", ".txt"}:
                lessons.append(path.read_text(encoding="utf-8"))
        blob = "\n".join(lessons)
        # Those sources must not contain the watermark, either hash, or the hidden trace detail.
        profile = load("practice")
        self.assertNotIn(profile.canary(), blob)
        self.assertNotIn(approved_hash(profile), blob)
        self.assertNotIn(shadow_hash(profile), blob)
        self.assertNotIn(DETAIL, blob)

    def test_modules_differ_and_both_copies_pass(self) -> None:
        """Fails when a shell module matches the filled copy, or when either suite fails.

        The test compares every shell module with the filled copy and runs both packet suites,
        and fails if any module matches or either suite does not exit cleanly.
        """
        for name in _APP:
            shell = (M04_L02_APP / name).read_bytes()
            filled = (M04_L02_WORK / "app" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        work = _suite(M04_L02_WORK)
        shell = _suite(M04_L02_APP.parent)
        self.assertEqual(work.returncode, 0, work.stdout + work.stderr)
        self.assertEqual(shell.returncode, 0, shell.stdout + shell.stderr)


if __name__ == "__main__":
    unittest.main()
