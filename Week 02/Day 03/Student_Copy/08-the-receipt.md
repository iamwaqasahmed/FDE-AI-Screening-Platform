# 08 — The receipt

[Chapter 07](07-the-reply.md) judged the reply by its fields. This chapter replaces the receipt and its test, then runs the suite.

You replace two files under `work/`: [receipt.py](work/app/receipt.py) and [test_receipt.py](work/tests/test_receipt.py). Leave the copies in `packet/` unchanged. Then you run the suite. The suite command on this page is `unittest`. It is not a check. A check prints `chk-w2-tests` or `chk-w2-ux`. Those two commands are only in [chapter 10](10-finish.md).

## Read these files

Open these in the packet. Read the comment at the top of each one. Do not edit them.

1. [receipt.py](packet/app/receipt.py). Search for `return "due"`. That line is the shell. Every receipt is due. The sent time, the clock, the minutes, and the switch are ignored.
2. [test_receipt.py](packet/tests/test_receipt.py). Search for `time.sleep`. The shell test waits on the wall clock, then expects due while the switch is on. The next block is a picture of that test. Do not paste it. Pasting it puts the wait back into `work/`. Keep reading. How the replacement works is not a paste. The first paste on this page is under Replace the receipt. That file is `receipt.py`. The test paste is under Replace the receipt test, after it. Do not jump to the test while `receipt.py` still returns due for every receipt.

```text
"""The shell receipt test. It waits, then expects every receipt to be due.

This is the shell. Chapter 08 replaces the copy under work/tests.
Leave this file in the packet unchanged.

The wait follows the wall clock. The tests check reads this file
as text. While time.sleep is in the file, the check says the receipt
test sleeps.
"""

import sys
import time
import unittest
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from receipt import receipt_state

OLD_SECONDS = 30


class ReceiptTests(unittest.TestCase):
    """The shell receipt test. It waits, then expects every receipt to be due."""
    def test_receipt_follows_the_wait(self) -> None:
        """Wait, then accept a due receipt while the switch is on.

        The shell app returns due for every call, so this passes
        after the wait. The case clock is not read. The switch is on
        and the result is still due. That is the fault.
        """
        time.sleep(OLD_SECONDS)
        sent = "2027-01-19T09:00:00"
        now = (datetime.fromisoformat(sent) + timedelta(seconds=OLD_SECONDS)).isoformat(timespec="seconds")
        self.assertEqual(receipt_state(sent, now, 0, True), "due")


if __name__ == "__main__":
    unittest.main()
```

3. [receipt.json](packet/release/clock/receipt.json). Search for `minutes`. The filled test reads that field. You do not type the number into the test. Search for `switch`. The value is `receipt-late`.
4. [ci.yml](work/.github/workflows/ci.yml). Search for `unittest`. You should see `tests` on that same command. The next block is a picture of that file. It is already in `work/`. Do not paste it into `receipt.py`, and do not paste it over `ci.yml`. Leave the file as it is.

```text
name: ci
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: tests
        run: python -m unittest discover -s tests -q
```

The tests check says `the receipt test sleeps` when the letters `sleep` appear anywhere in `receipt.py` or `test_receipt.py`. A comment that says not to sleep fails the same way. The message does not mean the suite is still waiting. It says `the suite accepted the receipt fault` when a late receipt is still due. It says `the receipt test does not match the clock` when the result does not follow the clock file. None of those messages names an interval or a delay.

The demo in [chapter 03](03-the-notice.md) already printed `switch off: passed` and `switch on: failed`. Those lines do not print `pending` or `due`. The test under Replace the receipt test does use those two words. That is expected. The demo and the test are different.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

`receipt_state` returns `pending` or `due`. The inputs are when the message was accepted, the pinned case clock, the minutes from the clock file, and the late switch. While the switch is on, the result stays `pending` even after the clock has moved. While the switch is off, the result is `due` only after the case clock has moved by those minutes. A clock that has not moved stays `pending`.

The shell slept on the wall clock and then expected every receipt to be due. A fixed sleep follows the wall clock. The receipt follows the case clock, and the switch can hold it. The replacement test reads the minutes from the clock file. It does not call `time.sleep`.

The clock guide says to advance the pinned time. That is the move this function is waiting for.

Before you paste, say what stays `pending` after the clock has moved, and which call must be absent from the test.

This section adds no file and no command.

## Replace the receipt

This block replaces [work/app/receipt.py](work/app/receipt.py). The full path is `Week 02/Day 03/Student_Copy/work/app/receipt.py`. It does not replace [packet/app/receipt.py](packet/app/receipt.py). It does not replace the test.

Open [work/app/receipt.py](work/app/receipt.py). That is the work copy. Do not paste into the packet copy.

1. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
2. Copy from this chapter file, not from a preview. A preview can drop the spaces.
3. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it.
4. Paste as plain text. The line `def receipt_state` starts at the left edge. The lines inside the function start with four spaces. Save.

If the terminal later shows `SyntaxError` or `IndentationError`, do not repair the spaces by hand. Run `prepare_work.py` again from the course folder, then paste the blocks from chapters 05, 06, 07, and this page again from the chapter files. Do not repair a Python file by hand.

