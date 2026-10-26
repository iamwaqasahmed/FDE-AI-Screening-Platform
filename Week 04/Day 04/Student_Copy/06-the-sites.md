# 06 — The sites

[Chapter 05](05-the-sprint.md) replaced the sprint. This chapter replaces four app files and the work copies of their four tests. You do eight pastes, in this order. Finish one before you start the next. Do the app file and its test before you start the next pair.

1. [replicas.py](work/app/replicas.py), under Replace the replicas
2. [test_replicas.py](work/tests/test_replicas.py), under Replace the replicas test
3. [route.py](work/app/route.py), under Replace the route
4. [test_route.py](work/tests/test_route.py), under Replace the route test
5. [failover.py](work/app/failover.py), under Replace the failover
6. [test_failover.py](work/tests/test_failover.py), under Replace the failover test
7. [hashes.py](work/app/hashes.py), under Replace the hashes
8. [test_hashes.py](work/tests/test_hashes.py), under Replace the hashes test

Paste only those eight blocks. The numbers in that list are the pastes. The numbers under Read these files are a different list. Those are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged.

The shell test is a picture. The filled test is the paste. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

You are reading until the heading Replace the replicas. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. The four steps from chapter 05 are repeated above each paste. The section How the replacement works sits above the first Replace heading. Read it. Do not paste it. Every code block above that Replace heading is a picture. You do not paste a picture. If the code block in front of you is above Replace the replicas, it is a picture. Do not paste it. If you are lost after that heading, stay on the Replace heading you have open. Finish it. Then do the next Replace heading down the page. Do not go back to the pictures. Do not run the suite on this page. [Chapter 07](07-the-outage.md) runs it after the rest of the app files are replaced.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, paste that block again from this chapter file. Do not repair the spaces by hand. Run `prepare_work.py` again only when a failure row in [chapter 09](09-finish.md) says so. A second run puts the shell tests back.

The check runs in chapter 09. Do not run it from this page.

The rows in these tests are a small fixture. They are not the pack rows. Do not copy a hash from the release file onto a test. Do not copy the drill budget or the timeout onto a test.

## Read these files

You are reading. You are not pasting yet. These numbers are not the paste list at the top of the page. Open these in the packet. Read the first line of each one. Do not edit them. The next block under a number is a picture of that file. Do not paste it. This block replaces nothing. An item is done when the search finds the shell sentence in the packet file. Close that file. Then do the next number.

1. Open [replicas.py](packet/app/replicas.py). Search for `Place traffic on site-a only.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/replicas.py](work/app/replicas.py) is under the Replace heading for this file.

```text
"""Place traffic on site-a only.

This is the starter. The sites argument is discarded.
placed always returns site-a and no other id.
"""


def placed(sites: dict) -> list[str]:
    """Ignore the sites list. Return site-a only."""
    # No site id is read from the argument.
    del sites
    return ["site-a"]
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 2.

2. Open [test_replicas.py](packet/tests/test_replicas.py). Search for `test_the_shell_places_one_site`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_replicas.py](work/tests/test_replicas.py) is under the Replace heading for this file.

```text
"""Tests for the starter replica placement.

site-a is down and site-b is up. These tests lock the
starter: the only placed id is site-a.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from replicas import placed

# site-a is down and site-b is up. The starter places site-a only.
_SITES = {"sites": [{"health": "down", "id": "site-a"}, {"health": "up", "id": "site-b"}]}


class ReplicaTests(unittest.TestCase):
    """The single site the starter places."""

    def test_the_shell_places_one_site(self) -> None:
        """The result is site-a alone. site-b is not placed."""
        self.assertEqual(placed(_SITES), ["site-a"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 3.

3. Open [route.py](packet/app/route.py). Search for `Keep sending to site-a after it fails health.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/route.py](work/app/route.py) is under the Replace heading for this file.

