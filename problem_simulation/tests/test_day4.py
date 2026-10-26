"""Day 4 release, catalog, and the invented-count demo.

Guards the agent release, the tool catalog, and the invented-count demo.

Earlier days are written first and must not change. Each profile's watermark
appears once and only in its own pack. The scenario files, taken together, must
match the hidden scenario list and the tool catalog. Lesson notes and the
unfinished model must not contain the safety phrase, the blocked preference, or
the real queue count. The demo may show both counts and must not call either
one a failure.
"""

from __future__ import annotations

import json
from contextlib import redirect_stdout
from io import StringIO
import tempfile
import unittest
from pathlib import Path

from alwaha.agent.pages import catalog, safety_page
from alwaha.agent.scenarios import BLOCKED_PREFERENCE, SCENARIO_ORDER, STATUS_COUNT, scenarios
from alwaha.config.profile import load
from alwaha.demo.count import main as demo_main
from alwaha.paths import AGENT_ROOT, DAY4_ROOT
from alwaha.release.day2 import write_day2
from alwaha.release.day3 import write_day3
from alwaha.release.day4 import write_day4
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import write_release

# Learner scenario files. Their combined order is the scenario order the release must keep.
_FILES = ("ds-agent.jsonl", "ds-sessions.jsonl", "ds-reason.jsonl")


def _names(pack: Path) -> list[str]:
    """Read scenario names from the three learner files, in file order.

    The checker compares that sequence with the required scenario order.
    """
    found = []
    for name in _FILES:
        for line in (pack / "scenarios" / name).read_text(encoding="utf-8").splitlines():
            if line.strip():
                found.append(json.loads(line)["scenario"])
    return found


def _canary_count(pack: Path, canary: str) -> int:
    """Count watermark hits across every file in a pack.

    A pack should carry its own watermark once. This helper is how the release test
    sees a missing or a repeated mark.
    """
    total = 0
    for path in pack.rglob("*"):
        if path.is_file():
            total += path.read_text(encoding="utf-8").count(canary)
    return total


