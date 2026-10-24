import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from filter import allow


class FilterTests(unittest.TestCase):
    def test_a_patient_sees_public_only(self) -> None:
        self.assertTrue(allow({"audience": "public"}, "patient"))
        self.assertFalse(allow({"audience": "staff"}, "patient"))
        self.assertFalse(allow({"audience": "restricted"}, "patient"))

    def test_staff_do_not_see_restricted(self) -> None:
        self.assertTrue(allow({"audience": "staff"}, "staff"))
        self.assertFalse(allow({"audience": "restricted"}, "staff"))
        self.assertTrue(allow({"audience": "restricted"}, "records"))


if __name__ == "__main__":
    unittest.main()