```text
"""Keep sending to site-a after it fails health.

This is the starter. The sites argument is discarded.
choose always returns site-a. Health on the list cannot
change the result.
"""


def choose(sites: dict) -> str:
    """Ignore the sites list. Return site-a."""
    # Health is not read. The choice stays site-a.
    del sites
    return "site-a"
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 4.

4. Open [test_route.py](packet/tests/test_route.py). Search for `test_the_shell_stays_on_the_dead_site`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_route.py](work/tests/test_route.py) is under the Replace heading for this file.

```text
"""Tests for the starter health route.

site-a is down and site-b is up. These tests lock the
starter: the choice stays site-a.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from route import choose

# site-a is down and site-b is up. The starter still returns site-a.
_SITES = {"sites": [{"health": "down", "id": "site-a"}, {"health": "up", "id": "site-b"}]}


class RouteTests(unittest.TestCase):
    """The down site the starter keeps choosing."""

    def test_the_shell_stays_on_the_dead_site(self) -> None:
        """The result is site-a even though its health is down."""
        self.assertEqual(choose(_SITES), "site-a")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 5.

5. Open [failover.py](packet/app/failover.py). Search for `Rebuild from the dead pod.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/failover.py](work/app/failover.py) is under the Replace heading for this file.

```text
"""Rebuild from the dead pod.

This is the starter. The rows are discarded, so pending
is always an empty list. seconds is timeout_seconds
from the drill. site is the killed name, or site-a when
killed is missing.
"""


def recover(drill: dict, rows: list) -> dict:
    """Drop the rows. Report the timeout and the killed site.

    pending is empty. A missing killed value becomes site-a.
    """
    # The workflow rows are unused.
    del rows
    return {
        "pending": [],
        "seconds": int(drill["timeout_seconds"]),
        "site": str(drill.get("killed") or "site-a"),
    }
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 6.

6. Open [test_failover.py](packet/tests/test_failover.py). Search for `test_the_shell_drops_the_approvals_and_waits`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_failover.py](work/tests/test_failover.py) is under the Replace heading for this file.

```text
"""Tests for the starter failover.

The drill budget is 10 seconds, the killed site is
site-a, and the timeout is 40 seconds. Two rows are
pending. These tests lock the starter: the site is
site-a, pending is empty, and seconds is 40.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from failover import recover

# Budget 10, killed site-a, and the timeout of 40 the starter reports.
_DRILL = {"budget_seconds": 10, "killed": "site-a", "timeout_seconds": 40}
# Pending approvals. The starter returns an empty list.
_ROWS = [{"id": "apr-2", "status": "pending"}, {"id": "apr-1", "status": "pending"}]


class FailoverTests(unittest.TestCase):
    """The killed site, an empty pending list, and the timeout."""

    def test_the_shell_drops_the_approvals_and_waits(self) -> None:
        """The site is site-a, pending is empty, and seconds is 40.

        It calls recover, then checks the site, the empty pending list, and the seconds.
        """
        got = recover(_DRILL, _ROWS)
        self.assertEqual(got["site"], "site-a")
        self.assertEqual(got["pending"], [])
        self.assertEqual(got["seconds"], 40)


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 7.

7. Open [hashes.py](packet/app/hashes.py). Search for `Accept every hash the site advertises.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/hashes.py](work/app/hashes.py) is under the Replace heading for this file.

```text
"""Accept every hash the site advertises.

This is the starter. The register is discarded. confirm
returns every model id on the site, sorted. A missing
models list returns an empty list. The hash on a model
is not read.
"""


def confirm(site: dict, register: list) -> list[str]:
    """Ignore the register. Return every model id on the site, sorted.

    Ids are turned into strings. A missing models list
    yields nothing.
    """
    # The register is unused, so no advertised id is dropped.
    del register
    return sorted(str(model["id"]) for model in site.get("models") or [])
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 8.

8. Open [test_hashes.py](packet/tests/test_hashes.py). Search for `test_the_shell_keeps_the_unregistered_hash`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_hashes.py](work/tests/test_hashes.py) is under the Replace heading for this file.

