"""Module 1, Lesson 1 build, interviews, and checks.

Guards the first release, the interview scorer, and the repo and interview checkers.

The build tests keep the corpus causes, make sure one profile writes the same pack
twice, and make sure two profiles do not share a watermark. The interview tests
walk each persona's question tree and the command the learner runs. The check
tests build a small work tree and then break it on purpose.

The work-tree fixture copies the starter, adds the dev credential, fills the
access request, and writes a winning question list plus a short note for the
two personas the checker reads. A problem list must describe the failure without
repeating a watermark or a banned sentence.
"""

from __future__ import annotations

import io
import shutil
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from alwaha.config.profile import load
from alwaha.corpus.texts import fact_problems, minutes, postmortem
from alwaha.engagement.interview import run, score_turns, winning_questions
from alwaha.engagement.personas import load_personas
from alwaha.interview import main as interview_main
from alwaha.check.interviews import interview_problems, load_truth
from alwaha.check.repo import repo_problems
from alwaha.paths import STARTER_ROOT
from alwaha.release.write import write_release
from alwaha.corpus.texts import assistant_use


def _fill_request(blank: str) -> str:
    """Fill the blank access-request fields the checker expects.

    The requester, the data, the purpose, and the classification are the fixture.
    Only the first empty label of each field is replaced, so a second copy of the
    label would stay blank.
    """
    # Fixture answers for the blank access request. They are not hidden release facts.
    values = {
        "Requester": "Noura Al-Qahtani",
        "Data": "dev credentials and the kickoff corpus",
        "Purpose": "Module 1 Lesson 1 interviews and the starter pipeline",
        "Classification": "internal",
    }
    filled = blank
    for field, value in values.items():
        filled = filled.replace(f"- {field}:", f"- {field}: {value}", 1)
    return filled


def _notes(persona_id: str) -> str:
    """A short note that attributes its lines to the persona and marks them as a claim
    or a request.

    The words are not a hidden fact. They exist so the checker has a note file to
    grade, and so a later test can append a banned sentence to one of them.
    """
    return "\n".join(
        [
            "| Who | Their words | Kind |",
            "| --- | --- | --- |",
            f"| {persona_id} | The opening line is theirs, not ours | claim |",
            f"| {persona_id} | Ask a follow-up before treating it as measured | request |",
            "",
        ]
    )


class BuildTests(unittest.TestCase):
    """Catches a corpus or a release that does not reproduce.

    A dropped cause, a pack that changes when the same profile is written twice, or
    a watermark that leaks from one profile into another, all fail here.
    """
    def test_minutes_keep_the_causes(self) -> None:
        """Fails when the minutes or the postmortem lose a cause the corpus is supposed to keep."""
        self.assertEqual(fact_problems(minutes(), postmortem()), [])

    def test_same_seed_matches_and_profiles_differ(self) -> None:
        """Fails when the same profile writes two different packs, when the sample letter
        carries the wrong watermark, or when the starter policy page drifts from the
        corpus page that was copied into the pack.
        """
        # Two profiles. Their watermarks must not be the same string.
        practice, small = load("practice"), load("small")
        self.assertNotEqual(practice.canary(), small.canary())
        # Write the small profile twice into one temporary pack.
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            first = write_release(small, root / "pack", root / "truth")
            second = write_release(small, root / "pack", root / "truth")
            # The two writes agree. The sample letter carries only the small watermark.
            self.assertEqual(first, second)
            letter = (root / "pack" / "sample" / "referral-letter.md").read_text(encoding="utf-8")
            self.assertIn(small.canary(), letter)
            self.assertNotIn(practice.canary(), letter)
            # The starter policy page and the copy inside the pack are the same corpus page.
            policy = (STARTER_ROOT / "policy" / "pol-assistant-use.md").read_text(encoding="utf-8")
            self.assertEqual(policy, assistant_use())
            self.assertEqual((root / "pack" / "corpus" / "pol-assistant-use.md").read_text(encoding="utf-8"), policy)


class InterviewTests(unittest.TestCase):
    """Catches an interview tree that opens too early, and a command that shows the score.

    A winning script has to release every fact. A follow-up asked before its parent
    must stay closed. The command the learner runs may speak the answer and must not
    print a score or the hidden fact id.
    """
    def test_winning_script_reaches_every_fact(self) -> None:
        """Fails when the prepared question list leaves any persona's required fact unreleased."""
        # Run each persona's winning question list. Every required fact must be released.
        for data in load_personas().values():
            result = score_turns(data, run(data, winning_questions(data)))
            self.assertTrue(result["ok"], data["id"])

    def test_follow_up_before_its_parent_stays_closed(self) -> None:
        """Fails when a child question, asked on its own, still counts as a completed interview.

        The parent has to be opened first. Keywords from the follow-up are not enough.
        """
        # Ask only the follow-up, with its parent still closed.
        data = load_personas()["cdo"]
        child = next(node for node in data["tree"] if node.parent)
        result = score_turns(data, run(data, [" ".join(child.keywords)]))
        # Keywords from the child are not enough. The interview stays incomplete.
        self.assertFalse(result["ok"])

    def test_command_prints_no_score(self) -> None:
        """Fails when the interview command hides the answer the persona would say, or when
        it prints a score or the hidden fact id.
        """
        # Write the winning questions to a script and run the learner command, capturing its output.
        data = load_personas()["cdo"]
        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "questions.txt"
            script.write_text("\n".join(winning_questions(data)), encoding="utf-8")
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                interview_main(["--persona", "cdo", "--script", str(script)])
        text = stdout.getvalue()
        # The answer is printed. A score and the hidden fact id are not.
        self.assertIn("16 weeks", text)
        self.assertNotIn("Score", text)
        self.assertNotIn("gpu-lead-time", text)


