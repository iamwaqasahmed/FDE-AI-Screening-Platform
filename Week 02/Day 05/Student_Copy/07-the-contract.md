# 07 — The contract

[Chapter 06](06-the-booking.md) replaced the booking, the file, and the notice. This chapter replaces the contract and its test, then runs the suite. The suite is not a check. The checks are only in [chapter 10](10-finish.md).

You replace two files under `work/`, in this order:

1. [contract.py](work/app/contract.py), under Replace the contract
2. [test_contract.py](work/tests/test_contract.py), under Replace the contract test

Paste only those two blocks. The block under Read these files is a picture of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.

Scroll to the heading Replace the contract. The code block under it is the first paste. The next Replace heading is Replace the contract test. Use the four steps from [chapter 05](05-the-sprint.md) on both. Everything above Replace the contract is a picture.

These files are Python. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. If the terminal shows `SyntaxError` or `IndentationError`, run `prepare_work.py` from the course folder and paste chapters 06 and 07 again from the chapter source. Do not repair the spaces by hand.

## Read these files

Open [contract.py](packet/app/contract.py). Search for `return True`. That line is the shell. Every status is accepted, including `booked`. The next block is a picture of that file. Do not paste it.

```text
"""Accept every booking status.

This is the shell. Chapter 07 replaces the copy under work/app.
Leave this file in the packet unchanged.

holds returns True for every status, including booked. While this
shell is the file that runs, the individual check says the contract
test accepted the live-slot fault.
"""

from __future__ import annotations


def holds(status: str) -> bool:
    """Return True and ignore the status.

    status is the booking state. queued and booked are both
    accepted. The live-slot fault is booked.
    """
    del status
    return True
```

Open [test_contract.py](packet/tests/test_contract.py). Search for `holds`. The word `holds` is in the shell test and in the work test. The shell method is `test_live_slot_fixture_holds`. That method accepts `booked`. Do not paste the shell test into `work/`.

The individual check says `the contract test accepted the live-slot fault` when this shell is the file that runs. A queued booking has to stay green. The live-slot fault has to go red. The check reads [live-slot.json](packet/release/fixtures/live-slot.json) from the built pack. The test you paste does not open that file. It uses the word `booked`. The sentence inside the test, "There is no pack file," means the test has no file of its own. Do not copy the fixture into `work/` to resolve that sentence. A copy fails with `a watermarked sample is in the work directory`.

## Replace the contract

This block replaces [work/app/contract.py](work/app/contract.py). The full path is `Week 02/Day 05/Student_Copy/work/app/contract.py`. It does not replace [packet/app/contract.py](packet/app/contract.py). It does not replace the test.

Open the work file. Select the whole file. Delete it. Copy the lines inside the block below. Do not copy the backtick lines. Paste. Save.

```text
"""A booked status is the live-slot fault.

Chapter 07 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell returns True for every status. While that shell is the
file that runs, the individual check says the contract test accepted
the live-slot fault.
"""

from __future__ import annotations


def holds(status: str) -> bool:
    """Accept a queued booking and reject a booked status.

    status is the booking state. queued is the status that holds.
    booked is the live-slot fault. It does not hold.
    """
    # Only a queued booking keeps the contract. A booked status fails it.
    return status == "queued"
```

Read the file back. You should see `status == "queued"`. The word `booked` is in the comment above that line. That is expected. The packet copy still returns `True`. That is expected.

## Replace the contract test

This block replaces [work/tests/test_contract.py](work/tests/test_contract.py). It does not replace [packet/tests/test_contract.py](packet/tests/test_contract.py). Use the same steps on the work file.

