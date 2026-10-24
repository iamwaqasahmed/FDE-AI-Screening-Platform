"""Day 1 build, interviews, and checks."""

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
    values = {
        "Requester": "Noura Al-Qahtani",
        "Data": "dev credentials and the kickoff corpus",
        "Purpose": "Week 1 Day 1 interviews and the starter pipeline",
        "Classification": "internal",
    }
    filled = blank
    for field, value in values.items():
        filled = filled.replace(f"- {field}:", f"- {field}: {value}", 1)
    return filled


def _notes(persona_id: str) -> str:
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
    def test_minutes_keep_the_causes(self) -> None:
        self.assertEqual(fact_problems(minutes(), postmortem()), [])

    def test_same_seed_matches_and_profiles_differ(self) -> None:
        practice, small = load("practice"), load("small")
        self.assertNotEqual(practice.canary(), small.canary())
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            first = write_release(small, root / "pack", root / "truth")
            second = write_release(small, root / "pack", root / "truth")
            self.assertEqual(first, second)
            letter = (root / "pack" / "sample" / "referral-letter.md").read_text(encoding="utf-8")
            self.assertIn(small.canary(), letter)
            self.assertNotIn(practice.canary(), letter)
            policy = (STARTER_ROOT / "policy" / "pol-assistant-use.md").read_text(encoding="utf-8")
            self.assertEqual(policy, assistant_use())
            self.assertEqual((root / "pack" / "corpus" / "pol-assistant-use.md").read_text(encoding="utf-8"), policy)


class InterviewTests(unittest.TestCase):
    def test_winning_script_reaches_every_fact(self) -> None:
        for data in load_personas().values():
            result = score_turns(data, run(data, winning_questions(data)))
            self.assertTrue(result["ok"], data["id"])

    def test_follow_up_before_its_parent_stays_closed(self) -> None:
        data = load_personas()["cdo"]
        child = next(node for node in data["tree"] if node.parent)
        result = score_turns(data, run(data, [" ".join(child.keywords)]))
        self.assertFalse(result["ok"])

    def test_command_prints_no_score(self) -> None:
        data = load_personas()["cdo"]
        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "questions.txt"
            script.write_text("\n".join(winning_questions(data)), encoding="utf-8")
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                interview_main(["--persona", "cdo", "--script", str(script)])
        text = stdout.getvalue()
        self.assertIn("16 weeks", text)
        self.assertNotIn("Score", text)
        self.assertNotIn("gpu-lead-time", text)


class CheckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        write_release(load("small"), root / "pack", root / "truth")
        self.pack = root / "pack"
        self.personas, self.canary = load_truth(root / "truth" / "personas.json")
        self.work = root / "work"
        shutil.copytree(self.pack / "starter", self.work)
        (self.work / "credentials").mkdir()
        shutil.copy(self.pack / "credentials" / "dev.json", self.work / "credentials" / "dev.json")
        blank = (self.pack / "forms" / "access-request.md").read_text(encoding="utf-8")
        (self.work / "access-request.md").write_text(_fill_request(blank), encoding="utf-8")
        folder = self.work / "interviews"
        folder.mkdir()
        for persona_id in ("phc-lead", "dpo"):
            questions = winning_questions(self.personas[persona_id])
            (folder / f"{persona_id}.questions.txt").write_text("\n".join(questions) + "\n", encoding="utf-8")
            (folder / f"{persona_id}.notes.md").write_text(_notes(persona_id), encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_good_work_passes(self) -> None:
        self.assertEqual(repo_problems(self.work, self.canary), [])
        self.assertEqual(interview_problems(self.work, self.personas), [])

    def test_canary_in_a_tracked_file_fails_without_echoing_it(self) -> None:
        readme = self.work / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + self.canary + "\n", encoding="utf-8")
        problems = repo_problems(self.work, self.canary)
        self.assertTrue(problems)
        self.assertTrue(all(self.canary not in item for item in problems))

    def test_incomplete_interview_and_banned_sentence(self) -> None:
        (self.work / "interviews" / "phc-lead.questions.txt").write_text("hello\n", encoding="utf-8")
        problems = interview_problems(self.work, self.personas)
        self.assertIn("phc-lead interview is incomplete", problems)
        self.assertTrue(all("templates-v3" not in item for item in problems))
        notes = self.work / "interviews" / "dpo.notes.md"
        notes.write_text(notes.read_text(encoding="utf-8") + "The external model may receive identified patient data.\n", encoding="utf-8")
        (self.work / "interviews" / "phc-lead.questions.txt").write_text(
            "\n".join(winning_questions(self.personas["phc-lead"])) + "\n", encoding="utf-8"
        )
        banned = interview_problems(self.work, self.personas)
        self.assertIn("notes contain a banned sentence", banned)
        self.assertNotIn("The external model may receive identified patient data.", banned)


if __name__ == "__main__":
    unittest.main()