class CheckTests(unittest.TestCase):
    """Catches a work tree the repo or interview checker mis-grades.

    A complete fixture must pass. A watermark copied into a tracked file must fail
    without the problem text echoing the watermark. An unfinished interview must
    fail without naming the hidden template fact, and a banned sentence in a note
    must fail without the problem text quoting that sentence.
    """
    def setUp(self) -> None:
        """Build a temporary small release and a work tree a finished learner would hand in.

        The starter is copied, the dev credential is added, the access request is filled,
        and two personas get a winning question file plus a short note. The persona
        truth and the watermark come from the hidden side of that release.
        """
        # A temporary small release. The pack and the hidden persona file both come from it.
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        write_release(load("small"), root / "pack", root / "truth")
        self.pack = root / "pack"
        self.personas, self.canary = load_truth(root / "truth" / "personas.json")
        # The work tree starts as the starter, then gains the dev credential and a filled request.
        self.work = root / "work"
        shutil.copytree(self.pack / "starter", self.work)
        (self.work / "credentials").mkdir()
        shutil.copy(self.pack / "credentials" / "dev.json", self.work / "credentials" / "dev.json")
        blank = (self.pack / "forms" / "access-request.md").read_text(encoding="utf-8")
        (self.work / "access-request.md").write_text(_fill_request(blank), encoding="utf-8")
        # Two personas get a winning question list and a short note. That is the finished hand-in.
        folder = self.work / "interviews"
        folder.mkdir()
        for persona_id in ("phc-lead", "dpo"):
            questions = winning_questions(self.personas[persona_id])
            (folder / f"{persona_id}.questions.txt").write_text("\n".join(questions) + "\n", encoding="utf-8")
            (folder / f"{persona_id}.notes.md").write_text(_notes(persona_id), encoding="utf-8")

    def tearDown(self) -> None:
        """Delete the temporary release and work tree created for this case."""
        self.tmp.cleanup()

    def test_good_work_passes(self) -> None:
        """Fails when the finished fixture still produces a repo problem or an interview problem."""
        self.assertEqual(repo_problems(self.work, self.canary), [])
        self.assertEqual(interview_problems(self.work, self.personas), [])

    def test_canary_in_a_tracked_file_fails_without_echoing_it(self) -> None:
        """Fails when a watermark pasted into the tracked readme is ignored, or when a
        problem message contains the watermark itself.
        """
        readme = self.work / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + self.canary + "\n", encoding="utf-8")
        problems = repo_problems(self.work, self.canary)
        self.assertTrue(problems)
        self.assertTrue(all(self.canary not in item for item in problems))

    def test_incomplete_interview_and_banned_sentence(self) -> None:
        """Fails in either direction the interview checker can leak.

        An unfinished question file must be reported without naming the hidden template
        fact. After that file is restored, a banned sentence in the other persona's note
        must be reported without the problem list quoting the sentence.
        """
        # Replace one winning script with a line that does not finish the interview.
        (self.work / "interviews" / "phc-lead.questions.txt").write_text("hello\n", encoding="utf-8")
        problems = interview_problems(self.work, self.personas)
        # The unfinished interview is reported, and the problem text does not name the hidden template.
        self.assertIn("phc-lead interview is incomplete", problems)
        self.assertTrue(all("templates-v3" not in item for item in problems))
        # Restore that script, then append a banned sentence to the other persona's note.
        notes = self.work / "interviews" / "dpo.notes.md"
        notes.write_text(notes.read_text(encoding="utf-8") + "The external model may receive identified patient data.\n", encoding="utf-8")
        (self.work / "interviews" / "phc-lead.questions.txt").write_text(
            "\n".join(winning_questions(self.personas["phc-lead"])) + "\n", encoding="utf-8"
        )
        banned = interview_problems(self.work, self.personas)
        # The note is reported, and the problem list does not quote the sentence.
        self.assertIn("notes contain a banned sentence", banned)
        self.assertNotIn("The external model may receive identified patient data.", banned)


if __name__ == "__main__":
    unittest.main()
