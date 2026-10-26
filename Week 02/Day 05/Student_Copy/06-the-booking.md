# 06 — The booking

[Chapter 05](05-the-sprint.md) sequenced the sprint. This chapter replaces the booking, the nightly file, and the notice. The smoke files are copied and not replaced.

You replace six files under `work/`, in this order:

1. [queue.py](work/app/queue.py), under Replace the booking
2. [test_queue.py](work/tests/test_queue.py), under Replace the booking test
3. [file_ain.py](work/app/file_ain.py), under Replace the file
4. [test_file.py](work/tests/test_file.py), under Replace the file test
5. [notify.py](work/app/notify.py), under Replace the notice
6. [test_notify.py](work/tests/test_notify.py), under Replace the notice test

Paste only those six blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged.

Scroll down to the heading Replace the booking. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. Five more Replace headings follow it. Use the four steps from [chapter 05](05-the-sprint.md) on each one. Everything above that first Replace heading is a picture or a check. You do not paste it.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, run `prepare_work.py` from the course folder and paste this chapter again from the chapter source. Do not repair the spaces by hand.

Do not run the suite on this page. The suite command is in [chapter 07](07-the-contract.md). It is not a check. The checks are only in [chapter 10](10-finish.md).

## The smoke files stay

Chapter 01 copied these files. You do not edit them on this page. Open [admit.py](work/app/admit.py) and search inside that file, not inside this chapter. Press Ctrl+F there and type `return "rejected"`. If you find it, the smoke copy is in place. Leave the file. The other rows are the same kind of check. Open one only if a later check names that file.

If `return "rejected"` is missing, run `prepare_work.py` from the course folder. That restores the smoke files. It also puts the blank sprint back, so paste [chapter 05](05-the-sprint.md) again before you paste the blocks on this page. If the search succeeds, leave `prepare_work.py` alone.

| Work file | Search for this | You should find it |
| --- | --- | --- |
| [admit.py](work/app/admit.py) | `return "rejected"` | Yes. Root is already rejected |
| [health.py](work/app/health.py) | `approved["hash"]` | Yes. The probe already reports the approved row |
| [router.py](work/app/router.py) | `ep-local-small` | Yes. The route is already private |
| [secrets.py](work/app/secrets.py) | `prod.json` | Yes. Prod already reads the prod file |
| [Dockerfile](work/deploy/Dockerfile) | `USER 1000` | Yes. The image account is already not root |
| [deployment.yaml](work/deploy/deployment.yaml) | `ns-team` | Yes. The manifest is already in the team namespace |
| [ci.yml](work/.github/workflows/ci.yml) | `unittest` | Yes. The workflow already runs the suite |

The same strings are in the packet copies. That is expected. Today those files match.

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the comment at the top of each one. Do not edit them. The first block you copy is under Replace the booking, further down this page.

1. [queue.py](packet/app/queue.py). Search for `return "booked"`. That line is the shell. Every hospital is booked. The next block is a picture of that file. Do not paste it.

```text
"""Book a slot at every hospital.

This is the shell. Chapter 06 replaces the copy under work/app.
Leave this file in the packet unchanged.

book ignores the facility and the fault. It returns booked for
every call. While this shell is the file that runs, the journey
check says a live slot was promised.
"""

from __future__ import annotations


def book(facility_id: str, fault: str = "") -> str:
    """Return booked and ignore every argument.

    facility_id is the hospital. fault is empty for a normal
    booking, or live-slot for the fault. Neither is used. Ain
    is booked the same way as every other hospital.
    """
    del facility_id, fault
    return "booked"
```

2. [file_ain.py](packet/app/file_ain.py). Search for `return None`. That line is the shell. A missing night clears the schedule. The next block is a picture of that file. Do not paste it.

```text
"""Replace the schedule even when the night file is missing.

This is the shell. Chapter 06 replaces the copy under work/app.
Leave this file in the packet unchanged.

apply_file drops yesterday. A missing night returns None. While
this shell is the file that runs, the journey check says a missed
night cleared the slots.
"""

from __future__ import annotations


def apply_file(previous: dict | None, arrived: dict | None) -> dict | None:
    """Drop yesterday and keep only a file that arrived.

    previous is the file already held. arrived is the night drop.
    None means the night did not arrive. previous is ignored. A
    missing night clears the schedule.
    """
    del previous
    if arrived is None:
        return None
    return arrived
```

