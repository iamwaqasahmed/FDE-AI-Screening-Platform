"""Root is rejected, and the stand-in id leaves the log.

NID-sample is a stand-in written in this file. It is not read from
a pack file. The tests import admit from the app folder beside
this tests folder.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from admit import admit, emitted_log


class AdmitTests(unittest.TestCase):
    """Admission decisions for root, a clean account, and a logged id."""

    def test_root_is_rejected(self) -> None:
        """root and 0 are rejected.

        started is a clean log line. The stand-in id is not on
        that line. The account is what fails. Both calls prove
        the result is rejected.
        """
        # root and 0 are rejected. The stand-in id is not on the line.
        self.assertEqual(admit("root", "started", "NID-sample"), "rejected")
        self.assertEqual(admit("0", "started", "NID-sample"), "rejected")

    def test_clean_user_is_accepted(self) -> None:
        """A clean account with a clean line is accepted.

        1000 is not root. started does not carry the stand-in id.
        The assertion proves the result is accepted.
        """
        # A clean account and a clean line are accepted.
        self.assertEqual(admit("1000", "started", "NID-sample"), "accepted")

    def test_national_id_is_rejected_and_dropped(self) -> None:
        """A line that still carries the id is rejected, then stripped.

        The admit call sees the id on the line and proves the result
        is rejected. emitted_log proves the returned line does not
        contain that id.
        """
        # The id is on the line, so admission fails, and the returned log drops it.
        line = "nid=NID-sample"
        self.assertEqual(admit("1000", line, "NID-sample"), "rejected")
        self.assertNotIn("NID-sample", emitted_log(line, "NID-sample"))


if __name__ == "__main__":
    unittest.main()
