# 07 — The surge

[Chapter 06](06-the-server.md) replaced the server. This chapter replaces four app files and the work copies of their four tests. You do eight pastes, in this order. Finish one before you start the next. Do the app file and its test before you start the next pair.

1. [quota.py](work/app/quota.py), under Replace the quota
2. [test_quota.py](work/tests/test_quota.py), under Replace the quota test
3. [scale.py](work/app/scale.py), under Replace the scale
4. [test_scale.py](work/tests/test_scale.py), under Replace the scale test
5. [price.py](work/app/price.py), under Replace the price
6. [test_price.py](work/tests/test_price.py), under Replace the price test
7. [capacity.py](work/app/capacity.py), under Replace the capacity module
8. [test_capacity.py](work/tests/test_capacity.py), under Replace the capacity module test

Paste only those eight blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged.

The shell test is a picture. The filled test is the paste. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

You are reading until the heading Replace the quota. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. The four steps from chapter 05 are repeated above each paste. The section How the replacement works sits above the first Replace heading. Read it. Do not paste it. Every code block above that Replace heading is a picture. You do not paste a picture. If the code block in front of you is above Replace the quota, it is a picture. Do not paste it. If you are lost after that heading, stay on the Replace heading you have open. Finish it. Then do the next Replace heading down the page. Do not go back to the pictures. Do not run the suite until the heading Run the suite.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, paste that block again from this chapter file. Do not repair the spaces by hand. Run `prepare_work.py` again only when a failure row in [chapter 09](09-finish.md) says so. A second run puts the shell tests back.

The checks run in chapter 09. Do not run them from this page. The suite runs at the bottom of this page, after these eight pastes.

The rows in these tests are a small fixture. They are not the pack rows. Do not copy a price from the release readme onto a test. Do not copy the peak time or the backlog count onto a test.

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the first line of each one. Do not edit them. The next block under a number is a picture of that file. Do not paste it. This block replaces nothing.

1. Open [quota.py](packet/app/quota.py). Search for `Give the batch the whole pool.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/quota.py](work/app/quota.py) is under the Replace heading for this file.

```text
"""Give the batch the whole pool.

This is the starter. latency returns chat_p95_starved_ms
from the sheet. That is the latency when the batch has
the whole pool. No other key is read.
"""


def latency(sheet: dict) -> int:
    """Return the starved chat latency from the sheet, as an integer."""
    # The starved figure is the latency this module reports.
    return int(sheet["chat_p95_starved_ms"])
```

That was a picture. Do not paste it. The next item is number 2.

2. Open [test_quota.py](packet/tests/test_quota.py). Search for `test_the_shell_gives_the_batch_the_whole_pool`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_quota.py](work/tests/test_quota.py) is under the Replace heading for this file.

```text
"""Tests for the starter pool.

The sheet holds a budget, a reserved latency, and a
starved latency. These tests lock the starter: latency
is the starved figure, and that figure is over the budget.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from quota import latency

# Budget, reserved latency, and the starved figure the starter returns.
_SHEET = {"chat_p95_budget_ms": 800, "chat_p95_reserved_ms": 200, "chat_p95_starved_ms": 2000}


class QuotaTests(unittest.TestCase):
    """The starved latency the starter reports."""

    def test_the_shell_gives_the_batch_the_whole_pool(self) -> None:
        """Latency is the starved 2000, and 2000 is over the budget of 800."""
        self.assertEqual(latency(_SHEET), 2000)
        self.assertGreater(latency(_SHEET), _SHEET["chat_p95_budget_ms"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 3.

3. Open [scale.py](packet/app/scale.py). Search for `Start when the peak arrives.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/scale.py](work/app/scale.py) is under the Replace heading for this file.

```text
"""Start when the peak arrives.

This is the starter. started returns peak_at from the
forecast as text. A missing peak_at becomes an empty
string. The sheet is discarded.
"""


def started(forecast: dict, sheet: dict) -> str:
    """Return the peak time unchanged. Ignore the sheet.

    peak_at is turned into a string. When it is missing,
    the result is an empty string.
    """
    # The sheet is unused. The peak is returned as given.
    del sheet
    return str(forecast.get("peak_at") or "")
```

That was a picture. Do not paste it. The next item is number 4.

4. Open [test_scale.py](packet/tests/test_scale.py). Search for `test_the_shell_starts_at_the_peak`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_scale.py](work/tests/test_scale.py) is under the Replace heading for this file.

```text
"""Tests for the starter scale.

