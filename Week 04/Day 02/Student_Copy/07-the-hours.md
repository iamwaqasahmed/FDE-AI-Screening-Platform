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

You are reading until the heading Replace the cache. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. The four steps from chapter 05 are repeated above each paste. Everything above that first Replace heading is a picture, or a file with no picture. You do not paste it. If you are lost after that heading, stay on the Replace heading you have open. Finish it. Then do the next Replace heading down the page. Do not go back to the pictures.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, paste that block again from this chapter file. Do not repair the spaces by hand. Run `prepare_work.py` again only when a failure row in [chapter 09](09-finish.md) says so. A second run puts the shell tests back.

The checks run in chapter 09. Do not run them from this page. The suite on this page runs only after the search table.

The rows in these tests are a small fixture. They are not the pack rows. Do not copy a hash from the replay onto a test. Do not write a share on a page outside the block you are pasting.

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the first line of each one. Do not edit them. A picture belongs to the numbered item above it. The cache test has no picture.

1. Open [cache.py](packet/app/cache.py). Search for `Keep the cached hours after the circular`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/cache.py](work/app/cache.py) is under the Replace heading for this file.

```text
"""Keep the cached hours after the circular."""

from __future__ import annotations


def answer(store: dict, event: dict) -> str:
    del event
    return str(store.get("hours") or "")
```

That was a picture. Do not paste it. The next item is number 2.

2. Open [test_cache.py](packet/tests/test_cache.py). Search for `test_the_cache_keeps_the_old_hours`. That name is the shell test. There is no picture of this file. There is no block under this item. The paste that replaces [work/tests/test_cache.py](work/tests/test_cache.py) is under Replace the cache test. Close the packet file. The next item is number 3.

3. Open [drift.py](packet/app/drift.py). Search for `Name one drift and stop`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/drift.py](work/app/drift.py) is under the Replace heading for this file.

```text
"""Name one drift and stop."""

from __future__ import annotations


def name(row: dict) -> str:
    del row
    return "ramadan hours"
```

That was a picture. Do not paste it. The next item is number 4.

4. Open [test_drift.py](packet/tests/test_drift.py). Search for `test_every_row_is_named_hours`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_drift.py](work/tests/test_drift.py) is under the Replace heading for this file.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from drift import name


class DriftTests(unittest.TestCase):
    def test_every_row_is_named_hours(self) -> None:
        self.assertEqual(name({"kind": "clinic"}), "ramadan hours")
        self.assertEqual(name({"kind": "criteria"}), "ramadan hours")


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 5.

5. Open [override.py](packet/app/override.py). Search for `Report no overrides`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/override.py](work/app/override.py) is under the Replace heading for this file.

```text
"""Report no overrides."""

from __future__ import annotations


def rate(rows: list[dict]) -> float:
    del rows
    return 0.0
```

That was a picture. Do not paste it. The next item is number 6.

6. Open [test_override.py](packet/tests/test_override.py). Search for `test_the_rate_stays_at_zero`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_override.py](work/tests/test_override.py) is under the Replace heading for this file.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from override import rate


class OverrideTests(unittest.TestCase):
    def test_the_rate_stays_at_zero(self) -> None:
        self.assertEqual(rate([{"stamped": True}, {"stamped": False}]), 0.0)


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 7.

7. Open [shadow.py](packet/app/shadow.py). Search for `Show the shadow reply and promote the candidate`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/shadow.py](work/app/shadow.py) is under the Replace heading for this file.

```text
"""Show the shadow reply and promote the candidate."""

from __future__ import annotations


def reply(turn: dict) -> str:
    return str(turn.get("shadow_reply") or "")


def promote(comparison: dict) -> str:
    return str(comparison.get("candidate_hash") or "")
```

That was a picture. Do not paste it. The next item is number 8.

8. Open [test_shadow.py](packet/tests/test_shadow.py). Search for `test_the_shadow_reply_is_shown`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_shadow.py](work/tests/test_shadow.py) is under the Replace heading for this file.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from shadow import promote, reply

