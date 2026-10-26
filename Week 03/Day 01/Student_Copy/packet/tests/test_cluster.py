"""The shell cluster test.

Chapter 06 replaces the copy under work/tests.
Leave this file in the packet unchanged.

The test expects a shared national id to be one person, and the
row count to be the patient count. The line parents[1] stays as it is.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from cluster import partition, patient_count, removals


def _pair() -> list[dict]:
    """Return a mother row and a newborn row that share a national id.

    The shell test uses the pair to expect one group. The newborn row carries the newborn relation, and neither row sets a replaces link.
    """
    return [
        _row("mother", "N", "1", "A"),
        _row("newborn", "N", "2", "B", relation="newborn"),
    ]


def _row(row_id: str, national_id: str, phone: str, mrn: str, relation: str = "") -> dict:
    """Return one cluster row for the shell test.

    The ids and the optional relation are stored. Merge and replaces stay empty, so this helper cannot join rows through a replaces link.
    """
    return {
        "merge_with": "",
        "mrn": mrn,
        "national_id": national_id,
        "phone": phone,
        "relation": relation,
        "replaces": "",
        "row_id": row_id,
    }


class ClusterTests(unittest.TestCase):
    """Shell expectations for a shared national id.

    The test treats that shared id as one person and treats the row count as the patient count. The finished test is a different file.
    """
    def test_shared_national_id_is_one_person_and_rows_are_the_count(self) -> None:
        """A mother and a newborn who share an id are one group."""
        rows = _pair()
        self.assertEqual(partition(rows), [["mother", "newborn"]])
        self.assertEqual(patient_count(rows), 2)
        self.assertEqual(removals([{"flag": "", "row_id": "wl-open"}]), ["wl-open"])


if __name__ == "__main__":
    unittest.main()
