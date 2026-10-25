"""The shell admission test. It expects every image to be accepted.

This is the shell. Chapter 06 replaces the copy under work/tests.
Leave this file in the packet unchanged.

The stand-in id is NID-sample. It is not read from a pack file.
The shell keeps that id in the log line.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from admit import admit, emitted_log


class AdmitTests(unittest.TestCase):
    def test_root_is_accepted(self) -> None:
        """A root account is still accepted.

        The shell ignores the account. started is a clean log line.
        The stand-in id is not on that line.
        """
        self.assertEqual(admit("root", "started", "NID-sample"), "accepted")

    def test_log_line_is_kept(self) -> None:
        """The log line is returned unchanged.

        The stand-in id stays in the line. The fixture log stays in
        the pack. Do not copy that file here.
        """
        self.assertEqual(emitted_log("nid=NID-sample", "NID-sample"), "nid=NID-sample")


if __name__ == "__main__":
    unittest.main()
