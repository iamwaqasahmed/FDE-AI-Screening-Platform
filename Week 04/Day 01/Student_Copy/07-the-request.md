# 07 — The request

[Chapter 06](06-the-guard.md) replaced the guard, the output, the supply check, the log redaction, and the session limit. This chapter replaces four files. You do four pastes, in this order. Finish one before you start the next.

1. [access.py](work/app/access.py), under Replace access
2. [test_access.py](work/tests/test_access.py), under Replace the access test
3. [erase.py](work/app/erase.py), under Replace deletion
4. [test_erase.py](work/tests/test_erase.py), under Replace the deletion test

Paste only those four blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged.

The shell test is a picture. The filled test is the paste. A deletion that clears the row and leaves the index is the shell. The paste clears the row, memory, the index, and the permitted logs. Do the app file and its test before you start the next pair.

You are reading until the heading Replace access. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. Everything above that heading is a picture. You do not paste it. If you are lost after that heading, stay on the Replace heading you have open. Finish it. Then do the next Replace heading down the page. Do not go back to the pictures.

These files are Python. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, open a terminal in the course folder and run `python "Week 04/Day 01/Student_Copy/prepare_work.py"`. Then paste chapters 05, 06, and 07 again from the chapter source. Do not repair the spaces by hand. A second run puts the shell tests back.

The checks run in chapter 10. Do not run them from this page.

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the comment at the top of each one. Do not edit them.

1. Open [access.py](packet/app/access.py). Search for `Leave every grant open`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/access.py](work/app/access.py) is under the Replace heading for this file.

```text
"""Leave every grant open.

settle copies every grant and sets status to open. as_of is discarded,
so no field is compared and every returned status is open. controls
returns an empty list, so no deploy check is named.
"""

from __future__ import annotations


def settle(grants: list[dict], as_of: str) -> list[dict]:
    """Mark every grant open and ignore the date argument.

    The input rows are not mutated. The new dicts are the return value.
    """
    # The date is unused. del only drops this local name.
    del as_of
    # Each copy keeps the other fields and forces status to open.
    return [{**row, "status": "open"} for row in grants]


def controls() -> list[str]:
    """Return no deploy checks.

    The list is empty on every call.
    """
    return []
```

2. Open [test_access.py](packet/tests/test_access.py). Search for `test_every_grant_stays_open`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_access.py](work/tests/test_access.py) is under the Replace heading for this file.

```text
"""Tests for grant settlement that leaves every grant open.

The fixture holds a staff grant still in force, a staff grant that has
ended, a delegate that has ended, and a break-glass grant with an empty
audit. Every status is expected to stay open, and that empty audit is
expected to stay empty. The checklist is expected to be empty.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from access import controls, settle

# A later staff grant, an earlier staff grant, an earlier delegate,
# and a break-glass grant whose audit is empty.
_GRANTS = [
    {"audit": "", "end": "2027-06-01", "id": "grant-open", "kind": "staff"},
    {"audit": "", "end": "2026-12-01", "id": "grant-stale", "kind": "staff"},
    {"audit": "", "end": "2027-01-01", "id": "grant-delegate", "kind": "delegate"},
    {"audit": "", "end": "2027-02-01", "id": "grant-glass", "kind": "break-glass"},
]


class AccessTests(unittest.TestCase):
    """Check that no grant closes and that the checklist has no names."""

    def test_every_grant_stays_open(self) -> None:
        """Every settled status is open, and the break-glass audit stays empty.

        settle is called with the as_of date in the test. The assertion does
        not expect any grant to close, and it expects the audit value from
        the fixture to be unchanged.
        """
        # Settle the four grants on the date written in the call.
        settled = {row["id"]: row for row in settle(_GRANTS, "2027-01-31")}
        # Every status stays open, and the break-glass audit is still empty.
        self.assertTrue(all(row["status"] == "open" for row in settled.values()))
        self.assertEqual(settled["grant-glass"]["audit"], "")

    def test_the_checklist_is_empty(self) -> None:
        """controls returns an empty list.

        No deploy name is expected. There is no fixture for this test.
        """
        # controls is called with no rows. The list it returns is empty.
        self.assertEqual(controls(), [])


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
```

3. Open [erase.py](packet/app/erase.py). Search for `Delete the database row and leave the other stores`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/erase.py](work/app/erase.py) is under the Replace heading for this file.

