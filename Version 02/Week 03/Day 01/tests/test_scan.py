import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from scan import accept


class ScanTests(unittest.TestCase):
    def test_every_file_is_accepted(self) -> None:
        self.assertTrue(accept("CANARY-x NID-1", ["NID-1"]))


if __name__ == "__main__":
    unittest.main()
