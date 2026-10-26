"""Day 5 of Week 4 checks for the connections and the proposal.

Guards the connection checker, the operations pages, the proposal, the readout,
and the individual lab.

The fixture is this day's pack plus the filled work tree. The filled copy must
pass. Shell swaps cover sign-in, the bus, the handoff, the leave feed, the
warehouse clock, the stage gate, the ranking, and the personal lab. A sprint
that puts the proposal first, notes that miss the summary and the leave, an
empty architecture, and an empty operations plan must fail. Proposal sections
are rewritten one at a time: a dot-vote, a ranking with no dependency, a roadmap
that starts with triage, an unmeasured saving, adoption with no phone channel,
the wrong client, and savings counted twice. An empty readout, placeholder
knowledge, and an empty retro must fail. Problem text must not echo the
watermark, the attack text, the hidden reading, or a count.
"""

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
from alwaha.paths import W4D5_APP, W4D5_WORK

_ANSWER = "count the same calls"


def _fill(text: str, heading: str, body: str) -> str:
    """Replace the body of one heading and leave every other section alone.

    The next heading, if there is one, stays where it was. This is how a test
    breaks a single proposal section without rewriting the page.
    """
    marker = f"## {heading}"
    start = text.find(marker)
    rest = text[start + len(marker) :]
    nxt = rest.find("\n## ")
    tail = "" if nxt < 0 else rest[nxt:]
    return text[: start + len(marker)] + "\n\n" + body.strip() + "\n" + tail


