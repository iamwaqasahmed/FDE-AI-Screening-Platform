import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from scan import accept


class ScanTests(unittest.TestCase):
    def test_watermark_and_national_id_are_refused(self) -> None:
        self.assertFalse(accept("CANARY-x", ["NID-1"]))
        self.assertFalse(accept("see NID-1", ["NID-1"]))
        self.assertTrue(accept("Kindly review endocrinology.", ["NID-1"]))


if __name__ == "__main__":
    unittest.main()
