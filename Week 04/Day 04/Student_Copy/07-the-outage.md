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

Paste only those eight blocks. The numbers in that list are the pastes. The numbers under Read these files are a different list. Those are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged.

The shell test is a picture. The filled test is the paste. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

You are reading until the heading Replace the breaker. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. The four steps from chapter 05 are repeated above each paste. The section How the replacement works sits above the first Replace heading. Read it. Do not paste it. Every code block above that Replace heading is a picture. You do not paste a picture. If the code block in front of you is above Replace the breaker, it is a picture. Do not paste it. If you are lost after that heading, stay on the Replace heading you have open. Finish it. Then do the next Replace heading down the page. Do not go back to the pictures. Do not run the suite until the heading Run the suite.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, paste that block again from this chapter file. Do not repair the spaces by hand. Run `prepare_work.py` again only when a failure row in [chapter 09](09-finish.md) says so. A second run puts the shell tests back.

The check runs in chapter 09. Do not run it from this page. The suite runs at the bottom of this page, after these eight pastes.

The rows in these tests are a small fixture. They are not the pack rows. Do not copy a price from the shares file onto a test. Do not copy a week count or a date from the lead-time file onto a test.

## Read these files

You are reading. You are not pasting yet. These numbers are not the paste list at the top of the page. Open these in the packet. Read the first line of each one. Do not edit them. The next block under a number is a picture of that file. Do not paste it. This block replaces nothing. An item is done when the search finds the shell sentence in the packet file. Close that file. Then do the next number.

1. Open [breaker.py](packet/app/breaker.py). Search for `Wait on insure until the request times out.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/breaker.py](work/app/breaker.py) is under the Replace heading for this file.

```text
"""Wait on insure until the request times out.

This is the starter. book does not branch. The breaker
stays closed, called stays true, and waited is
timeout_seconds. When timeout_seconds is missing,
waited is 0. The target is the partner, or insure when
the partner is missing.
"""


def book(outage: dict) -> dict:
    """Call the partner and wait out the timeout. Leave the breaker closed.

    A missing partner becomes insure. A missing timeout
    becomes 0.
    """
    # Always call. The breaker stays closed and the wait is the timeout.
    return {
        "breaker": "closed",
        "called": True,
        "target": str(outage.get("partner") or "insure"),
        "waited": int(outage.get("timeout_seconds") or 0),
    }
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 2.

2. Open [test_breaker.py](packet/tests/test_breaker.py). Search for `test_the_shell_waits_on_insure`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_breaker.py](work/tests/test_breaker.py) is under the Replace heading for this file.

```text
"""Tests for the starter breaker.

The partner is insure, status is down, and the timeout
is 40 seconds. These tests lock the starter: the target
is insure, the wait is above 0, and the call was made.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from breaker import book

# insure is down and the timeout is 40 seconds.
_OUTAGE = {"partner": "insure", "status": "down", "timeout_seconds": 40}


class BreakerTests(unittest.TestCase):
    """The closed breaker the starter keeps on this outage."""

    def test_the_shell_waits_on_insure(self) -> None:
        """The target is insure, waited is above 0, and called is true.

        It calls book, then checks the target, the wait, and the call.
        """
        got = book(_OUTAGE)
        self.assertEqual(got["target"], "insure")
        self.assertGreater(got["waited"], 0)
        self.assertTrue(got["called"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 3.

3. Open [degrade.py](packet/app/degrade.py). Search for `Fail the reply when the model is down.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/degrade.py](work/app/degrade.py) is under the Replace heading for this file.

