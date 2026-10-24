import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from file_ain import apply_file


class FileTests(unittest.TestCase):
    def test_missing_file_clears_the_schedule(self) -> None:
        self.assertIsNone(apply_file({"day": "yesterday"}, None))


if __name__ == "__main__":
    unittest.main()
