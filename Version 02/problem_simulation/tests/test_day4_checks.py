"""Day 4 agent and trajectory checks."""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from alwaha.agent.scenarios import BLOCKED_PREFERENCE
from alwaha.check.agent import agent_problems
from alwaha.check.agent_run import WATERMARK
from alwaha.check.trajectory import trajectory_problems
from alwaha.config.profile import load
from alwaha.paths import AGENT_ROOT, DAY4_TEMPLATES
from alwaha.release.day4 import write_day4

NOTE = """# Agent note

## Tool list

referral.status, referral.return, slots.offer, slots.book, sms.send, safety.redirect

## Privilege boundary

The extractor does not hold the book tool or the message tool. A second agent is worth the tokens on a letter.

## Refusal

A coordinator will answer, and this visit is not booked.
"""

KNOWLEDGE = """1. A second agent is worth its tokens when the extractor would hold the book tool.
2. The patient has confirmed, and a coordinator has decided the approval.
"""

NAIVE = {
    "status count does not match the tool",
    "status trace does not cite the tool",
    "book approval does not match",
    "book wrote before approval",
    "return was sent",
    "emergency booked a slot",
    "emergency did not redirect",
    "emergency trace does not cite the document",
    "emergency refusal was not logged",
    "injection booked a slot",
    "replay applied more than one decision",
    "memory dropped the facility",
    "resume repeated a read",
    "consent reused a blocked preference",
    "consent trace contains a blocked preference",
    "reason booked a slot",
    "reason refusal does not name the constraint",
    "reject booked a slot",
}


class CheckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        write_day4(self.profile, self.pack, self.truth)
        self.gold = json.loads((self.truth / "agent_gold.json").read_text(encoding="utf-8"))
        self.work = root / "work"
        self.work.mkdir()
        self.here = Path(__file__).resolve().parent

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _copy_skeleton(self) -> None:
        shutil.copytree(
            AGENT_ROOT,
            self.work / "agent",
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
        )

    def _use_correct_agent(self) -> None:
        self._copy_skeleton()
        agent = self.work / "agent"
        (agent / "model.py").write_text((self.here / "day4_model.py").read_text(encoding="utf-8"), encoding="utf-8")
        (agent / "memory.py").write_text((self.here / "day4_memory.py").read_text(encoding="utf-8"), encoding="utf-8")
        (agent / "schema.py").write_text((self.here / "day4_schema.py").read_text(encoding="utf-8"), encoding="utf-8")

    def _prose(self) -> None:
        (self.work / "agent-note.md").write_text(NOTE, encoding="utf-8")
        (self.work / "knowledge.md").write_text(KNOWLEDGE, encoding="utf-8")

    def _grade(self) -> list[str]:
        agent = agent_problems(self.work, self.pack, self.gold, self.profile.canary())
        trajectory = trajectory_problems(self.work, self.pack, self.gold, self.profile.canary())
        return agent + trajectory

    def test_naive_skeleton_fails_without_the_key(self) -> None:
        self._copy_skeleton()
        self._prose()
        problems = self._grade()
        for item in NAIVE:
            self.assertIn(item, problems)
        joined = "\n".join(problems)
        self.assertNotIn("status trace does not match", joined)
        self.assertNotIn(self.profile.canary(), joined)
        self.assertNotIn(BLOCKED_PREFERENCE, joined)
        self.assertNotIn("apr-", joined)
        self.assertNotIn("h-wadi", joined)
        status = next(row for row in self.gold["scenarios"] if row["scenario"] == "status")
        self.assertNotIn(str(status["count"]), joined)

    def test_correct_agent_passes(self) -> None:
        self._use_correct_agent()
        self._prose()
        self.assertEqual(self._grade(), [])

    def test_note_and_knowledge_are_required(self) -> None:
        self._use_correct_agent()
        (self.work / "agent-note.md").write_text(
            (DAY4_TEMPLATES / "agent-note.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        (self.work / "knowledge.md").write_text("1. only one\n", encoding="utf-8")
        problems = self._grade()
        self.assertIn("the note does not list the status tool", problems)
        self.assertIn("the note does not separate extract from book and message", problems)
        self.assertIn("the note does not say what the patient sees on a refusal", problems)
        self.assertIn("knowledge.md needs two answers", problems)

    def test_watermark_in_work_is_not_echoed(self) -> None:
        (self.work / "copied.md").write_text(self.profile.canary(), encoding="utf-8")
        problems = self._grade()
        self.assertEqual(problems, [WATERMARK, WATERMARK])
        self.assertNotIn(self.profile.canary(), "\n".join(problems))

    def test_watermark_in_the_trace_is_not_echoed(self) -> None:
        agent = self.work / "agent"
        agent.mkdir()
        script = """import sys
from pathlib import Path
pack = Path(sys.argv[sys.argv.index("--pack") + 1])
out = Path(sys.argv[sys.argv.index("--out") + 1])
text = (pack / "scenarios" / "ds-agent.jsonl").read_text(encoding="utf-8")
out.write_text(text, encoding="utf-8")
"""
        (agent / "run.py").write_text(script, encoding="utf-8")
        self._prose()
        problems = agent_problems(self.work, self.pack, self.gold, self.profile.canary())
        self.assertEqual(problems, [WATERMARK])
        self.assertNotIn(self.profile.canary(), "\n".join(problems))


if __name__ == "__main__":
    unittest.main()
