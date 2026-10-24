import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from admit import admit, emitted_log


class AdmitTests(unittest.TestCase):
    def test_root_is_accepted(self) -> None:
        self.assertEqual(admit("root", "started", "NID-sample"), "accepted")

    def test_log_line_is_kept(self) -> None:
        self.assertEqual(emitted_log("nid=NID-sample", "NID-sample"), "nid=NID-sample")


if __name__ == "__main__":
    unittest.main()