```text
"""Fail the reply when the model is down.

This is the starter. When the model is up, the body is
the row text and the mode is model. A missing text
becomes an empty string. When the model is down, the
body is empty and the mode is error. The down path
does not read the row.
"""


def reply(row: dict, model_up: bool) -> dict:
    """Use the model when it is up. Otherwise return an empty error.

    Every down call looks the same: an empty body and mode error.
    """
    # Up uses the row text. Down does not read the row.
    if model_up:
        return {"body": str(row.get("text") or ""), "mode": "model"}
    return {"body": "", "mode": "error"}
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 4.

4. Open [test_degrade.py](packet/tests/test_degrade.py). Search for `test_the_shell_fails_closed`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_degrade.py](work/tests/test_degrade.py) is under the Replace heading for this file.

```text
"""Tests for the starter degrade path.

One row is status. The other is booking. With the model
down, these tests lock the starter: both rows come back
as mode error.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from degrade import reply

# A status row. The starter still returns mode error.
_STATUS = {"id": "status-1", "kind": "status", "text": "The referral is still pending."}
# A booking row. It gets the same mode as the status row.
_BOOK = {"id": "book-1", "kind": "booking", "text": "Offer a slot."}


class DegradeTests(unittest.TestCase):
    """Both rows when the model is down."""

    def test_the_shell_fails_closed(self) -> None:
        """Both the status row and the booking row are mode error when the model is down."""
        self.assertEqual(reply(_STATUS, False)["mode"], "error")
        self.assertEqual(reply(_BOOK, False)["mode"], "error")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 5.

5. Open [procure.py](packet/app/procure.py). Search for `Buy the GPUs.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/procure.py](work/app/procure.py) is under the Replace heading for this file.

```text
"""Buy the GPUs.

This is the starter. The note is discarded. choice
always returns buy.
"""


def choice(note: dict) -> str:
    """Ignore the note. Return buy."""
    # The note is unused.
    del note
    return "buy"
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 6.

6. Open [test_procure.py](packet/tests/test_procure.py). Search for `test_the_shell_buys`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_procure.py](work/tests/test_procure.py) is under the Replace heading for this file.

```text
"""Tests for the starter procurement choice.

_LATE is ordered on 2027-02-03, deadline 2027-02-08,
with purchase_weeks 16 and rent_days 2. _SOON has
deadline 2027-06-01 and purchase_weeks 1. These tests
lock the starter: both notes return buy.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from procure import choice

# A near deadline and a long purchase. The starter still buys.
_LATE = {"deadline": "2027-02-08", "ordered_on": "2027-02-03", "purchase_weeks": 16, "rent_days": 2}
# A deadline the purchase can meet. The starter also buys.
_SOON = {"deadline": "2027-06-01", "ordered_on": "2027-02-03", "purchase_weeks": 1, "rent_days": 2}


class ProcureTests(unittest.TestCase):
    """Both notes, and the buy result the starter always returns."""

    def test_the_shell_buys(self) -> None:
        """Both the late note and the soon note return buy."""
        self.assertEqual(choice(_LATE), "buy")
        self.assertEqual(choice(_SOON), "buy")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 7.

7. Open [hospitals.py](packet/app/hospitals.py). Search for `Bill every hospital the full backlog.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/hospitals.py](work/app/hospitals.py) is under the Replace heading for this file.

```text
"""Bill every hospital the full backlog.

This is the starter. The amount is backlog_referrals
times tokens_per_referral times price_per_1k, using
integer division by 1000. That same amount is stored
for every hospital in shares. Only the hospital name
is taken from each share.
"""


def split(sheet: dict, price_per_1k: int) -> dict[str, int]:
    """Give every hospital the same full-backlog amount.

    The amount is the backlog times tokens per referral
    times the price, with integer division by 1000. Only
    the hospital name is read from each share.
    """
    tokens = int(sheet["tokens_per_referral"])
    # One full-backlog figure, repeated for each hospital name.
    full = int(sheet["backlog_referrals"]) * tokens * int(price_per_1k) // 1000
    return {str(row["hospital"]): full for row in sheet["shares"]}
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 8.

8. Open [test_hospitals.py](packet/tests/test_hospitals.py). Search for `test_the_shell_bills_the_full_backlog_everywhere`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_hospitals.py](work/tests/test_hospitals.py) is under the Replace heading for this file.