```text
"""Tests for the starter hash check.

The site lists lora-local and local-smallx. The register
lists lora-local only. These tests lock the starter:
local-smallx is still in the result.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from hashes import confirm

# lora-local and local-smallx are both advertised.
_SITE = {
    "models": [
        {"hash": "sha256:aaa", "id": "lora-local"},
        {"hash": "sha256:bbb", "id": "local-smallx"},
    ]
}
# Only lora-local is registered. The starter still keeps both.
_REGISTER = [{"hash": "sha256:aaa", "id": "lora-local"}]


class HashTests(unittest.TestCase):
    """The unregistered id the starter keeps."""

    def test_the_shell_keeps_the_unregistered_hash(self) -> None:
        """local-smallx is kept. The register does not remove it."""
        self.assertIn("local-smallx", confirm(_SITE, _REGISTER))


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The shell test is a picture. The filled test is the paste.

You are done reading. Do not paste any block above this line. If you are lost, you are still in the pictures. The next heading is How the replacement works. Read it. It is not a paste. The first paste is the heading Replace the replicas. Do not scroll back up to paste a picture.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

Site-a dies. The approvals do not.

`placed` returns every replica id, sorted, including the one that is down. Both sites sit behind the balancer. The shell returns only `site-a`. `site-a` is down, so `site-b` never enters the set. The filled file places both.

`choose` sends new traffic to a replica that is still healthy. When site-a is not up and site-b is up, the choice is site-b. Otherwise it takes the first healthy id. No healthy site returns an empty string. Health has to be the string `up`.

`recover` keeps approval ids whose status is pending, sorts them, and returns them with the drill budget and `site-b`. Those rows live in the workflow store. They are not on the pod that was killed. The shell rebuilt from the dead pod and dropped them.

`confirm` keeps a site model only when that id is on the register and the hash strings are equal. An extra id that site-b advertises is dropped. A matching id with a different hash is dropped.

Before you paste, say where a pending approval is read from, and which site receives new traffic.

This section adds no file and no command.

## Replace the replicas

This block replaces [work/app/replicas.py](work/app/replicas.py). The full path is `Week 04/Day 04/Student_Copy/work/app/replicas.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/replicas.py](work/app/replicas.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Place every replica behind the balancer.`.

```text
"""Place every replica behind the balancer.

placed reads the sites list and returns every id,
sorted. Only the id is used. A missing sites list
returns an empty list.
"""


def placed(sites: dict) -> list[str]:
    """Return every site id, sorted.

    A missing sites list places nothing.
    """
    # Every id is placed. The list is sorted.
    return sorted(str(row["id"]) for row in sites.get("sites") or [])
```

Open [work/app/replicas.py](work/app/replicas.py). You should see `Place every replica behind the balancer.`. You should not see `Place traffic on site-a only.`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the replicas test.

## Replace the replicas test

This block replaces [work/tests/test_replicas.py](work/tests/test_replicas.py). The full path is `Week 04/Day 04/Student_Copy/work/tests/test_replicas.py`. It does not replace the copy in `packet/`. The shell test is a picture. This block is the filled test.

1. Open the work file named here, [work/tests/test_replicas.py](work/tests/test_replicas.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_both_replicas_are_placed`.

```text
"""Tests for the finished replica placement.

site-a is down and site-b is up. Both ids should be
placed, with site-a before site-b.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from replicas import placed

# site-a is down and site-b is up. Both ids are placed.
_SITES = {"sites": [{"health": "down", "id": "site-a"}, {"health": "up", "id": "site-b"}]}


class ReplicaTests(unittest.TestCase):
    """Both site ids, including the one that is down."""

    def test_both_replicas_are_placed(self) -> None:
        """site-a and site-b are both placed."""
        self.assertEqual(placed(_SITES), ["site-a", "site-b"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

Open [work/tests/test_replicas.py](work/tests/test_replicas.py). You should see `test_both_replicas_are_placed`. You should not see `test_the_shell_places_one_site`. If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the route.

## Replace the route

This block replaces [work/app/route.py](work/app/route.py). The full path is `Week 04/Day 04/Student_Copy/work/app/route.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/route.py](work/app/route.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Send new traffic to a replica that is still healthy.`.

```text
"""Send new traffic to a replica that is still healthy.

choose splits the sites by health. health must be the
string up to count as healthy. Any other health,
including a missing health, counts as not up. When
site-a is in that not-up set and site-b is healthy,
the choice is site-b. Otherwise the choice is the first
healthy id, in list order, not sorted order. When no
site is healthy, the result is an empty string.
"""


def choose(sites: dict) -> str:
    """Prefer site-b when site-a is not up and site-b is up.

    The fallback is the first healthy id in list order.
    No healthy site returns an empty string. A site that
    is absent is not treated as site-a being down.
    """
    rows = list(sites.get("sites") or [])
    healthy = [str(row["id"]) for row in rows if row.get("health") == "up"]
    down = {str(row["id"]) for row in rows if row.get("health") != "up"}
    if "site-a" in down and "site-b" in healthy:
        # site-a is not up, and site-b is up.
        return "site-b"
    # Otherwise the first healthy id, or an empty string.
    return healthy[0] if healthy else ""
```

Open [work/app/route.py](work/app/route.py). You should see `Send new traffic to a replica that is still healthy.`. You should not see `Keep sending to site-a after it fails health.`. If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the route test.

## Replace the route test

This block replaces [work/tests/test_route.py](work/tests/test_route.py). The full path is `Week 04/Day 04/Student_Copy/work/tests/test_route.py`. It does not replace the copy in `packet/`. The shell test is a picture. This block is the filled test.

1. Open the work file named here, [work/tests/test_route.py](work/tests/test_route.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_a_dead_site_a_lands_on_site_b`.

```text
"""Tests for the finished health route.

site-a is down and site-b is up. New traffic should go
to site-b.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from route import choose

# site-a is down and site-b is up.
_SITES = {"sites": [{"health": "down", "id": "site-a"}, {"health": "up", "id": "site-b"}]}


class RouteTests(unittest.TestCase):
    """Traffic moving off a down site-a."""

    def test_a_dead_site_a_lands_on_site_b(self) -> None:
        """site-a is down, so the choice is site-b."""
        self.assertEqual(choose(_SITES), "site-b")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

Open [work/tests/test_route.py](work/tests/test_route.py). You should see `test_a_dead_site_a_lands_on_site_b`. You should not see `test_the_shell_stays_on_the_dead_site`. If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the failover.

## Replace the failover

This block replaces [work/app/failover.py](work/app/failover.py). The full path is `Week 04/Day 04/Student_Copy/work/app/failover.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/failover.py](work/app/failover.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Resume in-flight approvals from the workflow store.`.

```text
"""Resume in-flight approvals from the workflow store.

recover keeps ids whose status is pending, sorts those
ids, and returns them under pending. seconds is
budget_seconds from the drill. site is site-b. A row
that is not pending is left out. A row with no status
is left out.
"""


def recover(drill: dict, rows: list) -> dict:
    """Return the sorted pending ids, the budget, and site-b.

    Only status pending is kept. seconds is the drill
    budget as an integer. site is always site-b.
    """
    pending = sorted(str(row["id"]) for row in rows if row.get("status") == "pending")
    # Resume on site-b, inside the drill budget.
    return {"pending": pending, "seconds": int(drill["budget_seconds"]), "site": "site-b"}
```

Open [work/app/failover.py](work/app/failover.py). You should see `Resume in-flight approvals from the workflow store.`. You should not see `Rebuild from the dead pod.`. If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the failover test.

## Replace the failover test

This block replaces [work/tests/test_failover.py](work/tests/test_failover.py). The full path is `Week 04/Day 04/Student_Copy/work/tests/test_failover.py`. It does not replace the copy in `packet/`. The shell test is a picture. This block is the filled test.

1. Open the work file named here, [work/tests/test_failover.py](work/tests/test_failover.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_approvals_resume_inside_the_budget`.

```text
"""Tests for the finished failover.

The drill budget is 10 seconds, the killed site is
site-a, and the timeout is 40 seconds. The pending rows
are apr-2 and apr-1. Recovery should use site-b, list
those ids sorted, and keep seconds within the budget.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from failover import recover

# Budget 10 seconds, site-a killed, timeout 40 seconds.
_DRILL = {"budget_seconds": 10, "killed": "site-a", "timeout_seconds": 40}
# Two pending approvals, listed out of sorted order.
_ROWS = [{"id": "apr-2", "status": "pending"}, {"id": "apr-1", "status": "pending"}]


class FailoverTests(unittest.TestCase):
    """Pending approvals resumed on site-b."""

    def test_approvals_resume_inside_the_budget(self) -> None:
        """The site is site-b, pending is apr-1 then apr-2, and seconds stays within 10.

        It calls recover, then checks site-b, the sorted pending ids, and the budget.
        """
        got = recover(_DRILL, _ROWS)
        self.assertEqual(got["site"], "site-b")
        self.assertEqual(got["pending"], ["apr-1", "apr-2"])
        self.assertLessEqual(got["seconds"], _DRILL["budget_seconds"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

Open [work/tests/test_failover.py](work/tests/test_failover.py). You should see `test_approvals_resume_inside_the_budget`. You should not see `test_the_shell_drops_the_approvals_and_waits`. If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the hashes.

## Replace the hashes

This block replaces [work/app/hashes.py](work/app/hashes.py). The full path is `Week 04/Day 04/Student_Copy/work/app/hashes.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/hashes.py](work/app/hashes.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Keep a hash only when it matches the register.`.

```text
"""Keep a hash only when it matches the register.

confirm maps each register id to its hash. A model on
the site is kept only when that id is in the map and
the hash strings are equal. The kept ids come back
sorted. An id the register does not list is dropped.
A missing models list returns nothing.
"""


def confirm(site: dict, register: list) -> list[str]:
    """Return site model ids whose hash equals the registered hash.

    The compare is the hash string for the same id. A
    different hash is left out. A missing models list
    yields an empty result. The ids are sorted.
    """
    approved = {str(row["id"]): str(row["hash"]) for row in register}
    kept = [
        str(model["id"])
        for model in site.get("models") or []
        if approved.get(str(model.get("id"))) == str(model.get("hash"))
    ]
    # Stable order for the ids that matched.
    return sorted(kept)
```

Open [work/app/hashes.py](work/app/hashes.py). You should see `Keep a hash only when it matches the register.`. You should not see `Accept every hash the site advertises.`. If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the hashes test.

## Replace the hashes test

This block replaces [work/tests/test_hashes.py](work/tests/test_hashes.py). The full path is `Week 04/Day 04/Student_Copy/work/tests/test_hashes.py`. It does not replace the copy in `packet/`. The shell test is a picture. This block is the filled test.

1. Open the work file named here, [work/tests/test_hashes.py](work/tests/test_hashes.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_only_a_matching_hash_stays`.

```text
"""Tests for the finished hash check.

The site lists lora-local and local-smallx. The register
lists lora-local only, and that shared id carries the
same hash on both sides. The assertion expects only
lora-local.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from hashes import confirm

# lora-local matches the register. local-smallx uses another hash.
_SITE = {
    "models": [
        {"hash": "sha256:aaa", "id": "lora-local"},
        {"hash": "sha256:bbb", "id": "local-smallx"},
    ]
}
# The only registered id is lora-local.
_REGISTER = [{"hash": "sha256:aaa", "id": "lora-local"}]


class HashTests(unittest.TestCase):
    """The one id whose hash is on the register."""

    def test_only_a_matching_hash_stays(self) -> None:
        """Only lora-local is kept. local-smallx is not in the result."""
        self.assertEqual(confirm(_SITE, _REGISTER), ["lora-local"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

Open [work/tests/test_hashes.py](work/tests/test_hashes.py). You should see `test_only_a_matching_hash_stays`. You should not see `test_the_shell_keeps_the_unregistered_hash`. If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. That was the last paste on this page. The line that starts with Next is the end of this page.

This page is done when the four work app files and their four work tests show the filled sentences, and you do not see the shell sentences named above. Do not run the suite on this page. If you run it anyway, it can still print `Ran 8 tests` and `OK`. That count is not the finished suite. [Chapter 07](07-the-outage.md) prints `Ran 9 tests` after the rest of the files are replaced. Do not run a check from this page.

Next: [07 — The outage](07-the-outage.md).
