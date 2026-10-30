# 08 — The personal lab

[Chapter 07](07-the-spec.md) replaced the backlog, the stage gate, and the improvement gate. This chapter replaces the personal citation lab, then runs the suite.

You replace one file: [personal.py](work/app/personal.py), under Replace the personal lab. The block under Read these files is a picture of the shell. Pasting a picture puts the shell back. The work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copy in `packet/` unchanged. Do not paste a test. The tests are copied and not replaced. Do not delete `personal.py`. The suite imports it. Do not delete `repair.py`, `remeasure.py`, `cost.py`, `backlog.py`, or `gates.py`. The suite imports all six.

Scroll down to the heading Replace the personal lab. It is the first heading on this page that starts with Replace. The code block directly under it is the paste. The four steps from [chapter 05](05-the-sprint.md) are repeated above that paste. How the replacement works, below, is the exception. Read it. Do not paste it. Everything else above that Replace heading is a picture. You do not paste it.

This file is Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, run `prepare_work.py` from the course folder and paste chapters 05 through 08 again from the chapter source. Do not repair the spaces by hand.

Do not run a check on this page. The checks are only in [chapter 10](10-finish.md).

## Read this file

You are reading. You are not pasting yet. Open [personal.jsonl](packet/release/slices/personal.jsonl). Search for `asker`. A citation row has an audience and a version. A metric row has a floor and a value. The file has no keep field. Do not add one.

Open [personal.py](packet/app/personal.py). Search for `Cite every document and ignore the floor`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/personal.py](work/app/personal.py) is under the Replace heading.

```text
"""Cite every document and ignore the floor.

cite returns a citation that carries the document id from the row.
meets_budget discards the value and the floor and returns true.
"""

from __future__ import annotations


def cite(row: dict) -> dict | None:
    """Return a citation with the document id.

    row may carry a doc_id. That id is the field on the result.
    """
    # The document id is the field this citation copies.
    return {"doc_id": row.get("doc_id")}


def meets_budget(value: float, floor: float) -> bool:
    """Return true for any value and floor.

    value and floor are discarded.
    """
    # The value and the floor are unused.
    del value, floor
    return True
```

You are done reading. The next section is How the replacement works. Read it. The paste is the heading after that.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

`cite` returns nothing when the asker is a patient and the document audience is staff. On this slice that audience word is `staff` or `patient`. It is not Lesson 3's `public` or `restricted`. Do not rewrite the comparison to `public`. Any other row returns the audience, the document id, and the version. The shell returned only the document id, including a staff document shown to a patient.

`meets_budget` is true when the value clears the floor. A value on the floor still clears it. The shell returned true for every value and ignored the floor.

Before you paste, say which asker is refused a staff document, and what a citation that is kept still has to carry.

This section adds no file and no command.

## Replace the personal lab

This block replaces [work/app/personal.py](work/app/personal.py). The full path is `Module 03/Lesson 05/Student_Copy/work/app/personal.py`. It does not replace the copy in `packet/app`.

1. Open the work file named here, [work/app/personal.py](work/app/personal.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Keep version and audience, and refuse a staff document to a patient.`

```text
"""Keep version and audience, and refuse a staff document to a patient.

cite returns nothing when a patient asks and the document audience
is staff. Otherwise it returns audience, document id, and version.
meets_budget is true when the value clears the floor. A tiny
allowance is added so a value on the floor still clears it.
"""

from __future__ import annotations


def cite(row: dict) -> dict | None:
    """Return a citation the asker may keep, or nothing.

    row may carry asker, audience, doc_id, and version. A patient
    asking for a staff document gets nothing. A kept citation copies
    audience, document id, and version.
    """
    # A patient does not receive a staff document.
    if row.get("asker") == "patient" and row.get("audience") == "staff":
        return None
    # A kept citation carries the audience, the document id, and the version.
    return {
        "audience": row.get("audience"),
        "doc_id": row.get("doc_id"),
        "version": row.get("version"),
    }


def meets_budget(value: float, floor: float) -> bool:
    """Return whether value clears floor.

    value and floor are read as floats. A tiny allowance is added to
    value before the comparison, so a value on the floor clears it.
    """
    # The value clears the floor when it is at or above that floor.
    return float(value) + 1e-9 >= float(floor)
```

You should see `Keep version and audience, and refuse a staff document to a patient.` You should not see `Cite every document and ignore the floor.` If you still see that shell sentence, you pasted the picture. Delete the work file and paste the block under this heading again. `audience` can still appear on the returned citation. That is expected. It is one of the fields a kept citation carries.

## Search before the suite

This table is not a paste. Do not copy it into a file. Search each work file, not this chapter. A pasted picture fails the search. The string in the middle column is only in the replaced file. It is not in the shared tests.

| Work file | Search for this | You should not see |
| --- | --- | --- |
| [repair.py](work/app/repair.py) | `Replace a citation that is not in force.` | `Leave every citation as it was scored.` |
| [remeasure.py](work/app/remeasure.py) | `Score the citation slice before and after the repair.` | `Report the first score again.` |
| [cost.py](work/app/cost.py) | `Price the fix in labels, and stop when the budget is spent.` | `Charge nothing for the fix.` |
| [backlog.py](work/app/backlog.py) | `Drop the sponsor stories that are non-goals.` | `Keep every sponsor story.` |
| [gates.py](work/app/gates.py) | `Put the citation requirement on the risk tier.` | `Send the citation requirement to go-live.` |
| [personal.py](work/app/personal.py) | `Keep version and audience, and refuse a staff document to a patient.` | `Cite every document and ignore the floor.` |

If a row fails, go back to the chapter that replaces that file and paste that block again. Do not edit a test. A traceback names a test file. The app file is the same name without `test_`.

## Run the suite

Open a new terminal in the course folder. The demo window is still inside `problem_simulation`. Do not use that window for the suite. If you run this before the six app files are replaced, it fails. That failure is the shell. The next block is a command, not a picture.

```text
cd "Module 03/Lesson 05/Student_Copy/work"
python -m unittest discover -s tests -q
```

If the `cd` line says the system cannot find the path, this window is not the course folder. Open a new terminal the way [chapter 01](01-setup.md) showed, then run both lines.

You should see a line that starts with `Ran 11 tests`, then a blank line, then `OK`.

`Ran 11 tests` also appears when the suite fails. Read the line under it. That line has to be `OK`. If the line is `FAILED`, the shell is still in place. One passing test does not finish the suite. A traceback names a test file. The app file is the same name without `test_`. Do not edit the test.

If the terminal shows `SyntaxError` or `IndentationError`, run this from the course folder:

```text
python "Module 03/Lesson 05/Student_Copy/prepare_work.py"
```

Then paste chapters 05 through 08 again from the chapter source. Do not repair the spaces by hand. A second run puts the commented gate back. Paste the workflow from [chapter 07](07-the-spec.md) again after that.

A suite that prints `OK` can still fail chapter 10. The suite does not read the pages, and it does not read the workflow.

This page is done when the suite prints `Ran 11 tests` and `OK`, and the six searches pass.

Next: [09 — The pages](09-the-pages.md).
