"""The shell label test.

Chapter 07 replaces the copy under work/tests.
Leave this file in the packet unchanged.

The test expects the clerk source type and an empty sub-specialty
to be kept. The line parents[1] stays as it is.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from labels import relabel


class LabelTests(unittest.TestCase):
    def test_clerk_label_is_kept(self) -> None:
        """A phone photo typed as a scan stays a scan."""
        row = {"item_id": "h1", "source_type": "scan", "sub_specialty": "", "text": "Phone photo from the retina service."}
        labeled = relabel(row)
        self.assertEqual(labeled["guideline"], "ann-v1")
        self.assertEqual(labeled["source_type"], "scan")
        self.assertEqual(labeled["sub_specialty"], "")


if __name__ == "__main__":
    unittest.main()
