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

You are reading until the heading Replace the quota. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. The four steps from chapter 05 are repeated above each paste. Everything above that first Replace heading is a picture. You do not paste it. If the block in front of you is above Replace the quota, it is a picture. Do not paste it. If you are lost after that heading, stay on the Replace heading you have open. Finish it. Then do the next Replace heading down the page. Do not go back to the pictures. Do not run the suite until the heading Run the suite.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, paste that block again from this chapter file. Do not repair the spaces by hand. Run `prepare_work.py` again only when a failure row in [chapter 09](09-finish.md) says so. A second run puts the shell tests back.

The checks run in chapter 09. Do not run them from this page. The suite runs at the bottom of this page, after these eight pastes.

The rows in these tests are a small fixture. They are not the pack rows. Do not copy a price from the release readme onto a test. Do not copy the peak time or the backlog count onto a test.

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the first line of each one. Do not edit them. The next block under a number is a picture of that file. Do not paste it. This block replaces nothing.

1. Open [quota.py](packet/app/quota.py). Search for `Give the batch the whole pool.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/quota.py](work/app/quota.py) is under the Replace heading for this file.

```text
"""Give the batch the whole pool."""


def latency(sheet: dict) -> int:
    return int(sheet["chat_p95_starved_ms"])
```

That was a picture. Do not paste it. The next item is number 2.

2. Open [test_quota.py](packet/tests/test_quota.py). Search for `test_the_shell_gives_the_batch_the_whole_pool`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_quota.py](work/tests/test_quota.py) is under the Replace heading for this file.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from quota import latency

_SHEET = {"chat_p95_budget_ms": 800, "chat_p95_reserved_ms": 200, "chat_p95_starved_ms": 2000}


class QuotaTests(unittest.TestCase):
    def test_the_shell_gives_the_batch_the_whole_pool(self) -> None:
        self.assertEqual(latency(_SHEET), 2000)
        self.assertGreater(latency(_SHEET), _SHEET["chat_p95_budget_ms"])


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 3.

3. Open [scale.py](packet/app/scale.py). Search for `Start when the peak arrives.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/scale.py](work/app/scale.py) is under the Replace heading for this file.

```text
"""Start when the peak arrives."""


def started(forecast: dict, sheet: dict) -> str:
    del sheet
    return str(forecast.get("peak_at") or "")
```

That was a picture. Do not paste it. The next item is number 4.

4. Open [test_scale.py](packet/tests/test_scale.py). Search for `test_the_shell_starts_at_the_peak`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_scale.py](work/tests/test_scale.py) is under the Replace heading for this file.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from scale import started

_FORECAST = {"peak_at": "2024-06-11T04:15:00+03:00"}
_SHEET = {"cold_start_seconds": 15}


class ScaleTests(unittest.TestCase):
    def test_the_shell_starts_at_the_peak(self) -> None:
        self.assertEqual(started(_FORECAST, _SHEET), _FORECAST["peak_at"])


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 5.

5. Open [price.py](packet/app/price.py). Search for `Price the batch at yesterday's external rate.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/price.py](work/app/price.py) is under the Replace heading for this file.

```text
"""Price the batch at yesterday's external rate."""


def rate(today: dict, yesterday: dict) -> int:
    del today
    return int(yesterday["price.ext_large_per_1k"])
```

That was a picture. Do not paste it. The next item is number 6.

6. Open [test_price.py](packet/tests/test_price.py). Search for `test_the_shell_uses_yesterday`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_price.py](work/tests/test_price.py) is under the Replace heading for this file.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from price import rate

_TODAY = {"sar": 41}
_YESTERDAY = {"price.ext_large_per_1k": 17}


class PriceTests(unittest.TestCase):
    def test_the_shell_uses_yesterday(self) -> None:
        self.assertEqual(rate(_TODAY, _YESTERDAY), 17)


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 7.

7. Open [capacity.py](packet/app/capacity.py). Search for `Leave the price and the backlog off the table.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/capacity.py](work/app/capacity.py) is under the Replace heading for this file.

```text
"""Leave the price and the backlog off the table."""


def table(plan: dict) -> dict:
    return {
        "chat_p95": plan.get("chat_p95"),
        "tokens_per_second": plan.get("tokens_per_second"),
    }
```

That was a picture. Do not paste it. The next item is number 8.

8. Open [test_capacity.py](packet/tests/test_capacity.py). Search for `test_the_shell_omits_the_price_and_the_backlog`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_capacity.py](work/tests/test_capacity.py) is under the Replace heading for this file.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from capacity import table

_PLAN = {"chat_p95": 200, "hours": 33.3333, "sar": 41, "tokens_per_second": 100}


class CapacityTests(unittest.TestCase):
    def test_the_shell_omits_the_price_and_the_backlog(self) -> None:
        got = table(_PLAN)
        self.assertNotIn("sar", got)
        self.assertNotIn("hours", got)
        self.assertEqual(got["tokens_per_second"], 100)
        self.assertEqual(got["chat_p95"], 200)


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it.

You are done reading. Do not paste any block above this line. The next heading, Replace the quota, is the first paste on this page.

## Replace the quota

This block replaces [work/app/quota.py](work/app/quota.py). The full path is `Week 04/Day 03/Student_Copy/work/app/quota.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/quota.py](work/app/quota.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Keep a chat reserve on the shared pool.`.

```text
"""Keep a chat reserve on the shared pool."""

from __future__ import annotations


def latency(sheet: dict) -> int:
    return int(sheet["chat_p95_reserved_ms"])
```

Open [work/app/quota.py](work/app/quota.py). You should see `Keep a chat reserve on the shared pool.`. You should not see `Give the batch the whole pool.`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the quota test.

## Replace the quota test

