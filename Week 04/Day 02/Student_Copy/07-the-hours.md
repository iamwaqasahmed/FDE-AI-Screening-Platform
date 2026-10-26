# 07 — The hours

[Chapter 06](06-the-board.md) replaced the trace, the board, and the meter. This chapter replaces four app files and the work copies of their four tests. You do eight pastes, in this order. Finish one before you start the next. Do the app file and its test before you start the next pair.

1. [cache.py](work/app/cache.py), under Replace the cache
2. [test_cache.py](work/tests/test_cache.py), under Replace the cache test
3. [drift.py](work/app/drift.py), under Replace the drifts
4. [test_drift.py](work/tests/test_drift.py), under Replace the drift test
5. [override.py](work/app/override.py), under Replace the override
6. [test_override.py](work/tests/test_override.py), under Replace the override test
7. [shadow.py](work/app/shadow.py), under Replace the shadow hold
8. [test_shadow.py](work/tests/test_shadow.py), under Replace the shadow test

Paste only those eight blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. The cache test has no picture. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged.

The shell test is a picture. The filled test is the paste. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

You are reading until the heading Replace the cache. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. The four steps from chapter 05 are repeated above each paste. The section How the replacement works sits above the first Replace heading. Read it. Do not paste it. Every code block above that Replace heading is a picture. A file under Read these files that has no picture is still not a paste. You do not paste a picture. If you are lost after that heading, stay on the Replace heading you have open. Finish it. Then do the next Replace heading down the page. Do not go back to the pictures.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, paste that block again from this chapter file. Do not repair the spaces by hand. Run `prepare_work.py` again only when a failure row in [chapter 09](09-finish.md) says so. A second run puts the shell tests back.

The checks run in chapter 09. Do not run them from this page. The suite on this page runs only after the search table.

The rows in these tests are a small fixture. They are not the pack rows. Do not copy a hash from the replay onto a test. Do not write a share on a page outside the block you are pasting.

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the first line of each one. Do not edit them. A picture belongs to the numbered item above it. The cache test has no picture.

1. Open [cache.py](packet/app/cache.py). Search for `Keep the cached hours after the circular`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/cache.py](work/app/cache.py) is under the Replace heading for this file.

```text
"""Keep the cached hours after the circular.

answer discards the event and returns the hours string from the store.
A missing hours value becomes an empty string. The event body is never
read, including when the event is a changed circular.
"""

from __future__ import annotations


def answer(store: dict, event: dict) -> str:
    """Return the cached hours and ignore the event.

    The store is not changed. A missing hours value becomes an empty string.
    """
    # The event is unused, so a changed document cannot replace the cache.
    del event
    return str(store.get("hours") or "")
```

That was a picture. Do not paste it. The next item is number 2.

2. Open [test_cache.py](packet/tests/test_cache.py). Search for `test_the_cache_keeps_the_old_hours`. That name is the shell test. There is no picture of this file. There is no block under this item. The paste that replaces [work/tests/test_cache.py](work/tests/test_cache.py) is under Replace the cache test. Close the packet file. The next item is number 3.

3. Open [drift.py](packet/app/drift.py). Search for `Name one drift and stop`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/drift.py](work/app/drift.py) is under the Replace heading for this file.

```text
"""Name one drift and stop.

name discards the row and always returns the hours label. The row
is not read, so every call gets the same name.
"""

from __future__ import annotations


def name(row: dict) -> str:
    """Return the hours label for every row.

    The argument is discarded. There is no other label in this module.
    """
    # The row is unused. The label below does not depend on it.
    del row
    return "ramadan hours"
```

That was a picture. Do not paste it. The next item is number 4.

4. Open [test_drift.py](packet/tests/test_drift.py). Search for `test_every_row_is_named_hours`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_drift.py](work/tests/test_drift.py) is under the Replace heading for this file.

