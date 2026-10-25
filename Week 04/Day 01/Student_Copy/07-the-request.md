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
"""Leave every grant open."""

from __future__ import annotations


def settle(grants: list[dict], as_of: str) -> list[dict]:
    del as_of
    return [{**row, "status": "open"} for row in grants]


def controls() -> list[str]:
    return []
```

2. Open [test_access.py](packet/tests/test_access.py). Search for `test_every_grant_stays_open`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_access.py](work/tests/test_access.py) is under the Replace heading for this file.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from access import controls, settle

_GRANTS = [
    {"audit": "", "end": "2027-06-01", "id": "grant-open", "kind": "staff"},
    {"audit": "", "end": "2026-12-01", "id": "grant-stale", "kind": "staff"},
    {"audit": "", "end": "2027-01-01", "id": "grant-delegate", "kind": "delegate"},
    {"audit": "", "end": "2027-02-01", "id": "grant-glass", "kind": "break-glass"},
]


class AccessTests(unittest.TestCase):
    def test_every_grant_stays_open(self) -> None:
        settled = {row["id"]: row for row in settle(_GRANTS, "2027-01-31")}
        self.assertTrue(all(row["status"] == "open" for row in settled.values()))
        self.assertEqual(settled["grant-glass"]["audit"], "")

    def test_the_checklist_is_empty(self) -> None:
        self.assertEqual(controls(), [])


if __name__ == "__main__":
    unittest.main()
```

3. Open [erase.py](packet/app/erase.py). Search for `Delete the database row and leave the other stores`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/erase.py](work/app/erase.py) is under the Replace heading for this file.

```text
"""Delete the database row and leave the other stores."""

from __future__ import annotations


def export_categories(stores: dict, person_id: str) -> list[str]:
    if any(row.get("person_id") == person_id for row in stores.get("row", [])):
        return ["row"]
    return []


def drop(stores: dict, person_id: str) -> dict:
    cleared = {}
    for name in ("row", "memory", "index", "logs"):
        rows = [dict(row) for row in stores.get(name, [])]
        if name == "row":
            rows = [row for row in rows if row.get("person_id") != person_id]
        cleared[name] = rows
    return cleared
```

4. Open [test_erase.py](packet/tests/test_erase.py). Search for `test_the_index_still_holds_the_person`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_erase.py](work/tests/test_erase.py) is under the Replace heading for this file.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from erase import drop, export_categories

_STORES = {
    "index": [{"person_id": "person-access"}],
    "logs": [{"person_id": "person-access"}],
    "memory": [{"person_id": "person-access"}],
    "row": [{"person_id": "person-access"}],
}


class EraseTests(unittest.TestCase):
    def test_the_export_names_only_the_row(self) -> None:
        self.assertEqual(export_categories(_STORES, "person-access"), ["row"])

    def test_the_index_still_holds_the_person(self) -> None:
        cleared = drop(_STORES, "person-access")
        self.assertEqual(cleared["row"], [])
        self.assertEqual(cleared["index"], [{"person_id": "person-access"}])
        self.assertEqual(cleared["memory"], [{"person_id": "person-access"}])
        self.assertEqual(cleared["logs"], [{"person_id": "person-access"}])


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
"""Close a stale grant, refuse an expired delegate, and audit break-glass."""

from __future__ import annotations

CHECKLIST = (
    "non-root",
    "health-probe",
    "resource-limits",
    "no-phi-in-logs",
    "image-provenance",
    "registered-model-hash",
)


def settle(grants: list[dict], as_of: str) -> list[dict]:
    out = []
    for grant in grants:
        row = dict(grant)
        kind = row.get("kind")
        if kind == "break-glass" and not row.get("audit"):
            row["audit"] = "audit-" + str(row.get("id") or "")
            row["status"] = "open"
        elif (row.get("end") or "") < as_of and kind in {"staff", "delegate"}:
            row["status"] = "closed"
        else:
            row["status"] = "open"
        out.append(row)
    return out


def controls() -> list[str]:
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
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from access import controls, settle

_GRANTS = [
    {"audit": "", "end": "2027-06-01", "id": "grant-open", "kind": "staff"},
    {"audit": "", "end": "2026-12-01", "id": "grant-stale", "kind": "staff"},
    {"audit": "", "end": "2027-01-01", "id": "grant-delegate", "kind": "delegate"},
    {"audit": "", "end": "2027-02-01", "id": "grant-glass", "kind": "break-glass"},
]


class AccessTests(unittest.TestCase):
    def test_stale_and_expired_grants_close_and_break_glass_is_audited(self) -> None:
        settled = {row["id"]: row for row in settle(_GRANTS, "2027-01-31")}
        self.assertEqual(settled["grant-open"]["status"], "open")
        self.assertEqual(settled["grant-stale"]["status"], "closed")
        self.assertEqual(settled["grant-delegate"]["status"], "closed")
        self.assertEqual(settled["grant-glass"]["status"], "open")
        self.assertTrue(settled["grant-glass"]["audit"])

    def test_the_checklist_matches_pol_deploy(self) -> None:
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
"""Delete the person from the row, memory, the index, and permitted logs."""

from __future__ import annotations

STORES = ("row", "memory", "index", "logs")


def export_categories(stores: dict, person_id: str) -> list[str]:
    found = []
    for name in STORES:
        if any(row.get("person_id") == person_id for row in stores.get(name, [])):
            found.append(name)
    return found


def drop(stores: dict, person_id: str) -> dict:
    cleared = {}
    for name in STORES:
        rows = stores.get(name, [])
        if name == "logs" and any(row.get("person_id") == person_id for row in rows):
            cleared[name] = [{"redacted": True}]
        else:
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
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from erase import drop, export_categories

_STORES = {
    "index": [{"person_id": "person-access"}],
    "logs": [{"person_id": "person-access"}],
    "memory": [{"person_id": "person-access"}],
    "row": [{"person_id": "person-access"}],
}


class EraseTests(unittest.TestCase):
    def test_the_export_names_every_store(self) -> None:
        self.assertEqual(export_categories(_STORES, "person-access"), ["row", "memory", "index", "logs"])

    def test_deletion_clears_every_store(self) -> None:
        cleared = drop(_STORES, "person-access")
        self.assertEqual(export_categories(cleared, "person-access"), [])
        self.assertEqual(cleared["logs"], [{"redacted": True}])


if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_erase.py](work/tests/test_erase.py). You should see `test_deletion_clears_every_store`. You should not see `test_the_index_still_holds_the_person`. If you still see that shell name, you pasted the picture. That was the last paste on this page.

This page is done when access closes the stale staff grant and the expired delegate, break-glass has an audit row, the open staff grant stays open, and deletion clears the row, memory, the index, and the permitted logs. The shell sentences are gone. Do not run a check from this page.

Next: [08 — The fair measure](08-the-fair.md).