This block replaces [work/tests/test_quota.py](work/tests/test_quota.py). The full path is `Week 04/Day 03/Student_Copy/work/tests/test_quota.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/tests/test_quota.py](work/tests/test_quota.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_a_chat_reserve_stays_inside_the_budget`.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from quota import latency

_SHEET = {"chat_p95_budget_ms": 800, "chat_p95_reserved_ms": 200, "chat_p95_starved_ms": 2000}


class QuotaTests(unittest.TestCase):
    def test_a_chat_reserve_stays_inside_the_budget(self) -> None:
        self.assertEqual(latency(_SHEET), 200)
        self.assertLessEqual(latency(_SHEET), _SHEET["chat_p95_budget_ms"])


if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_quota.py](work/tests/test_quota.py). You should see `test_a_chat_reserve_stays_inside_the_budget`. You should not see `test_the_shell_gives_the_batch_the_whole_pool`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the scale.

## Replace the scale

This block replaces [work/app/scale.py](work/app/scale.py). The full path is `Week 04/Day 03/Student_Copy/work/app/scale.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/scale.py](work/app/scale.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Start one cold start before the peak.`.

```text
"""Start one cold start before the peak."""

from __future__ import annotations

from datetime import datetime, timedelta


def started(forecast: dict, sheet: dict) -> str:
    peak = datetime.fromisoformat(str(forecast["peak_at"]))
    cold = int(sheet["cold_start_seconds"])
    return (peak - timedelta(seconds=cold)).isoformat()
```

Open [work/app/scale.py](work/app/scale.py). You should see `Start one cold start before the peak.`. You should not see `Start when the peak arrives.`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the scale test.

## Replace the scale test

This block replaces [work/tests/test_scale.py](work/tests/test_scale.py). The full path is `Week 04/Day 03/Student_Copy/work/tests/test_scale.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/tests/test_scale.py](work/tests/test_scale.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_the_start_leads_the_peak_by_the_cold_start`.

```text
import sys
import unittest
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from scale import started

_FORECAST = {"peak_at": "2024-06-11T04:15:00+03:00"}
_SHEET = {"cold_start_seconds": 15}


class ScaleTests(unittest.TestCase):
    def test_the_start_leads_the_peak_by_the_cold_start(self) -> None:
        peak = datetime.fromisoformat(_FORECAST["peak_at"])
        expect = (peak - timedelta(seconds=15)).isoformat()
        self.assertEqual(started(_FORECAST, _SHEET), expect)
        self.assertNotEqual(expect, _FORECAST["peak_at"])


if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_scale.py](work/tests/test_scale.py). You should see `test_the_start_leads_the_peak_by_the_cold_start`. You should not see `test_the_shell_starts_at_the_peak`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the price.

## Replace the price

This block replaces [work/app/price.py](work/app/price.py). The full path is `Week 04/Day 03/Student_Copy/work/app/price.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/price.py](work/app/price.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Price the batch at today's external rate.`.

```text
"""Price the batch at today's external rate."""

from __future__ import annotations


def rate(today: dict, yesterday: dict) -> int:
    del yesterday
    return int(today["sar"])
```

Open [work/app/price.py](work/app/price.py). You should see `Price the batch at today's external rate.`. You should not see `Price the batch at yesterday's external rate.`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the price test.

## Replace the price test

This block replaces [work/tests/test_price.py](work/tests/test_price.py). The full path is `Week 04/Day 03/Student_Copy/work/tests/test_price.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/tests/test_price.py](work/tests/test_price.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_today_replaces_yesterday`.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from price import rate

_TODAY = {"sar": 41}
_YESTERDAY = {"price.ext_large_per_1k": 17}


class PriceTests(unittest.TestCase):
    def test_today_replaces_yesterday(self) -> None:
        self.assertEqual(rate(_TODAY, _YESTERDAY), 41)
        self.assertGreater(rate(_TODAY, _YESTERDAY), _YESTERDAY["price.ext_large_per_1k"])


if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_price.py](work/tests/test_price.py). You should see `test_today_replaces_yesterday`. You should not see `test_the_shell_uses_yesterday`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the capacity module.

## Replace the capacity module

This block replaces [work/app/capacity.py](work/app/capacity.py). The full path is `Week 04/Day 03/Student_Copy/work/app/capacity.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/capacity.py](work/app/capacity.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Record tokens per second, SAR, chat latency, and hours.`.

```text
"""Record tokens per second, SAR, chat latency, and hours."""

from __future__ import annotations


def table(plan: dict) -> dict:
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

This block replaces [work/tests/test_capacity.py](work/tests/test_capacity.py). The full path is `Week 04/Day 03/Student_Copy/work/tests/test_capacity.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/tests/test_capacity.py](work/tests/test_capacity.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_the_table_records_the_price_and_the_hours`.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from capacity import table

_PLAN = {"chat_p95": 200, "hours": 33.3333, "sar": 41, "tokens_per_second": 100}


class CapacityTests(unittest.TestCase):
    def test_the_table_records_the_price_and_the_hours(self) -> None:
        self.assertEqual(table(_PLAN), _PLAN)


if __name__ == "__main__":
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
cd "Week 04/Day 03/Student_Copy/work"
python -m unittest discover -s tests -q
```

You should see a line that starts with `Ran 9 tests`, then a blank line, then `OK`.

If the line says `FAILED`, the app and the tests in this folder do not match. A traceback names a test file. The app file is the same name without `test_`. Paste that pair again. Do not repair the spaces by hand.

The suite does not read the pages, and it does not read the workflow. A suite that prints `OK` can still fail [chapter 09](09-finish.md).

This page is done when the search table matches and the suite has printed `Ran 9 tests` and `OK`. Do not run a check from this page.

Next: [08 — The pages](08-the-pages.md).

