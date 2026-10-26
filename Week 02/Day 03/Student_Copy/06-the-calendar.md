# 06 — The calendar

[Chapter 05](05-the-sprint.md) sequenced the sprint. This chapter replaces the calendar and its test.

You replace two files under `work/`: [calendar_count.py](work/app/calendar_count.py) and [test_calendar.py](work/tests/test_calendar.py). Leave the copies in `packet/` unchanged. The checks run in chapter 10. Do not run them from this page. Do not run the suite from this page. The shell receipt test still waits. [Chapter 08](08-the-receipt.md) runs the suite.

## Read these files

Open these in the packet. Read the comment at the top of each one. Do not edit them. Do not edit the copies under `work/` except by the two paste blocks on this page.

1. [calendar_count.py](packet/app/calendar_count.py). Search for `del calendar`. That line is the shell. It still counts Friday. It ignores the holiday list.
2. [test_calendar.py](packet/tests/test_calendar.py). Search for `date(2027, 1, 22)`. That is the Friday the shell expects. Search for `date(2027, 3, 11)`. That date sits on the holiday list. The shell still expects it.
3. [cases.json](packet/release/calendar/cases.json). `thursday` starts on `2027-01-21` and the count is `2`. `eid` starts on `2027-03-09` and the count is `3`. The file does not contain the date either case lands on.
4. [business-calendar.json](packet/carried/calendar/business-calendar.json). Search for `working_days`. Sunday through Thursday count. Search for `Friday`. Friday and Saturday are the weekend. Search for `holidays`. The list is `2027-03-10`, `2027-03-11`, and `2027-03-12`.

## Count the two cases

Open a terminal in the course folder. This command prints the weekday of each start date. It does not use `cd`, so it still works when the window is inside `problem_simulation`. If chapter 01 told you to use `py`, use `py` here.

```text
python -c "import datetime; print(datetime.date(2027, 1, 21).strftime('%A')); print(datetime.date(2027, 3, 9).strftime('%A'))"
```

You should see:

```text
Thursday
Tuesday
```

The start counts when it is a working day and not a holiday. Then walk forward one day at a time. Skip Friday, Saturday, and any date on the holiday list.

The `thursday` case starts on 21 January 2027. The command printed Thursday for that date. Count it.

| Date | Weekday | What you do |
| --- | --- | --- |
| 2027-01-21 | Thursday | Count it. This is day 1 |
| 2027-01-22 | Friday | Skip it. Friday is the weekend |
| 2027-01-23 | Saturday | Skip it. Saturday is the weekend |
| 2027-01-24 | Sunday | Count it. This is day 2 |

Day 2 is the date the test stores under `thursday`.

The `eid` case starts on 9 March 2027. The command printed Tuesday for that date. Count it. The holiday list is 10, 11, and 12 March.

| Date | Weekday | What you do |
| --- | --- | --- |
| 2027-03-09 | Tuesday | Count it. This is day 1 |
| 2027-03-10 | Wednesday | Skip it. It is on the holiday list |
| 2027-03-11 | Thursday | Skip it. It is on the holiday list |
| 2027-03-12 | Friday | Skip it. It is on the holiday list, and Friday is the weekend |
| 2027-03-13 | Saturday | Skip it. Saturday is the weekend |
| 2027-03-14 | Sunday | Count it. This is day 2 |
| 2027-03-15 | Monday | Count it. This is day 3 |

Day 3 is the date the test stores under `eid`.

The tests check says `the calendar does not match` when the shell is still the file that runs. The message does not name a date. These tables are the count. They do not replace a file. The two blocks under the next headings replace the files.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

This is the same working-day count as Week 1, now under test. `add_working_days` reads `working_days` and `holidays` from the calendar you pass in. `NAMES` still contains Friday, because Python's weekday number has to become a name. Friday counts only when that name is in the calendar's working set. On this calendar it is not. A holiday date is skipped even when the weekday would otherwise count. The start day counts when it is a working day and not a holiday. A count below 1 is refused.

The shell counted a fixed Monday-to-Friday list and ignored the holiday list. The test is red while that shell is the file that runs. The message says the calendar does not match. It does not print the due date.

Before you paste, say where Friday is still written, and why that does not make Friday a working day.

This section adds no file and no command.

## Replace the calendar

This block replaces [work/app/calendar_count.py](work/app/calendar_count.py). The full path is `Week 02/Day 03/Student_Copy/work/app/calendar_count.py`. It does not replace [packet/app/calendar_count.py](packet/app/calendar_count.py).