3. [notify.py](packet/app/notify.py). Search for `return "booked"`. That line is the shell. A failed notice confirms a slot. The next block is a picture of that file. Do not paste it.

```text
"""Confirm a slot when the notice fails.

This is the shell. Chapter 06 replaces the copy under work/app.
Leave this file in the packet unchanged.

notify returns booked when the notice was not sent. While this
shell is the file that runs, the journey check says a failed
notice confirmed a slot.
"""

from __future__ import annotations


def notify(status: str, sent: bool) -> str:
    """Confirm a slot when the notice fails.

    status is the booking state. sent is whether the notice left.
    A failed notice returns booked. A notice that was sent returns
    the status it was given.
    """
    if not sent:
        return "booked"
    return status
```

4. [test_queue.py](packet/tests/test_queue.py). Search for `test_ain_books_a_slot`. The shell test expects Ain to be booked. Do not paste that file into `work/`.
5. [test_file.py](packet/tests/test_file.py). Search for `test_missing_file_clears_the_schedule`. Do not paste that file into `work/`.
6. [test_notify.py](packet/tests/test_notify.py). Search for `test_failed_notice_confirms_a_slot`. Do not paste that file into `work/`.

The journey check says `a live slot was promised` when the shell booking is the file that runs. It says `a missed night cleared the slots` when the shell file is the file that runs. It says `a failed notice confirmed a slot` when the shell notice is the file that runs. None of those messages names a clinic code.

## Replace the booking

This block replaces [work/app/queue.py](work/app/queue.py). The full path is `Week 02/Day 05/Student_Copy/work/app/queue.py`. It does not replace [packet/app/queue.py](packet/app/queue.py). It does not replace the test.

Open the work file. The path must contain `Student_Copy\work`. Select the whole file. Delete it. Copy the lines inside the block below. Do not copy the backtick lines. Paste. Save.

```text
"""Queue a booking at Ain until the nightly file arrives.

Chapter 06 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell returns booked for every hospital. While that shell is
the file that runs, the journey check says a live slot was promised.
"""

from __future__ import annotations


def book(facility_id: str, fault: str = "") -> str:
    """Queue Ain, and book only a live-slot fault or another hospital.

    facility_id is the hospital. h-ain waits for the nightly file.
    fault is empty for a normal booking. live-slot is the fault
    that must not be confirmed. Any other hospital is booked.
    """
    # Ain without the live-slot fault stays queued for the nightly file.
    if facility_id == "h-ain" and fault != "live-slot":
        return "queued"
    # A live-slot fault, and any facility that is not h-ain, is booked.
    return "booked"
```

Read the file back. You should see `return "queued"`. You should also see `return "booked"` on the next line. That line is the live-slot fault, and it is also the line for a facility that is not `h-ain`. That is expected. The packet copy still contains `return "booked"` as its only return. That is expected.

## Replace the booking test

This block replaces [work/tests/test_queue.py](work/tests/test_queue.py). It does not replace [packet/tests/test_queue.py](packet/tests/test_queue.py). Use the same steps on the work file.

```text
"""Work tests. Chapter 06 replaces the copy under work/tests.

Leave the packet shell unchanged. Ain stays queued. The live-slot
fault is still booked. A hospital that is not Ain is booked.

The fixture is the hospital id and, on one call, the live-slot
fault. There is no pack file.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from queue import book


class QueueTests(unittest.TestCase):
    """Ain stays queued unless the live-slot fault is set. Another hospital is booked."""

    def test_ain_stays_queued(self) -> None:
        """Ain waits. The live-slot fault and another hospital do not.

        The first assertion proves Ain with an empty fault stays
        queued. The next assertion is the live-slot fault, and it
        is booked. The last assertion proves a hospital that is not
        Ain is booked.
        """
        self.assertEqual(book("h-ain", ""), "queued")
        # booked on this line is the live-slot fault. That is expected.
        self.assertEqual(book("h-ain", "live-slot"), "booked")
        self.assertEqual(book("h-wadi", ""), "booked")


if __name__ == "__main__":
    unittest.main()
```

Read the file back. You should see `test_ain_stays_queued`. The line for the live-slot fault still says `booked`. That is expected. The line `parents[1]` stays as it is. It points at the `app` folder beside `tests`.

## Replace the file

This block replaces [work/app/file_ain.py](work/app/file_ain.py). It does not replace [packet/app/file_ain.py](packet/app/file_ain.py). Use the same steps on the work file.

