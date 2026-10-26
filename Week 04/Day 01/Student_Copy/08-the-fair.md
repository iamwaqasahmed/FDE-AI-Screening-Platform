# 08 — The fair measure

[Chapter 07](07-the-request.md) replaced access and deletion. This chapter does two pastes, then a search, then the suite. Finish one before you start the next.

1. [fair.py](work/app/fair.py), under Replace the fair measure
2. [test_fair.py](work/tests/test_fair.py), under Replace the fair test
3. The search table. It is not a paste
4. The suite

Paste only those two blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged.

The shell test is a picture. The filled test is the paste. You are reading until the heading Replace the fair measure. It is the first heading on this page that starts with Replace. Everything above that heading is a picture. If you are lost after that heading, stay on the Replace heading you have open. Finish it. Then do the next Replace heading. Do not go back to the pictures.

These files are Python. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, open a terminal in the course folder and run `python "Week 04/Day 01/Student_Copy/prepare_work.py"`. Then paste chapters 05 through 08 again from the chapter source. Do not repair the spaces by hand.

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the comment at the top of each one. Do not edit them.

1. Open [fair.py](packet/app/fair.py). Search for `Report no gap and no stamp rate`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/fair.py](work/app/fair.py) is under the Replace heading for this file.

```text
"""Report no gap and no stamp rate.

gap and stamp_rate both discard the rows they are given and return
zero. Nothing on the row changes either result.
"""

from __future__ import annotations


def gap(rows: list[dict]) -> float:
    """Return zero for any rows.

    del drops the local name. The rows are not read.
    """
    del rows
    return 0.0


def stamp_rate(rows: list[dict]) -> float:
    """Return zero for any rows.

    No field is read. An empty list and a full list match.
    """
    del rows
    return 0.0
```

2. Open [test_fair.py](packet/tests/test_fair.py). Search for `test_the_gap_is_zero`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_fair.py](work/tests/test_fair.py) is under the Replace heading for this file.

```text
"""Tests for a gap and a stamp rate that are both zero.

The decision fixture and the stamp fixture are passed in. Both
results are expected to be zero no matter what the rows contain.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from fair import gap, stamp_rate

# A yes in one district and insurance class, and a no in the other.
_ROWS = [
    {"decision": "yes", "district": "d-nakhl", "insurance": "class-a"},
    {"decision": "no", "district": "d-rim", "insurance": "class-b"},
]
# One stamped row and one row that is not stamped.
_STAMPS = [{"stamped": True}, {"stamped": False}]


class FairTests(unittest.TestCase):
    """Check that neither fixture moves the result off zero."""

    def test_the_gap_is_zero(self) -> None:
        """gap returns zero for the decision fixture.

        The yes and no decisions are in the fixture. They do not change
        the result. The assertion is zero.
        """
        self.assertEqual(gap(_ROWS), 0.0)

    def test_the_stamp_rate_is_zero(self) -> None:
        """stamp_rate returns zero for the stamp fixture.

        One row is stamped and one is not. The assertion is still zero.
        """
        self.assertEqual(stamp_rate(_STAMPS), 0.0)


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
```

You are done reading. The next heading, Replace the fair measure, is the first paste on this page.

## Replace the fair measure

This block replaces [work/app/fair.py](work/app/fair.py). The full path is `Week 04/Day 01/Student_Copy/work/app/fair.py`. It does not replace the copy in `packet/app`. The disparity is the spread across district and insurance class. The stamp rate is the share of stamped rows. Read the rows in [outcomes.jsonl](packet/release/fairness/outcomes.jsonl) and [approvals.jsonl](packet/release/fairness/approvals.jsonl). Read the bound in [bound.json](packet/release/fairness/bound.json). Do not copy a rate or the bound onto a page.

