"""Day 5 of Week 3: the second run, the rehearsal brief, and the readout."""

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
from alwaha.paths import W3D5_APP, W3D5_ROOT
from alwaha.release.fingerprint import fingerprint
from alwaha.release.w3d4 import write_w3d4
from alwaha.release.w3d5 import write_w3d5

_CDO = ["What does the front desk cover?", "When does the board want the service live?"]
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
    chunks = []
    for path in pack.rglob("*"):
        if path.is_file():
            chunks.append(path.read_text(encoding="utf-8"))
    return "\n".join(chunks)


class ReleaseTests(unittest.TestCase):
    def test_same_seed_matches_and_day_4_stays(self) -> None:
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
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_w3d5(practice, root / "practice" / "pack", root / "practice-truth")
            write_w3d5(small, root / "small" / "pack", root / "small-truth")
            self.assertNotIn(practice.canary(), _blob(root / "practice" / "pack"))
            self.assertNotIn(small.canary(), _blob(root / "small" / "pack"))
            self.assertNotEqual(
                (root / "practice" / "pack" / "finance" / "prices.csv").read_text(encoding="utf-8"),
                (root / "small" / "pack" / "finance" / "prices.csv").read_text(encoding="utf-8"),
            )
            practice_gold = json.loads((root / "practice-truth" / "w3d5_gold.json").read_text(encoding="utf-8"))
            small_gold = json.loads((root / "small-truth" / "w3d5_gold.json").read_text(encoding="utf-8"))
            self.assertEqual(practice_gold, gold(practice))
            self.assertEqual(small_gold, gold(small))

    def test_the_pack_keeps_labels_and_the_gate_map_out(self) -> None:
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            write_w3d5(profile, pack, root / "truth")
            hidden = gold(profile)
            blob = _blob(pack)
            self.assertIn(hidden["case_date"], (pack / "notices" / "rehearsal.md").read_text(encoding="utf-8"))
            self.assertNotIn('"label"', (pack / "slices" / "before.jsonl").read_text(encoding="utf-8"))
            self.assertNotIn("keep", (pack / "slices" / "personal.jsonl").read_text(encoding="utf-8"))
            self.assertNotIn("req-cite", (pack / "gates" / "stage-gate.md").read_text(encoding="utf-8"))
            self.assertNotIn("16 weeks", blob)
            self.assertNotIn("phc-templates still generates", blob)
            self.assertNotIn(profile.canary(), blob)
            self.assertGreater(hidden["metrics"]["after"], hidden["metrics"]["before"])


class DemoTests(unittest.TestCase):
    def test_demo_names_the_disagreement_and_not_the_price(self) -> None:
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
        self.assertNotIn("p-triage", text)
        self.assertNotIn(str(hidden["cost"]["price"]), text)
        self.assertNotIn(profile.canary(), text)

    def test_lessons_do_not_state_the_canary(self) -> None:
        lessons = []
        for path in W3D5_ROOT.rglob("*"):
            if not path.is_file() or "work" in path.parts:
                continue
            if path.suffix in {".md", ".py", ".yml", ".yaml"}:
                lessons.append(path.read_text(encoding="utf-8"))
        self.assertNotIn(load("practice").canary(), "\n".join(lessons))

    def test_modules_differ_and_only_the_copy_passes(self) -> None:
        for name in _APP:
            shell = (W3D5_APP / name).read_bytes()
            filled = (W3D5_ROOT / "work" / "app" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        for name in _TESTS:
            shell = (W3D5_ROOT / "tests" / name).read_bytes()
            filled = (W3D5_ROOT / "work" / "tests" / name).read_bytes()
            self.assertEqual(shell, filled, name)
        shell_ci = (W3D5_ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
        work_ci = (W3D5_ROOT / "work" / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
        self.assertIn("# improvement-gate:", shell_ci)
        self.assertIn("\n  improvement-gate:\n", work_ci)
        work = _suite(W3D5_ROOT / "work")
        shell = _suite(W3D5_ROOT)
        self.assertEqual(work.returncode, 0, work.stdout + work.stderr)
        self.assertNotEqual(shell.returncode, 0, shell.stdout + shell.stderr)

    def test_the_disagreement_uses_the_existing_trees(self) -> None:
        personas = load_personas()
        sponsor = run(personas["cdo"], _CDO)
        officer = run(personas["dpo"], _DPO)
        self.assertIn("triage", sponsor[0]["answer"])
        self.assertEqual(sponsor[0]["released"], [])
        self.assertEqual(officer[-1]["released"], ["signed-ruling"])
        self.assertFalse(any(char.isdigit() for char in officer[-1]["answer"]))


def _suite(folder: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
        cwd=folder,
        capture_output=True,
        text=True,
        check=False,
    )


if __name__ == "__main__":
    unittest.main()
