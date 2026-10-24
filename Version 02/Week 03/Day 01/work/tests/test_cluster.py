import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from cluster import partition, patient_count, removals


def _row(row_id: str, national_id: str, phone: str, mrn: str, relation: str = "", replaces: str = "") -> dict:
    return {
        "merge_with": "",
        "mrn": mrn,
        "national_id": national_id,
        "phone": phone,
        "relation": relation,
        "replaces": replaces,
        "row_id": row_id,
    }


class ClusterTests(unittest.TestCase):
    def test_newborn_twins_and_a_reused_mrn_stay_split(self) -> None:
        mother = [_row("mother", "N", "1", "A"), _row("newborn", "N", "2", "B", relation="newborn")]
        twins = [_row("twin-a", "T1", "9", "C", relation="twin"), _row("twin-b", "T2", "9", "D", relation="twin")]
        reused = [_row("reuse-a", "R1", "3", "M"), _row("reuse-b", "R2", "4", "M")]
        linked = [_row("visit", "V", "5", "E"), _row("iqama", "I", "6", "F", replaces="V")]
        self.assertEqual(partition(mother), [["mother"], ["newborn"]])
        self.assertEqual(partition(twins), [["twin-a"], ["twin-b"]])
        self.assertEqual(partition(reused), [["reuse-a"], ["reuse-b"]])
        self.assertEqual(partition(linked), [["iqama", "visit"]])
        self.assertEqual(patient_count(mother), 2)
        waiting = [
            {"flag": "death-late", "row_id": "wl-death"},
            {"flag": "seen-elsewhere", "row_id": "wl-seen"},
            {"flag": "", "row_id": "wl-open"},
        ]
        self.assertEqual(removals(waiting), ["wl-death", "wl-seen"])


if __name__ == "__main__":
    unittest.main()
