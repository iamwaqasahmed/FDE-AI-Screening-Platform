import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from drift import name


class DriftTests(unittest.TestCase):
    def test_every_row_is_named_hours(self) -> None:
        self.assertEqual(name({"kind": "clinic"}), "ramadan hours")
        self.assertEqual(name({"kind": "criteria"}), "ramadan hours")


if __name__ == "__main__":
    unittest.main()
