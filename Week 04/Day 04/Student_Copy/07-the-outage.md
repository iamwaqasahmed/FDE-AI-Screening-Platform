# 07 — The outage

[Chapter 06](06-the-sites.md) replaced the sites. This chapter replaces four app files and the work copies of their four tests. You do eight pastes, in this order. Finish one before you start the next. Do the app file and its test before you start the next pair.

1. [breaker.py](work/app/breaker.py), under Replace the breaker
2. [test_breaker.py](work/tests/test_breaker.py), under Replace the breaker test
3. [degrade.py](work/app/degrade.py), under Replace the degradation
4. [test_degrade.py](work/tests/test_degrade.py), under Replace the degradation test
5. [procure.py](work/app/procure.py), under Replace the purchase
6. [test_procure.py](work/tests/test_procure.py), under Replace the purchase test
7. [hospitals.py](work/app/hospitals.py), under Replace the hospitals
8. [test_hospitals.py](work/tests/test_hospitals.py), under Replace the hospitals test

Paste only those eight blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged.

The shell test is a picture. The filled test is the paste. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

You are reading until the heading Replace the breaker. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. The four steps from chapter 05 are repeated above each paste. Everything above that first Replace heading is a picture. You do not paste it. If the block in front of you is above Replace the breaker, it is a picture. Do not paste it. If you are lost after that heading, stay on the Replace heading you have open. Finish it. Then do the next Replace heading down the page. Do not go back to the pictures. Do not run the suite until the heading Run the suite.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, paste that block again from this chapter file. Do not repair the spaces by hand. Run `prepare_work.py` again only when a failure row in [chapter 09](09-finish.md) says so. A second run puts the shell tests back.

The check runs in chapter 09. Do not run it from this page. The suite runs at the bottom of this page, after these eight pastes.

The rows in these tests are a small fixture. They are not the pack rows. Do not copy a price from the shares file onto a test. Do not copy a week count or a date from the lead-time file onto a test.

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the first line of each one. Do not edit them. The next block under a number is a picture of that file. Do not paste it. This block replaces nothing.

1. Open [breaker.py](packet/app/breaker.py). Search for `Wait on insure until the request times out.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/breaker.py](work/app/breaker.py) is under the Replace heading for this file.

```text
"""Wait on insure until the request times out."""


def book(outage: dict) -> dict:
    return {
        "breaker": "closed",
        "called": True,
        "target": str(outage.get("partner") or "insure"),
        "waited": int(outage.get("timeout_seconds") or 0),
    }
```

That was a picture. Do not paste it. The next item is number 2.

2. Open [test_breaker.py](packet/tests/test_breaker.py). Search for `test_the_shell_waits_on_insure`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_breaker.py](work/tests/test_breaker.py) is under the Replace heading for this file.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from breaker import book

_OUTAGE = {"partner": "insure", "status": "down", "timeout_seconds": 40}


class BreakerTests(unittest.TestCase):
    def test_the_shell_waits_on_insure(self) -> None:
        got = book(_OUTAGE)
        self.assertEqual(got["target"], "insure")
        self.assertGreater(got["waited"], 0)
        self.assertTrue(got["called"])


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 3.

3. Open [degrade.py](packet/app/degrade.py). Search for `Fail the reply when the model is down.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/degrade.py](work/app/degrade.py) is under the Replace heading for this file.

```text
"""Fail the reply when the model is down."""


def reply(row: dict, model_up: bool) -> dict:
    if model_up:
        return {"body": str(row.get("text") or ""), "mode": "model"}
    return {"body": "", "mode": "error"}
```

That was a picture. Do not paste it. The next item is number 4.

4. Open [test_degrade.py](packet/tests/test_degrade.py). Search for `test_the_shell_fails_closed`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_degrade.py](work/tests/test_degrade.py) is under the Replace heading for this file.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from degrade import reply

_STATUS = {"id": "status-1", "kind": "status", "text": "The referral is still pending."}
_BOOK = {"id": "book-1", "kind": "booking", "text": "Offer a slot."}


class DegradeTests(unittest.TestCase):
    def test_the_shell_fails_closed(self) -> None:
        self.assertEqual(reply(_STATUS, False)["mode"], "error")
        self.assertEqual(reply(_BOOK, False)["mode"], "error")


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 5.

5. Open [procure.py](packet/app/procure.py). Search for `Buy the GPUs.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/procure.py](work/app/procure.py) is under the Replace heading for this file.

```text
"""Buy the GPUs."""


def choice(note: dict) -> str:
    del note
    return "buy"
