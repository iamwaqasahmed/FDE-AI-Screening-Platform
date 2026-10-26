"""Day 4 of Week 3: the benchmark, the campaign, and the judge.

Guards the benchmark release, the campaign notice, and the judge demo.

The previous retrieval day must survive the write. Profiles must differ, carry
no watermark, and disagree on the later visits. The campaign note may show the
case date and must not show the later visit counts. Labels, the held answer,
and the effect must stay out of the learner pack. The demo may say the judge
disagreed with the citation and must not name the item. The shell suite must
fail, the filled suite must pass, and only the filled pipeline may have the
evaluation gate turned on.
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
from alwaha.demo.judge import main as demo_main
from alwaha.engagement.interview import run
from alwaha.engagement.personas import load_personas
from alwaha.engagement.w3d4 import gold
from alwaha.engagement.w3d4_judge import HELD_DOC, HELD_SPAN
from alwaha.paths import W3D4_APP, W3D4_ROOT, W3D4_TEMPLATES, W3D4_WORK
from alwaha.release.fingerprint import fingerprint
from alwaha.release.w3d3 import write_w3d3
from alwaha.release.w3d4 import write_w3d4

# Sponsor script. The second turn should release the campaign fact and should not contain a digit.
_CDO = [
    "When does the board want the service live?",
    "Is an eye-screening campaign coming, and does the session plan still use last year's months?",
]
_APP = (
    "score.py",
    "forecast.py",
    "failures.py",
    "judge.py",
    "intervals.py",
    "experiment.py",
    "gate.py",
)
_TESTS = (
    "test_score.py",
    "test_forecast.py",
    "test_failures.py",
    "test_judge.py",
    "test_intervals.py",
    "test_experiment.py",
    "test_gate.py",
)
# Failure type names that must not appear in the learner-facing failure file.
_TYPES = ("hallucination", "retrieval", "reasoning", "workflow")


def _blob(pack: Path) -> str:
    """Join every file in a pack so a held answer cannot hide outside the notices."""
    chunks = []
    for path in pack.rglob("*"):
        if path.is_file():
            chunks.append(path.read_text(encoding="utf-8"))
    return "\n".join(chunks)


def _canary_count(pack: Path, canary: str) -> int:
    """Count watermark hits across every file in a pack.

    This day's pack is supposed to have none.
    """
    total = 0
    for path in pack.rglob("*"):
        if path.is_file():
            total += path.read_text(encoding="utf-8").count(canary)
    return total


class ReleaseTests(unittest.TestCase):
    """Catches a pack that rewrites the previous day, that leaks a label or a held
    answer, or that publishes the campaign's effect.
    """
    def test_same_seed_matches_and_day_3_stays(self) -> None:
        """Fails when a second write disagrees, when the previous pack changes, or when
        this day's gold is missing from the hidden side or present in the pack.
        """
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            truth = root / "truth"
            write_w3d3(profile, root / "w3d3", truth)
            before = fingerprint(root / "w3d3")
            first = write_w3d4(profile, root / "w3d4", truth)
            again = write_w3d4(profile, root / "w3d4", truth)
            self.assertEqual(first, again)
            self.assertEqual(before, fingerprint(root / "w3d3"))
            self.assertTrue((truth / "w3d4_gold.json").is_file())
            self.assertFalse((root / "w3d4" / "w3d4_gold.json").exists())

    def test_profiles_differ_and_the_canary_stays_out(self) -> None:
        """Fails when either pack contains a watermark, when the fingerprints match, or
        when the later-visit lists do not differ across profiles.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_w3d4(practice, root / "practice" / "pack", root / "practice-truth")
            write_w3d4(small, root / "small" / "pack", root / "small-truth")
            self.assertEqual(_canary_count(root / "practice" / "pack", practice.canary()), 0)
            self.assertEqual(_canary_count(root / "small" / "pack", small.canary()), 0)
            self.assertNotEqual(fingerprint(root / "practice" / "pack"), fingerprint(root / "small" / "pack"))
            practice_gold = json.loads((root / "practice-truth" / "w3d4_gold.json").read_text(encoding="utf-8"))
            small_gold = json.loads((root / "small-truth" / "w3d4_gold.json").read_text(encoding="utf-8"))
            self.assertEqual(practice_gold, gold(practice))
            self.assertEqual(small_gold, gold(small))
            self.assertNotEqual(practice_gold["later_visits"], small_gold["later_visits"])

    def test_the_pack_keeps_labels_and_the_effect_out(self) -> None:
        """Fails when the campaign note drops the case date or prints a later visit count,
        when labels or failure types or the held item appear in the pack, or when the
        winner and the peek winner are not the two different arms. Extraction must still
        meet its budget.
        """
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            write_w3d4(profile, pack, root / "truth")
            hidden = json.loads((root / "truth" / "w3d4_gold.json").read_text(encoding="utf-8"))
            blob = _blob(pack)
            note = (pack / "notices" / "campaign.md").read_text(encoding="utf-8")
            self.assertIn(hidden["case_date"], note)
            for row in hidden["later_visits"]:
                self.assertNotIn(str(row["visits"]), note)
            self.assertNotIn("winner", (pack / "notices" / "ab-status.md").read_text(encoding="utf-8"))
            self.assertNotIn('"label"', (pack / "slices" / "score.jsonl").read_text(encoding="utf-8"))
            failure_text = (pack / "slices" / "failures.jsonl").read_text(encoding="utf-8")
            for name in _TYPES:
                self.assertNotIn(name, failure_text)
            held = hidden["calibration_held"][0]
            self.assertNotIn(held["answer"], blob)
            self.assertNotIn(HELD_SPAN, blob)
            self.assertNotIn(HELD_DOC, blob)
            self.assertNotIn(profile.canary(), blob)
            self.assertGreaterEqual(hidden["metrics"]["extraction"], hidden["budgets"]["extraction"])
            self.assertEqual(hidden["ab_status"]["winner"], "clause")
            self.assertEqual(hidden["ab_status"]["peek_winner"], "short")