```text
"""A receipt follows the case clock. The late switch keeps it pending.

Chapter 08 replaces the work copy with this file.
Leave the packet shell unchanged.

receipt_state returns pending while the switch is on. Otherwise it
returns due only after the case clock has moved by the minutes argument.
Do not wait on the wall clock. While the shell is the file that runs,
the tests check says the suite accepted the receipt fault.
"""

from __future__ import annotations

from datetime import datetime, timedelta


def receipt_state(sent_at: str, now: str, minutes: int, switch_on: bool) -> str:
    """Return pending or due from the case clock and the switch.

    sent_at is when the message was accepted. now is the pinned case
    clock. minutes comes from the clock file. switch_on holds the
    receipt pending after the clock has moved. A clock that has not
    moved far enough is still pending.
    """
    if switch_on:
        return "pending"
    sent = datetime.fromisoformat(sent_at)
    current = datetime.fromisoformat(now)
    if current >= sent + timedelta(minutes=minutes):
        return "due"
    return "pending"
```

Read the file back. You should see `pending` when the switch is on. You should see `due` only after the clock has moved. You should not see `time.sleep`.

## Replace the receipt test

This block replaces [work/tests/test_receipt.py](work/tests/test_receipt.py). It does not replace [packet/tests/test_receipt.py](packet/tests/test_receipt.py). Use the same four steps on the work file. Copy from this chapter file, not from a preview. Do not paste the picture from the top of this page.

```text
"""The receipt follows the case clock and the switch.

Chapter 08 replaces the work copy with this file.
Leave the packet shell unchanged.

The minutes value is read from the clock file. This file does not
wait on the wall clock. The same later time is pending while the
switch is on, and due when the switch is off.
"""

import json
import sys
import unittest
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from receipt import receipt_state

# parents[0] is tests. parents[1] is work. parents[2] is Student_Copy
# or Solution_Copy. parents[3] is Day 03. parents[4] is Week 02.
# parents[5] is the course folder. data/ sits there.
_ROOT = Path(__file__).resolve().parents[5]
_SENT = "2027-01-19T09:00:00"


class ReceiptTests(unittest.TestCase):
    """The receipt follows the case clock and the switch."""
    def test_clock_and_switch(self) -> None:
        """Pending at the sent time, due after the move, pending when the switch is on.

        minutes is the field in the clock file. span is that number.
        later is the sent time plus that many minutes on the case clock.
        The third call uses the same later time with the switch on.
        """
        minutes = json.loads((_ROOT / "data" / "rel-w2d3" / "clock" / "receipt.json").read_text(encoding="utf-8"))
        span = int(minutes["minutes"])
        later = (datetime.fromisoformat(_SENT) + timedelta(minutes=span)).isoformat(timespec="seconds")
        self.assertEqual(receipt_state(_SENT, _SENT, span, False), "pending")
        self.assertEqual(receipt_state(_SENT, later, span, False), "due")
        self.assertEqual(receipt_state(_SENT, later, span, True), "pending")


if __name__ == "__main__":
    unittest.main()
```

Read the file back. You should see three results, in this order: `pending`, `due`, `pending`. You should see `receipt.json` on the line that reads `minutes`. You should not see `time.sleep`. The shell's wait is gone. The third result is the switch. The demo's second line, `switch on: failed`, is that same fact printed without the word pending.

## Run the suite

Do this only after both files on this page are pasted, and after the calendar and the reply from chapters 06 and 07 are pasted. If the command sits with no output, the shell receipt test is still waiting. Press Ctrl+C. Paste the block under Replace the receipt test, then run the command again.

Open a new terminal in the course folder. Do not reuse the window that is inside `problem_simulation`. If the window is already inside `Week 02/Day 03/Student_Copy/work`, skip the `cd` line and run the python line. If chapter 01 told you to use `py`, use `py` here.

```text
cd "Week 02/Day 03/Student_Copy/work"
python -m unittest discover -s tests -q
```

You should see a line that starts with `Ran 6 tests`, then a blank line, then `OK`. A line of dashes can sit above `Ran`. The time on the `Ran` line can differ. There is no `FAIL` and no `ERROR`. That is the suite you want. This command is not the check. The workflow runs this same command. You already saw `unittest` and `tests` in `ci.yml`. Leave that file as it is.

If you see `The system cannot find the path specified` or `No such file or directory` on the `cd` line, this window is not the course folder. Open a new terminal in the course folder and run both lines. If the error names `data/rel-w1d3` or `data/rel-w2d3`, the paste can still be right and a pack is missing. Chapter 01 writes `data/rel-w2d3` only. Week 1 Day 3 writes `data/rel-w1d3`. From a terminal in the course folder, run `cd problem_simulation`, then `python -m alwaha.build --profile practice --release rel-w1d3` for the calendar, and `python -m alwaha.build --profile practice --release rel-w2d3` for today's cases, clock file, and fixture. Then run the suite again. Do not copy those files by hand. If the count is not 6, or you see `FAIL` or `ERROR`, a paste from chapter 06, chapter 07, or this page did not land. Do not repair the file by hand. Paste that chapter's block again from the chapter file. If you see `SyntaxError` or `IndentationError`, run `prepare_work.py` from the course folder and paste chapters 05, 06, 07, and this page again from the chapter files.

Do not run either check until [chapter 10](10-finish.md).

Next: [09 — The pages](09-the-pages.md).