```

That was a picture. Do not paste it. The next item is number 6.

6. Open [test_procure.py](packet/tests/test_procure.py). Search for `test_the_shell_buys`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_procure.py](work/tests/test_procure.py) is under the Replace heading for this file.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from procure import choice

_LATE = {"deadline": "2027-02-08", "ordered_on": "2027-02-03", "purchase_weeks": 16, "rent_days": 2}
_SOON = {"deadline": "2027-06-01", "ordered_on": "2027-02-03", "purchase_weeks": 1, "rent_days": 2}


class ProcureTests(unittest.TestCase):
    def test_the_shell_buys(self) -> None:
        self.assertEqual(choice(_LATE), "buy")
        self.assertEqual(choice(_SOON), "buy")


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 7.

7. Open [hospitals.py](packet/app/hospitals.py). Search for `Bill every hospital the full backlog.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/hospitals.py](work/app/hospitals.py) is under the Replace heading for this file.

```text
"""Bill every hospital the full backlog."""


def split(sheet: dict, price_per_1k: int) -> dict[str, int]:
    tokens = int(sheet["tokens_per_referral"])
    full = int(sheet["backlog_referrals"]) * tokens * int(price_per_1k) // 1000
    return {str(row["hospital"]): full for row in sheet["shares"]}
```

That was a picture. Do not paste it. The next item is number 8.

8. Open [test_hospitals.py](packet/tests/test_hospitals.py). Search for `test_the_shell_bills_the_full_backlog_everywhere`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_hospitals.py](work/tests/test_hospitals.py) is under the Replace heading for this file.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from hospitals import split

_SHEET = {
    "backlog_referrals": 12000,
    "shares": [
        {"hospital": "h-nakhl", "referrals": 2000},
        {"hospital": "h-safra", "referrals": 3000},
        {"hospital": "h-wadi", "referrals": 4000},
        {"hospital": "h-ain", "referrals": 3000},
    ],
    "tokens_per_referral": 1000,
}


class HospitalTests(unittest.TestCase):
    def test_the_shell_bills_the_full_backlog_everywhere(self) -> None:
        got = split(_SHEET, 4)
        self.assertEqual(set(got.values()), {48000})


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. The shell test is a picture. The filled test is the paste.

You are done reading. Do not paste any block above this line. The next heading, Replace the breaker, is the first paste on this page.

## Replace the breaker

This block replaces [work/app/breaker.py](work/app/breaker.py). The full path is `Week 04/Day 04/Student_Copy/work/app/breaker.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/breaker.py](work/app/breaker.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Open the breaker and leave the partner uncalled.`.

```text
"""Open the breaker and leave the partner uncalled."""


def book(outage: dict) -> dict:
    if str(outage.get("status")) == "down":
        return {"breaker": "open", "called": False, "target": "rules-worker", "waited": 0}
    return {
        "breaker": "closed",
        "called": True,
        "target": str(outage.get("partner") or ""),
        "waited": 0,
    }
```

Open [work/app/breaker.py](work/app/breaker.py). You should see `Open the breaker and leave the partner uncalled.`. You should not see `Wait on insure until the request times out.`. If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the breaker test.

## Replace the breaker test

This block replaces [work/tests/test_breaker.py](work/tests/test_breaker.py). The full path is `Week 04/Day 04/Student_Copy/work/tests/test_breaker.py`. It does not replace the copy in `packet/`. The shell test is a picture. This block is the filled test.

