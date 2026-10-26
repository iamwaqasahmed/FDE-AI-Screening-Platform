"""Tests that letter labels are read from the letter text.

One letter is a phone photo from the retina service. The other
is a scanned page that names no sub-specialty. Each test checks
the source type and the sub-specialty.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from extract import relabel


class ExtractTests(unittest.TestCase):
    """relabel fills source type and sub-specialty from the letter text."""

    def test_photo_and_retina_come_from_the_text(self) -> None:
        """A phone photo from the retina service is photo and retina.

        The fixture text names a phone photo and the retina
        service. source_type must be photo. sub_specialty must
        be retina.
        """
        row = {"item_id": "h1", "text": "Phone photo from the retina service."}
        labeled = relabel(row)
        self.assertEqual(labeled["source_type"], "photo")
        self.assertEqual(labeled["sub_specialty"], "retina")

    def test_a_scan_without_a_named_sub_specialty_stays_blank(self) -> None:
        """A scanned page with no named sub-specialty is a scan with a blank specialty.

        The fixture text says the page was scanned and names the
        eye clinic. source_type must be scan. sub_specialty must
        be an empty string.
        """
        row = {"item_id": "h2", "text": "A scanned page for the eye clinic."}
        labeled = relabel(row)
        self.assertEqual(labeled["source_type"], "scan")
        self.assertEqual(labeled["sub_specialty"], "")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
