# 07 — The proposal

[Chapter 06](06-the-connections.md) replaced the connections. This chapter replaces three app files and the work copies of their three tests. You do six pastes, in this order. Finish one before you start the next. Do the app file and its test before you start the next pair.

1. [rank.py](work/app/rank.py), under Replace the ranking
2. [test_rank.py](work/tests/test_rank.py), under Replace the ranking test
3. [gates.py](work/app/gates.py), under Replace the gates
4. [test_gates.py](work/tests/test_gates.py), under Replace the gates test
5. [personal.py](work/app/personal.py), under Replace the personal lab
6. [test_personal.py](work/tests/test_personal.py), under Replace the personal lab test

Paste only those six blocks. The numbers in that list are the pastes. The numbers under Read these files are a different list. Those are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged.

The shell test is a picture. The filled test is the paste. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

You are reading until the heading Replace the ranking. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. The four steps from chapter 05 are repeated above each paste. The section How the replacement works sits above the first Replace heading. Read it. Do not paste it. Every code block above that Replace heading is a picture. You do not paste a picture. If the code block in front of you is above Replace the ranking, it is a picture. Do not paste it. If you are lost after that heading, stay on the Replace heading you have open. Finish it. Then do the next Replace heading down the page. Do not go back to the pictures. Do not run the suite until the heading Run the suite.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, paste that block again from this chapter file. Do not repair the spaces by hand. Run `prepare_work.py` again only when a failure row in [chapter 09](09-finish.md) says so. A second run puts the shell tests back.

The checks run in chapter 09. Do not run one from this page. The suite runs at the bottom of this page, after these six pastes.

The rows in these tests are a small fixture. They are not the pack rows. Do not copy the attack text onto a test.

## Read these files

You are reading. You are not pasting yet. These numbers are not the paste list at the top of the page. Open these in the packet. Read the first line of each one. Do not edit them. The next block under a number is a picture of that file. Do not paste it. This block replaces nothing. An item is done when the search finds the shell sentence in the packet file. Close that file. Then do the next number.

1. Open [rank.py](packet/app/rank.py). Search for `Put the blocked problem first.` That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/rank.py](work/app/rank.py) is under the Replace heading for this file.

```text
"""Put the blocked problem first.

This is the starter. It ignores the rows and always returns
p-triage. That problem still has a blocker, so it cannot open.
The finished module walks the rows and returns the first id
whose blocker list is empty.
"""


def first(rows: list) -> str:
    """Ignore the model and return the blocked problem.

    The rows are discarded. The caller always hears the same id.
    """
    # The argument is unused. Order and blockers are not read.
    del rows
    return "p-triage"
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 2.

2. Open [test_rank.py](packet/tests/test_rank.py). Search for `test_the_shell_starts_with_triage`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_rank.py](work/tests/test_rank.py) is under the Replace heading for this file.

```text
"""Tests for the starter ranking.

The shell ignores the rows and returns p-triage, the blocked problem.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from rank import first

# The first row is blocked. The second row is open. The shell ignores both.
_ROWS = [
    {"blockers": ["pol-clinical-safety"], "id": "p-triage"},
    {"blockers": [], "id": "p-clock"},
]


class RankTests(unittest.TestCase):
    """Tests for the starter ranking."""
    def test_the_shell_starts_with_triage(self) -> None:
        """The result is p-triage even though that row is blocked."""
        self.assertEqual(first(_ROWS), "p-triage")


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. This item is done when the search finds that shell name in the packet file. Close the packet file. The next item is number 3.

3. Open [gates.py](packet/app/gates.py). Search for `Leave the clinical safety cell empty and skip go-live.` That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/gates.py](work/app/gates.py) is under the Replace heading for this file.

```text
"""Leave the clinical safety cell empty and skip go-live.

This is the starter. It ignores the item. The cell comes back
empty, and the gate is reported as G0, which is not go-live.
The finished module, on gate G4, names med-dir and keeps G4.
"""


def evidence(item: dict) -> dict:
    """Ignore the item. Return an empty cell and gate G0.

    G4 on the item is not read, so go-live is skipped.
    """
    # The argument is unused. Owner and gate are not taken from the item.
    del item
    return {"cell": "", "gate": "G0"}
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 4.

4. Open [test_gates.py](packet/tests/test_gates.py). Search for `test_the_shell_skips_go_live`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_gates.py](work/tests/test_gates.py) is under the Replace heading for this file.

```text
"""Tests for the starter gate.

