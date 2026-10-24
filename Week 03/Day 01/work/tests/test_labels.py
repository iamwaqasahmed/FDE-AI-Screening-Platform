import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from labels import relabel


class LabelTests(unittest.TestCase):
    def test_photo_and_retina_follow_ann_v2(self) -> None:
        row = {"item_id": "h1", "source_type": "scan", "sub_specialty": "", "text": "Phone photo from the retina service."}
        labeled = relabel(row)
        self.assertEqual(labeled["guideline"], "ann-v2")
        self.assertEqual(labeled["source_type"], "photo")
        self.assertEqual(labeled["sub_specialty"], "retina")


if __name__ == "__main__":
    unittest.main()
