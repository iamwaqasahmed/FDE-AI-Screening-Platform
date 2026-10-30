"""Module 3, Lesson 3: criteria v4, the change feed, and citations.

Guards the criteria release, the change feed, and the citation binding.

Earlier days must survive the write. Practice and small packs must match and
must carry no watermark. The notice must name the specialties that changed and
must not name the one that did not. The draft status and the unauthorized
circular must remain visible in the learner files, while held question text must
not. The demo may name the leaflet pair and must not quote the clause. The
shell suite must fail and the filled suite must pass.
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
from alwaha.demo.duplicate import main as demo_main
from alwaha.engagement.interview import run
from alwaha.engagement.personas import load_personas
from alwaha.engagement.m03_l03 import gold
from alwaha.engagement.m03_l03_docs import feed, snapshot
from alwaha.engagement.m03_l03_rules import apply, build, rank
from alwaha.paths import M03_L03_APP, M03_L03_ROOT, M03_L03_TEMPLATES, M03_L03_WORK
from alwaha.release.m01_l02 import write_m01_l02
from alwaha.release.m01_l03 import write_m01_l03
from alwaha.release.m01_l04 import write_m01_l04
from alwaha.release.m01_l05 import write_m01_l05
from alwaha.release.fingerprint import fingerprint
from alwaha.release.m02_l01 import write_m02_l01
from alwaha.release.m02_l02 import write_m02_l02
from alwaha.release.m02_l03 import write_m02_l03
from alwaha.release.m02_l04 import write_m02_l04
from alwaha.release.m02_l05 import write_m02_l05
from alwaha.release.m03_l01 import write_m03_l01
from alwaha.release.m03_l02 import write_m03_l02
from alwaha.release.m03_l03 import write_m03_l03
from alwaha.release.write import write_release

# Primary-care script. The second turn should release the template fact.
_PHC = [
    "Why does a hospital return a referral?",
    "Which criteria version does the template form use?",
]
# Coordinator script. The second turn should release the draft and should not name a specialty.
_COORD = [
    "Why is the coordinator queue so long?",
    "Was the v4 criteria circulated as a draft, and is it the version in use?",
]
_APP = (
    "chunk.py",
    "embed.py",
    "index.py",
    "search.py",
    "filter.py",
    "bind.py",
    "cite.py",
    "sync.py",
    "vision.py",
    "conflict.py",
    "catalog.py",
)
_TESTS = (
    "test_chunk.py",
    "test_embed.py",
    "test_index.py",
    "test_search.py",
    "test_filter.py",
    "test_bind.py",
    "test_cite.py",
    "test_sync.py",
    "test_vision.py",
    "test_conflict.py",
    "test_catalog.py",
)
# Held question ids and the document each one must bind to. The gold file is checked against this map.
_EXPECT = {
    "held-endo": "crit-endo-v4",
    "held-flight": "crit-endo-v3",
    "held-hours": "circ-ramadan",
    "held-leaflet": "leaflet-prep",
    "held-neuro": "crit-neuro-v3",
}


def _canary_count(pack: Path, canary: str) -> int:
    """Count watermark hits across every file in a pack.

    This day's pack is supposed to have none.
    """
    total = 0
    for path in pack.rglob("*"):
        if path.is_file():
            total += path.read_text(encoding="utf-8").count(canary)
    return total


def _blob(pack: Path) -> str:
    """Join every file in a pack so a held question cannot hide in a fixture the prose
    join would skip.
    """
    chunks = []
    for path in pack.rglob("*"):
        if path.is_file():
            chunks.append(path.read_text(encoding="utf-8"))
    return "\n".join(chunks)


class ReleaseTests(unittest.TestCase):
    """Catches a pack that rewrites an earlier day, that differs by profile, or that
    publishes a held question.
    """
    def test_same_seed_matches_and_earlier_days_stay(self) -> None:
        """Fails when a second write disagrees, when an earlier pack or gold file changes,
        or when this lesson's gold is missing from the hidden side or present in the pack.
        """
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            packs = [root / f"m01l{index}" for index in range(1, 6)]
            truth = root / "truth"
            write_release(profile, packs[0], truth)
            write_m01_l02(profile, packs[1], truth)
            write_m01_l03(profile, packs[2], truth)
            write_m01_l04(profile, packs[3], truth)
            write_m01_l05(profile, packs[4], truth)
            week2 = [root / f"m02l{index}" for index in range(1, 6)]
            write_m02_l01(profile, week2[0], truth)
            write_m02_l02(profile, week2[1], truth)
            write_m02_l03(profile, week2[2], truth)
            write_m02_l04(profile, week2[3], truth)
            write_m02_l05(profile, week2[4], truth)
            write_m03_l01(profile, root / "m03_l01", truth)
            write_m03_l02(profile, root / "m03_l02", truth)
            # Fingerprints of the earlier packs, including the two previous days, plus their gold files.
            before = (
                tuple(fingerprint(pack) for pack in packs),
                tuple(fingerprint(pack) for pack in week2),
                fingerprint(root / "m03_l01"),
                fingerprint(root / "m03_l02"),
                (truth / "personas.json").read_bytes(),
                (truth / "m03_l01_gold.json").read_bytes(),
                (truth / "m03_l02_gold.json").read_bytes(),
            )
            # Write this lesson twice. The two results must agree, and the earlier lessons must stay as they were.
            first = write_m03_l03(profile, root / "m03_l03", truth)
            again = write_m03_l03(profile, root / "m03_l03", truth)
            self.assertEqual(first, again)
            self.assertEqual(
                before,
                (
                    tuple(fingerprint(pack) for pack in packs),
                    tuple(fingerprint(pack) for pack in week2),
                    fingerprint(root / "m03_l01"),
                    fingerprint(root / "m03_l02"),
                    (truth / "personas.json").read_bytes(),
                    (truth / "m03_l01_gold.json").read_bytes(),
                    (truth / "m03_l02_gold.json").read_bytes(),
                ),
            )
            # This day's gold stays on the hidden side.
            self.assertTrue((truth / "m03_l03_gold.json").is_file())
            self.assertFalse((root / "m03_l03" / "m03_l03_gold.json").exists())

    def test_profiles_match_and_the_canary_stays_out(self) -> None:
        """Fails when either pack contains a watermark, when the two packs differ, or when
        a gold file drifts from the generator.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_m03_l03(practice, root / "practice" / "pack", root / "practice-truth")
            write_m03_l03(small, root / "small" / "pack", root / "small-truth")
            self.assertEqual(_canary_count(root / "practice" / "pack", practice.canary()), 0)
            self.assertEqual(_canary_count(root / "small" / "pack", small.canary()), 0)
            self.assertEqual(fingerprint(root / "practice" / "pack"), fingerprint(root / "small" / "pack"))
            for profile, folder in ((practice, "practice-truth"), (small, "small-truth")):
                hidden = json.loads((root / folder / "m03_l03_gold.json").read_text(encoding="utf-8"))
                self.assertEqual(hidden, gold(profile))

    def test_the_notice_names_three_specialties_and_the_held_text_stays_out(self) -> None:
        """Fails when the notice omits a changed specialty or includes the unchanged one,
        when the draft or the unauthorized circular is hidden, or when a held question
        appears in the pack. The vector rank and the hybrid rank must still disagree
        on the question that separates them.
        """
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            write_m03_l03(profile, pack, root / "truth")
            hidden = json.loads((root / "truth" / "m03_l03_gold.json").read_text(encoding="utf-8"))
            blob = _blob(pack)
            note = (pack / "notices" / "criteria-v4.md").read_text(encoding="utf-8")
            # The notice names the three changed specialties and not the unchanged one.
            for name in ("endo", "ophth", "card"):
                self.assertIn(name, note)
            self.assertNotIn("neuro", note)
            # The draft page and the unauthorized circular are still visible. The watermark is not in the pack.
            self.assertIn("status: draft", (pack / "dms" / "crit-endo-v4.md").read_text(encoding="utf-8"))
            self.assertIn("circ-ramadan-unauth", (pack / "feed" / "changes.jsonl").read_text(encoding="utf-8"))
            self.assertNotIn(profile.canary(), blob)
            # Each held question points at the expected document, and the question text stays out of the pack.
            expects = {row["question"]["question_id"]: row["expect"] for row in hidden["held"]}
            for question_id, doc_id in _EXPECT.items():
                self.assertEqual(expects[question_id]["doc_id"], doc_id)
            for row in hidden["held"]:
                self.assertNotIn(row["question"]["text"], blob)
            self.assertEqual(expects["held-none"]["refusal"], "no-document")
            # Vector rank and hybrid rank still disagree on the question that separates them.
            current = apply(snapshot(), feed())["docs"]
            question = hidden["hybrid_question"]["text"]
            self.assertEqual(rank(question, build(current), "vector")[0]["doc_id"], hidden["vector_doc"])
            self.assertEqual(rank(question, build(current), "hybrid")[0]["doc_id"], hidden["hybrid_doc"])