The shell reports gate G0 and an empty cell, even when the item is G4.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from gates import evidence

# Go-live. The shell is expected to skip it.
_ITEM = {"gate": "G4", "id": "go-live"}


class GateTests(unittest.TestCase):
    """Tests for the starter gate."""
    def test_the_shell_skips_go_live(self) -> None:
        """The gate comes back as G0 and the cell is empty."""
        got = evidence(_ITEM)
        self.assertEqual(got["gate"], "G0")
        self.assertEqual(got["cell"], "")


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. This item is done when the search finds that shell name in the packet file. Close the packet file. The next item is number 5.

5. Open [personal.py](packet/app/personal.py). Search for `Let the attack book.` That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/personal.py](work/app/personal.py) is under the Replace heading for this file. Do not copy the attack text from the release file onto this page.

```text
"""Let the attack book.

This is the starter. It ignores the row. blocked is false and
booked is true, so a direct attack is allowed through and a visit
is booked. The finished module blocks family atk-direct and does
not book.
"""


def stop(row: dict) -> dict:
    """Ignore the row. Let the visit book.

    family is not read, so a direct attack gets the same result
    as any other row.
    """
    # The argument is unused. The shell does not look at family.
    del row
    return {"blocked": False, "booked": True}
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 6.

6. Open [test_personal.py](packet/tests/test_personal.py). Search for `test_the_shell_books_the_attack`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_personal.py](work/tests/test_personal.py) is under the Replace heading for this file.

```text
"""Tests for the starter personal lab.

The shell does not block the row, and it books the visit.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from personal import stop

# The family names a direct attack. The words of that attack are not stored here.
_ROW = {"family": "atk-direct", "id": "personal-direct"}


class PersonalTests(unittest.TestCase):
    """Tests for the starter personal lab."""
    def test_the_shell_books_the_attack(self) -> None:
        """The row is not blocked, and a visit is booked."""
        got = stop(_ROW)
        self.assertFalse(got["blocked"])
        self.assertTrue(got["booked"])


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. This item is done when the search finds that shell name in the packet file. Close the packet file. The six pictures are done. The next heading is Replace the ranking. That heading is the first paste.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

The proposal is a ranking you can defend, a gate with an owner, and one attack that still must not book.

`first` walks the value model in the order it is written. It returns the first id whose blocker list is empty. It does not sort again, and it does not start at `p-triage`. A problem with a blocker cannot open. The shell put the blocked problem first because it was the sponsor's sentence.

`evidence` names `med-dir` in the clinical safety cell when the item is G4, go-live. Any other gate leaves that cell blank. The shell left the cell empty at go-live, so nobody owned clinical safety on the day the system would be allowed to run.

`stop` blocks family `atk-direct` and never sets booked. Any other family is not this attack. It is not booked either. This function does not book a visit. The wording of the attack stays in the pack. You do not copy it into the file.

Before you paste, say which problem `first` skips, who owns clinical safety at G4, and what `stop` refuses to set.

This section adds no file and no command.

## Replace the ranking

This block replaces the app file [work/app/rank.py](work/app/rank.py). The full path is `Week 04/Day 05/Student_Copy/work/app/rank.py`. It does not replace the test. The test is the next heading.

1. Open the work file named here, [work/app/rank.py](work/app/rank.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Return the first problem that has no blocker.`

```text
"""Return the first problem that has no blocker.

The value model lists problems in order. A problem with a blocker
cannot start. The start is the first row whose blocker list is
empty. If every row is blocked, there is nothing to start, and
the result is blank.
"""


def first(rows: list) -> str:
    """Walk the rows in order. Return the first id with no blockers.

    An empty blocker list means the problem can open. This function
    does not sort again. It keeps the model's order and skips a row
    that still names a blocker.
    """
    opened = [str(row["id"]) for row in rows if not row.get("blockers")]
    # The first open id is the start. No open row means a blank start.
    return opened[0] if opened else ""
```

Open [work/app/rank.py](work/app/rank.py). You should see `Return the first problem that has no blocker.` You should not see `Put the blocked problem first.` If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the ranking test.

## Replace the ranking test

This block replaces the test file [work/tests/test_rank.py](work/tests/test_rank.py). The full path is `Week 04/Day 05/Student_Copy/work/tests/test_rank.py`. The picture of the shell test is above. This block is the paste. It does not replace [rank.py](work/app/rank.py).

1. Open the work file named here, [work/tests/test_rank.py](work/tests/test_rank.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_a_blocked_problem_is_not_first`.

```text
"""Tests for the finished ranking.