```text
"""Keep yesterday's file when the night drop is missing.

Chapter 06 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell returns None when the night file is missing. While that
shell is the file that runs, the journey check says a missed night
cleared the slots.
"""

from __future__ import annotations


def apply_file(previous: dict | None, arrived: dict | None) -> dict | None:
    """Keep yesterday when the night file is missing.

    previous is the file already held. arrived is the file that
    landed tonight. None means the night drop did not arrive.
    A missing night returns previous. A file that arrived replaces it.
    """
    # A missed night leaves yesterday in place.
    if arrived is None:
        return previous
    # The last file wins. Today's file replaces yesterday.
    return arrived
```

Read the file back. You should see `return previous`. The type line can still say `None`. That is expected. You should also see `return arrived`. That is the line that replaces yesterday when a file arrives. The packet copy still returns `None` for a missing night. That is expected.

## Replace the file test

This block replaces [work/tests/test_file.py](work/tests/test_file.py). It does not replace [packet/tests/test_file.py](packet/tests/test_file.py). Use the same steps on the work file.

```text
"""Work tests. Chapter 06 replaces the copy under work/tests.

Leave the packet shell unchanged. A missing night keeps yesterday.
A file that arrives replaces it.

The fixture is a previous schedule whose day is yesterday. None
stands in for a night file that did not arrive. A later call passes
a file whose day is today.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from file_ain import apply_file


class FileTests(unittest.TestCase):
    """A missing night keeps the previous schedule, and an arrived file replaces it."""

    def test_missing_file_keeps_yesterday(self) -> None:
        """None for the night drop keeps the previous file.

        The first assertion proves a missing night returns the same
        previous schedule. The later assertion proves a file that
        arrives replaces that schedule with the arrived day.
        """
        previous = {"day": "yesterday"}
        self.assertEqual(apply_file(previous, None), previous)
        self.assertEqual(apply_file(previous, {"day": "today"}), {"day": "today"})


if __name__ == "__main__":
    unittest.main()
```

Read the file back. You should see `test_missing_file_keeps_yesterday`. The call still passes `None` as the night file. That is expected. `None` here means the night did not arrive.

## Replace the notice

This block replaces [work/app/notify.py](work/app/notify.py). It does not replace [packet/app/notify.py](packet/app/notify.py). Use the same steps on the work file.

```text
"""Leave a queued booking queued when the notice fails.

Chapter 06 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell returns booked when the notice was not sent. While that
shell is the file that runs, the journey check says a failed notice
confirmed a slot.
"""

from __future__ import annotations


def notify(status: str, sent: bool) -> str:
    """Leave a queued booking queued whether or not the notice was sent.

    status is the booking state. sent is whether the notice left.
    A queued booking stays queued. sent is not used. Any other
    status is returned as it arrived.
    """
    del sent
    # A failed notice does not turn a queue into a confirmed slot.
    if status == "queued":
        return "queued"
    return status
```

Read the file back. You should see `return "queued"`. The argument `sent` is still on the function line, and the body says `del sent`. That is expected. A failed notice does not change a queued booking.

## Replace the notice test

This block replaces [work/tests/test_notify.py](work/tests/test_notify.py). It does not replace [packet/tests/test_notify.py](packet/tests/test_notify.py). Use the same steps on the work file.

```text
"""Work tests. Chapter 06 replaces the copy under work/tests.

Leave the packet shell unchanged. A failed notice stays queued.
A notice that was sent stays queued too.

The fixture is the word queued. sent is false on the first call
and true on the later call. Both results have to stay queued.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from notify import notify


class NotifyTests(unittest.TestCase):
    """A queued notice stays queued whether or not it was sent."""

    def test_failed_notice_stays_queued(self) -> None:
        """queued stays queued when sent is false and when it is true.

        The first assertion proves a failed notice stays queued.
        The later assertion proves a notice that was sent stays
        queued too.
        """
        self.assertEqual(notify("queued", False), "queued")
        self.assertEqual(notify("queued", True), "queued")


if __name__ == "__main__":
    unittest.main()
```

Read the file back. You should see `test_failed_notice_stays_queued`. Both calls pass `queued`. One passes `False` for the notice. That is the failed notice.

This page is done when `work/app/queue.py` contains `return "queued"`, `work/app/file_ain.py` contains `return previous`, and `work/app/notify.py` contains `return "queued"`. The packet copies still contain `return "booked"` and `return None`. That is expected. Do not run a command on this page. Do not run the check until [chapter 10](10-finish.md).

Next: [07 — The contract](07-the-contract.md).