1. Open the work file named here, [work/tests/test_breaker.py](work/tests/test_breaker.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_the_breaker_opens_and_insure_is_not_called`.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from breaker import book

_OUTAGE = {"partner": "insure", "status": "down", "timeout_seconds": 40}


class BreakerTests(unittest.TestCase):
    def test_the_breaker_opens_and_insure_is_not_called(self) -> None:
        got = book(_OUTAGE)
        self.assertEqual(got["breaker"], "open")
        self.assertEqual(got["waited"], 0)
        self.assertFalse(got["called"])
        self.assertNotEqual(got["target"], "insure")


if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_breaker.py](work/tests/test_breaker.py). You should see `test_the_breaker_opens_and_insure_is_not_called`. You should not see `test_the_shell_waits_on_insure`. If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the degradation.

## Replace the degradation

This block replaces [work/app/degrade.py](work/app/degrade.py). The full path is `Week 04/Day 04/Student_Copy/work/app/degrade.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/degrade.py](work/app/degrade.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Keep status available when the model is down.`.

```text
"""Keep status available when the model is down."""


def reply(row: dict, model_up: bool) -> dict:
    text = str(row.get("text") or "")
    if model_up:
        return {"body": text, "mode": "model"}
    if row.get("kind") == "status":
        return {"body": text, "mode": "status"}
    return {"body": "rules-worker", "mode": "rules-worker"}
```

Open [work/app/degrade.py](work/app/degrade.py). You should see `Keep status available when the model is down.`. You should not see `Fail the reply when the model is down.`. If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the degradation test.

## Replace the degradation test

This block replaces [work/tests/test_degrade.py](work/tests/test_degrade.py). The full path is `Week 04/Day 04/Student_Copy/work/tests/test_degrade.py`. It does not replace the copy in `packet/`. The shell test is a picture. This block is the filled test.

1. Open the work file named here, [work/tests/test_degrade.py](work/tests/test_degrade.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_status_still_works_and_booking_uses_the_rules_worker`.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from degrade import reply

_STATUS = {"id": "status-1", "kind": "status", "text": "The referral is still pending."}
_BOOK = {"id": "book-1", "kind": "booking", "text": "Offer a slot."}


class DegradeTests(unittest.TestCase):
    def test_status_still_works_and_booking_uses_the_rules_worker(self) -> None:
        status = reply(_STATUS, False)
        self.assertEqual(status["mode"], "status")
        self.assertEqual(status["body"], _STATUS["text"])
        self.assertEqual(reply(_BOOK, False)["mode"], "rules-worker")
        self.assertEqual(reply(_STATUS, True)["mode"], "model")


if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_degrade.py](work/tests/test_degrade.py). You should see `test_status_still_works_and_booking_uses_the_rules_worker`. You should not see `test_the_shell_fails_closed`. If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the purchase.

## Replace the purchase

This block replaces [work/app/procure.py](work/app/procure.py). The full path is `Week 04/Day 04/Student_Copy/work/app/procure.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/procure.py](work/app/procure.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Rent when a purchase misses the deadline.`.

```text
"""Rent when a purchase misses the deadline."""

from __future__ import annotations

from datetime import date, timedelta


def choice(note: dict) -> str:
    start = date.fromisoformat(str(note["ordered_on"]))
    deadline = date.fromisoformat(str(note["deadline"]))
    bought = start + timedelta(weeks=int(note["purchase_weeks"]))
    rented = start + timedelta(days=int(note["rent_days"]))
    if bought <= deadline:
        return "buy"
    if rented <= deadline:
        return "rent"
    return "buy"
```

Open [work/app/procure.py](work/app/procure.py). You should see `Rent when a purchase misses the deadline.`. You should not see `Buy the GPUs.`. If you still see that shell sentence, you pasted the picture. A correct paste still has a buy path for a purchase that meets the deadline. That is expected. The shell sentence `Buy the GPUs.` must be gone.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the purchase test.

## Replace the purchase test

This block replaces [work/tests/test_procure.py](work/tests/test_procure.py). The full path is `Week 04/Day 04/Student_Copy/work/tests/test_procure.py`. It does not replace the copy in `packet/`. The shell test is a picture. This block is the filled test.

