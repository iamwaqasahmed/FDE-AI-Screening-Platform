"""Day 5 of Week 4: the three connections and the rehearsal proposal.

Guards the three connections and the rehearsal proposal release.

The previous drill day must survive the write. Packs must not carry a watermark,
the gold name, the hidden reading of the benefit question, or a bare leave or
phone count. The value model must block the triage problem, and the pack must
not contain a currency word. The readme may show the case date and must not
show the attack text or the counts. The access and architect interviews must
reach the handoff summary and the leave. The demo may print the question and
must not print the answer. Both suites must pass.
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
from alwaha.demo.benefit import main as demo_main
from alwaha.engagement.interview import run
from alwaha.engagement.personas import load_personas
from alwaha.engagement.w4d5 import gold
from alwaha.engagement.w4d5_rows import attack
from alwaha.paths import W4D5_APP, W4D5_ROOT, W4D5_WORK
from alwaha.release.fingerprint import fingerprint
from alwaha.release.w4d4 import write_w4d4
from alwaha.release.w4d5 import write_w4d5

# Shell modules that must differ from the filled copy.
_APP = ("signin.py", "bus.py", "handoff.py", "leave.py", "warehouse.py", "rank.py", "gates.py", "personal.py")
# Hidden reading of the benefit question. The pack, the demo, and the lesson pages must not print it.
_ANSWER = "count the same calls"
_TEXT = {".md", ".py", ".yml", ".yaml", ".json", ".txt"}


def _blob(pack: Path) -> str:
    """Join every file in a pack so a bare count cannot hide in one fixture."""
    chunks = []
    for path in pack.rglob("*"):
        if path.is_file():
            chunks.append(path.read_text(encoding="utf-8"))
    return "\n".join(chunks)


def _lines(path: Path) -> list[str]:
    """Return the non-empty lines of a question file."""
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _bare(text: str, number: int) -> bool:
    """True when a number stands alone in the text, not as part of a longer run of digits.

    A count hidden in the gold file must not be excused by a date that happens to
    contain the same digits.
    """
    return re.search(rf"(?<!\d){number}(?!\d)", text) is not None


def _suite(folder: Path) -> subprocess.CompletedProcess[str]:
    """Run a packet's own unit tests and return the process result without raising."""
    return subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
        cwd=folder,
        capture_output=True,
        text=True,
        check=False,
    )