```text
"""Tests for a drift name that is always the hours label.

A clinic row and a criteria row are both expected to be named as
hours. The label does not vary by kind.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from drift import name


class DriftTests(unittest.TestCase):
    """Check that both kinds return the hours label."""

    def test_every_row_is_named_hours(self) -> None:
        """Both kinds return the hours label.

        The clinic kind and the criteria kind are the fixtures. Neither
        call changes the label.
        """
        self.assertEqual(name({"kind": "clinic"}), "ramadan hours")
        self.assertEqual(name({"kind": "criteria"}), "ramadan hours")


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 5.

5. Open [override.py](packet/app/override.py). Search for `Report no overrides`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/override.py](work/app/override.py) is under the Replace heading for this file.

```text
"""Report no overrides.

rate discards the rows and returns zero on every call. No field is
read, so a stamped row and an unstamped row produce the same result.
"""

from __future__ import annotations


def rate(rows: list[dict]) -> float:
    """Return zero for any rows.

    The argument is discarded. The result does not depend on its length.
    """
    # The rows are unused. del only drops this local name.
    del rows
    return 0.0
```

That was a picture. Do not paste it. The next item is number 6.

6. Open [test_override.py](packet/tests/test_override.py). Search for `test_the_rate_stays_at_zero`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_override.py](work/tests/test_override.py) is under the Replace heading for this file.

```text
"""Tests for an override rate that stays at zero.

The call passes one stamped row and one row that is not stamped.
The rate is expected to be zero anyway.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from override import rate


class OverrideTests(unittest.TestCase):
    """Check that a mixed stamped list still returns zero."""

    def test_the_rate_stays_at_zero(self) -> None:
        """rate returns zero for a mixed stamped list.

        One row is stamped and one is not. The assertion is zero.
        """
        self.assertEqual(rate([{"stamped": True}, {"stamped": False}]), 0.0)


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 7.

7. Open [shadow.py](packet/app/shadow.py). Search for `Show the shadow reply and promote the candidate`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/shadow.py](work/app/shadow.py) is under the Replace heading for this file.

```text
"""Show the shadow reply and promote the candidate.

reply returns the shadow reply, or an empty string when it is missing.
promote returns the candidate hash with no other check, or an empty
string when the hash is missing.
"""

from __future__ import annotations


def reply(turn: dict) -> str:
    """Return the shadow reply.

    A missing shadow reply becomes an empty string. Other keys are ignored.
    """
    # Only the shadow reply is read.
    return str(turn.get("shadow_reply") or "")


def promote(comparison: dict) -> str:
    """Return the candidate hash and ignore the other fields.

    A missing hash becomes an empty string. No flag has to be true.
    """
    # No flag is read. The hash is returned whenever it is present.
    return str(comparison.get("candidate_hash") or "")
```

That was a picture. Do not paste it. The next item is number 8.

8. Open [test_shadow.py](packet/tests/test_shadow.py). Search for `test_the_shadow_reply_is_shown`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_shadow.py](work/tests/test_shadow.py) is under the Replace heading for this file.

```text
"""Tests for a reply that shows the shadow text.

The turn fixture has a registered reply and a shadow reply. The
reply is expected to be the shadow one. A candidate hash is expected
back even when the comparison flag is false.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from shadow import promote, reply

# A registered reply, a shadow reply, and a candidate hash.
_TURN = {
    "candidate_hash": "sha256:candidate",
    "registered_reply": "Your referral is still pending.",
    "shadow_reply": "Your referral was accepted by the shadow adapter.",
}


class ShadowTests(unittest.TestCase):
    """Check the shadow reply and promotion without a comparison."""

    def test_the_shadow_reply_is_shown(self) -> None:
        """reply returns the shadow reply from the turn fixture.

        The registered reply on that fixture is not the result.
        """
        self.assertEqual(reply(_TURN), _TURN["shadow_reply"])

    def test_a_hash_is_promoted_with_no_comparison(self) -> None:
        """promote returns the candidate hash when compared is false.

        The call has no matched flag. The assertion expects the hash.
        """
        self.assertEqual(promote({"candidate_hash": "sha256:candidate", "compared": False}), "sha256:candidate")


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it.

