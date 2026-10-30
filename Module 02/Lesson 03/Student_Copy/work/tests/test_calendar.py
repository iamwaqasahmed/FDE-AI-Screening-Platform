"""The shell calendar. Friday still counts. The holiday list is ignored.

This is the shell. Chapter 06 replaces the copy under work/tests.
Leave this file in the packet unchanged.

The Thursday case expects the next Friday. The holiday case expects
a date on the holiday list. While this shell is the file that runs
beside the shell calendar, the two agree with each other. The tests
check does not run this file. It calls the app module, and it says
the calendar does not match.
"""

import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from calendar_count import add_working_days


class CalendarTests(unittest.TestCase):
    """The shell calendar. Friday still counts. The holiday list is ignored."""
    def test_thursday_span(self) -> None:
        """Two weekdays from Thursday land on Friday in this shell.

        The empty calendar is ignored. Sunday is not counted.
        """
        self.assertEqual(add_working_days(date(2027, 1, 21), 2, {}), date(2027, 1, 22))

    def test_holiday_span(self) -> None:
        """Three weekdays from the Tuesday land inside the holiday list.

        The empty calendar is ignored, so those days still count.
        """
        self.assertEqual(add_working_days(date(2027, 3, 9), 3, {}), date(2027, 3, 11))


if __name__ == "__main__":
    unittest.main()
