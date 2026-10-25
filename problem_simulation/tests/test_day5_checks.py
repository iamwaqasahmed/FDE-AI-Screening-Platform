"""Day 5 score, design, readout, and individual checks."""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from alwaha.check.agent import agent_problems
from alwaha.check.agent_run import WATERMARK
from alwaha.check.design import design_problems
from alwaha.check.individual import individual_problems
from alwaha.check.readout import readout_problems
from alwaha.check.trajectory import trajectory_problems
from alwaha.config.profile import load
from alwaha.paths import AGENT_ROOT, DAY5_ROOT, DAY5_WORK
from alwaha.release.day4 import write_day4
from alwaha.release.day5 import write_day5

_PROSE = ("architecture.md", "design.md", "readout.md", "trace-note.md", "knowledge.md")


def _trace_row(item: dict) -> dict:
    return {
        "scenario": item["scenario"],
        "reply": {
            "intent": "answer",
            "text": "Done.",
            "count": item["count"],
            "facility_id": item["facility_id"],
            "constraint": item["constraint"],
        },
        "citations": list(item["citations"]),
        "tool_trace": list(item["tool_trace"]),
        "pending_approval_ids": list(item["pending_approval_ids"]),
        "approval_ids": list(item["approval_ids"]),
        "booked": item["booked"],
        "returned": item["returned"],
        "redirected": item["redirected"],
        "sms": item["sms"],
        "refusal_logged": item["refusal_logged"],
        "preference_used": item["preference_used"],
        "decisions": item["decisions"],
        "failure": item.get("failure", ""),
    }


class CheckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "day4"
        self.failures = root / "day5"
        self.truth = root / "truth"
        write_day4(self.profile, self.pack, self.truth)
        write_day5(self.profile, self.failures, self.truth)
        agent_gold = json.loads((self.truth / "agent_gold.json").read_text(encoding="utf-8"))
        self.day5 = json.loads((self.truth / "day5_gold.json").read_text(encoding="utf-8"))
        self.gold = {"scenarios": agent_gold["scenarios"] + self.day5["scenarios"]}
        self.work = root / "work"
        self.work.mkdir()
        self.here = Path(__file__).resolve().parent
        self.filled = DAY5_WORK

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _copy_skeleton(self) -> None:
        shutil.copytree(
            DAY5_ROOT / "Student_Copy" / "packet" / "agent",
            self.work / "agent",
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
        )

    def _use_correct_agent(self) -> None:
        self._copy_skeleton()
        agent = self.work / "agent"
        (agent / "model.py").write_text((self.here / "day5_model.py").read_text(encoding="utf-8"), encoding="utf-8")
        (agent / "schema.py").write_text((self.here / "day5_schema.py").read_text(encoding="utf-8"), encoding="utf-8")
        (agent / "memory.py").write_text((self.here / "day4_memory.py").read_text(encoding="utf-8"), encoding="utf-8")

    def _prose(self) -> None:
        for name in _PROSE:
            shutil.copy(self.filled / name, self.work / name)

    def _score(self) -> tuple[list[str], list[str]]:
        canary = self.profile.canary()
        return (
            agent_problems(self.work, self.pack, self.gold, canary, self.failures, written=False),
            trajectory_problems(self.work, self.pack, self.gold, canary, self.failures, written=False),
        )

    def _written(self) -> tuple[list[str], list[str], list[str]]:
        canary = self.profile.canary()
        return (
            design_problems(self.work, self.day5, canary, [self.pack, self.failures]),
            readout_problems(self.work, self.day5, canary),
            individual_problems(self.work, self.day5, canary),
        )

    def _emit(self, rows: list[dict]) -> None:
        payload = json.dumps(rows)
        script = (
            "import sys\n"
            "from pathlib import Path\n"
            "out = Path(sys.argv[sys.argv.index('--out') + 1])\n"
            f"out.write_text({payload!r}, encoding='utf-8')\n"
        )
        agent = self.work / "agent"
        agent.mkdir(exist_ok=True)
        (agent / "run.py").write_text(script, encoding="utf-8")

    def test_filled_copy_matches_the_passing_agent(self) -> None:
        work = self.filled / "agent"
        skeleton = DAY5_ROOT / "Student_Copy" / "packet" / "agent"
        for name in ("run.py", "tools.py"):
            self.assertEqual((work / name).read_text(encoding="utf-8"), (skeleton / name).read_text(encoding="utf-8"))
        self.assertEqual((work / "model.py").read_text(encoding="utf-8"), (self.here / "day5_model.py").read_text(encoding="utf-8"))
        self.assertEqual((work / "schema.py").read_text(encoding="utf-8"), (self.here / "day5_schema.py").read_text(encoding="utf-8"))
        self.assertEqual((work / "memory.py").read_text(encoding="utf-8"), (self.here / "day4_memory.py").read_text(encoding="utf-8"))
        self.assertEqual((skeleton / "model.py").read_text(encoding="utf-8"), (AGENT_ROOT / "model.py").read_text(encoding="utf-8"))

    def test_correct_agent_and_notes_pass(self) -> None:
        self._use_correct_agent()
        self._prose()
        agent, trajectory = self._score()
        design, readout, individual = self._written()
        self.assertEqual(agent, [])
        self.assertEqual(trajectory, [])
        self.assertEqual(design, [])
        self.assertEqual(readout, [])
        self.assertEqual(individual, [])

    def test_timeout_that_books_fails(self) -> None:
        self._copy_skeleton()
        agent, _trajectory = self._score()
        self.assertIn("timeout booked a slot", agent)
        joined = "\n".join(agent)
        self.assertNotIn(self.profile.canary(), joined)
        self.assertNotIn("16", joined)

    def test_race_that_books_twice_fails(self) -> None:
        rows = [_trace_row(item) for item in self.gold["scenarios"]]
        race = next(row for row in rows if row["scenario"] == "race-slot")
        race["tool_trace"].append("slots.book")
        self._emit(rows)
        agent, _trajectory = self._score()
        self.assertIn("race-slot booked twice", agent)

    def test_diagram_without_a_human_step_fails(self) -> None:
        self._prose()
        path = self.work / "architecture.md"
        text = path.read_text(encoding="utf-8")
        text = text.replace("coordinator", "queue").replace("Coordinator", "Queue").replace("human", "staff")
        path.write_text(text, encoding="utf-8")
        design, _readout, _individual = self._written()
        self.assertIn("the diagram has no human step", design)

    def test_triage_promise_fails(self) -> None:
        self._prose()
        path = self.work / "design.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nThe assistant may set clinical urgency.\n", encoding="utf-8")
        design, _readout, _individual = self._written()
        self.assertEqual(design, ["design contains a banned sentence"])
        self.assertNotIn("The assistant may set clinical urgency.", design)

    def test_readout_without_the_deadline_hides_the_lead_time(self) -> None:
        self._prose()
        path = self.work / "readout.md"
        path.write_text(path.read_text(encoding="utf-8").replace("16 weeks", "a later season"), encoding="utf-8")
        _design, readout, _individual = self._written()
        self.assertIn("the readout does not answer the deadline", readout)
        joined = "\n".join(readout)
        self.assertNotIn("16", joined)
        self.assertNotIn("GPU", joined)
        self.assertNotIn("unsigned", joined.lower())

    def test_trace_note_without_the_document_hides_the_id(self) -> None:
        self._prose()
        path = self.work / "trace-note.md"
        path.write_text(path.read_text(encoding="utf-8").replace("pol-clinical-safety", ""), encoding="utf-8")
        _design, _readout, individual = self._written()
        self.assertIn("the trace note does not name the document", individual)
        self.assertNotIn("pol-clinical-safety", "\n".join(individual))

    def test_watermark_in_work_is_not_echoed(self) -> None:
        self._prose()
        (self.work / "copied.jsonl").write_text(self.profile.canary(), encoding="utf-8")
        agent, _trajectory = self._score()
        design, _readout, _individual = self._written()
        self.assertEqual(agent, [WATERMARK])
        self.assertEqual(design, [WATERMARK])
        self.assertNotIn(self.profile.canary(), "\n".join(agent + design))


if __name__ == "__main__":
    unittest.main()
