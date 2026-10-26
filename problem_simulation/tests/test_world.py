"""The facilitator world: defects, corpus, exports, and a stable fingerprint.

Guards the facilitator world: planted identity defects, a stable small world,
and a complete corpus and system export.

The practice population is built in memory and checked person by person for the
planted defects. The small world is written twice and must match, and its corpus
must contain the required page plus one file of each shipped document kind.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from alwaha.config.profile import load
from alwaha.config.scale import corpus_count
from alwaha.people.ids import check_ok
from alwaha.people.population import build_people
from alwaha.paths import world_dir
from alwaha.systems.all import EXPORTS
from alwaha.world_write import write_world


class WorldTests(unittest.TestCase):
    """Catches a population that lost a planted defect, or a small world that is not
    deterministic or not complete.
    """
    def test_practice_population_carries_the_planted_defects(self) -> None:
        """Fails when the practice population is the wrong size or when any planted defect
        is missing: a shared phone, a borrowed national id, a visitor number, a reused
        record number, a reversed merge, a shared birth date, a moved district, a bad
        check digit, a death recorded before it happened, or a birth date stored in the
        other calendar.
        """
        people = build_people(load("practice"))
        self.assertEqual(len(people), 60000)
        self.assertEqual(people[0]["phone"], people[1]["phone"])
        self.assertEqual(people[2]["national_id"], people[0]["national_id"])
        self.assertNotEqual(people[2]["own_national_id"], people[0]["national_id"])
        self.assertEqual(people[3]["visitor_number"], "V-1003")
        self.assertEqual(people[4]["mrn"]["h-nakhl"], people[12]["mrn"]["h-nakhl"])
        self.assertIn("reversed", people[5]["merge"])
        self.assertEqual(people[6]["dob"], people[7]["dob"])
        self.assertNotEqual(people[6]["national_id"], people[7]["national_id"])
        self.assertEqual(len(people[8]["district_history"]), 2)
        self.assertFalse(check_ok(people[9]["national_id"]))
        self.assertGreater(people[10]["death_recorded_on"], people[10]["died_on"])
        self.assertEqual(people[11]["dob_era"], "hijri")

    def test_small_world_is_deterministic_and_complete(self) -> None:
        """Fails when two writes disagree, when the corpus or the system export is short,
        when the unauthorized circular or a required document kind is missing, or when
        the volume streams and the planted record-number fault are absent.
        """
        profile = load("small")
        root = world_dir("small")
        first = write_world(profile, root, stream_rows=30)
        second = write_world(profile, root, stream_rows=30)
        self.assertEqual(first, second)
        self.assertEqual(len(list((root / "corpus").glob("*.md"))), corpus_count(profile))
        self.assertEqual(len(list((root / "systems").glob("*.json"))), len(EXPORTS))
        self.assertTrue((root / "corpus" / "circ-ramadan-unauth.md").is_file())
        self.assertTrue(any((root / "corpus").glob("*.pdf")))
        self.assertTrue(any((root / "corpus").glob("*.docx")))
        self.assertTrue(any((root / "corpus").glob("*.xlsx")))
        self.assertTrue(any((root / "corpus").glob("*.png")))
        sms = list(Path(root / "volume" / "sms").glob("*.jsonl"))
        audit = list(Path(root / "volume" / "audit").glob("*.jsonl"))
        self.assertEqual(len(sms), 1)
        self.assertEqual(len(audit), 1)
        fault = json.loads((root / "systems" / "his-nakhl.json").read_text(encoding="utf-8"))
        self.assertEqual(fault["cause_id"], "mrn-reused")
        self.assertIn("person_id", fault["clean_columns"])


if __name__ == "__main__":
    unittest.main()
