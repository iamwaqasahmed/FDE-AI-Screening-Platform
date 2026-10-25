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

Paste only those eight blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged.

The shell test is a picture. The filled test is the paste. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

You are reading until the heading Replace the replicas. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. The four steps from chapter 05 are repeated above each paste. Everything above that first Replace heading is a picture. You do not paste it. If the block in front of you is above Replace the replicas, it is a picture. Do not paste it. If you are lost after that heading, stay on the Replace heading you have open. Finish it. Then do the next Replace heading down the page. Do not go back to the pictures. Do not run the suite on this page. [Chapter 07](07-the-outage.md) runs it after the rest of the app files are replaced.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, paste that block again from this chapter file. Do not repair the spaces by hand. Run `prepare_work.py` again only when a failure row in [chapter 09](09-finish.md) says so. A second run puts the shell tests back.

The check runs in chapter 09. Do not run it from this page.

The rows in these tests are a small fixture. They are not the pack rows. Do not copy a hash from the release file onto a test. Do not copy the drill budget or the timeout onto a test.

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the first line of each one. Do not edit them. The next block under a number is a picture of that file. Do not paste it. This block replaces nothing.

1. Open [replicas.py](packet/app/replicas.py). Search for `Place traffic on site-a only.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/replicas.py](work/app/replicas.py) is under the Replace heading for this file.

```text
"""Place traffic on site-a only."""


def placed(sites: dict) -> list[str]:
    del sites
    return ["site-a"]
```

That was a picture. Do not paste it. The next item is number 2.

2. Open [test_replicas.py](packet/tests/test_replicas.py). Search for `test_the_shell_places_one_site`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_replicas.py](work/tests/test_replicas.py) is under the Replace heading for this file.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from replicas import placed

_SITES = {"sites": [{"health": "down", "id": "site-a"}, {"health": "up", "id": "site-b"}]}


class ReplicaTests(unittest.TestCase):
    def test_the_shell_places_one_site(self) -> None:
        self.assertEqual(placed(_SITES), ["site-a"])


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 3.

3. Open [route.py](packet/app/route.py). Search for `Keep sending to site-a after it fails health.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/route.py](work/app/route.py) is under the Replace heading for this file.

```text
"""Keep sending to site-a after it fails health."""


def choose(sites: dict) -> str:
    del sites
    return "site-a"
```

That was a picture. Do not paste it. The next item is number 4.

4. Open [test_route.py](packet/tests/test_route.py). Search for `test_the_shell_stays_on_the_dead_site`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_route.py](work/tests/test_route.py) is under the Replace heading for this file.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from route import choose

_SITES = {"sites": [{"health": "down", "id": "site-a"}, {"health": "up", "id": "site-b"}]}


class RouteTests(unittest.TestCase):
    def test_the_shell_stays_on_the_dead_site(self) -> None:
        self.assertEqual(choose(_SITES), "site-a")


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 5.

5. Open [failover.py](packet/app/failover.py). Search for `Rebuild from the dead pod.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/failover.py](work/app/failover.py) is under the Replace heading for this file.

```text
"""Rebuild from the dead pod."""


def recover(drill: dict, rows: list) -> dict:
    del rows
    return {
        "pending": [],
        "seconds": int(drill["timeout_seconds"]),
        "site": str(drill.get("killed") or "site-a"),
    }
```

That was a picture. Do not paste it. The next item is number 6.

6. Open [test_failover.py](packet/tests/test_failover.py). Search for `test_the_shell_drops_the_approvals_and_waits`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_failover.py](work/tests/test_failover.py) is under the Replace heading for this file.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from failover import recover

_DRILL = {"budget_seconds": 10, "killed": "site-a", "timeout_seconds": 40}
_ROWS = [{"id": "apr-2", "status": "pending"}, {"id": "apr-1", "status": "pending"}]


class FailoverTests(unittest.TestCase):
    def test_the_shell_drops_the_approvals_and_waits(self) -> None:
        got = recover(_DRILL, _ROWS)
        self.assertEqual(got["site"], "site-a")
        self.assertEqual(got["pending"], [])
        self.assertEqual(got["seconds"], 40)


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 7.

7. Open [hashes.py](packet/app/hashes.py). Search for `Accept every hash the site advertises.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/hashes.py](work/app/hashes.py) is under the Replace heading for this file.

```text
"""Accept every hash the site advertises."""


def confirm(site: dict, register: list) -> list[str]:
    del register
    return sorted(str(model["id"]) for model in site.get("models") or [])
```

