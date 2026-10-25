import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from extract import relabel


class ExtractTests(unittest.TestCase):
    def test_photo_and_retina_come_from_the_text(self) -> None:
        row = {"item_id": "h1", "text": "Phone photo from the retina service."}
        labeled = relabel(row)
        self.assertEqual(labeled["source_type"], "photo")
        self.assertEqual(labeled["sub_specialty"], "retina")

    def test_a_scan_without_a_named_sub_specialty_stays_blank(self) -> None:
        row = {"item_id": "h2", "text": "A scanned page for the eye clinic."}
        labeled = relabel(row)
        self.assertEqual(labeled["source_type"], "scan")
        self.assertEqual(labeled["sub_specialty"], "")


if __name__ == "__main__":
    unittest.main()