class DemoTests(unittest.TestCase):
    """Catches a demo or a lesson that quotes a held question, a module that was not
    changed, a shell suite that passes, or an interview that drops the draft.
    """
    def test_demo_names_the_pair_and_not_the_clause(self) -> None:
        """Fails when the demo does not list the leaflets and the superseded line, or when
        it prints the watermark, the vision clause, or the midnight wording.
        """
        profile = load("practice")
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "practice"])
        text = stdout.getvalue()
        hidden = gold(profile)
        self.assertEqual(text.splitlines(), [*hidden["leaflets"], "one is superseded"])
        self.assertNotIn(profile.canary(), text)
        self.assertNotIn(hidden["vision"], text)
        self.assertNotIn("past midnight", text)

    def test_lessons_do_not_state_the_held_questions(self) -> None:
        """Fails when lesson notes or templates contain the watermark or a held question.

        The test reads every lesson note and template and fails if the watermark or a held
        question appears in that prose.
        """
        notes = [path.read_text(encoding="utf-8") for path in M03_L03_ROOT.glob("README.md")]
        notes.extend(path.read_text(encoding="utf-8") for path in M03_L03_TEMPLATES.glob("*.md"))
        lesson_text = "\n".join(notes)
        hidden = gold(load("practice"))
        self.assertNotIn(load("practice").canary(), lesson_text)
        for row in hidden["held"]:
            self.assertNotIn(row["question"]["text"], lesson_text)

    def test_modules_differ_and_only_the_copy_passes(self) -> None:
        """Fails when a shell module matches the filled copy, when a packet test was
        rewritten, when the filled suite fails, or when the shell suite passes.
        """
        # Shell modules differ from the filled copy. Packet tests were not rewritten.
        packet = M03_L03_APP.parent
        for name in _APP:
            shell = (M03_L03_APP / name).read_bytes()
            filled = (M03_L03_WORK / "app" / name).read_bytes()
            self.assertNotEqual(shell, filled, name)
        for name in _TESTS:
            shell = (packet / "tests" / name).read_bytes()
            filled = (M03_L03_WORK / "tests" / name).read_bytes()
            self.assertEqual(shell, filled, name)
        # The filled suite passes. The shell suite does not.
        work = _suite(M03_L03_WORK)
        shell = _suite(packet)
        self.assertEqual(work.returncode, 0, work.stdout + work.stderr)
        self.assertNotEqual(shell.returncode, 0, shell.stdout + shell.stderr)

    def test_interviews_release_the_draft_and_the_template(self) -> None:
        """Fails when the template fact or the draft fact does not surface, or when the
        draft answer names a specialty. The required-fact lists must stay as they were.
        """
        personas = load_personas()
        phc = run(personas["phc-lead"], _PHC)
        self.assertEqual(phc[1]["released"], ["templates-v3"])
        coord = run(personas["coord-lead"], _COORD)
        self.assertEqual(coord[1]["released"], ["v4-draft"])
        self.assertNotIn("endo", coord[1]["answer"])
        self.assertEqual(personas["phc-lead"]["must_surface"], ("templates-v3",))
        self.assertEqual(personas["coord-lead"]["must_surface"], ("shorthand", "thursday", "v4-draft"))


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