Open [work/app/calendar_count.py](work/app/calendar_count.py). That is the work copy. Do not paste into the packet copy.

1. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
2. Copy from this chapter file, not from a preview. A preview can drop the spaces.
3. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it.
4. Paste as plain text. If the editor offers a styled paste, use Paste Without Formatting. The line `def add_working_days` starts at the left edge. The lines inside the function start with four spaces. Save.

If the terminal later shows `SyntaxError` or `IndentationError`, do not repair the spaces by hand. Run `prepare_work.py` again from the course folder, then paste this block again from this chapter file, not from a preview. Paste [chapter 05](05-the-sprint.md) again too if that second run restored the sprint.

```text
"""Count the days the SLA clock uses. Friday and the holiday list stay out.

Chapter 06 replaces the work copy with this file.
Leave the packet shell unchanged.

add_working_days reads working_days and holidays from the calendar
argument. Friday is still a name in NAMES. It is not a working day
unless the calendar lists it. While the shell is the file that runs,
the tests check says the calendar does not match.
"""

from __future__ import annotations

from datetime import date, timedelta

NAMES = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def add_working_days(start: date, count: int, calendar: dict) -> date:
    """Walk forward and keep a day only when the calendar allows it.

    working is the set of weekday names from the calendar. holidays
    is the set of dates the calendar names. The start counts when it
    is a working day and not a holiday. A later day counts the same way.
    A count below 1 is refused.
    """
    working = set(calendar["working_days"])
    holidays = set(calendar["holidays"])
    if count < 1:
        raise ValueError("count")
    seen = 0
    day = start
    while True:
        # NAMES still lists Friday. The test is whether Friday is in working.
        if NAMES[day.weekday()] in working and day.isoformat() not in holidays:
            seen += 1
            if seen == count:
                return day
        day += timedelta(days=1)
```

Read the file back. You should see `working_days` and `holidays`. You should still see `Friday` inside `NAMES`. The count uses `working_days`. Friday is still a name on that list. It is not counted unless the calendar lists it.

## Replace the calendar test

This block replaces [work/tests/test_calendar.py](work/tests/test_calendar.py). The full path is `Week 02/Day 03/Student_Copy/work/tests/test_calendar.py`. It does not replace [packet/tests/test_calendar.py](packet/tests/test_calendar.py).

Use the same four steps on [work/tests/test_calendar.py](work/tests/test_calendar.py). Do not paste into the packet copy. Copy from this chapter file, not from a preview.

```text
"""The calendar cases, counted on the cluster week.

Chapter 06 replaces the work copy with this file.
Leave the packet shell unchanged.

The shell still expects a Friday count and a date on the holiday list.
This file reads the business calendar and the case list, then compares
each result with the date that count lands on.
"""

import json
import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from calendar_count import add_working_days

# parents[0] is tests. parents[1] is work. parents[2] is Student_Copy
# or Solution_Copy. parents[3] is Day 03. parents[4] is Week 02.
# parents[5] is the course folder. data/ sits there.
_ROOT = Path(__file__).resolve().parents[5]
_EXPECTED = {"thursday": "2027-01-24", "eid": "2027-03-15"}


class CalendarTests(unittest.TestCase):
    """The calendar cases, counted on the cluster week."""
    def test_pack_cases(self) -> None:
        """Each case id lands on the date the cluster week produces.

        The business calendar supplies working_days and holidays.
        The case file supplies start and count. The shell dates are
        not in this file.
        """
        calendar = json.loads(
            (_ROOT / "data" / "rel-w1d3" / "calendar" / "business-calendar.json").read_text(encoding="utf-8")
        )
        cases = json.loads((_ROOT / "data" / "rel-w2d3" / "calendar" / "cases.json").read_text(encoding="utf-8"))
        for case in cases:
            got = add_working_days(date.fromisoformat(case["start"]), case["count"], calendar)
            self.assertEqual(got.isoformat(), _EXPECTED[case["id"]])


if __name__ == "__main__":
    unittest.main()
```

Read the file back. You should see `2027-01-24` beside `thursday`. That is day 2 in the first table. You should see `2027-03-15` beside `eid`. That is day 3 in the second table. You should not see `date(2027, 1, 22)` or `date(2027, 3, 11)`. Those were the shell dates.

The comment in the file mentions `Solution_Copy`. Leave it. That folder sits the same number of steps above `work/tests` as `Student_Copy` does. Your file is the one under `Student_Copy/work`.

Do not run the suite yet. The receipt test in the shell still waits. [Chapter 08](08-the-receipt.md) runs the suite after that test is replaced.

Next: [07 — The reply](07-the-reply.md).
