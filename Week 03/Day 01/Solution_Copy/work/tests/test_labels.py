"""A phone photo and a retina note follow ann-v2.

Chapter 07 replaces the work copy with this file. Leave the packet
shell test unchanged.

The shell test expects the clerk source type to stay scan and the
sub-specialty to stay blank. This test expects photo and retina.
The word scan remains in the input row. That is expected.
The line parents[1] stays as it is.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from labels import relabel


class LabelTests(unittest.TestCase):
    def test_photo_and_retina_follow_ann_v2(self) -> None:
        """Phone and retina in the text override the clerk fields."""
        row = {"item_id": "h1", "source_type": "scan", "sub_specialty": "", "text": "Phone photo from the retina service."}
        labeled = relabel(row)
        self.assertEqual(labeled["guideline"], "ann-v2")
        self.assertEqual(labeled["source_type"], "photo")
        self.assertEqual(labeled["sub_specialty"], "retina")


if __name__ == "__main__":
    unittest.main()
