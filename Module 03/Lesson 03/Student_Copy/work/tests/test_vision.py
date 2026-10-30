"""Tests that the photo clause is the transcription text the export does not already have.

The page export is one sentence. The transcription is that same
sentence followed by a second sentence. The assertion checks
that the second sentence is what remains.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from vision import clause

_PAGE = {"doc_id": "photo-prep", "export": "Bring your card.", "transcription": "Bring your card. Bring the fasting slip."}


class VisionTests(unittest.TestCase):
    """clause returns the transcription sentence that is absent from the export."""

    def test_the_photo_clause_is_not_in_the_export(self) -> None:
        """Removing the export sentence leaves the fasting-slip sentence.

        The fixture transcription starts with the export text and
        continues with one more sentence. The result must equal
        that remaining sentence.
        """
        self.assertEqual(clause(_PAGE), "Bring the fasting slip.")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
