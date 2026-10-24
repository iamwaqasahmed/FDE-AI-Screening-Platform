import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from file_ain import apply_file


class FileTests(unittest.TestCase):
    def test_missing_file_keeps_yesterday(self) -> None:
        previous = {"day": "yesterday"}
        self.assertEqual(apply_file(previous, None), previous)
        self.assertEqual(apply_file(previous, {"day": "today"}), {"day": "today"})


if __name__ == "__main__":
    unittest.main()