class ReleaseTests(unittest.TestCase):
    """Catches a pack that rewrites the previous day, leaks a count, or leaves triage
    unblocked in the value model.
    """
    def test_same_seed_matches_and_day_4_stays(self) -> None:
        """Fails when a second write disagrees, when the previous pack changes, or when
        this day's gold is missing from the hidden side or present in the pack.
        """
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            truth = root / "truth"
            write_w4d4(profile, root / "w4d4", truth)
            before = fingerprint(root / "w4d4")
            first = write_w4d5(profile, root / "w4d5", truth)
            again = write_w4d5(profile, root / "w4d5", truth)
            self.assertEqual(first, again)
            self.assertEqual(before, fingerprint(root / "w4d4"))
            self.assertTrue((truth / "w4d5_gold.json").is_file())
            self.assertFalse((root / "w4d5" / "w4d5_gold.json").exists())

    def test_profiles_differ_and_the_counts_stay_out(self) -> None:
        """Fails when a pack contains a watermark, the gold name, the hidden benefit
        reading, or a bare count. The two profiles must differ in those counts. The
        event name and the warehouse clock must be the cancelled session and the
        referral time, and triage must be the blocked problem.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_w4d5(practice, root / "practice" / "pack", root / "practice-truth")
            write_w4d5(small, root / "small" / "pack", root / "small-truth")
            practice_blob = _blob(root / "practice" / "pack")
            small_blob = _blob(root / "small" / "pack")
            practice_gold = json.loads((root / "practice-truth" / "w4d5_gold.json").read_text(encoding="utf-8"))
            small_gold = json.loads((root / "small-truth" / "w4d5_gold.json").read_text(encoding="utf-8"))
            self.assertNotIn(practice.canary(), practice_blob)
            self.assertNotIn(small.canary(), small_blob)
            self.assertNotIn("w4d5_gold", practice_blob)
            self.assertNotIn(_ANSWER, practice_blob)
            self.assertFalse(_bare(practice_blob, practice_gold["leave_lag"]))
            self.assertFalse(_bare(practice_blob, practice_gold["phone_only"]))
            self.assertFalse(_bare(small_blob, small_gold["leave_lag"]))
            self.assertFalse(_bare(small_blob, small_gold["phone_only"]))
            self.assertNotEqual(practice_gold["leave_lag"], small_gold["leave_lag"])
            self.assertNotEqual(practice_gold["phone_only"], small_gold["phone_only"])
            self.assertEqual(practice_gold["event"], "session.cancelled")
            self.assertEqual(practice_gold["clock"], "referred_at")
            self.assertEqual(practice_gold, gold(practice))
            self.assertEqual(small_gold, gold(small))
            pack = root / "practice" / "pack"
            model = json.loads((pack / "value" / "model.json").read_text(encoding="utf-8"))
            blocked = [row["id"] for row in model["problems"] if row["blockers"]]
            self.assertEqual(blocked, ["p-triage"])
            self.assertNotIn("sar", practice_blob.lower())
            readme = (pack / "README.md").read_text(encoding="utf-8")
            self.assertIn("2027-02-04", readme)
            self.assertNotIn(attack()["text"], readme)
            self.assertNotIn(str(practice_gold["leave_lag"]), readme)
            self.assertNotIn(str(practice_gold["phone_only"]), readme)

    def test_the_interviews_reach_the_summary_and_the_leave(self) -> None:
        """Fails when the access script does not release the reason mix and the handoff
        summary, or when the architect script does not release the late leave and the
        warehouse feed. The required-fact lists must stay as they were.
        """
        questions = W4D5_ROOT / "Student_Copy" / "packet" / "interviews"
        access = run(load_personas()["access-mgr"], _lines(questions / "access-mgr.questions.txt"))
        released = [fact_id for turn in access for fact_id in turn["released"]]
        self.assertEqual(released, ["reason-mix", "handoff-summary"])
        self.assertEqual(load_personas()["access-mgr"]["must_surface"], ("returns-and-slots", "reason-mix"))
        ea = run(load_personas()["ea"], _lines(questions / "ea.questions.txt"))
        released = [fact_id for turn in ea for fact_id in turn["released"]]
        self.assertEqual(released, ["late-leave", "warehouse-bi"])
        self.assertEqual(load_personas()["ea"]["must_surface"], ("ain-file", "hl7-pair"))

    def test_demo_prints_the_question(self) -> None:
        """Fails when the demo does not print the benefit question, or when it prints the
        hidden reading, a count, the attack text, or the watermark.
        """
        profile = load("practice")
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "practice"])
        text = stdout.getvalue()
        shown = gold(profile)
        self.assertEqual(text.splitlines(), [shown["demo"]["question"]])
        self.assertNotIn(_ANSWER, text)
        self.assertNotIn(str(shown["leave_lag"]), text)
        self.assertNotIn(str(shown["phone_only"]), text)
        self.assertNotIn(attack()["text"], text)
        self.assertNotIn(profile.canary(), text)

    def test_lessons_do_not_state_the_canary_or_the_counts(self) -> None:
        """Fails when a lesson or packet source contains the watermark, or when a lesson
        page contains the attack text or a bare count.
        """
        release_trees = (
            W4D5_ROOT / "Student_Copy" / "packet" / "release",
            W4D5_ROOT / "Solution_Copy" / "sources",
        )
        profile = load("practice")
        shown = gold(profile)
        prose = []
        code = []
        for path in W4D5_ROOT.rglob("*"):
            if any(path.is_relative_to(root) for root in release_trees):
                continue
            if not path.is_file() or path.suffix not in _TEXT:
                continue
            text = path.read_text(encoding="utf-8")
            code.append(text)
            if path.suffix == ".md":
                prose.append(text)
        notes = "\n".join(prose)
        blob = "\n".join(code)
        self.assertNotIn(profile.canary(), blob)
        self.assertNotIn(attack()["text"], notes)
        self.assertFalse(_bare(notes, shown["leave_lag"]))
        self.assertFalse(_bare(notes, shown["phone_only"]))

    def test_modules_differ_and_both_copies_pass(self) -> None:
        """Fails when a shell module matches the filled copy, or when either suite fails."""
        for name in _APP:
            shell = (W4D5_APP / name).read_bytes()
            filled = (W4D5_WORK / "app" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        work = _suite(W4D5_WORK)
        shell = _suite(W4D5_APP.parent)
        self.assertEqual(work.returncode, 0, work.stdout + work.stderr)
        self.assertEqual(shell.returncode, 0, shell.stdout + shell.stderr)


if __name__ == "__main__":
    unittest.main()