The first row is blocked. The second row has an empty blocker
list. The start is the second id.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from rank import first

# The first row is blocked. The second row has an empty blocker list.
_ROWS = [
    {"blockers": ["pol-clinical-safety"], "id": "p-triage"},
    {"blockers": [], "id": "p-clock"},
]


class RankTests(unittest.TestCase):
    """Tests for the finished ranking."""
    def test_a_blocked_problem_is_not_first(self) -> None:
        """p-clock is the start because p-triage still has a blocker."""
        self.assertEqual(first(_ROWS), "p-clock")


if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_rank.py](work/tests/test_rank.py). You should see `test_a_blocked_problem_is_not_first`. You should not see `test_the_shell_starts_with_triage`. If you still see that shell name, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the gates.

## Replace the gates

This block replaces the app file [work/app/gates.py](work/app/gates.py). The full path is `Week 04/Day 05/Student_Copy/work/app/gates.py`. It does not replace the test. The test is the next heading.

1. Open the work file named here, [work/app/gates.py](work/app/gates.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Name the clinical safety owner at go-live.`

```text
"""Name the clinical safety owner at go-live.

Go-live is gate G4. The clinical safety cell at that gate is owned
by med-dir. evidence returns that owner when the item is G4.
Any other gate returns a blank cell and the gate it was given.
"""


def evidence(item: dict) -> dict:
    """For G4, name med-dir. For any other gate, leave the cell blank.

    A missing gate is stored as an empty string and is not treated
    as go-live.
    """
    gate = str(item.get("gate") or "")
    if gate == "G4":
        # Go-live names the clinical safety owner.
        return {"cell": "med-dir", "gate": "G4"}
    return {"cell": "", "gate": gate}
```

Open [work/app/gates.py](work/app/gates.py). You should see `Name the clinical safety owner at go-live.` You should not see `Leave the clinical safety cell empty and skip go-live.` If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the gates test.

## Replace the gates test

This block replaces the test file [work/tests/test_gates.py](work/tests/test_gates.py). The full path is `Week 04/Day 05/Student_Copy/work/tests/test_gates.py`. The picture of the shell test is above. This block is the paste. It does not replace [gates.py](work/app/gates.py).

1. Open the work file named here, [work/tests/test_gates.py](work/tests/test_gates.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_go_live_names_the_clinical_safety_owner`.

```text
"""Tests for the finished go-live gate.

The item is gate G4. The result keeps G4 and names med-dir
in the clinical safety cell.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from gates import evidence

# Go-live. The finished module names the clinical safety owner.
_ITEM = {"gate": "G4", "id": "go-live"}


class GateTests(unittest.TestCase):
    """Tests for the finished go-live gate."""
    def test_go_live_names_the_clinical_safety_owner(self) -> None:
        """Go-live stays G4 and the cell is med-dir."""
        got = evidence(_ITEM)
        self.assertEqual(got["gate"], "G4")
        self.assertEqual(got["cell"], "med-dir")


if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_gates.py](work/tests/test_gates.py). You should see `test_go_live_names_the_clinical_safety_owner`. You should not see `test_the_shell_skips_go_live`. If you still see that shell name, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the personal lab.

## Replace the personal lab

This block replaces the app file [work/app/personal.py](work/app/personal.py). The full path is `Week 04/Day 05/Student_Copy/work/app/personal.py`. It does not replace the test. The test is the next heading. Do not copy the attack text into this file.

1. Open the work file named here, [work/app/personal.py](work/app/personal.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Stop a direct attack. Do not book.`

```text
"""Stop a direct attack. Do not book.

The personal lab sees one row. family "atk-direct" is a direct
attack. That row is blocked, and nothing is booked. Any other
family is not this attack. It is not blocked, and it is not booked
either. This function does not book a visit. The wording of the
attack is not read here.
"""


def stop(row: dict) -> dict:
    """Block a direct attack. Never set booked to true.

    The family is the only field that matters.
    """
    if str(row.get("family") or "") == "atk-direct":
        # A direct attack stops here. The visit is not booked.
        return {"blocked": True, "booked": False}
    # Anything else is outside this guard. Still do not book.
    return {"blocked": False, "booked": False}
```

Open [work/app/personal.py](work/app/personal.py). You should see `Stop a direct attack. Do not book.` You should not see `Let the attack book.` If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the personal lab test.

## Replace the personal lab test

This block replaces the test file [work/tests/test_personal.py](work/tests/test_personal.py). The full path is `Week 04/Day 05/Student_Copy/work/tests/test_personal.py`. The picture of the shell test is above. This block is the paste. It does not replace [personal.py](work/app/personal.py).

1. Open the work file named here, [work/tests/test_personal.py](work/tests/test_personal.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_the_attack_is_blocked`.

```text
"""Tests for the finished personal lab.

The row's family is atk-direct. The guard blocks it and does not
book a visit. The attack wording is not in this file.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from personal import stop

# The family names a direct attack. The words of that attack are not stored here.
_ROW = {"family": "atk-direct", "id": "personal-direct"}


class PersonalTests(unittest.TestCase):
    """Tests for the finished personal lab."""
    def test_the_attack_is_blocked(self) -> None:
        """blocked is true and booked is false."""
        got = stop(_ROW)
        self.assertTrue(got["blocked"])
        self.assertFalse(got["booked"])


if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_personal.py](work/tests/test_personal.py). You should see `test_the_attack_is_blocked`. You should not see `test_the_shell_books_the_attack`. If you still see that shell name, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. That was the last paste on this page. The next heading is Search before the suite. Finish that heading before you run the suite.

## Search before the suite

Do this before you run the suite. Do not skip this table. A picture that was pasted fails the middle column. The shell suite in chapter 01 also prints `Ran 8 tests` and `OK`. An OK line by itself does not mean these files are the filled copies. The middle column is how you know.

This table is not a paste. Do not copy it into a file. Search each work file, not this chapter. A pasted picture fails the search. The string in the middle column is only in the replaced app file. It is not in the filled test for that module. A correct paste may still contain an old name on a different line.

| Work file | Search for this | You should not see |
| --- | --- | --- |
| [signin.py](work/app/signin.py) | `Accept a staff role. Refuse a service token.` | `Treat every token as staff.` |
| [bus.py](work/app/bus.py) | `Keep the event, including a field this consumer does not know.` | `Drop an unknown field, and drop a cancellation.` |
| [handoff.py](work/app/handoff.py) | `A handoff with no summary is refused.` | `Return an agent id and an empty summary.` |
| [leave.py](work/app/leave.py) | `Late leave cancels the published session.` | `Ignore leave that arrives after the session is published.` |
| [warehouse.py](work/app/warehouse.py) | `The referral clock is the referred date.` | `Read the booking date.` |
| [rank.py](work/app/rank.py) | `Return the first problem that has no blocker.` | `Put the blocked problem first.` |
| [gates.py](work/app/gates.py) | `Name the clinical safety owner at go-live.` | `Leave the clinical safety cell empty and skip go-live.` |
| [personal.py](work/app/personal.py) | `Stop a direct attack. Do not book.` | `Let the attack book.` |

If a row fails, go back to the chapter that replaces that file and paste that block again. Do not edit a test. A traceback names a test file. The app file is the same name without `test_`. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

## Run the suite

Open a new terminal in the course folder. The demo window is still inside `problem_simulation`. Do not use that window for the suite. If the `cd` line says the path cannot be found, this window is still inside `problem_simulation`. Open a new terminal in the course folder and run both lines. Do not skip that `cd` and run the suite inside `problem_simulation`.

```text
cd "Week 04/Day 05/Student_Copy/work"
python -m unittest discover -s tests -q
```

You should see a line that starts with `Ran 8 tests`, then a blank line, then `OK`.

That count is the same number the shell printed in chapter 01. This pass is the filled suite only when the search table above matched first. The shell pass was before these files were replaced. If the line says `FAILED`, the app and the tests in this folder do not match. A traceback names a test file. The app file is the same name without `test_`. Paste that pair again. Do not repair the spaces by hand.

The suite does not read the pages, and it does not read the workflow. A suite that prints `OK` can still fail [chapter 09](09-finish.md).

This page is done when the search table matches and the suite has printed `Ran 8 tests` and `OK`. Do not run a check from this page.

Next: [08 — The pages](08-the-pages.md).