```text
"""Tests for the starter hospital split.

The backlog is 12000. Tokens per referral is 1000. The
price argument is 4. Four hospitals list their own
counts. These tests lock the starter: every hospital
is billed 48000.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from hospitals import split

# The full backlog and four hospital rows with their own counts.
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
    """The single full-backlog amount the starter repeats."""

    def test_the_shell_bills_the_full_backlog_everywhere(self) -> None:
        """Every hospital is billed 48000, so the set of amounts is that one value."""
        got = split(_SHEET, 4)
        self.assertEqual(set(got.values()), {48000})


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The shell test is a picture. The filled test is the paste.

You are done reading. Do not paste any block above this line. If you are lost, you are still in the pictures. The next heading is How the replacement works. Read it. It is not a paste. The first paste is the heading Replace the breaker. Do not scroll back up to paste a picture.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

Insurance is a partner, not a third site. A purchase is a date, not a preference.

`book` opens the breaker when status is `down`. Called is false, waited is 0, and the target is `rules-worker`. The partner is not called, so the booking does not sit until the timeout. Any other status leaves the breaker closed and calls the partner. The shell waited on `insure` until the request died.

`reply` uses the model when the model is up, even for a status row. When the model is down and the kind is status, the mode is status and the body is still the row text. Any other kind, with the model down, goes to `rules-worker` and does not pretend the model answered. Status still works. Booking does not wait.

`choice` adds `purchase_weeks` to the order date and `rent_days` as days. Buy wins when the purchase date is on or before the deadline. When the purchase misses and the rental still meets the deadline, the result is rent. If the rental also misses, the result is buy. The shell bought every note, including the one that cannot arrive before Ramadan.

`split` bills each hospital from the referrals on its own share row. The shell billed the full backlog to every hospital.

Before you paste, say what the patient can still do when the model is down, and when rent wins.

This section adds no file and no command.

## Replace the breaker

This block replaces [work/app/breaker.py](work/app/breaker.py). The full path is `Week 04/Day 04/Student_Copy/work/app/breaker.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/breaker.py](work/app/breaker.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Open the breaker and leave the partner uncalled.`.

```text
"""Open the breaker and leave the partner uncalled.

book reads status. When status is down, the breaker is
open, called is false, the target is rules-worker, and
waited is 0. The partner name is not used on that path.
Any other status, including a missing status, leaves the
breaker closed, sets called to true, and uses the partner
name. A missing partner becomes an empty string. waited
is 0 on that path too.
"""


def book(outage: dict) -> dict:
    """Open the breaker when status is down. Otherwise call the partner.

    The down path targets rules-worker and does not call
    the partner. The other path targets the partner.
    waited is 0 either way.
    """
    # A down partner is not called.
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
"""Tests for the finished breaker.

The partner is insure, status is down, and the timeout
is 40 seconds. The breaker should be open, waited should
be 0, called should be false, and the target should not
be insure.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from breaker import book

# insure is down, with a timeout of 40 seconds.
_OUTAGE = {"partner": "insure", "status": "down", "timeout_seconds": 40}


class BreakerTests(unittest.TestCase):
    """An open breaker while insure is down."""

    def test_the_breaker_opens_and_insure_is_not_called(self) -> None:
        """The breaker is open, waited is 0, and the partner was not called.

        called is false. The target is not insure.
        """
        got = book(_OUTAGE)
        self.assertEqual(got["breaker"], "open")
        self.assertEqual(got["waited"], 0)
        self.assertFalse(got["called"])
        self.assertNotEqual(got["target"], "insure")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
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
"""Keep status available when the model is down.

reply reads the row text. A missing text becomes an
empty string. When the model is up, the mode is model
and the body is that text. When the model is down and
kind is status, the mode is status and the body is still
that text. Any other kind, with the model down, returns
the body rules-worker and the mode rules-worker.
"""


def reply(row: dict, model_up: bool) -> dict:
    """Prefer the model. Then a status body. Otherwise rules-worker.

    The model branch runs first, so a status row still uses
    the model when the model is up. The status branch keeps
    the row text. The last branch does not use the row text.
    """
    text = str(row.get("text") or "")
    # The model is up, so the row is served as a model reply.
    if model_up:
        return {"body": text, "mode": "model"}
    # Status can be served from the row while the model is down.
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
"""Tests for the finished degrade path.

One row is status. The other is booking. With the model
down, the status row stays in status mode and keeps its
text, and the booking row uses rules-worker. With the
model up, the status row uses the model.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from degrade import reply

# A status row. Its text should survive a down model.
_STATUS = {"id": "status-1", "kind": "status", "text": "The referral is still pending."}
# A booking row. A down model sends it to rules-worker.
_BOOK = {"id": "book-1", "kind": "booking", "text": "Offer a slot."}


class DegradeTests(unittest.TestCase):
    """Status, booking, and a model that is up or down."""

    def test_status_still_works_and_booking_uses_the_rules_worker(self) -> None:
        """A down model still serves status, and booking uses rules-worker.

        The status body stays the row text. An up model reports
        mode model.
        """
        status = reply(_STATUS, False)
        self.assertEqual(status["mode"], "status")
        self.assertEqual(status["body"], _STATUS["text"])
        self.assertEqual(reply(_BOOK, False)["mode"], "rules-worker")
        self.assertEqual(reply(_STATUS, True)["mode"], "model")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
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
"""Rent when a purchase misses the deadline.

choice reads ordered_on, deadline, purchase_weeks, and
rent_days. The purchase date is ordered_on plus
purchase_weeks. The rental date is ordered_on plus
rent_days. When the purchase date is on or before the
deadline, the choice is buy. When the purchase misses
and the rental date is on or before the deadline, the
choice is rent. When both miss, the choice is buy.
"""

from __future__ import annotations

from datetime import date, timedelta


def choice(note: dict) -> str:
    """Return buy when the purchase fits, otherwise rent when the rental fits.

    purchase_weeks is added as weeks. rent_days is added
    as days. If the rental also misses the deadline, the
    result is buy.
    """
    start = date.fromisoformat(str(note["ordered_on"]))
    deadline = date.fromisoformat(str(note["deadline"]))
    bought = start + timedelta(weeks=int(note["purchase_weeks"]))
    rented = start + timedelta(days=int(note["rent_days"]))
    # Buy when the purchase date meets the deadline.
    if bought <= deadline:
        return "buy"
    # The purchase is late. Rent if the rental still meets it.
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
"""Tests for the finished procurement choice.

_LATE is ordered on 2027-02-03, deadline 2027-02-08,
with purchase_weeks 16 and rent_days 2. _SOON keeps
that order date and rent_days, with deadline 2027-06-01
and purchase_weeks 1. The late note should rent. The
note that fits should buy.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from procure import choice

# Order date, a near deadline, a long purchase, and a short rental.
_LATE = {"deadline": "2027-02-08", "ordered_on": "2027-02-03", "purchase_weeks": 16, "rent_days": 2}
# The same order date, with a deadline the purchase can meet.
_SOON = {"deadline": "2027-06-01", "ordered_on": "2027-02-03", "purchase_weeks": 1, "rent_days": 2}


class ProcureTests(unittest.TestCase):
    """A purchase that misses, and a purchase that fits."""

    def test_rent_when_the_purchase_misses(self) -> None:
        """The late note, whose purchase misses the deadline, is rent."""
        self.assertEqual(choice(_LATE), "rent")

    def test_buy_when_the_purchase_fits(self) -> None:
        """The soon note, whose purchase fits the deadline, is buy."""
        self.assertEqual(choice(_SOON), "buy")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
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
"""Bill each hospital its own share of the backlog.

split walks the shares. For each row it multiplies that
row's referrals by tokens_per_referral and by price_per_1k,
then uses integer division by 1000. The key is the
hospital. Each hospital is billed from its own referrals.
"""


def split(sheet: dict, price_per_1k: int) -> dict[str, int]:
    """Bill every hospital from the referrals on its own share row.

    tokens_per_referral comes from the sheet and is shared.
    price_per_1k is the price argument. Integer division
    by 1000 finishes each amount.
    """
    # One token size for every row. The referral counts differ.
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
"""Tests for the finished hospital split.

The backlog is 12000 referrals. Tokens per referral is
1000. The price argument is 4. The four hospitals carry
their own referral counts. Each hospital should be billed
on its own count, and the amounts should not all match.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from hospitals import split

# Backlog, tokens per referral, and each hospital's own count.
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
    """A separate bill for each hospital share."""

    def test_each_share_is_billed_on_its_own(self) -> None:
        """h-nakhl is 8000, h-safra is 12000, h-wadi is 16000, and h-ain is 12000.

        Those amounts are not all the same value.
        """
        got = split(_SHEET, 4)
        self.assertEqual(got["h-nakhl"], 8000)
        self.assertEqual(got["h-safra"], 12000)
        self.assertEqual(got["h-wadi"], 16000)
        self.assertEqual(got["h-ain"], 12000)
        self.assertGreater(len(set(got.values())), 1)


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
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

The filled purchase module still returns buy when the purchase meets the deadline. That is expected. Search for the whole sentence `Buy the GPUs.` A search for the word buy is not that sentence. The shell sentence must be gone. If you still see `Buy the GPUs.`, you pasted the picture.

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