```text
"""Delete the database row and leave the other stores.

export_categories looks only at the row store. It returns that name
when the person is there, and an empty list otherwise. drop copies
row, memory, index, and logs. Only the row copy has this person
removed. Memory, the index, and logs are returned unchanged.
"""

from __future__ import annotations


def export_categories(stores: dict, person_id: str) -> list[str]:
    """Return the row store name when it holds the person.

    Any other store is ignored, even when it holds the same person.
    A missing row store is read as empty, so the result is empty too.
    """
    # Memory, the index, and logs are not inspected.
    if any(row.get("person_id") == person_id for row in stores.get("row", [])):
        return ["row"]
    return []


def drop(stores: dict, person_id: str) -> dict:
    """Copy the four stores and remove the person from the row only.

    The result always has row, memory, index, and logs, in that order.
    The caller's lists are not mutated.
    """
    cleared = {}
    for name in ("row", "memory", "index", "logs"):
        # Copy every store first. A missing store becomes an empty list.
        rows = [dict(row) for row in stores.get(name, [])]
        # The other three names skip this filter and keep every copied row.
        if name == "row":
            rows = [row for row in rows if row.get("person_id") != person_id]
        cleared[name] = rows
    return cleared
```

4. Open [test_erase.py](packet/tests/test_erase.py). Search for `test_the_index_still_holds_the_person`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_erase.py](work/tests/test_erase.py) is under the Replace heading for this file.

```text
"""Tests for person deletion that clears the row and leaves the other stores.

The fixture puts the same person in the index, logs, memory, and the
row. The export is expected to name only the row. After drop, the row
is expected to be empty and the other stores are expected to still
hold the person.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from erase import drop, export_categories

# The same person is present in the index, logs, memory, and the row.
_STORES = {
    "index": [{"person_id": "person-access"}],
    "logs": [{"person_id": "person-access"}],
    "memory": [{"person_id": "person-access"}],
    "row": [{"person_id": "person-access"}],
}


class EraseTests(unittest.TestCase):
    """Check that the export and the deletion both stop at the row."""

    def test_the_export_names_only_the_row(self) -> None:
        """The export is the row store alone.

        Index, memory, and logs hold the person in the fixture, and they
        are not expected in the list.
        """
        # The export names the row store alone.
        self.assertEqual(export_categories(_STORES, "person-access"), ["row"])

    def test_the_index_still_holds_the_person(self) -> None:
        """drop clears the row and leaves the other stores.

        The index, memory, and logs still contain the fixture row. The row
        store is empty.
        """
        # Drop the person, then read the four stores.
        cleared = drop(_STORES, "person-access")
        # The row is empty. Index, memory, and logs still hold the person.
        self.assertEqual(cleared["row"], [])
        self.assertEqual(cleared["index"], [{"person_id": "person-access"}])
        self.assertEqual(cleared["memory"], [{"person_id": "person-access"}])
        self.assertEqual(cleared["logs"], [{"person_id": "person-access"}])


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
```

You are done reading. The next heading, Replace access, is the first paste on this page.

## Replace access

This block replaces [work/app/access.py](work/app/access.py). The full path is `Week 04/Day 01/Student_Copy/work/app/access.py`. It does not replace the copy in `packet/app`.

