"""Day 5 of Week 3: the second run, the rehearsal brief, and the readout.

Guards the second-run release, the rehearsal brief, and the readout demo.

The previous benchmark day must survive the write. Profiles must differ in their
price sheets and must not carry a watermark. The rehearsal note may show the
case date. Labels, the keep-or-drop mark, the gate ids, and the deadline phrase
must stay out of the learner pack. The demo may name the disagreement and must
not print a price. The shell suite must fail and the filled suite must pass,
and only the filled pipeline may have the improvement gate turned on.
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
from alwaha.demo.brief import main as demo_main
from alwaha.engagement.interview import run
from alwaha.engagement.personas import load_personas
from alwaha.engagement.w3d5 import gold
from alwaha.paths import W3D5_APP, W3D5_ROOT, W3D5_TEMPLATES, W3D5_WORK
from alwaha.release.fingerprint import fingerprint
from alwaha.release.w3d4 import write_w3d4
from alwaha.release.w3d5 import write_w3d5

# Sponsor script. The opening turn should mention triage and should not release a fact.
_CDO = ["What does the front desk cover?", "When does the board want the service live?"]
# Data-protection script. The last turn should release the signed ruling and should not contain a digit.
_DPO = [
    "How is patient data protected?",
    "What does the ruling say about the external model?",
    "Is the ruling signed?",
]
_APP = ("repair.py", "remeasure.py", "cost.py", "backlog.py", "gates.py", "personal.py")
_TESTS = (
    "test_repair.py",
    "test_remeasure.py",
    "test_cost.py",
    "test_backlog.py",
    "test_gates.py",
    "test_personal.py",
)


def _blob(pack: Path) -> str:
    """Join every file in a pack so a gate id cannot hide outside the notices.

    The release test searches that joined text and fails when a deadline phrase or the watermark
    shows up anywhere in the pack.
    """
    chunks = []
    for path in pack.rglob("*"):
        if path.is_file():
            chunks.append(path.read_text(encoding="utf-8"))
    return "\n".join(chunks)


class ReleaseTests(unittest.TestCase):
    """Catches a pack that rewrites the previous day or that publishes a label, a gate
    id, or the deadline phrase.
    """
    def test_same_seed_matches_and_day_4_stays(self) -> None:
        """Fails when a second write disagrees, when the previous pack changes, or when
        this day's gold is missing from the hidden side or present in the pack.
        """
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            truth = root / "truth"
            write_w3d4(profile, root / "w3d4", truth)
            before = fingerprint(root / "w3d4")
            first = write_w3d5(profile, root / "w3d5", truth)
            again = write_w3d5(profile, root / "w3d5", truth)
            self.assertEqual(first, again)
            self.assertEqual(before, fingerprint(root / "w3d4"))
            self.assertTrue((truth / "w3d5_gold.json").is_file())
            self.assertFalse((root / "w3d5" / "w3d5_gold.json").exists())

    def test_profiles_differ_and_the_canary_stays_out(self) -> None:
        """Fails when either pack contains a watermark, when the price sheets match, or
        when a gold file drifts from the generator.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_w3d5(practice, root / "practice" / "pack", root / "practice-truth")
            write_w3d5(small, root / "small" / "pack", root / "small-truth")
            # Neither pack contains its watermark, and the price sheets differ.
            self.assertNotIn(practice.canary(), _blob(root / "practice" / "pack"))
            self.assertNotIn(small.canary(), _blob(root / "small" / "pack"))
            self.assertNotEqual(
                (root / "practice" / "pack" / "finance" / "prices.csv").read_text(encoding="utf-8"),
                (root / "small" / "pack" / "finance" / "prices.csv").read_text(encoding="utf-8"),
            )
            # Both gold files match the generator.
            practice_gold = json.loads((root / "practice-truth" / "w3d5_gold.json").read_text(encoding="utf-8"))
            small_gold = json.loads((root / "small-truth" / "w3d5_gold.json").read_text(encoding="utf-8"))
            self.assertEqual(practice_gold, gold(practice))
            self.assertEqual(small_gold, gold(small))

    def test_the_pack_keeps_labels_and_the_gate_map_out(self) -> None:
        """Fails when the rehearsal note drops the case date, when labels or the keep mark
        or a gate id or the deadline phrase appear in the pack, or when the second
        measurement is not the better of the two.
        """
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            write_w3d5(profile, pack, root / "truth")
            # The rehearsal note keeps the case date.
            hidden = gold(profile)
            blob = _blob(pack)
            self.assertIn(hidden["case_date"], (pack / "notices" / "rehearsal.md").read_text(encoding="utf-8"))
            # Labels, the keep mark, a gate id, and the deadline phrase stay out of the pack.
            self.assertNotIn('"label"', (pack / "slices" / "before.jsonl").read_text(encoding="utf-8"))
            self.assertNotIn("keep", (pack / "slices" / "personal.jsonl").read_text(encoding="utf-8"))
            self.assertNotIn("req-cite", (pack / "gates" / "stage-gate.md").read_text(encoding="utf-8"))
            self.assertNotIn("16 weeks", blob)
            self.assertNotIn("phc-templates still generates", blob)
            self.assertNotIn(profile.canary(), blob)
            # The second measurement is the better of the two.
            self.assertGreater(hidden["metrics"]["after"], hidden["metrics"]["before"])


