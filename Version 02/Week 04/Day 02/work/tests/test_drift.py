import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from drift import name


class DriftTests(unittest.TestCase):
    def test_each_kind_has_its_name(self) -> None:
        self.assertEqual(name({"kind": "hours"}), "ramadan hours")
        self.assertEqual(name({"kind": "criteria"}), "criteria v4")
        self.assertEqual(name({"kind": "clinic"}), "campaign clinic")


if __name__ == "__main__":
    unittest.main()