1. Open the work file named here, [work/app/access.py](work/app/access.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `audit-`.

```text
"""Close a stale grant, refuse an expired delegate, and audit break-glass.

settle copies each grant and writes a status. A break-glass grant
with no audit value is given an audit id and left open. That check
runs before the end check, so a late end does not close it. A staff
or delegate grant is closed only when its end text is strictly less
than as_of. Text that is equal stays open. Every other grant is
marked open, including break-glass that already has an audit value.
A missing end is read as empty text.

controls returns the deploy checklist in the order stored below.
The tuple itself is not handed to the caller.
"""

from __future__ import annotations

# Deploy check names, in the order controls returns them.
CHECKLIST = (
    "non-root",
    "health-probe",
    "resource-limits",
    "no-phi-in-logs",
    "image-provenance",
    "registered-model-hash",
)


def settle(grants: list[dict], as_of: str) -> list[dict]:
    """Return a new list of grants with status set, and audit bare break-glass.

    The input list is not mutated. end and as_of are compared as text.
    A missing id becomes an empty suffix on the audit value.
    """
    out = []
    for grant in grants:
        # Copy first so the caller's dict keeps the status it arrived with.
        row = dict(grant)
        kind = row.get("kind")
        # An empty or missing audit value counts as unaudited. The id is
        # prefixed and the grant stays open.
        if kind == "break-glass" and not row.get("audit"):
            row["audit"] = "audit-" + str(row.get("id") or "")
            row["status"] = "open"
        # Only these two kinds close, and only when the end text is earlier.
        elif (row.get("end") or "") < as_of and kind in {"staff", "delegate"}:
            row["status"] = "closed"
        else:
            row["status"] = "open"
        out.append(row)
    return out


def controls() -> list[str]:
    """Return a new list of the deploy check names, in checklist order.

    The caller can change the list it receives. CHECKLIST stays as it is.
    """
    return list(CHECKLIST)
```

Open [work/app/access.py](work/app/access.py). You should see `audit-`. You should not see `Leave every grant open`. If you still see that shell sentence, you pasted the picture. `grant-open` stays open. That is expected. Its end is after the case date. Stay on this page. The next heading is Replace the access test.

## Replace the access test

This block replaces [work/tests/test_access.py](work/tests/test_access.py). The full path is `Week 04/Day 01/Student_Copy/work/tests/test_access.py`. It does not replace the copy in `packet/tests`.

1. Open the work file named here, [work/tests/test_access.py](work/tests/test_access.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_stale_and_expired_grants_close_and_break_glass_is_audited`.

```text
"""Tests for grant settlement that closes an ended staff or delegate grant.

The fixture holds a staff grant still in force, a staff grant that has
ended, a delegate that has ended, and a break-glass grant with an empty
audit. settle is called with the as_of date written in the test.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from access import controls, settle

# A later staff grant, an earlier staff grant, an earlier delegate,
# and a break-glass grant whose audit is empty.
_GRANTS = [
    {"audit": "", "end": "2027-06-01", "id": "grant-open", "kind": "staff"},
    {"audit": "", "end": "2026-12-01", "id": "grant-stale", "kind": "staff"},
    {"audit": "", "end": "2027-01-01", "id": "grant-delegate", "kind": "delegate"},
    {"audit": "", "end": "2027-02-01", "id": "grant-glass", "kind": "break-glass"},
]


class AccessTests(unittest.TestCase):
    """Check closed grants, the break-glass audit, and the deploy checklist."""

    def test_stale_and_expired_grants_close_and_break_glass_is_audited(self) -> None:
        """The ended staff and delegate grants close. Break-glass stays open.

        The fixture is settled at the as_of in the call. The staff grant whose
        end is later stays open. The staff grant and the delegate whose ends
        are earlier close. The break-glass grant stays open, and its audit
        value is truthy, so an audit id was written.
        """
        # Settle the four grants, then look each one up by id.
        settled = {row["id"]: row for row in settle(_GRANTS, "2027-01-31")}
        # The staff grant that ends later stays open. The ended staff grant
        # and the ended delegate close.
        self.assertEqual(settled["grant-open"]["status"], "open")
        self.assertEqual(settled["grant-stale"]["status"], "closed")
        self.assertEqual(settled["grant-delegate"]["status"], "closed")
        # Break-glass stays open, and its audit field now holds an id.
        self.assertEqual(settled["grant-glass"]["status"], "open")
        self.assertTrue(settled["grant-glass"]["audit"])

    def test_the_checklist_matches_pol_deploy(self) -> None:
        """controls returns the deploy names in checklist order.

        There is no separate fixture. The assertion lists every name this
        module is expected to report.
        """
        # The deploy names, in the order controls reports them.
        self.assertEqual(
            controls(),
            [
                "non-root",
                "health-probe",
                "resource-limits",
                "no-phi-in-logs",
                "image-provenance",
                "registered-model-hash",
            ],
        )


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_access.py](work/tests/test_access.py). You should see `test_stale_and_expired_grants_close_and_break_glass_is_audited`. You should not see `test_every_grant_stays_open`. If you still see that shell name, you pasted the picture. Stay on this page. The next heading is Replace deletion.

## Replace deletion

This block replaces [work/app/erase.py](work/app/erase.py). The full path is `Week 04/Day 01/Student_Copy/work/app/erase.py`. It does not replace the copy in `packet/app`.

1. Open the work file named here, [work/app/erase.py](work/app/erase.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `permitted logs`.

```text
"""Delete the person from the row, memory, the index, and permitted logs.

export_categories walks the stores in STORES order and names each one
that still holds the person. A missing store is treated as empty.
drop removes the person from the row, memory, and the index by copying
the other rows. When logs still hold the person, the whole logs list
is replaced by one redacted marker, including any other people's rows.
When logs do not hold the person, those rows are copied and filtered
the same way as the other stores.
"""

from __future__ import annotations

# Store names, in the order the export lists them and drop walks them.
STORES = ("row", "memory", "index", "logs")


def export_categories(stores: dict, person_id: str) -> list[str]:
    """Return the store names that still contain this person.

    The names follow STORES, not the order of keys on the dict. A store
    with no matching person_id is omitted.
    """
    found = []
    for name in STORES:
        if any(row.get("person_id") == person_id for row in stores.get(name, [])):
            found.append(name)
    return found


def drop(stores: dict, person_id: str) -> dict:
    """Return a new store dict with this person removed, and logs redacted.

    Every STORES key is present on the result. A missing input store is
    read as an empty list. Logs that contain the person become a single
    row whose redacted field is true.
    """
    cleared = {}
    for name in STORES:
        rows = stores.get(name, [])
        # One matching log row replaces the entire logs list with the marker.
        if name == "logs" and any(row.get("person_id") == person_id for row in rows):
            cleared[name] = [{"redacted": True}]
        else:
            # Copy the rows that belong to someone else. The caller's lists stay put.
            cleared[name] = [dict(row) for row in rows if row.get("person_id") != person_id]
    return cleared
```

Open [work/app/erase.py](work/app/erase.py). You should see `permitted logs`. You should not see `Delete the database row and leave the other stores`. If you still see that shell sentence, you pasted the picture. Stay on this page. The next heading is Replace the deletion test.

## Replace the deletion test

This block replaces [work/tests/test_erase.py](work/tests/test_erase.py). The full path is `Week 04/Day 01/Student_Copy/work/tests/test_erase.py`. It does not replace the copy in `packet/tests`.

1. Open the work file named here, [work/tests/test_erase.py](work/tests/test_erase.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_deletion_clears_every_store`.

```text
"""Tests for person deletion across the row, memory, the index, and logs.

The fixture puts the same person in each of those stores. The export
should name every store. After drop, that person should be gone, and
logs should be the redacted marker.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from erase import drop, export_categories

# The same person is present in the index, logs, memory, and the row.
_STORES = {
    "index": [{"person_id": "person-access"}],
    "logs": [{"person_id": "person-access"}],
    "memory": [{"person_id": "person-access"}],
    "row": [{"person_id": "person-access"}],
}


class EraseTests(unittest.TestCase):
    """Check the export list and the stores after deletion."""

    def test_the_export_names_every_store(self) -> None:
        """The export lists row, memory, index, and logs.

        The person in the fixture is present in each store, so each store
        name is expected, in that order.
        """
        # Row, then memory, then the index, then logs.
        self.assertEqual(export_categories(_STORES, "person-access"), ["row", "memory", "index", "logs"])

    def test_deletion_clears_every_store(self) -> None:
        """After drop, the person is in no store, and logs are the redacted marker.

        export_categories on the cleared stores is empty. The logs store is
        the single redacted row in the assertion.
        """
        # Drop the person, then ask which stores still name them.
        cleared = drop(_STORES, "person-access")
        self.assertEqual(export_categories(cleared, "person-access"), [])
        # Logs keep a redacted marker in place of the original row.
        self.assertEqual(cleared["logs"], [{"redacted": True}])


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_erase.py](work/tests/test_erase.py). You should see `test_deletion_clears_every_store`. You should not see `test_the_index_still_holds_the_person`. If you still see that shell name, you pasted the picture. That was the last paste on this page.

This page is done when access closes the stale staff grant and the expired delegate, break-glass has an audit row, the open staff grant stays open, and deletion clears the row, memory, the index, and the permitted logs. The shell sentences are gone. Do not run a check from this page.

Next: [08 — The fair measure](08-the-fair.md).