```text
"""Work tests. Chapter 07 replaces the copy under work/tests.

Leave the packet shell unchanged. The word holds is in this file.
A queued booking stays green. The live-slot fault goes red.

Each test passes a status word straight to holds. There is no pack
file. queued must hold. booked must not.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from contract import holds


class ContractTests(unittest.TestCase):
    """The contract holds for a queued booking and fails for booked."""

    def test_queued_fixture_holds(self) -> None:
        """A queued booking keeps the contract.

        The fixture is the word queued. The assertion proves holds
        accepts that word.
        """
        # queued is the booking state this contract still accepts.
        self.assertTrue(holds("queued"))

    def test_live_slot_fault_fails_the_contract(self) -> None:
        """booked on this line is the live-slot fault. It does not hold.

        The fixture is the word booked. The assertion proves holds
        rejects that word.
        """
        # booked is the live-slot fault. The contract does not hold.
        self.assertFalse(holds("booked"))


if __name__ == "__main__":
    unittest.main()
```

Read the file back. You should see `holds`. You should see `test_queued_fixture_holds` and `test_live_slot_fault_fails_the_contract`. The second test still contains `booked` inside `assertFalse(holds("booked"))`. That is expected. `booked` on that line is the live-slot fault. The line `parents[1]` stays as it is.

## Search before the suite

These strings exist in the replaced work files. A pasted picture fails the search. Open the work file, not the packet file.

| Work file | Search for this | You should find it |
| --- | --- | --- |
| [queue.py](work/app/queue.py) | `return "queued"` | Yes. `return "booked"` is still on the next line. That is expected |
| [file_ain.py](work/app/file_ain.py) | `return previous` | Yes. The type line can still say `None`. That is expected |
| [notify.py](work/app/notify.py) | `return "queued"` | Yes |
| [contract.py](work/app/contract.py) | `status == "queued"` | Yes |
| [test_queue.py](work/tests/test_queue.py) | `test_ain_stays_queued` | Yes. The live-slot line still says `booked`. That is expected |
| [test_file.py](work/tests/test_file.py) | `test_missing_file_keeps_yesterday` | Yes |
| [test_notify.py](work/tests/test_notify.py) | `test_failed_notice_stays_queued` | Yes |
| [test_contract.py](work/tests/test_contract.py) | `test_live_slot_fault_fails_the_contract` | Yes. `holds` is also in the packet test. This method name is only in the work test |

If a row fails, you pasted a picture or you skipped that file. The queue, file, and notice rows are the blocks in [chapter 06](06-the-booking.md). The contract rows are the blocks above, under Replace the contract and Replace the contract test. Paste the failed row's block again from that chapter. Search the work file, not the packet file.

## Run the suite

Leave the window you used for the demo. That window is inside `problem_simulation`, and this command is not. Open a new terminal in the course folder, the same way as chapter 01. `dir` should list `problem_simulation` and `Week 02`. If chapter 01 told you to use `py`, use `py` here.

```text
cd "Week 02/Day 05/Student_Copy/work"
python -m unittest discover -s tests -q
```

If the `cd` line says the path cannot be found, this window is not the course folder. Open a new one and run both lines again. Do not chain `cd ..` to climb out of another folder.

You should see a line that starts with `Ran 11 tests`, then a blank line, then `OK`. The time on the `Ran` line can differ. There is no `FAIL` and no `ERROR`. The prompt returns after `OK`.

If the line says `Ran 10 tests`, the contract test is still the shell. Paste [test_contract.py](work/tests/test_contract.py) again from the block above, and paste [contract.py](work/app/contract.py) again. Then run the suite again.

If the terminal says `SyntaxError` or `IndentationError`, run this from the course folder:

```text
python "Week 02/Day 05/Student_Copy/prepare_work.py"
```

That puts the shells back. Paste chapters 05, 06, and 07 again from the chapter source. Then run the suite again.

The suite does not read the pages. A green suite can still fail the checks in chapter 10.

This page is done when the suite prints `Ran 11 tests` and `OK`, and `work/tests/test_contract.py` contains `test_live_slot_fault_fails_the_contract`. The packet contract still returns `True`. That is expected.

Next: [08 — The pages](08-the-pages.md).
