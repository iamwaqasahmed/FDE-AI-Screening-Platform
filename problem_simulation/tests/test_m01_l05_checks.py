"""Module 1, Lesson 5 score, design, readout, and individual checks.

Guards the agent score, the trajectory score, and the written design, readout,
and individual checks.

The fixture writes the agent pack and the failure pack, then joins their gold
scenarios. A correct agent is the reference model, schema, and memory copied
onto the unfinished skeleton. The prose pages are copied from the filled
solution. A timeout that books, a race that books twice, a diagram with no
human step, a banned urgency sentence, a readout that drops the deadline, and
a trace note that drops the document must all fail without echoing the hidden
value. A watermark copied into the work tree must fail the same way.
"""

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
from alwaha.paths import AGENT_ROOT, M01_L05_ROOT, M01_L05_WORK
from alwaha.release.m01_l04 import write_m01_l04
from alwaha.release.m01_l05 import write_m01_l05

# Pages copied from the filled solution before a prose checker runs.
_PROSE = ("architecture.md", "design.md", "readout.md", "trace-note.md", "knowledge.md")


def _trace_row(item: dict) -> dict:
    """Turn one gold scenario into the trace row a stand-in agent would print.

    The reply text is a plain completion. Counts, tools, and flags are copied from
    the gold item so a test can break one field and leave the rest honest.
    """
    # The reply is a plain completion. Counts and flags are copied so a test can break one field.
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
        # Flags and the failure name come from the gold item. A missing failure is an empty string.
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
    """Catches a grader that accepts a booking it should refuse, or that quotes a
    hidden fact back at the learner.

    The skeleton copy, the correct-agent copy, and the prose copy are the three
    fixtures. Score runs the agent and trajectory checkers. Written runs the design,
    readout, and individual checkers.
    """
    def setUp(self) -> None:
        """Write the agent pack and the failure pack, and join their gold scenarios.

        The work directory starts empty. Tests copy the skeleton or the prose into it.
        The filled solution path is kept so a test can compare the reference agent with
        the copy a learner is given.
        """
        # A temporary agent pack and a failure pack for the small profile.
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "m01_l04"
        self.failures = root / "m01_l05"
        self.truth = root / "truth"
        write_m01_l04(self.profile, self.pack, self.truth)
        write_m01_l05(self.profile, self.failures, self.truth)
        # One gold list: the agent scenarios followed by this day's failure scenarios.
        agent_gold = json.loads((self.truth / "agent_gold.json").read_text(encoding="utf-8"))
        self.m01_l05 = json.loads((self.truth / "m01_l05_gold.json").read_text(encoding="utf-8"))
        self.gold = {"scenarios": agent_gold["scenarios"] + self.m01_l05["scenarios"]}
        # The work directory starts empty. Tests copy the skeleton or the prose into it.
        self.work = root / "work"
        self.work.mkdir()
        self.here = Path(__file__).resolve().parent
        self.filled = M01_L05_WORK

    def tearDown(self) -> None:
        """Delete the temporary packs and work directory."""
        self.tmp.cleanup()

    def _copy_skeleton(self) -> None:
        """Copy the unfinished agent into the work tree, skipping cached bytecode.

        This is the agent that still books on the timeout path. Tests that want the
        reference agent overwrite pieces of this copy.
        """
        shutil.copytree(
            M01_L05_ROOT / "Student_Copy" / "packet" / "agent",
            self.work / "agent",
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
        )

    def _use_correct_agent(self) -> None:
        """Replace the skeleton model, schema, and memory with the reference copies.

        The runner and the tools stay the unfinished ones, which is what a finished
        learner is expected to keep.
        """
        self._copy_skeleton()
        agent = self.work / "agent"
        (agent / "model.py").write_text((self.here / "m01_l05_model.py").read_text(encoding="utf-8"), encoding="utf-8")
        (agent / "schema.py").write_text((self.here / "m01_l05_schema.py").read_text(encoding="utf-8"), encoding="utf-8")
        (agent / "memory.py").write_text((self.here / "m01_l04_memory.py").read_text(encoding="utf-8"), encoding="utf-8")

    def _prose(self) -> None:
        """Copy the filled architecture, design, readout, trace note, and knowledge pages
        into the work tree.
        """
        for name in _PROSE:
            shutil.copy(self.filled / name, self.work / name)

    def _score(self) -> tuple[list[str], list[str]]:
        """Run the agent checker and the trajectory checker against the joined gold.

        The failure pack is passed in, and the checker is told the rows were not
        pre-written, so it runs the agent.
        """
        canary = self.profile.canary()
        return (
            agent_problems(self.work, self.pack, self.gold, canary, self.failures, written=False),
            trajectory_problems(self.work, self.pack, self.gold, canary, self.failures, written=False),
        )

    def _written(self) -> tuple[list[str], list[str], list[str]]:
        """Run the design, readout, and individual checkers on the prose pages.

        Both packs are handed to the design checker, and the watermark belongs to the profile,
        so a page that pastes it fails without this helper printing the watermark.
        """
        canary = self.profile.canary()
        return (
            design_problems(self.work, self.m01_l05, canary, [self.pack, self.failures]),
            readout_problems(self.work, self.m01_l05, canary),
            individual_problems(self.work, self.m01_l05, canary),
        )

    def _emit(self, rows: list[dict]) -> None:
        """Install a stand-in runner that writes the given rows and does nothing else.

        Used when a test needs one bad trace without running the real agent.
        """
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
        """Fails when the filled solution's runner or tools drift from the skeleton, or
        when its model, schema, or memory drift from the reference copies. The skeleton
        model must remain the unfinished model.
        """
        work = self.filled / "agent"
        skeleton = M01_L05_ROOT / "Student_Copy" / "packet" / "agent"
        for name in ("run.py", "tools.py"):
            self.assertEqual((work / name).read_text(encoding="utf-8"), (skeleton / name).read_text(encoding="utf-8"))
        self.assertEqual((work / "model.py").read_text(encoding="utf-8"), (self.here / "m01_l05_model.py").read_text(encoding="utf-8"))
        self.assertEqual((work / "schema.py").read_text(encoding="utf-8"), (self.here / "m01_l05_schema.py").read_text(encoding="utf-8"))
        self.assertEqual((work / "memory.py").read_text(encoding="utf-8"), (self.here / "m01_l04_memory.py").read_text(encoding="utf-8"))
        self.assertEqual((skeleton / "model.py").read_text(encoding="utf-8"), (AGENT_ROOT / "model.py").read_text(encoding="utf-8"))

    def test_correct_agent_and_notes_pass(self) -> None:
        """Fails when the reference agent or the filled prose still produces a problem
        from any of the five checkers.
        """
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
        """Fails when the unfinished agent is allowed to book on the timeout path, or when
        the problem list contains the watermark or the hidden deadline.
        """
        self._copy_skeleton()
        agent, _trajectory = self._score()
        self.assertIn("timeout booked a slot", agent)
        joined = "\n".join(agent)
        self.assertNotIn(self.profile.canary(), joined)
        self.assertNotIn("16", joined)

    def test_race_that_books_twice_fails(self) -> None:
        """Fails when a trace that records a second booking on the race scenario is accepted.

        The rest of the gold rows are left as they are. Only that scenario's tool list
        grows.
        """
        rows = [_trace_row(item) for item in self.gold["scenarios"]]
        race = next(row for row in rows if row["scenario"] == "race-slot")
        race["tool_trace"].append("slots.book")
        self._emit(rows)
        agent, _trajectory = self._score()
        self.assertIn("race-slot booked twice", agent)

    def test_diagram_without_a_human_step_fails(self) -> None:
        """Fails when the architecture page still passes after the human role has been
        renamed away.
        """
        self._prose()
        path = self.work / "architecture.md"
        text = path.read_text(encoding="utf-8")
        text = text.replace("coordinator", "queue").replace("Coordinator", "Queue").replace("human", "staff")
        path.write_text(text, encoding="utf-8")
        design, _readout, _individual = self._written()
        self.assertIn("the diagram has no human step", design)

    def test_triage_promise_fails(self) -> None:
        """Fails when a banned urgency sentence in the design is accepted, or when the
        problem list quotes that sentence.
        """
        self._prose()
        path = self.work / "design.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nThe assistant may set clinical urgency.\n", encoding="utf-8")
        design, _readout, _individual = self._written()
        self.assertEqual(design, ["design contains a banned sentence"])
        self.assertNotIn("The assistant may set clinical urgency.", design)

    def test_readout_without_the_deadline_hides_the_lead_time(self) -> None:
        """Fails when a readout that no longer states the deadline is accepted, or when
        the problem list reveals the lead time, the hardware, or the unsigned fact.
        """
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
        """Fails when a trace note that drops the safety document is accepted, or when the
        problem list prints the document id.
        """
        self._prose()
        path = self.work / "trace-note.md"
        path.write_text(path.read_text(encoding="utf-8").replace("pol-clinical-safety", ""), encoding="utf-8")
        _design, _readout, individual = self._written()
        self.assertIn("the trace note does not name the document", individual)
        self.assertNotIn("pol-clinical-safety", "\n".join(individual))

    def test_watermark_in_work_is_not_echoed(self) -> None:
        """Fails when a file that contains only the watermark is ignored by either checker,
        or when a problem message contains the watermark.
        """
        self._prose()
        (self.work / "copied.jsonl").write_text(self.profile.canary(), encoding="utf-8")
        agent, _trajectory = self._score()
        design, _readout, _individual = self._written()
        self.assertEqual(agent, [WATERMARK])
        self.assertEqual(design, [WATERMARK])
        self.assertNotIn(self.profile.canary(), "\n".join(agent + design))


if __name__ == "__main__":
    unittest.main()
