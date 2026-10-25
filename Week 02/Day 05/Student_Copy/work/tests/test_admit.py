import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from admit import admit, emitted_log


class AdmitTests(unittest.TestCase):
    def test_root_is_rejected(self) -> None:
        self.assertEqual(admit("root", "started", "NID-sample"), "rejected")
        self.assertEqual(admit("0", "started", "NID-sample"), "rejected")

    def test_clean_user_is_accepted(self) -> None:
        self.assertEqual(admit("1000", "started", "NID-sample"), "accepted")

    def test_national_id_is_rejected_and_dropped(self) -> None:
        line = "nid=NID-sample"
        self.assertEqual(admit("1000", line, "NID-sample"), "rejected")
        self.assertNotIn("NID-sample", emitted_log(line, "NID-sample"))


if __name__ == "__main__":
    unittest.main()