class DemoTests(unittest.TestCase):
    """Catches a demo or a lesson that names the held item, a module that was not
    changed, a shell suite that passes, or a campaign question that became a
    first-week fact.
    """
    def test_demo_names_the_miss_and_not_the_item(self) -> None:
        """Fails when the demo does not say the judge marked the citation correct while
        the citation is not the in-force document, or when it prints the held answer,
        the span, the document id, or the watermark.
        """
        profile = load("practice")
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "practice"])
        text = stdout.getvalue()
        hidden = gold(profile)
        self.assertEqual(
            text.splitlines(),
            ["the judge marked the citation correct", "the citation is not the in-force document"],
        )
        held = hidden["calibration_held"][0]
        self.assertNotIn(held["answer"], text)
        self.assertNotIn(held["span"], text)
        self.assertNotIn(held["doc_id"], text)
        self.assertNotIn(profile.canary(), text)

    def test_lessons_do_not_state_the_held_item(self) -> None:
        """Fails when lesson notes or templates contain the watermark, the held answer, or
        the span.
        """
        notes = [path.read_text(encoding="utf-8") for path in W3D4_ROOT.glob("*.md")]
        notes.extend(path.read_text(encoding="utf-8") for path in W3D4_TEMPLATES.glob("*.md"))
        lesson_text = "\n".join(notes)
        hidden = gold(load("practice"))
        held = hidden["calibration_held"][0]
        self.assertNotIn(load("practice").canary(), lesson_text)
        self.assertNotIn(held["answer"], lesson_text)
        self.assertNotIn(held["span"], lesson_text)

    def test_modules_differ_and_only_the_copy_passes(self) -> None:
        """Fails when a shell module matches the filled copy, when a packet test was
        rewritten, when the evaluation gate is not commented in the shell and active
        in the filled copy, when the filled suite fails, or when the shell suite passes.
        """
        packet = W3D4_APP.parent
        for name in _APP:
            shell = (W3D4_APP / name).read_bytes()
            filled = (W3D4_WORK / "app" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        for name in _TESTS:
            shell = (packet / "tests" / name).read_bytes()
            filled = (W3D4_WORK / "tests" / name).read_bytes()
            self.assertEqual(shell, filled, name)
        shell_ci = (packet / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
        work_ci = (W3D4_WORK / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
        self.assertIn("# evaluation-gate:", shell_ci)
        self.assertIn("\n  evaluation-gate:\n", work_ci)
        work = _suite(W3D4_WORK)
        shell = _suite(packet)
        self.assertEqual(work.returncode, 0, work.stdout + work.stderr)
        self.assertNotEqual(shell.returncode, 0, shell.stdout + shell.stderr)

    def test_the_campaign_question_is_not_a_week_1_fact(self) -> None:
        """Fails when the campaign question does not release its own fact, when that
        answer contains a digit, or when the sponsor's required-fact list changed.
        """
        personas = load_personas()
        turns = run(personas["cdo"], _CDO)
        self.assertEqual(turns[1]["released"], ["eye-campaign"])
        self.assertFalse(any(char.isdigit() for char in turns[1]["answer"]))
        self.assertEqual(personas["cdo"]["must_surface"], ("gpu-lead-time",))


def _suite(folder: Path) -> subprocess.CompletedProcess[str]:
    """Run a packet's own unit tests and return the process result without raising."""
    return subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
        cwd=folder,
        capture_output=True,
        text=True,
        check=False,
    )


if __name__ == "__main__":
    unittest.main()