You are done reading. Do not paste any block above this line. The next heading is How the replacement works. Read it. It is not a paste. The first paste is the heading Replace the cache.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

Four small decisions that keep a stale answer from surviving the afternoon.

`answer` returns the event body when the topic is `document.changed` and the document id is the Ramadan hours circular. Both have to match. Any other event returns the hours string already on the cache. A different circular does not clear the hours. The shell returned the cache for every event, so evening clinics stayed open after the circular moved them.

`name` maps a drift kind to its label. The three kinds are hours, criteria, and clinic. An unknown kind is an error, not a silent extra drift.

`rate` is the share of coordinator rows whose `stamped` field is true. That is the override rate. An empty list returns zero.

`reply` returns the registered reply. The shadow reply is not read, so a candidate cannot change what the patient is sent. `promote` returns the candidate hash only when the comparison was both compared and matched. Either flag missing or false yields an empty string. Promotion waits.

Before you paste, say which event drops the cached hours, and what a patient is sent while a shadow comparison is still running.

This section adds no file and no command.

## Replace the cache

This block replaces [work/app/cache.py](work/app/cache.py). The full path is `Week 04/Day 02/Student_Copy/work/app/cache.py`. It does not replace the copy in `packet/app`.

1. Open the work file named here, [work/app/cache.py](work/app/cache.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Drop cached hours when the Ramadan circular changes`.

```text
"""Drop cached hours when the Ramadan circular changes.

answer returns the event body when the topic is document.changed and
the doc id is the hours circular. Both have to match. Any other event
returns the hours string stored on the cache. A missing body or missing
hours becomes an empty string. The store dict is not updated. The
caller simply receives the string that should be used for this event.
"""

from __future__ import annotations


def answer(store: dict, event: dict) -> str:
    """Use the event body for the hours circular. Otherwise use the cache.

    The cache is not rewritten. A missing value on the chosen side becomes
    an empty string.
    """
    # This document's body is the answer. The cached hours are not returned.
    if event.get("topic") == "document.changed" and event.get("doc_id") == "circ-ramadan-hours":
        return str(event.get("body") or "")
    # Any other topic or doc id leaves the cached hours as the answer.
    return str(store.get("hours") or "")
```

Open [work/app/cache.py](work/app/cache.py). You should see `Drop cached hours when the Ramadan circular changes`. You should not see `Keep the cached hours after the circular`. If you still see that shell sentence, you pasted the picture. If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand. Stay on this page. The next heading is Replace the cache test.

## Replace the cache test

This block replaces [work/tests/test_cache.py](work/tests/test_cache.py). The full path is `Week 04/Day 02/Student_Copy/work/tests/test_cache.py`. It does not replace the copy in `packet/tests`. The rows in this test are a small fixture. They are not the pack rows.

1. Open the work file named here, [work/tests/test_cache.py](work/tests/test_cache.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_the_circular_replaces_the_cached_hours`.

```text
"""Tests for an hours cache that follows the hours circular.

The old hours string is the cache. One event is the hours circular.
Another event is a different document. The circular should replace
the cached hours. The other document should leave them.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from cache import answer

# Cached hours. The closing time in this string is what the first test looks for.
_OLD = "Code hrs-ramadan closes the evening clinics at 21:00."
# The hours circular. Its body is the replacement answer.
_EVENT = {
    "body": "Evening clinics close at 01:00. Daytime slots are not offered.",
    "doc_id": "circ-ramadan-hours",
    "topic": "document.changed",
}
# A different document on the same topic. It should not replace the cache.
_OTHER = {"body": "Bring the card.", "doc_id": "leaflet-prep", "topic": "document.changed"}


class CacheTests(unittest.TestCase):
    """Check the hours circular and a document that is not that circular."""

    def test_the_circular_replaces_the_cached_hours(self) -> None:
        """The answer is the circular body, not the cached hours.

        The first assertion compares with the event body. The second checks
        that the closing time named in the assertion is absent.
        """
        # The circular body replaces the cache, and the old closing time is absent.
        self.assertEqual(answer({"hours": _OLD}, _EVENT), _EVENT["body"])
        self.assertNotIn("21:00", answer({"hours": _OLD}, _EVENT))

    def test_another_document_leaves_the_hours_cache(self) -> None:
        """A different document returns the cached hours unchanged.

        The event body is not the answer. The assertion expects the old string.
        """
        # The other document leaves the cached hours in place.
        self.assertEqual(answer({"hours": _OLD}, _OTHER), _OLD)


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_cache.py](work/tests/test_cache.py). You should see `test_the_circular_replaces_the_cached_hours` and `test_another_document_leaves_the_hours_cache`. You should not see `test_the_cache_keeps_the_old_hours`. If you still see that shell name, you pasted the picture. Stay on this page. The next heading is Replace the drifts.

## Replace the drifts

This block replaces [work/app/drift.py](work/app/drift.py). The full path is `Week 04/Day 02/Student_Copy/work/app/drift.py`. It does not replace the copy in `packet/app`.

1. Open the work file named here, [work/app/drift.py](work/app/drift.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Name the three drifts`.

```text
"""Name the three drifts.

name maps the row's kind to the label stored in _LABELS. The kind is
read as a string. A kind that is not in the map raises KeyError. A
missing kind becomes the string None, which is not a label, so that
lookup raises too.
"""

from __future__ import annotations

# Kind to label. The keys are the only kinds this function accepts.
_LABELS = {"clinic": "campaign clinic", "criteria": "criteria v4", "hours": "ramadan hours"}


def name(row: dict) -> str:
    """Return the label for this row's kind.

    The map is not copied or extended. An unknown kind is an error.
    """
    return _LABELS[str(row.get("kind"))]
```

Open [work/app/drift.py](work/app/drift.py). You should see `Name the three drifts`. You should not see `Name one drift and stop`. If you still see that shell sentence, you pasted the picture. If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand. Stay on this page. The next heading is Replace the drift test.

## Replace the drift test

This block replaces [work/tests/test_drift.py](work/tests/test_drift.py). The full path is `Week 04/Day 02/Student_Copy/work/tests/test_drift.py`. It does not replace the copy in `packet/tests`.

1. Open the work file named here, [work/tests/test_drift.py](work/tests/test_drift.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_each_kind_has_its_name`.

```text
"""Tests for drift labels.

Each call passes a kind. The label should match that kind: hours,
criteria, and clinic.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from drift import name


class DriftTests(unittest.TestCase):
    """Check the label for each kind."""

    def test_each_kind_has_its_name(self) -> None:
        """Each kind returns its own label.

        The assertions are the hours label, the criteria label, and the
        clinic label, in that order.
        """
        self.assertEqual(name({"kind": "hours"}), "ramadan hours")
        self.assertEqual(name({"kind": "criteria"}), "criteria v4")
        self.assertEqual(name({"kind": "clinic"}), "campaign clinic")


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_drift.py](work/tests/test_drift.py). You should see `test_each_kind_has_its_name`. You should not see `test_every_row_is_named_hours`. If you still see that shell name, you pasted the picture. Stay on this page. The next heading is Replace the override.

## Replace the override

This block replaces [work/app/override.py](work/app/override.py). The full path is `Week 04/Day 02/Student_Copy/work/app/override.py`. It does not replace the copy in `packet/app`.

1. Open the work file named here, [work/app/override.py](work/app/override.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Share of stamped coordinator actions`.

```text
"""Share of stamped coordinator actions.

rate is the share of rows whose stamped field is true. A missing
stamped field counts as not stamped. An empty list returns zero so
the length is never used as a divisor.
"""

from __future__ import annotations


def rate(rows: list[dict]) -> float:
    """Return how many rows are stamped, divided by the row count.

    A truthy stamped field counts. An empty list returns zero.
    """
    # An empty list has no share. Return zero before dividing.
    if not rows:
        return 0.0
    # Each stamped row counts once. The divisor is the whole list, not the stamped rows.
    return sum(1 for row in rows if row.get("stamped")) / len(rows)
```

Open [work/app/override.py](work/app/override.py). You should see `Share of stamped coordinator actions`. You should not see `Report no overrides`. If you still see that shell sentence, you pasted the picture. Do not write the share on a page outside this file. If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand. Stay on this page. The next heading is Replace the override test.

## Replace the override test

This block replaces [work/tests/test_override.py](work/tests/test_override.py). The full path is `Week 04/Day 02/Student_Copy/work/tests/test_override.py`. It does not replace the copy in `packet/tests`. The rows in this test are a small fixture. They are not the pack rows.

1. Open the work file named here, [work/tests/test_override.py](work/tests/test_override.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_the_rate_is_the_stamped_share`.

```text
"""Tests for the stamped share of coordinator actions.

The fixture is one stamped row and one row that is not stamped.
The rate should be that stamped share.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from override import rate


class OverrideTests(unittest.TestCase):
    """Check the stamped share of the fixture."""

    def test_the_rate_is_the_stamped_share(self) -> None:
        """The stamped share of the fixture is the value in the assertion.

        One row is stamped and one is not.
        """
        # One stamped row and one row that is not stamped.
        rows = [{"stamped": True}, {"stamped": False}]
        self.assertEqual(rate(rows), 0.5)


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_override.py](work/tests/test_override.py). You should see `test_the_rate_is_the_stamped_share`. You should not see `test_the_rate_stays_at_zero`. If you still see that shell name, you pasted the picture. Stay on this page. The next heading is Replace the shadow hold.

## Replace the shadow hold

This block replaces [work/app/shadow.py](work/app/shadow.py). The full path is `Week 04/Day 02/Student_Copy/work/app/shadow.py`. It does not replace the copy in `packet/app`.

1. Open the work file named here, [work/app/shadow.py](work/app/shadow.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Keep the registered reply. Promote only after a comparison`.

```text
"""Keep the registered reply. Promote only after a comparison.

reply returns the registered reply, or an empty string when it is
missing. The shadow reply is not read. promote returns the candidate
hash only when the comparison was both compared and matched. Either
flag missing or false yields an empty string. A missing hash on a
ready comparison also becomes an empty string.
"""

from __future__ import annotations


def reply(turn: dict) -> str:
    """Return the registered reply.

    A missing registered reply becomes an empty string. Other keys on
    the turn are ignored.
    """
    # The shadow reply is not consulted.
    return str(turn.get("registered_reply") or "")


def promote(comparison: dict) -> str:
    """Return the candidate hash only after a match that was compared.

    Otherwise return an empty string. A missing hash on a ready
    comparison is stored as an empty string too.
    """
    # Both flags must be true. One true flag is not enough.
    if comparison.get("compared") and comparison.get("matched"):
        return str(comparison.get("candidate_hash") or "")
    return ""
```

Open [work/app/shadow.py](work/app/shadow.py). You should see `Keep the registered reply. Promote only after a comparison`. You should not see `Show the shadow reply and promote the candidate`. If you still see that shell sentence, you pasted the picture. If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand. Stay on this page. The next heading is Replace the shadow test.

## Replace the shadow test

This block replaces [work/tests/test_shadow.py](work/tests/test_shadow.py). The full path is `Week 04/Day 02/Student_Copy/work/tests/test_shadow.py`. It does not replace the copy in `packet/tests`. The hash in this test is a small fixture. It is not a pack hash.

1. Open the work file named here, [work/tests/test_shadow.py](work/tests/test_shadow.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_promotion_waits_for_a_comparison`.

```text
"""Tests for a reply that stays on the registered text.

The turn fixture has a registered reply and a shadow reply. The
reply should be the registered one. Promotion should return a hash
only when the comparison was compared and matched.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from shadow import promote, reply

# A registered reply, a shadow reply, and a candidate hash.
_TURN = {
    "candidate_hash": "sha256:candidate",
    "registered_reply": "Your referral is still pending.",
    "shadow_reply": "Your referral was accepted by the shadow adapter.",
}


class ShadowTests(unittest.TestCase):
    """Check the patient reply and the promotion gate."""

    def test_the_patient_reply_stays_registered(self) -> None:
        """reply returns the registered reply from the turn fixture.

        The shadow reply on that fixture is not the result.
        """
        self.assertEqual(reply(_TURN), _TURN["registered_reply"])

    def test_promotion_waits_for_a_comparison(self) -> None:
        """A comparison that was not compared promotes nothing.

        The bare fixture is refused and the result is empty. The ready
        fixture was compared and matched, so it returns the candidate hash.
        """
        # Not compared and not matched. Promotion should refuse this one.
        bare = {"candidate_hash": "sha256:candidate", "compared": False, "matched": False}
        # Compared and matched. Promotion should return the hash.
        ready = {"candidate_hash": "sha256:candidate", "compared": True, "matched": True}
        self.assertEqual(promote(bare), "")
        self.assertEqual(promote(ready), "sha256:candidate")


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_shadow.py](work/tests/test_shadow.py). You should see `test_the_patient_reply_stays_registered` and `test_promotion_waits_for_a_comparison`. You should not see `test_the_shadow_reply_is_shown`. If you still see that shell name, you pasted the picture. That was the last paste on this page.

## Search before the suite

Do this before you run the suite. A picture that was pasted fails the middle column.

This table is not a paste. Do not copy it into a file. Search each work file, not this chapter. A pasted picture fails the search. The string in the middle column is only in the replaced app file. It is not in the filled test for that module. A correct paste may still contain an old name on a different line.

| Work file | Search for this | You should not see |
| --- | --- | --- |
| [spans.py](work/app/spans.py) | `Read the tool, the hash, and the token count` | `Report CPU and drop the trace fields` |
| [dashboard.py](work/app/dashboard.py) | `Latency, errors, tool failures, and the alert span` | `A board that only has CPU` |
| [meter.py](work/app/meter.py) | `Sum gateway cost by hospital` | `Cost for one hospital` |
| [cache.py](work/app/cache.py) | `Drop cached hours when the Ramadan circular changes` | `Keep the cached hours after the circular` |
| [drift.py](work/app/drift.py) | `Name the three drifts` | `Name one drift and stop` |
| [override.py](work/app/override.py) | `Share of stamped coordinator actions` | `Report no overrides` |
| [shadow.py](work/app/shadow.py) | `Keep the registered reply. Promote only after a comparison` | `Show the shadow reply and promote the candidate` |

The filled dashboard module does not say CPU. The dashboard page in [chapter 08](08-the-pages.md) says CPU stays flat. That is expected. The shell sentence `A board that only has CPU` must be gone from `dashboard.py`. If you still see the shell sentence, you pasted the picture.

If a row fails, go back to the chapter that replaces that file and paste that block again. Do not edit a test. A traceback names a test file. The app file is the same name without `test_`. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

## Run the suite

Open a new terminal in the course folder. The demo window is still inside `problem_simulation`. Do not use that window for the suite. If the `cd` line says the path cannot be found, this window is still inside `problem_simulation`. Open a new terminal in the course folder and run both lines.

```text
cd "Week 04/Day 02/Student_Copy/work"
python -m unittest discover -s tests -q
```

You should see a line that starts with `Ran 9 tests`, then a blank line, then `OK`.

If the line says `FAILED`, the app and the tests in this folder do not match. A traceback names a test file. The app file is the same name without `test_`. Paste that pair again. Do not repair the spaces by hand.

The suite does not read the pages, and it does not read the workflow. A suite that prints `OK` can still fail [chapter 09](09-finish.md).

This page is done when the search table matches and the suite has printed `Ran 9 tests` and `OK`. Do not run a check from this page.

Next: [08 — The pages](08-the-pages.md).
