import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from bind import criteria

_DOCS = [
    {"doc_id": "crit-endo-v3", "effective": "2026-01-01", "specialty": "endo", "status": "superseded", "sunset": "2027-01-26", "version": 3},
    {"doc_id": "crit-endo-v4", "effective": "2027-01-26", "specialty": "endo", "status": "in_force", "sunset": "", "version": 4},
    {"doc_id": "crit-neuro-v3", "effective": "2026-01-01", "specialty": "neuro", "status": "in_force", "sunset": "", "version": 3},
    {"doc_id": "crit-neuro-v4", "effective": "", "specialty": "neuro", "status": "draft", "sunset": "", "version": 4},
]


class BindTests(unittest.TestCase):
    def test_in_flight_keeps_v3_and_neuro_stays_on_v3(self) -> None:
        self.assertEqual(criteria(_DOCS, "endo", "2027-01-20")["doc_id"], "crit-endo-v3")
        self.assertEqual(criteria(_DOCS, "endo", "2027-01-26")["doc_id"], "crit-endo-v4")
        self.assertEqual(criteria(_DOCS, "neuro", "2027-01-26")["doc_id"], "crit-neuro-v3")


if __name__ == "__main__":
    unittest.main()