_TURN = {
    "candidate_hash": "sha256:candidate",
    "registered_reply": "Your referral is still pending.",
    "shadow_reply": "Your referral was accepted by the shadow adapter.",
}


class ShadowTests(unittest.TestCase):
    def test_the_shadow_reply_is_shown(self) -> None:
        self.assertEqual(reply(_TURN), _TURN["shadow_reply"])

    def test_a_hash_is_promoted_with_no_comparison(self) -> None:
        self.assertEqual(promote({"candidate_hash": "sha256:candidate", "compared": False}), "sha256:candidate")


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it.

You are done reading. Do not paste any block above this line. The next heading, Replace the cache, is the first paste on this page.

## Replace the cache

This block replaces [work/app/cache.py](work/app/cache.py). The full path is `Week 04/Day 02/Student_Copy/work/app/cache.py`. It does not replace the copy in `packet/app`.

1. Open the work file named here, [work/app/cache.py](work/app/cache.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Drop cached hours when the Ramadan circular changes`.

```text
"""Drop cached hours when the Ramadan circular changes."""

from __future__ import annotations


def answer(store: dict, event: dict) -> str:
    if event.get("topic") == "document.changed" and event.get("doc_id") == "circ-ramadan-hours":
        return str(event.get("body") or "")
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
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from cache import answer

_OLD = "Code hrs-ramadan closes the evening clinics at 21:00."
_EVENT = {
    "body": "Evening clinics close at 01:00. Daytime slots are not offered.",
    "doc_id": "circ-ramadan-hours",
    "topic": "document.changed",
}
_OTHER = {"body": "Bring the card.", "doc_id": "leaflet-prep", "topic": "document.changed"}


class CacheTests(unittest.TestCase):
    def test_the_circular_replaces_the_cached_hours(self) -> None:
        self.assertEqual(answer({"hours": _OLD}, _EVENT), _EVENT["body"])
        self.assertNotIn("21:00", answer({"hours": _OLD}, _EVENT))

    def test_another_document_leaves_the_hours_cache(self) -> None:
        self.assertEqual(answer({"hours": _OLD}, _OTHER), _OLD)


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
"""Name the three drifts."""

from __future__ import annotations

_LABELS = {"clinic": "campaign clinic", "criteria": "criteria v4", "hours": "ramadan hours"}


def name(row: dict) -> str:
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
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from drift import name


class DriftTests(unittest.TestCase):
    def test_each_kind_has_its_name(self) -> None:
        self.assertEqual(name({"kind": "hours"}), "ramadan hours")
        self.assertEqual(name({"kind": "criteria"}), "criteria v4")
        self.assertEqual(name({"kind": "clinic"}), "campaign clinic")


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
"""Share of stamped coordinator actions."""

from __future__ import annotations


def rate(rows: list[dict]) -> float:
    if not rows:
        return 0.0
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
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from override import rate


class OverrideTests(unittest.TestCase):
    def test_the_rate_is_the_stamped_share(self) -> None:
        rows = [{"stamped": True}, {"stamped": False}]
        self.assertEqual(rate(rows), 0.5)


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
"""Keep the registered reply. Promote only after a comparison."""

from __future__ import annotations


def reply(turn: dict) -> str:
    return str(turn.get("registered_reply") or "")


def promote(comparison: dict) -> str:
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
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from shadow import promote, reply

_TURN = {
    "candidate_hash": "sha256:candidate",
    "registered_reply": "Your referral is still pending.",
    "shadow_reply": "Your referral was accepted by the shadow adapter.",
}


class ShadowTests(unittest.TestCase):
    def test_the_patient_reply_stays_registered(self) -> None:
        self.assertEqual(reply(_TURN), _TURN["registered_reply"])

    def test_promotion_waits_for_a_comparison(self) -> None:
        bare = {"candidate_hash": "sha256:candidate", "compared": False, "matched": False}
        ready = {"candidate_hash": "sha256:candidate", "compared": True, "matched": True}
        self.assertEqual(promote(bare), "")
        self.assertEqual(promote(ready), "sha256:candidate")


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