1. Open the work file named here, [work/tests/test_procure.py](work/tests/test_procure.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_rent_when_the_purchase_misses`.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from procure import choice

_LATE = {"deadline": "2027-02-08", "ordered_on": "2027-02-03", "purchase_weeks": 16, "rent_days": 2}
_SOON = {"deadline": "2027-06-01", "ordered_on": "2027-02-03", "purchase_weeks": 1, "rent_days": 2}


class ProcureTests(unittest.TestCase):
    def test_rent_when_the_purchase_misses(self) -> None:
        self.assertEqual(choice(_LATE), "rent")

    def test_buy_when_the_purchase_fits(self) -> None:
        self.assertEqual(choice(_SOON), "buy")


if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_procure.py](work/tests/test_procure.py). You should see `test_rent_when_the_purchase_misses` and `test_buy_when_the_purchase_fits`. You should not see `test_the_shell_buys`. If you still see that shell sentence, you pasted the picture. The buy test is expected. It is the purchase that meets the deadline.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the hospitals.

## Replace the hospitals

This block replaces [work/app/hospitals.py](work/app/hospitals.py). The full path is `Week 04/Day 04/Student_Copy/work/app/hospitals.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/hospitals.py](work/app/hospitals.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Bill each hospital its own share of the backlog.`.

```text
"""Bill each hospital its own share of the backlog."""


def split(sheet: dict, price_per_1k: int) -> dict[str, int]:
    tokens = int(sheet["tokens_per_referral"])
    return {
        str(row["hospital"]): int(row["referrals"]) * tokens * int(price_per_1k) // 1000
        for row in sheet["shares"]
    }
```

Open [work/app/hospitals.py](work/app/hospitals.py). You should see `Bill each hospital its own share of the backlog.`. You should not see `Bill every hospital the full backlog.`. If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the hospitals test.

## Replace the hospitals test

This block replaces [work/tests/test_hospitals.py](work/tests/test_hospitals.py). The full path is `Week 04/Day 04/Student_Copy/work/tests/test_hospitals.py`. It does not replace the copy in `packet/`. The shell test is a picture. This block is the filled test.

1. Open the work file named here, [work/tests/test_hospitals.py](work/tests/test_hospitals.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_each_share_is_billed_on_its_own`.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from hospitals import split

_SHEET = {
    "backlog_referrals": 12000,
    "shares": [
        {"hospital": "h-nakhl", "referrals": 2000},
        {"hospital": "h-safra", "referrals": 3000},
        {"hospital": "h-wadi", "referrals": 4000},
        {"hospital": "h-ain", "referrals": 3000},
    ],
    "tokens_per_referral": 1000,
}


class HospitalTests(unittest.TestCase):
    def test_each_share_is_billed_on_its_own(self) -> None:
        got = split(_SHEET, 4)
        self.assertEqual(got["h-nakhl"], 8000)
        self.assertEqual(got["h-safra"], 12000)
        self.assertEqual(got["h-wadi"], 16000)
        self.assertEqual(got["h-ain"], 12000)
        self.assertGreater(len(set(got.values())), 1)


if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_hospitals.py](work/tests/test_hospitals.py). You should see `test_each_share_is_billed_on_its_own`. You should not see `test_the_shell_bills_the_full_backlog_everywhere`. If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. That was the last paste on this page. The next heading is Search before the suite. Finish that heading before you run the suite.

## Search before the suite

Do this before you run the suite. A picture that was pasted fails the middle column.

This table is not a paste. Do not copy it into a file. Search each work file, not this chapter. A pasted picture fails the search. The string in the middle column is only in the replaced app file. It is not in the filled test for that module. A correct paste may still contain an old name on a different line.

| Work file | Search for this | You should not see |
| --- | --- | --- |
| [replicas.py](work/app/replicas.py) | `Place every replica behind the balancer.` | `Place traffic on site-a only.` |
| [route.py](work/app/route.py) | `Send new traffic to a replica that is still healthy.` | `Keep sending to site-a after it fails health.` |
| [failover.py](work/app/failover.py) | `Resume in-flight approvals from the workflow store.` | `Rebuild from the dead pod.` |
| [hashes.py](work/app/hashes.py) | `Keep a hash only when it matches the register.` | `Accept every hash the site advertises.` |
| [breaker.py](work/app/breaker.py) | `Open the breaker and leave the partner uncalled.` | `Wait on insure until the request times out.` |
| [degrade.py](work/app/degrade.py) | `Keep status available when the model is down.` | `Fail the reply when the model is down.` |
| [procure.py](work/app/procure.py) | `Rent when a purchase misses the deadline.` | `Buy the GPUs.` |
| [hospitals.py](work/app/hospitals.py) | `Bill each hospital its own share of the backlog.` | `Bill every hospital the full backlog.` |

The filled purchase module still returns buy when the purchase meets the deadline. That is expected. The shell sentence `Buy the GPUs.` must be gone. If you still see that shell sentence, you pasted the picture.

If a row fails, go back to the chapter that replaces that file and paste that block again. Do not edit a test. A traceback names a test file. The app file is the same name without `test_`. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

## Run the suite

Open a new terminal in the course folder. The demo window is still inside `problem_simulation`. Do not use that window for the suite. If the `cd` line says the path cannot be found, this window is still inside `problem_simulation`. Open a new terminal in the course folder and run both lines. Do not skip that `cd` and run the suite inside `problem_simulation`.

```text
cd "Week 04/Day 04/Student_Copy/work"
python -m unittest discover -s tests -q
```

You should see a line that starts with `Ran 9 tests`, then a blank line, then `OK`.

If the line says `FAILED`, the app and the tests in this folder do not match. A traceback names a test file. The app file is the same name without `test_`. Paste that pair again. Do not repair the spaces by hand.

The suite does not read the pages, and it does not read the workflow. A suite that prints `OK` can still fail [chapter 09](09-finish.md).

This page is done when the search table matches and the suite has printed `Ran 9 tests` and `OK`. Do not run a check from this page.

Next: [08 — The pages](08-the-pages.md).