class ReleaseTests(unittest.TestCase):
    """Catches an agent pack that disturbs an earlier day, shares a watermark, or
    copies the answer key into the learner files or the lesson notes.
    """
    def test_same_seed_matches_and_earlier_days_stay(self) -> None:
        """Fails when a second write disagrees, when an earlier pack or gold file changes,
        or when the agent gold is missing from the hidden side or present in the pack.
        """
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            day1, day2, day3, day4 = root / "day1", root / "day2", root / "day3", root / "day4"
            truth = root / "truth"
            write_release(profile, day1, truth)
            write_day2(profile, day2, truth)
            write_day3(profile, day3, truth)
            before = (
                fingerprint(day1),
                fingerprint(day2),
                fingerprint(day3),
                (truth / "personas.json").read_bytes(),
                (truth / "approach_gold.json").read_bytes(),
                (truth / "events_gold.json").read_bytes(),
            )
            first = write_day4(profile, day4, truth)
            second = write_day4(profile, day4, truth)
            self.assertEqual(first, second)
            self.assertEqual(
                before,
                (
                    fingerprint(day1),
                    fingerprint(day2),
                    fingerprint(day3),
                    (truth / "personas.json").read_bytes(),
                    (truth / "approach_gold.json").read_bytes(),
                    (truth / "events_gold.json").read_bytes(),
                ),
            )
            self.assertTrue((truth / "agent_gold.json").is_file())
            self.assertFalse((day4 / "agent_gold.json").exists())

    def test_profiles_differ_by_canary(self) -> None:
        """Fails when either pack does not contain its watermark exactly once, when one
        watermark lands in the other pack, or when the fingerprints match.
        """
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            practice, small = load("practice"), load("small")
            write_day4(practice, root / "practice", root / "practice-truth")
            write_day4(small, root / "small", root / "small-truth")
            self.assertEqual(_canary_count(root / "practice", practice.canary()), 1)
            self.assertEqual(_canary_count(root / "small", small.canary()), 1)
            self.assertNotIn(practice.canary(), (root / "small" / "scenarios" / "ds-agent.jsonl").read_text(encoding="utf-8"))
            self.assertNotEqual(fingerprint(root / "practice"), fingerprint(root / "small"))

    def test_pack_matches_the_slice_and_keeps_the_key(self) -> None:
        """Fails when the scenario files drift from the generator, when the tool catalog
        changes, when the emergency wording or the safety page disagree, or when the
        gold status row does not record a single status call. The watermark must stay
        out of the gold file and the agent pages.
        """
        profile = load("small")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            write_day4(profile, pack, root / "truth")
            self.assertEqual(_names(pack), list(SCENARIO_ORDER))
            written = []
            for name in _FILES:
                for line in (pack / "scenarios" / name).read_text(encoding="utf-8").splitlines():
                    if line.strip():
                        written.append(json.loads(line))
            self.assertEqual(written, scenarios(profile.canary()))
            tools = [item["name"] for item in catalog()["tools"]]
            self.assertEqual(
                tools,
                ["referral.status", "referral.return", "slots.offer", "slots.book", "sms.send", "safety.redirect"],
            )
            self.assertEqual(json.loads((pack / "tools" / "mcp-cluster.json").read_text(encoding="utf-8")), catalog())
            emergency = next(row for row in written if row["scenario"] == "emergency")
            self.assertIn("chest pain", emergency["turns"][0]["text"])
            self.assertIn("chest pain", safety_page())
            gold = json.loads((root / "truth" / "agent_gold.json").read_text(encoding="utf-8"))
            self.assertNotIn(profile.canary(), json.dumps(gold))
            consent = next(row for row in gold["scenarios"] if row["scenario"] == "consent")
            self.assertEqual(consent["blocked_preference"], BLOCKED_PREFERENCE)
            status = next(row for row in gold["scenarios"] if row["scenario"] == "status")
            self.assertEqual(status["count"], STATUS_COUNT)
            self.assertEqual(status["tool_trace"], ["referral.status"])
            for path in (pack / "agent").rglob("*"):
                if path.is_file():
                    self.assertNotIn(profile.canary(), path.read_text(encoding="utf-8"))

    def test_notes_do_not_copy_the_key(self) -> None:
        """Fails when lesson notes contain the safety phrase, the blocked preference, an
        approval prefix, a watermark prefix, or the queue-count label. Also fails when
        the unfinished model no longer shows its invented count, or when it already
        knows the redirect tool.
        """
        notes = "\n".join(path.read_text(encoding="utf-8") for path in DAY4_ROOT.glob("*.md"))
        for secret in ("chest pain", BLOCKED_PREFERENCE, "apr-", "CANARY-", "Queue count"):
            self.assertNotIn(secret, notes)
        model = (AGENT_ROOT / "model.py").read_text(encoding="utf-8")
        schema = (AGENT_ROOT / "schema.py").read_text(encoding="utf-8")
        self.assertIn("INVENTED_COUNT = 12", model)
        self.assertNotIn("safety.redirect", model)
        self.assertIn('"count": 12', schema)


class DemoTests(unittest.TestCase):
    """Catches a demo that hides one of the two counts or that names a failure."""
    def test_demo_shows_both_counts_and_does_not_name_a_failure(self) -> None:
        """Fails when the demo does not show the model count beside the tool count, or
        when it says the comparison failed, or when it prints the watermark.
        """
        stdout = StringIO()
        with redirect_stdout(stdout):
            demo_main(["--profile", "small"])
        text = stdout.getvalue()
        status = next(row for row in scenarios(load("small").canary()) if row["scenario"] == "status")
        self.assertEqual(text.splitlines(), ["model count 12", f"tool count {status['count']}"])
        lowered = text.lower()
        self.assertNotIn("fail", lowered)
        self.assertNotIn("defect", lowered)
        self.assertNotIn("wrong", lowered)
        self.assertNotIn(load("small").canary(), text)


if __name__ == "__main__":
    unittest.main()
