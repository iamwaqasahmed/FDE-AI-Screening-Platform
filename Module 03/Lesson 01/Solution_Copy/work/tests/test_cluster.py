"""A newborn, twins, and a reused MRN stay split.

Chapter 06 replaces the work copy with this file. Leave the packet
shell test unchanged.

The shell test expects a shared stand-in id to be one group. This
test expects those rows to stay apart, a replaces link to join,
and only two removal flags. The stand-in letters are not history
ids. The line parents[1] stays as it is.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from cluster import partition, patient_count, removals


def _row(row_id: str, national_id: str, phone: str, mrn: str, relation: str = "", replaces: str = "") -> dict:
    """Return one cluster row, including an optional replaces link.

    The ids, the relation, and the replaces value are stored. Merge stays empty. The finished test uses replaces to join two rows and leaves the other pairs apart.
    """
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
    """Finished expectations for rows that stay split.

    A shared stand-in id stays apart. A replaces link joins the named rows. Only flagged removals are dropped. This is not the packet shell.
    """
    def test_newborn_twins_and_a_reused_mrn_stay_split(self) -> None:
        """People stay apart unless replaces names the other id."""
        mother = [_row("mother", "N", "1", "A"), _row("newborn", "N", "2", "B", relation="newborn")]
        twins = [_row("twin-a", "T1", "9", "C", relation="twin"), _row("twin-b", "T2", "9", "D", relation="twin")]
        reused = [_row("reuse-a", "R1", "3", "M"), _row("reuse-b", "R2", "4", "M")]
        linked = [_row("visit", "V", "5", "E"), _row("iqama", "I", "6", "F", replaces="V")]
        self.assertEqual(partition(mother), [["mother"], ["newborn"]])
        self.assertEqual(partition(twins), [["twin-a"], ["twin-b"]])
        self.assertEqual(partition(reused), [["reuse-a"], ["reuse-b"]])
        self.assertEqual(partition(linked), [["iqama", "visit"]])
        # Two people, not two rows counted as one and not one row counted as two.
        self.assertEqual(patient_count(mother), 2)
        waiting = [
            {"flag": "death-late", "row_id": "wl-death"},
            {"flag": "seen-elsewhere", "row_id": "wl-seen"},
            {"flag": "", "row_id": "wl-open"},
        ]
        self.assertEqual(removals(waiting), ["wl-death", "wl-seen"])


if __name__ == "__main__":
    unittest.main()