1. Open the work file named here, [work/app/fair.py](work/app/fair.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `setdefault`.

```text
"""Disparity by district and insurance class, and the Thursday stamp rate.

gap is the wider yes-rate spread across district and across insurance.
A yes decision is the decision text yes. For each key, rows are grouped
and each group's rate is the share of yes decisions. The spread is the
highest rate minus the lowest. gap returns the larger spread. No rows,
or a key with no groups, contributes nothing, and no spreads at all
returns zero.

stamp_rate is the share of rows whose stamped field is true. An empty
list returns zero so the length is never used as a divisor.
"""

from __future__ import annotations


def _rates(rows: list[dict], key: str) -> list[float]:
    """Group rows by key and return the yes-rate of each group.

    Group order follows the first time each key value appears. The spread
    later uses the highest and lowest rates, so that order does not matter.
    """
    groups: dict[str, list[bool]] = {}
    for row in rows:
        # The row must have this key and a decision. Other decision text counts as no.
        groups.setdefault(row[key], []).append(row["decision"] == "yes")
    # Skip an empty group so the rate is never a division by an empty length.
    return [sum(flags) / len(flags) for flags in groups.values() if flags]


def gap(rows: list[dict]) -> float:
    """Return the wider yes-rate spread across district and insurance.

    Each spread is the highest group rate minus the lowest. The result is
    the larger of those spreads, or zero when neither key produced one.
    """
    spreads = []
    for key in ("district", "insurance"):
        rates = _rates(rows, key)
        # A key that formed no groups does not add a spread.
        if rates:
            spreads.append(max(rates) - min(rates))
    if not spreads:
        return 0.0
    return max(spreads)


def stamp_rate(rows: list[dict]) -> float:
    """Return the share of rows with a true stamped field.

    A missing stamped field counts as not stamped. An empty list returns zero.
    """
    # An empty list has no share. Return zero before dividing.
    if not rows:
        return 0.0
    return sum(1 for row in rows if row.get("stamped")) / len(rows)
```

Open [work/app/fair.py](work/app/fair.py). You should see `setdefault`. You should not see `Report no gap and no stamp rate`. If you still see that shell sentence, you pasted the picture. Stay on this page. The next heading is Replace the fair test.

## Replace the fair test

This block replaces [work/tests/test_fair.py](work/tests/test_fair.py). The full path is `Week 04/Day 01/Student_Copy/work/tests/test_fair.py`. It does not replace the copy in `packet/tests`. The rows in this test are a small fixture. They are not the pack rows.

1. Open the work file named here, [work/tests/test_fair.py](work/tests/test_fair.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_the_gap_is_the_spread_across_both_slices`.

```text
"""Tests for the disparity gap and the stamp share.

One fixture has a yes in one district and insurance class, and a no
in the other. The other fixture has one stamped row and one row that
is not stamped.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from fair import gap, stamp_rate

# A yes in one district and insurance class, and a no in the other.
_ROWS = [
    {"decision": "yes", "district": "d-nakhl", "insurance": "class-a"},
    {"decision": "no", "district": "d-rim", "insurance": "class-b"},
]
# One stamped row and one row that is not stamped.
_STAMPS = [{"stamped": True}, {"stamped": False}]


class FairTests(unittest.TestCase):
    """Check the gap on the decision rows and the share on the stamp rows."""

    def test_the_gap_is_the_spread_across_both_slices(self) -> None:
        """The gap on the decision fixture is the spread in the assertion.

        Each slice has a yes and a no, so the spread is the whole range
        from yes to no. The assertion is that spread.
        """
        self.assertEqual(gap(_ROWS), 1.0)

    def test_the_stamp_rate_is_the_thursday_share(self) -> None:
        """The stamp share of the stamp fixture is the value in the assertion.

        One row is stamped and one is not. The assertion is that share.
        """
        self.assertEqual(stamp_rate(_STAMPS), 0.5)


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_fair.py](work/tests/test_fair.py). You should see `test_the_gap_is_the_spread_across_both_slices`. You should not see `test_the_gap_is_zero`. If you still see that shell name, you pasted the picture. Stay on this page. The next heading is Search before the suite. That table is not a paste.

## Search before the suite

This table is not a paste. Do not copy it into a file. Search each work file, not this chapter. A pasted picture fails the search. The string in the middle column is only in the replaced app file. It is not in the filled test for that module. A correct paste may still contain an old name on a different line.

| Work file | Search for this | You should not see |
| --- | --- | --- |
| [guard.py](work/app/guard.py) | `unapproved action is held` | `A letter still books` |
| [output.py](work/app/output.py) | `html.escape` | `Leave model HTML as the model wrote it` |
| [supply.py](work/app/supply.py) | `IN_FORCE` | `Load the candidate hash and follow the tool text` |
| [redact.py](work/app/redact.py) | `[redacted]` | `Leave a log line as it was written` |
| [limit.py](work/app/limit.py) | `TOKEN_CAP` | `Allow the session and the holds` |
| [access.py](work/app/access.py) | `audit-` | `Leave every grant open` |
| [erase.py](work/app/erase.py) | `permitted logs` | `Delete the database row and leave the other stores` |
| [fair.py](work/app/fair.py) | `setdefault` | `Report no gap and no stamp rate` |

The filled guard still says `book` on the approved path. That is expected. The shell sentence `A letter still books` must be gone. If you still see the shell sentence, you pasted the picture.

If a row fails, go back to the chapter that replaces that file and paste that block again. Do not edit a test. A traceback names a test file. The app file is the same name without `test_`. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

## Run the suite

Open a new terminal in the course folder. The demo window is still inside `problem_simulation`. Do not use that window for the suite. If the `cd` line says the path cannot be found, this window is still inside `problem_simulation`. Open a new terminal in the course folder and run both lines.

```text
cd "Week 04/Day 01/Student_Copy/work"
python -m unittest discover -s tests -q
```

You should see a line that starts with `Ran 19 tests`, then a blank line, then `OK`.

`Ran 19 tests` also appears when the suite fails. The line under it has to be `OK`. One passing test does not finish the suite. A traceback names a test file. The app file is the same name without `test_`. Do not edit the test. Paste the block for that file again.

A suite that prints `OK` can still fail chapter 10. The suite does not read the pages, and it does not read the workflow.

This page is done when the suite prints `Ran 19 tests` and `OK`, and the eight searches pass.

Next: [09 — The pages](09-the-pages.md).