class DemoTests(unittest.TestCase):
    """Catches a demo that prints a price, a lesson that prints the watermark, a shell
    suite that passes, or an interview that does not use the existing trees.
    """
    def test_demo_names_the_disagreement_and_not_the_price(self) -> None:
        """Fails when the demo does not state the sponsor's triage ask beside the
        data-protection refusal, or when it prints the triage id, a price, or the watermark.
        """
        # Run the demo. The lines are the sponsor's ask and the data-protection refusal.
        profile = load("practice")
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "practice"])
        text = stdout.getvalue()
        hidden = gold(profile)
        self.assertEqual(
            text.splitlines(),
            [
                "the sponsor asks for triage in the front desk",
                "the dpo keeps patient data off ext-large",
            ],
        )
        # The triage id, the price, and the watermark stay out of the output.
        self.assertNotIn("p-triage", text)
        self.assertNotIn(str(hidden["cost"]["price"]), text)
        self.assertNotIn(profile.canary(), text)

    def test_lessons_do_not_state_the_canary(self) -> None:
        """Fails when lesson notes or templates contain the watermark.

        The test reads every lesson note and template and fails if the watermark appears in that
        prose.
        """
        notes = [path.read_text(encoding="utf-8") for path in W3D5_ROOT.glob("*.md")]
        notes.extend(path.read_text(encoding="utf-8") for path in W3D5_TEMPLATES.glob("*.md"))
        lesson_text = "\n".join(notes)
        self.assertNotIn(load("practice").canary(), lesson_text)

    def test_modules_differ_and_only_the_copy_passes(self) -> None:
        """Fails when a shell module matches the filled copy, when a packet test was
        rewritten, when the improvement gate is not commented in the shell and active
        in the filled copy, when the filled suite fails, or when the shell suite passes.
        """
        # Shell modules differ from the filled copy. Packet tests were not rewritten.
        packet = W3D5_APP.parent
        for name in _APP:
            shell = (W3D5_APP / name).read_bytes()
            filled = (W3D5_WORK / "app" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        for name in _TESTS:
            shell = (packet / "tests" / name).read_bytes()
            filled = (W3D5_WORK / "tests" / name).read_bytes()
            self.assertEqual(shell, filled, name)
        # The improvement gate is commented in the shell and active in the filled copy.
        shell_ci = (packet / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
        work_ci = (W3D5_WORK / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
        self.assertIn("# improvement-gate:", shell_ci)
        self.assertIn("\n  improvement-gate:\n", work_ci)
        # The filled suite passes. The shell suite does not.
        work = _suite(W3D5_WORK)
        shell = _suite(packet)
        self.assertEqual(work.returncode, 0, work.stdout + work.stderr)
        self.assertNotEqual(shell.returncode, 0, shell.stdout + shell.stderr)

    def test_the_disagreement_uses_the_existing_trees(self) -> None:
        """Fails when the sponsor's opening turn releases a fact, or when the
        data-protection script does not end on the signed ruling. That last answer
        must not contain a digit.
        """
        personas = load_personas()
        sponsor = run(personas["cdo"], _CDO)
        officer = run(personas["dpo"], _DPO)
        self.assertIn("triage", sponsor[0]["answer"])
        self.assertEqual(sponsor[0]["released"], [])
        self.assertEqual(officer[-1]["released"], ["signed-ruling"])
        self.assertFalse(any(char.isdigit() for char in officer[-1]["answer"]))


def _suite(folder: Path) -> subprocess.CompletedProcess[str]:
    """Run a packet's own unit tests and return the process result without raising.

    The caller runs the filled packet, which must exit cleanly, and the unfinished packet,
    which must fail.
    """
    return subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
        cwd=folder,
        capture_output=True,
        text=True,
        check=False,
    )


if __name__ == "__main__":
    unittest.main()
