"""Day 5 of Week 4 checks for the connections and the proposal."""

from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.individual_w4 import BOOKED
from alwaha.check.integrate_w4 import CLOCK, EVENT, LATE, MISSED, SERVICE, SUMMARY, UNKNOWN
from alwaha.check.notes_w4d5 import ACCESS, EA, SEQUENCE
from alwaha.check.ops_w4 import ARCH, CELL, GATE, OWNER
from alwaha.check.rcp_w4 import ADOPT, CLIENT, DEPEND, DOT, METRICS, ROADMAP, SEPARATE
from alwaha.check.readout_w4 import (
    ASKS,
    CITE,
    EVENT as KNOW_EVENT,
    EXTERNAL,
    RANK,
    RETRO_HEAD,
    URGENCY,
)
from alwaha.check.readout_w4 import _MISSES
from alwaha.config.profile import load
from alwaha.engagement.w4d5 import gold
from alwaha.engagement.w4d5_rows import attack
from alwaha.paths import W4D5_APP, W4D5_ROOT

_ANSWER = "count the same calls"


def _fill(text: str, heading: str, body: str) -> str:
    marker = f"## {heading}"
    start = text.find(marker)
    rest = text[start + len(marker) :]
    nxt = rest.find("\n## ")
    tail = "" if nxt < 0 else rest[nxt:]
    return text[: start + len(marker)] + "\n\n" + body.strip() + "\n" + tail


class CheckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        from alwaha.release.w4d5 import write_w4d5

        write_w4d5(self.profile, self.pack, self.truth)
        self.gold = gold(self.profile)
        self.work = root / "work"
        shutil.copytree(W4D5_ROOT / "work", self.work, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _integrate(self) -> list[str]:
        from alwaha.check.integrate_w4 import integrate_problems

        return integrate_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _ops(self) -> list[str]:
        from alwaha.check.ops_w4 import ops_problems

        return ops_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _rcp(self) -> list[str]:
        from alwaha.check.rcp_w4 import rcp_problems

        return rcp_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _readout(self) -> list[str]:
        from alwaha.check.readout_w4 import readout_problems

        return readout_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _individual(self) -> list[str]:
        from alwaha.check.individual_w4 import individual_problems

        return individual_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        joined = "\n".join(problems)
        self.assertNotIn(self.profile.canary(), joined)
        self.assertNotIn(attack()["text"], joined)
        self.assertNotIn(_ANSWER, joined)
        self.assertNotIn(str(self.gold["leave_lag"]), joined)
        self.assertNotIn(str(self.gold["phone_only"]), joined)

    def _swap(self, name: str) -> None:
        shutil.copy(W4D5_APP / name, self.work / "app" / name)

    def _section(self, path: Path, heading: str, body: str) -> None:
        path.write_text(_fill(path.read_text(encoding="utf-8"), heading, body), encoding="utf-8")

    def test_filled_work_passes(self) -> None:
        self.assertEqual(self._integrate(), [])
        self.assertEqual(self._ops(), [])
        self.assertEqual(self._rcp(), [])
        self.assertEqual(self._readout(), [])
        self.assertEqual(self._individual(), [])

    def test_shell_signin_accepts_the_service_token(self) -> None:
        self._swap("signin.py")
        problems = self._integrate()
        self.assertEqual(problems, [SERVICE])
        self._hidden(problems)

    def test_shell_bus_drops_the_event(self) -> None:
        self._swap("bus.py")
        problems = self._integrate()
        self.assertEqual(problems, [UNKNOWN, MISSED])
        self._hidden(problems)

    def test_shell_handoff_has_no_summary(self) -> None:
        self._swap("handoff.py")
        problems = self._integrate()
        self.assertEqual(problems, [SUMMARY])
        self._hidden(problems)

    def test_shell_leave_keeps_the_session(self) -> None:
        self._swap("leave.py")
        problems = self._integrate()
        self.assertEqual(problems, [LATE, EVENT])
        self._hidden(problems)

    def test_shell_warehouse_uses_the_booking_date(self) -> None:
        self._swap("warehouse.py")
        problems = self._integrate()
        self.assertEqual(problems, [CLOCK])
        self._hidden(problems)

    def test_sprint_out_of_order_fails(self) -> None:
        (self.work / "sprint.md").write_text("# Sprint\n\nThe proposal comes first.\n", encoding="utf-8")
        problems = self._integrate()
        self.assertEqual(problems, [SEQUENCE])
        self._hidden(problems)

    def test_notes_miss_the_summary_and_the_leave(self) -> None:
        (self.work / "interviews" / "access-mgr.notes.md").write_text("# access-mgr\n\nNo-shows dominate.\n", encoding="utf-8")
        (self.work / "interviews" / "ea.notes.md").write_text("# ea\n\nWe have an API strategy.\n", encoding="utf-8")
        problems = self._integrate()
        self.assertEqual(problems, [ACCESS, EA])
        self._hidden(problems)

    def test_an_empty_architecture_fails(self) -> None:
        (self.work / "architecture-deploy.md").write_text("# Deployment architecture\n", encoding="utf-8")
        problems = self._ops()
        self.assertEqual(problems, [ARCH])
        self._hidden(problems)

    def test_an_empty_operations_plan_fails(self) -> None:
        (self.work / "operations.md").write_text("# Operations\n", encoding="utf-8")
        problems = self._ops()
        self.assertEqual(problems, [OWNER, CELL, GATE])
        self._hidden(problems)

    def test_shell_gates_skip_go_live(self) -> None:
        self._swap("gates.py")
        problems = self._ops()
        self.assertEqual(problems, [CELL, GATE])
        self._hidden(problems)

    def test_shell_rank_starts_with_triage(self) -> None:
        self._swap("rank.py")
        problems = self._rcp()
        self.assertEqual(problems, [ROADMAP])
        self._hidden(problems)

    def test_a_dot_vote_ranking_fails(self) -> None:
        path = self.work / "rcp" / "proposal.md"
        self._section(path, "Ranking", "p-triage is first. p-waitlist depends on identity.")
        problems = self._rcp()
        self.assertEqual(problems, [DOT])
        self._hidden(problems)

    def test_a_ranking_without_a_dependency_fails(self) -> None:
        path = self.work / "rcp" / "proposal.md"
        self._section(path, "Ranking", "The dot-vote is not the value model. p-clock is first.")
        problems = self._rcp()
        self.assertEqual(problems, [DEPEND])
        self._hidden(problems)

    def test_a_roadmap_that_starts_with_triage_fails(self) -> None:
        path = self.work / "rcp" / "proposal.md"
        self._section(path, "Roadmap", "p-triage is the first build.")
        problems = self._rcp()
        self.assertEqual(problems, [ROADMAP])
        self._hidden(problems)

    def test_unmeasured_metrics_fail(self) -> None:
        path = self.work / "rcp" / "proposal.md"
        self._section(path, "Metrics", "The team hopes for a large saving.")
        problems = self._rcp()
        self.assertEqual(problems, [METRICS])
        self._hidden(problems)

    def test_adoption_without_the_phone_channel_fails(self) -> None:
        path = self.work / "rcp" / "proposal.md"
        self._section(path, "Adoption", "Patients will use the app.")
        problems = self._rcp()
        self.assertEqual(problems, [ADOPT])
        self._hidden(problems)

    def test_a_proposal_for_another_client_fails(self) -> None:
        path = self.work / "rcp" / "proposal.md"
        self._section(path, "Client", "The sponsor is the board.")
        problems = self._rcp()
        self.assertEqual(problems, [CLIENT])
        self._hidden(problems)

    def test_separate_savings_fail(self) -> None:
        path = self.work / "rcp" / "proposal.md"
        self._section(path, "Plan", "The vendor saving and the contact-center saving are separate.")
        problems = self._rcp()
        self.assertEqual(problems, [SEPARATE])
        self._hidden(problems)

    def test_an_empty_readout_fails(self) -> None:
        (self.work / "readout.md").write_text("# Readout\n", encoding="utf-8")
        problems = self._readout()
        expected = [
            URGENCY,
            EXTERNAL,
            _MISSES["ranking"],
            _MISSES["handoff"],
            _MISSES["leave"],
            _MISSES["benefit"],
            _MISSES["channel"],
            ASKS,
            CITE,
        ]
        self.assertEqual(problems, expected)
        self._hidden(problems)

    def test_knowledge_needs_both_answers(self) -> None:
        (self.work / "knowledge.md").write_text("# Knowledge\n\n1. Yes.\n2. No.\n", encoding="utf-8")
        problems = self._readout()
        self.assertEqual(problems, [KNOW_EVENT, RANK])
        self._hidden(problems)

    def test_an_empty_retro_fails(self) -> None:
        (self.work / "retro.md").write_text("# Retro\n", encoding="utf-8")
        problems = self._readout()
        self.assertEqual(problems, [RETRO_HEAD])
        self._hidden(problems)

    def test_shell_personal_books_the_attack(self) -> None:
        self._swap("personal.py")
        problems = self._individual()
        self.assertEqual(problems, [BOOKED])
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        (self.work / "note.txt").write_text(self.profile.canary(), encoding="utf-8")
        problems = self._integrate()
        self.assertEqual(problems, [WATERMARK])
        self.assertNotIn(self.profile.canary(), problems[0])


if __name__ == "__main__":
    unittest.main()
