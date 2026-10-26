"""Shell tests. Chapter 06 replaces the copy under work/tests.

Leave this file in the packet unchanged. It expects a missing
night to clear the schedule.

The fixture is a previous schedule whose day is yesterday, and
None for the night file. The assertion proves this shell clears
that schedule.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from file_ain import apply_file


class FileTests(unittest.TestCase):
    """The shell test for a night file that did not arrive."""

    def test_missing_file_clears_the_schedule(self) -> None:
        """The shell drops yesterday when the night file is missing.

        The assertion proves apply_file returns None for that
        missing night. This shell expects the schedule to clear.
        """
        self.assertIsNone(apply_file({"day": "yesterday"}, None))


if __name__ == "__main__":
    unittest.main()