The forecast peak is 2024-06-11T04:15:00+03:00. The sheet
cold start is 15 seconds. These tests lock the starter:
the result equals the peak itself.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from scale import started

# The peak the starter returns as the start time.
_FORECAST = {"peak_at": "2024-06-11T04:15:00+03:00"}
# A cold start of 15 seconds. The starter does not apply it.
_SHEET = {"cold_start_seconds": 15}


class ScaleTests(unittest.TestCase):
    """The peak timestamp the starter returns unchanged."""

    def test_the_shell_starts_at_the_peak(self) -> None:
        """The result is the peak timestamp. The cold start on the sheet is unused."""
        self.assertEqual(started(_FORECAST, _SHEET), _FORECAST["peak_at"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 5.

5. Open [price.py](packet/app/price.py). Search for `Price the batch at yesterday's external rate.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/price.py](work/app/price.py) is under the Replace heading for this file.

```text
"""Price the batch at yesterday's external rate.

This is the starter. rate returns price.ext_large_per_1k
from the yesterday record, as an integer. The today
record is discarded.
"""


def rate(today: dict, yesterday: dict) -> int:
    """Return yesterday's external price as an integer. Ignore today.

    today is part of the signature so both records can be
    passed in. It is not read.
    """
    # The today record is not the price this module reports.
    del today
    return int(yesterday["price.ext_large_per_1k"])
```

That was a picture. Do not paste it. The next item is number 6.

6. Open [test_price.py](packet/tests/test_price.py). Search for `test_the_shell_uses_yesterday`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_price.py](work/tests/test_price.py) is under the Replace heading for this file.

```text
"""Tests for the starter price.

Today's record holds sar. Yesterday's record holds
price.ext_large_per_1k. These tests lock the starter:
the result is yesterday's price.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from price import rate

# Today's sar. The starter does not return it.
_TODAY = {"sar": 41}
# The external price the starter returns.
_YESTERDAY = {"price.ext_large_per_1k": 17}


class PriceTests(unittest.TestCase):
    """The yesterday price the starter returns."""

    def test_the_shell_uses_yesterday(self) -> None:
        """The result is 17, the price on the yesterday record."""
        self.assertEqual(rate(_TODAY, _YESTERDAY), 17)


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 7.

7. Open [capacity.py](packet/app/capacity.py). Search for `Leave the price and the backlog off the table.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/capacity.py](work/app/capacity.py) is under the Replace heading for this file.

```text
"""Leave the price and the backlog off the table.

This is the starter. table copies chat_p95 and
tokens_per_second. get is used, so a missing field
becomes None. Every other field on the plan is left
off. That is how the price and the backlog stay off
this table.
"""


def table(plan: dict) -> dict:
    """Return chat latency and tokens per second. Leave every other field off.

    A missing chat_p95 or tokens_per_second is stored as None.
    """
    # Price and backlog are not copied onto this table.
    return {
        "chat_p95": plan.get("chat_p95"),
        "tokens_per_second": plan.get("tokens_per_second"),
    }
```

That was a picture. Do not paste it. The next item is number 8.

8. Open [test_capacity.py](packet/tests/test_capacity.py). Search for `test_the_shell_omits_the_price_and_the_backlog`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_capacity.py](work/tests/test_capacity.py) is under the Replace heading for this file.

```text
"""Tests for the starter capacity table.

The plan holds chat_p95, hours, sar, and tokens_per_second.
These tests lock the starter: sar and hours are absent,
tokens_per_second stays 100, and chat_p95 stays 200.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from capacity import table

# The plan has four fields. The starter copies two of them.
_PLAN = {"chat_p95": 200, "hours": 33.3333, "sar": 41, "tokens_per_second": 100}


class CapacityTests(unittest.TestCase):
    """The two fields the starter keeps, and the two it drops."""

    def test_the_shell_omits_the_price_and_the_backlog(self) -> None:
        """sar and hours are absent. tokens_per_second is 100 and chat_p95 is 200.

        It calls table, then checks that sar and hours are left out and the kept fields stay.
        """
        got = table(_PLAN)
        self.assertNotIn("sar", got)
        self.assertNotIn("hours", got)
        self.assertEqual(got["tokens_per_second"], 100)
        self.assertEqual(got["chat_p95"], 200)


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

That was a picture. Do not paste it.

You are done reading. Do not paste any block above this line. The next heading is How the replacement works. Read it. It is not a paste. The first paste is the heading Replace the quota.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

Chat and the batch share one pool. Four functions keep the chat reserve, the cold start, today's price, and the table the readout will show.

`latency` returns the reserved chat latency from the sheet, the figure that holds when a chat reserve remains. The starved latency is on the same sheet and is not the result. The shell returned the starved number because the batch had taken the whole pool.

`started` reads the peak time and the cold-start seconds and moves the start earlier by that many seconds. Scaling only after the peak has already begun misses those seconds. The shell started at the peak.

`rate` returns today's `sar` and discards yesterday's record. Yesterday's key can still be `price.ext_large_per_1k`. It is not today's price. The shell priced the batch at yesterday's rate.

`table` copies four fields the other functions already computed: tokens per second, SAR, chat latency, and hours. It does not recompute them. A plan that is missing one field is not a capacity table.

Before you paste, say why the start time is earlier than the peak, and which price record is ignored.

This section adds no file and no command.

## Replace the quota

This block replaces [work/app/quota.py](work/app/quota.py). The full path is `Module 04/Lesson 03/Student_Copy/work/app/quota.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/quota.py](work/app/quota.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Keep a chat reserve on the shared pool.`.

```text
"""Keep a chat reserve on the shared pool.

latency returns chat_p95_reserved_ms from the sheet.
That is the latency kept when a chat reserve remains
on the pool. No other key on the sheet is read.
"""

from __future__ import annotations


def latency(sheet: dict) -> int:
    """Return the reserved chat latency from the sheet, as an integer."""
    # The reserve is the latency this module reports.
    return int(sheet["chat_p95_reserved_ms"])
```

Open [work/app/quota.py](work/app/quota.py). You should see `Keep a chat reserve on the shared pool.`. You should not see `Give the batch the whole pool.`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the quota test.

## Replace the quota test

This block replaces [work/tests/test_quota.py](work/tests/test_quota.py). The full path is `Module 04/Lesson 03/Student_Copy/work/tests/test_quota.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/tests/test_quota.py](work/tests/test_quota.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_a_chat_reserve_stays_inside_the_budget`.

```text
"""Tests for the finished chat reserve.

The sheet holds a budget, a reserved latency, and a
starved latency. The result should be the reserved
latency, and that figure should be at or under the budget.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from quota import latency

# Budget, reserved latency, and starved latency.
_SHEET = {"chat_p95_budget_ms": 800, "chat_p95_reserved_ms": 200, "chat_p95_starved_ms": 2000}


class QuotaTests(unittest.TestCase):
    """The reserved latency against the chat budget."""

    def test_a_chat_reserve_stays_inside_the_budget(self) -> None:
        """Latency is the reserved 200, and 200 is at or under the budget of 800."""
        self.assertEqual(latency(_SHEET), 200)
        self.assertLessEqual(latency(_SHEET), _SHEET["chat_p95_budget_ms"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

Open [work/tests/test_quota.py](work/tests/test_quota.py). You should see `test_a_chat_reserve_stays_inside_the_budget`. You should not see `test_the_shell_gives_the_batch_the_whole_pool`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the scale.

## Replace the scale

This block replaces [work/app/scale.py](work/app/scale.py). The full path is `Module 04/Lesson 03/Student_Copy/work/app/scale.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/scale.py](work/app/scale.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Start one cold start before the peak.`.

```text
"""Start one cold start before the peak.

started reads peak_at from the forecast and
cold_start_seconds from the sheet. It moves the peak
earlier by that many seconds and returns the new time
with isoformat.
"""

from __future__ import annotations

from datetime import datetime, timedelta


def started(forecast: dict, sheet: dict) -> str:
    """Return the peak time minus the cold-start seconds.

    peak_at is parsed as a date and time. cold_start_seconds
    is a whole number of seconds. The return value is isoformat.
    """
    peak = datetime.fromisoformat(str(forecast["peak_at"]))
    cold = int(sheet["cold_start_seconds"])
    # Lead the peak by the cold start on the sheet.
    return (peak - timedelta(seconds=cold)).isoformat()
```

Open [work/app/scale.py](work/app/scale.py). You should see `Start one cold start before the peak.`. You should not see `Start when the peak arrives.`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the scale test.

## Replace the scale test

This block replaces [work/tests/test_scale.py](work/tests/test_scale.py). The full path is `Module 04/Lesson 03/Student_Copy/work/tests/test_scale.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/tests/test_scale.py](work/tests/test_scale.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_the_start_leads_the_peak_by_the_cold_start`.

```text
"""Tests for the finished cold start.

The forecast peak is 2024-06-11T04:15:00+03:00. The sheet
cold start is 15 seconds. The start should equal that
peak minus 15 seconds, and that earlier time should not
equal the peak.
"""

import sys
import unittest
from datetime import datetime, timedelta
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from scale import started

# The peak timestamp the cold start is subtracted from.
_FORECAST = {"peak_at": "2024-06-11T04:15:00+03:00"}
# The cold start, in seconds.
_SHEET = {"cold_start_seconds": 15}


class ScaleTests(unittest.TestCase):
    """The peak time minus the cold start on the sheet."""

    def test_the_start_leads_the_peak_by_the_cold_start(self) -> None:
        """started matches the peak minus 15 seconds, and that time is not the peak.

        It takes the peak minus the cold start, then checks that
        started returns that earlier time, not the peak.
        """
        peak = datetime.fromisoformat(_FORECAST["peak_at"])
        expect = (peak - timedelta(seconds=15)).isoformat()
        self.assertEqual(started(_FORECAST, _SHEET), expect)
        self.assertNotEqual(expect, _FORECAST["peak_at"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

Open [work/tests/test_scale.py](work/tests/test_scale.py). You should see `test_the_start_leads_the_peak_by_the_cold_start`. You should not see `test_the_shell_starts_at_the_peak`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the price.

## Replace the price

This block replaces [work/app/price.py](work/app/price.py). The full path is `Module 04/Lesson 03/Student_Copy/work/app/price.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/price.py](work/app/price.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Price the batch at today's external rate.`.

```text
"""Price the batch at today's external rate.

rate returns the sar figure on the today record, as an
integer. The yesterday record is discarded, so the older
price is not the result.
"""

from __future__ import annotations


def rate(today: dict, yesterday: dict) -> int:
    """Return today's sar as an integer. Ignore yesterday.

    yesterday is part of the signature so both records can
    be passed in. It is not read.
    """
    # The older record is not the price reported here.
    del yesterday
    return int(today["sar"])
```

Open [work/app/price.py](work/app/price.py). You should see `Price the batch at today's external rate.`. You should not see `Price the batch at yesterday's external rate.`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the price test.

## Replace the price test

This block replaces [work/tests/test_price.py](work/tests/test_price.py). The full path is `Module 04/Lesson 03/Student_Copy/work/tests/test_price.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/tests/test_price.py](work/tests/test_price.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_today_replaces_yesterday`.

```text
"""Tests for the finished price.

Today's record holds sar. Yesterday's record holds
price.ext_large_per_1k. The rate should be today's sar,
and that value should be greater than yesterday's price.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from price import rate

# The sar figure the rate should return.
_TODAY = {"sar": 41}
# The older external price. It must not win.
_YESTERDAY = {"price.ext_large_per_1k": 17}


class PriceTests(unittest.TestCase):
    """Today's sar compared with yesterday's price."""

    def test_today_replaces_yesterday(self) -> None:
        """The result is 41, today's sar, and it is above yesterday's price."""
        self.assertEqual(rate(_TODAY, _YESTERDAY), 41)
        self.assertGreater(rate(_TODAY, _YESTERDAY), _YESTERDAY["price.ext_large_per_1k"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

Open [work/tests/test_price.py](work/tests/test_price.py). You should see `test_today_replaces_yesterday`. You should not see `test_the_shell_uses_yesterday`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the capacity module.

## Replace the capacity module

This block replaces [work/app/capacity.py](work/app/capacity.py). The full path is `Module 04/Lesson 03/Student_Copy/work/app/capacity.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/capacity.py](work/app/capacity.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Record tokens per second, SAR, chat latency, and hours.`.

```text
"""Record tokens per second, SAR, chat latency, and hours.

table copies four fields off the plan: tokens_per_second,
sar, chat_p95, and hours. It does not recompute them.
Each field is read by name, so the plan must already
carry all four.
"""

from __future__ import annotations


def table(plan: dict) -> dict:
    """Copy tokens_per_second, sar, chat_p95, and hours off the plan.

    The values are stored under those same keys. Nothing
    is calculated here.
    """
    # Price, hours, chat latency, and throughput stay together.
    return {
        "chat_p95": plan["chat_p95"],
        "hours": plan["hours"],
        "sar": plan["sar"],
        "tokens_per_second": plan["tokens_per_second"],
    }
```

Open [work/app/capacity.py](work/app/capacity.py). You should see `Record tokens per second, SAR, chat latency, and hours.`. You should not see `Leave the price and the backlog off the table.`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the capacity module test.

## Replace the capacity module test

This block replaces [work/tests/test_capacity.py](work/tests/test_capacity.py). The full path is `Module 04/Lesson 03/Student_Copy/work/tests/test_capacity.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/tests/test_capacity.py](work/tests/test_capacity.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_the_table_records_the_price_and_the_hours`.

```text
"""Tests for the finished capacity table.

The plan holds chat_p95, hours, sar, and tokens_per_second.
The table should come back equal to that whole plan, so
none of the four fields is dropped.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from capacity import table

# Chat latency, hours, sar, and tokens per second.
_PLAN = {"chat_p95": 200, "hours": 33.3333, "sar": 41, "tokens_per_second": 100}


class CapacityTests(unittest.TestCase):
    """The plan fields the finished table keeps."""

    def test_the_table_records_the_price_and_the_hours(self) -> None:
        """The table equals the plan, including sar and hours."""
        self.assertEqual(table(_PLAN), _PLAN)


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

Open [work/tests/test_capacity.py](work/tests/test_capacity.py). You should see `test_the_table_records_the_price_and_the_hours`. You should not see `test_the_shell_omits_the_price_and_the_backlog`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. That was the last paste on this page. The next heading is Search before the suite. Finish that heading before you run the suite.

## Search before the suite

Do this before you run the suite. A picture that was pasted fails the middle column.

This table is not a paste. Do not copy it into a file. Search each work file, not this chapter. A pasted picture fails the search. The string in the middle column is only in the replaced app file. It is not in the filled test for that module. A correct paste may still contain an old name on a different line.

| Work file | Search for this | You should not see |
| --- | --- | --- |
| [adapters.py](work/app/adapters.py) | `Serve every approved adapter on one process.` | `Serve ext-large and the lookalike.` |
| [batch.py](work/app/batch.py) | `Report the batched rate and the hours it needs.` | `Report the unbatched rate.` |
| [route.py](work/app/route.py) | `Keep a phi row on its local adapter.` | `Send every call to ext-large.` |
| [public.py](work/app/public.py) | `Return a cached public answer without a model call.` | `Call the model for a cached public answer.` |
| [quota.py](work/app/quota.py) | `Keep a chat reserve on the shared pool.` | `Give the batch the whole pool.` |
| [scale.py](work/app/scale.py) | `Start one cold start before the peak.` | `Start when the peak arrives.` |
| [price.py](work/app/price.py) | `Price the batch at today's external rate.` | `Price the batch at yesterday's external rate.` |
| [capacity.py](work/app/capacity.py) | `Record tokens per second, SAR, chat latency, and hours.` | `Leave the price and the backlog off the table.` |

The filled capacity module still says SAR where the table records today's price. That is expected. The shell sentence `Leave the price and the backlog off the table` must be gone. If you still see that shell sentence, you pasted the picture.

If a row fails, go back to the chapter that replaces that file and paste that block again. Do not edit a test. A traceback names a test file. The app file is the same name without `test_`. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

## Run the suite

Open a new terminal in the course folder. The demo window is still inside `problem_simulation`. Do not use that window for the suite. If the `cd` line says the path cannot be found, this window is still inside `problem_simulation`. Open a new terminal in the course folder and run both lines.

```text
cd "Module 04/Lesson 03/Student_Copy/work"
python -m unittest discover -s tests -q
```

You should see a line that starts with `Ran 9 tests`, then a blank line, then `OK`.

If the line says `FAILED`, the app and the tests in this folder do not match. A traceback names a test file. The app file is the same name without `test_`. Paste that pair again. Do not repair the spaces by hand.

The suite does not read the pages, and it does not read the workflow. A suite that prints `OK` can still fail [chapter 09](09-finish.md).

This page is done when the search table matches and the suite has printed `Ran 9 tests` and `OK`. Do not run a check from this page.

Next: [08 — The pages](08-the-pages.md).