class CheckTests(unittest.TestCase):
    """Catches a grader that accepts a service token, a booking-date clock, or a
    proposal that starts the roadmap with triage.
    """
    def setUp(self) -> None:
        """Write this day's pack and copy the filled work tree."""
        # A temporary pack for the small profile. The gold comes from the generator.
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        from alwaha.release.w4d5 import write_w4d5

        write_w4d5(self.profile, self.pack, self.truth)
        self.gold = gold(self.profile)
        # The filled work tree, without cached bytecode.
        self.work = root / "work"
        shutil.copytree(W4D5_WORK, self.work, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    def tearDown(self) -> None:
        """Delete the temporary pack and work tree."""
        self.tmp.cleanup()

    def _integrate(self) -> list[str]:
        """Run the connection checker."""
        from alwaha.check.integrate_w4 import integrate_problems

        return integrate_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _ops(self) -> list[str]:
        """Run the operations checker."""
        from alwaha.check.ops_w4 import ops_problems

        return ops_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _rcp(self) -> list[str]:
        """Run the proposal checker."""
        from alwaha.check.rcp_w4 import rcp_problems

        return rcp_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _readout(self) -> list[str]:
        """Run the readout checker."""
        from alwaha.check.readout_w4 import readout_problems

        return readout_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _individual(self) -> list[str]:
        """Run the individual lab checker."""
        from alwaha.check.individual_w4 import individual_problems

        return individual_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        """Fail this case when a problem list echoes the watermark, the attack text, the
        hidden benefit reading, or a count.
        """
        joined = "\n".join(problems)
        self.assertNotIn(self.profile.canary(), joined)
        self.assertNotIn(attack()["text"], joined)
        self.assertNotIn(_ANSWER, joined)
        self.assertNotIn(str(self.gold["leave_lag"]), joined)
        self.assertNotIn(str(self.gold["phone_only"]), joined)

    def _swap(self, name: str) -> None:
        """Replace one work module with the unfinished shell of the same name."""
        shutil.copy(W4D5_APP / name, self.work / "app" / name)

    def _section(self, path: Path, heading: str, body: str) -> None:
        """Rewrite one section of a page using the heading filler.

        The rest of the filled proposal stays in place, so the failure can be blamed
        on that section.
        """
        path.write_text(_fill(path.read_text(encoding="utf-8"), heading, body), encoding="utf-8")

    def test_filled_work_passes(self) -> None:
        """Fails when the filled work tree still produces a connection, operations,
        proposal, readout, or individual problem.
        """
        self.assertEqual(self._integrate(), [])
        self.assertEqual(self._ops(), [])
        self.assertEqual(self._rcp(), [])
        self.assertEqual(self._readout(), [])
        self.assertEqual(self._individual(), [])

    def test_shell_signin_accepts_the_service_token(self) -> None:
        """Fails when sign-in that accepts the service token is accepted."""
        self._swap("signin.py")
        problems = self._integrate()
        self.assertEqual(problems, [SERVICE])
        self._hidden(problems)

    def test_shell_bus_drops_the_event(self) -> None:
        """Fails when a bus that drops an unknown event, and so misses the cancelled
        session, is accepted.
        """
        self._swap("bus.py")
        problems = self._integrate()
        self.assertEqual(problems, [UNKNOWN, MISSED])
        self._hidden(problems)

    def test_shell_handoff_has_no_summary(self) -> None:
        """Fails when a handoff with no summary is accepted."""
        self._swap("handoff.py")
        problems = self._integrate()
        self.assertEqual(problems, [SUMMARY])
        self._hidden(problems)

    def test_shell_leave_keeps_the_session(self) -> None:
        """Fails when leave that keeps the session, or that watches the wrong event, is
        accepted.
        """
        self._swap("leave.py")
        problems = self._integrate()
        self.assertEqual(problems, [LATE, EVENT])
        self._hidden(problems)

    def test_shell_warehouse_uses_the_booking_date(self) -> None:
        """Fails when the warehouse clock uses the booking date instead of the referral time."""
        self._swap("warehouse.py")
        problems = self._integrate()
        self.assertEqual(problems, [CLOCK])
        self._hidden(problems)

    def test_sprint_out_of_order_fails(self) -> None:
        """Fails when a sprint that puts the proposal first is accepted."""
        (self.work / "sprint.md").write_text("# Sprint\n\nThe proposal comes first.\n", encoding="utf-8")
        problems = self._integrate()
        self.assertEqual(problems, [SEQUENCE])
        self._hidden(problems)

    def test_notes_miss_the_summary_and_the_leave(self) -> None:
        """Fails when the access note misses the handoff summary or the architect note
        misses the leave. The leftover sentences are true and still not enough.
        """
        (self.work / "interviews" / "access-mgr.notes.md").write_text("# access-mgr\n\nNo-shows dominate.\n", encoding="utf-8")
        (self.work / "interviews" / "ea.notes.md").write_text("# ea\n\nWe have an API strategy.\n", encoding="utf-8")
        problems = self._integrate()
        self.assertEqual(problems, [ACCESS, EA])
        self._hidden(problems)

    def test_an_empty_architecture_fails(self) -> None:
        """Fails when an empty deployment architecture is accepted."""
        (self.work / "architecture-deploy.md").write_text("# Deployment architecture\n", encoding="utf-8")
        problems = self._ops()
        self.assertEqual(problems, [ARCH])
        self._hidden(problems)

    def test_an_empty_operations_plan_fails(self) -> None:
        """Fails when an empty operations page is accepted. It needs an owner, an on-call
        cell, and a go-live gate.
        """
        (self.work / "operations.md").write_text("# Operations\n", encoding="utf-8")
        problems = self._ops()
        self.assertEqual(problems, [OWNER, CELL, GATE])
        self._hidden(problems)

    def test_shell_gates_skip_go_live(self) -> None:
        """Fails when a gate table that skips go-live is accepted. The on-call cell and
        the gate should both be caught.
        """
        self._swap("gates.py")
        problems = self._ops()
        self.assertEqual(problems, [CELL, GATE])
        self._hidden(problems)

    def test_shell_rank_starts_with_triage(self) -> None:
        """Fails when a ranking that starts with triage is accepted. Triage is blocked and
        cannot lead the roadmap.
        """
        self._swap("rank.py")
        problems = self._rcp()
        self.assertEqual(problems, [ROADMAP])
        self._hidden(problems)

    def test_a_dot_vote_ranking_fails(self) -> None:
        """Fails when a ranking section that leads with triage and cites a dependency is
        accepted. Leading with the blocked problem is a dot-vote, not the value model.
        """
        path = self.work / "rcp" / "proposal.md"
        self._section(path, "Ranking", "p-triage is first. p-waitlist depends on identity.")
        problems = self._rcp()
        self.assertEqual(problems, [DOT])
        self._hidden(problems)

    def test_a_ranking_without_a_dependency_fails(self) -> None:
        """Fails when a ranking that rejects the dot-vote but names no dependency is accepted."""
        path = self.work / "rcp" / "proposal.md"
        self._section(path, "Ranking", "The dot-vote is not the value model. p-clock is first.")
        problems = self._rcp()
        self.assertEqual(problems, [DEPEND])
        self._hidden(problems)

    def test_a_roadmap_that_starts_with_triage_fails(self) -> None:
        """Fails when the roadmap section builds triage first."""
        path = self.work / "rcp" / "proposal.md"
        self._section(path, "Roadmap", "p-triage is the first build.")
        problems = self._rcp()
        self.assertEqual(problems, [ROADMAP])
        self._hidden(problems)

    def test_unmeasured_metrics_fail(self) -> None:
        """Fails when the metrics section hopes for a saving and does not measure one."""
        path = self.work / "rcp" / "proposal.md"
        self._section(path, "Metrics", "The team hopes for a large saving.")
        problems = self._rcp()
        self.assertEqual(problems, [METRICS])
        self._hidden(problems)

    def test_adoption_without_the_phone_channel_fails(self) -> None:
        """Fails when adoption assumes an app and never mentions the phone channel."""
        path = self.work / "rcp" / "proposal.md"
        self._section(path, "Adoption", "Patients will use the app.")
        problems = self._rcp()
        self.assertEqual(problems, [ADOPT])
        self._hidden(problems)

    def test_a_proposal_for_another_client_fails(self) -> None:
        """Fails when the client section names the board instead of the cluster."""
        path = self.work / "rcp" / "proposal.md"
        self._section(path, "Client", "The sponsor is the board.")
        problems = self._rcp()
        self.assertEqual(problems, [CLIENT])
        self._hidden(problems)

    def test_separate_savings_fail(self) -> None:
        """Fails when the vendor saving and the contact-center saving are counted as two
        different piles. They are the same calls.
        """
        path = self.work / "rcp" / "proposal.md"
        self._section(path, "Plan", "The vendor saving and the contact-center saving are separate.")
        problems = self._rcp()
        self.assertEqual(problems, [SEPARATE])
        self._hidden(problems)

    def test_an_empty_readout_fails(self) -> None:
        """Fails when an empty readout is accepted. It has to cover urgency, the external
        model, the ranking, the handoff, the leave, the benefit, the channel, the asks,
        and a citation.
        """
        # Replace the readout with a heading and nothing else.
        (self.work / "readout.md").write_text("# Readout\n", encoding="utf-8")
        problems = self._readout()
        # Every required section is reported missing.
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
        # The problem list does not echo a hidden value.
        self._hidden(problems)

    def test_knowledge_needs_both_answers(self) -> None:
        """Fails when placeholder answers are accepted in place of which event matters and
        how the ranking is chosen.
        """
        (self.work / "knowledge.md").write_text("# Knowledge\n\n1. Yes.\n2. No.\n", encoding="utf-8")
        problems = self._readout()
        self.assertEqual(problems, [KNOW_EVENT, RANK])
        self._hidden(problems)

    def test_an_empty_retro_fails(self) -> None:
        """Fails when an empty retro is accepted. The retro needs its required headings."""
        (self.work / "retro.md").write_text("# Retro\n", encoding="utf-8")
        problems = self._readout()
        self.assertEqual(problems, [RETRO_HEAD])
        self._hidden(problems)

    def test_shell_personal_books_the_attack(self) -> None:
        """Fails when the unfinished personal lab, which books the attack, is accepted."""
        self._swap("personal.py")
        problems = self._individual()
        self.assertEqual(problems, [BOOKED])
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        """Fails when a file that contains only the watermark is ignored, or when a problem
        message contains the watermark.
        """
        (self.work / "note.txt").write_text(self.profile.canary(), encoding="utf-8")
        problems = self._integrate()
        self.assertEqual(problems, [WATERMARK])
        self.assertNotIn(self.profile.canary(), problems[0])


if __name__ == "__main__":
    unittest.main()
