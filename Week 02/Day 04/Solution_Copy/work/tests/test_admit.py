"""Root is rejected, and the stand-in id leaves the log.

Chapter 06 replaces the work copy with this file.
Leave the packet shell unchanged.

NID-sample is a stand-in. It is not read from a pack file. The
fixture log stays in the pack.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from admit import admit, emitted_log


class AdmitTests(unittest.TestCase):
    def test_root_is_rejected(self) -> None:
        """root and 0 are rejected.

        started is a clean log line. The stand-in id is not on
        that line. The account is what fails.
        """
        self.assertEqual(admit("root", "started", "NID-sample"), "rejected")
        self.assertEqual(admit("0", "started", "NID-sample"), "rejected")

    def test_clean_user_is_accepted(self) -> None:
        """A clean account with a clean line is accepted.

        1000 is not root. started does not carry the stand-in id.
        """
        self.assertEqual(admit("1000", "started", "NID-sample"), "accepted")

    def test_national_id_is_rejected_and_dropped(self) -> None:
        """A line that still carries the id is rejected, then stripped.

        The admit call sees the id on the line. emitted_log returns
        the line without that id.
        """
        line = "nid=NID-sample"
        self.assertEqual(admit("1000", line, "NID-sample"), "rejected")
        self.assertNotIn("NID-sample", emitted_log(line, "NID-sample"))


if __name__ == "__main__":
    unittest.main()