That was a picture. Do not paste it. The next item is number 8.

8. Open [test_hashes.py](packet/tests/test_hashes.py). Search for `test_the_shell_keeps_the_unregistered_hash`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_hashes.py](work/tests/test_hashes.py) is under the Replace heading for this file.

```text
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from hashes import confirm

_SITE = {
    "models": [
        {"hash": "sha256:aaa", "id": "lora-local"},
        {"hash": "sha256:bbb", "id": "local-smallx"},
    ]
}
_REGISTER = [{"hash": "sha256:aaa", "id": "lora-local"}]


class HashTests(unittest.TestCase):
    def test_the_shell_keeps_the_unregistered_hash(self) -> None:
        self.assertIn("local-smallx", confirm(_SITE, _REGISTER))


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. The shell test is a picture. The filled test is the paste.

You are done reading. Do not paste any block above this line. The next heading, Replace the replicas, is the first paste on this page.

## Replace the replicas

This block replaces [work/app/replicas.py](work/app/replicas.py). The full path is `Week 04/Day 04/Student_Copy/work/app/replicas.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/replicas.py](work/app/replicas.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Place every replica behind the balancer.`.

```text
"""Place every replica behind the balancer."""


def placed(sites: dict) -> list[str]:
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
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from replicas import placed

_SITES = {"sites": [{"health": "down", "id": "site-a"}, {"health": "up", "id": "site-b"}]}


class ReplicaTests(unittest.TestCase):
    def test_both_replicas_are_placed(self) -> None:
        self.assertEqual(placed(_SITES), ["site-a", "site-b"])


if __name__ == "__main__":
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
"""Send new traffic to a replica that is still healthy."""


def choose(sites: dict) -> str:
    rows = list(sites.get("sites") or [])
    healthy = [str(row["id"]) for row in rows if row.get("health") == "up"]
    down = {str(row["id"]) for row in rows if row.get("health") != "up"}
    if "site-a" in down and "site-b" in healthy:
        return "site-b"
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
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from route import choose

_SITES = {"sites": [{"health": "down", "id": "site-a"}, {"health": "up", "id": "site-b"}]}


class RouteTests(unittest.TestCase):
    def test_a_dead_site_a_lands_on_site_b(self) -> None:
        self.assertEqual(choose(_SITES), "site-b")


if __name__ == "__main__":
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
"""Resume in-flight approvals from the workflow store."""


def recover(drill: dict, rows: list) -> dict:
    pending = sorted(str(row["id"]) for row in rows if row.get("status") == "pending")
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
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from failover import recover

_DRILL = {"budget_seconds": 10, "killed": "site-a", "timeout_seconds": 40}
_ROWS = [{"id": "apr-2", "status": "pending"}, {"id": "apr-1", "status": "pending"}]


class FailoverTests(unittest.TestCase):
    def test_approvals_resume_inside_the_budget(self) -> None:
        got = recover(_DRILL, _ROWS)
        self.assertEqual(got["site"], "site-b")
        self.assertEqual(got["pending"], ["apr-1", "apr-2"])
        self.assertLessEqual(got["seconds"], _DRILL["budget_seconds"])


if __name__ == "__main__":
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
"""Keep a hash only when it matches the register."""


def confirm(site: dict, register: list) -> list[str]:
    approved = {str(row["id"]): str(row["hash"]) for row in register}
    kept = [
        str(model["id"])
        for model in site.get("models") or []
        if approved.get(str(model.get("id"))) == str(model.get("hash"))
    ]
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
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from hashes import confirm

_SITE = {
    "models": [
        {"hash": "sha256:aaa", "id": "lora-local"},
        {"hash": "sha256:bbb", "id": "local-smallx"},
    ]
}
_REGISTER = [{"hash": "sha256:aaa", "id": "lora-local"}]


class HashTests(unittest.TestCase):
    def test_only_a_matching_hash_stays(self) -> None:
        self.assertEqual(confirm(_SITE, _REGISTER), ["lora-local"])


if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_hashes.py](work/tests/test_hashes.py). You should see `test_only_a_matching_hash_stays`. You should not see `test_the_shell_keeps_the_unregistered_hash`. If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. That was the last paste on this page.

This page is done when the four work app files and their four work tests show the filled sentences, and you do not see the shell sentences named above. Do not run the suite yet. Do not run a check from this page.

Next: [07 — The outage](07-the-outage.md).
