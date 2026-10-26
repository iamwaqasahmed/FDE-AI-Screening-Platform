# 06 — The server

[Chapter 05](05-the-sprint.md) sequenced the sprint. This chapter replaces four app files and the work copies of their four tests. You do eight pastes, in this order. Finish one before you start the next. Do the app file and its test before you start the next pair.

1. [adapters.py](work/app/adapters.py), under Replace the adapters
2. [test_adapters.py](work/tests/test_adapters.py), under Replace the adapters test
3. [batch.py](work/app/batch.py), under Replace the batch
4. [test_batch.py](work/tests/test_batch.py), under Replace the batch test
5. [route.py](work/app/route.py), under Replace the route
6. [test_route.py](work/tests/test_route.py), under Replace the route test
7. [public.py](work/app/public.py), under Replace the public cache
8. [test_public.py](work/tests/test_public.py), under Replace the public cache test

Paste only those eight blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged.

The shell test is a picture. The filled test is the paste. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

You are reading until the heading Replace the adapters. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. The four steps from chapter 05 are repeated above each paste. The section How the replacement works sits above the first Replace heading. Read it. Do not paste it. Every code block above that Replace heading is a picture. You do not paste a picture. If the code block in front of you is above Replace the adapters, it is a picture. Do not paste it. If you are lost after that heading, stay on the Replace heading you have open. Finish it. Then do the next Replace heading down the page. Do not go back to the pictures.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, paste that block again from this chapter file. Do not repair the spaces by hand. Run `prepare_work.py` again only when a failure row in [chapter 09](09-finish.md) says so. A second run puts the shell tests back.

The checks run in chapter 09. Do not run them from this page. The suite runs in chapter 07, after the surge files are replaced.

The rows in these tests are a small fixture. They are not the pack rows. Do not copy a hash from the registry onto a test. Do not copy a rate from the release readme onto a test.

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the first line of each one. Do not edit them. The next block under a number is a picture of that file. Do not paste it. This block replaces nothing.

1. Open [adapters.py](packet/app/adapters.py). Search for `Serve ext-large and the lookalike.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/adapters.py](work/app/adapters.py) is under the Replace heading for this file.

```text
"""Serve ext-large and the lookalike.

This is the starter. The registry is discarded. The
result is ext-large, then the candidate id. A missing
candidate id becomes an empty string. The names are
not filtered, and they are not sorted.
"""


def loaded(registry: dict, candidate: dict) -> list[str]:
    """Ignore the registry. Return ext-large and the candidate id.

    The candidate id is read with get. When id is missing,
    the second name is an empty string.
    """
    # The registry argument is unused.
    del registry
    return ["ext-large", str(candidate.get("id") or "")]
```

That was a picture. Do not paste it. The next item is number 2.

2. Open [test_adapters.py](packet/tests/test_adapters.py). Search for `test_the_shell_loads_ext_large_and_the_lookalike`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_adapters.py](work/tests/test_adapters.py) is under the Replace heading for this file.

```text
"""Tests for the starter adapter loader.

The registry lists three approved local-small models:
lora-local, lora-extract, and lora-intent. The candidate
id is local-smallx. These tests lock the starter result:
ext-large, then local-smallx.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from adapters import loaded

# Three approved local-small models. The starter does not walk them.
_REGISTRY = {
    "models": [
        {"base": "local-small", "id": "lora-local", "status": "approved"},
        {"base": "local-small", "id": "lora-extract", "status": "approved"},
        {"base": "local-small", "id": "lora-intent", "status": "approved"},
    ]
}
# The unregistered id the starter returns beside ext-large.
_CANDIDATE = {"id": "local-smallx", "status": "unregistered"}


class AdapterTests(unittest.TestCase):
    """The two names the starter returns for this candidate."""

    def test_the_shell_loads_ext_large_and_the_lookalike(self) -> None:
        """The result is ext-large, then local-smallx.

        The approved ids in the registry are not that result.
        """
        self.assertEqual(loaded(_REGISTRY, _CANDIDATE), ["ext-large", "local-smallx"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 3.

3. Open [batch.py](packet/app/batch.py). Search for `Report the unbatched rate.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/batch.py](work/app/batch.py) is under the Replace heading for this file.

```text
"""Report the unbatched rate.

This is the starter. rate reads local_unbatched_tps.
hours uses that rate for the forecast backlog:
referrals times tokens per referral, divided by the
rate, divided by 3600, then rounded to 4 decimal places.
"""


def rate(sheet: dict) -> int:
    """Return the unbatched tokens-per-second figure on the sheet."""
    # The unbatched rate is the only figure this function reads.
    return int(sheet["local_unbatched_tps"])


def hours(sheet: dict, forecast: dict) -> float:
    """Return how many hours the backlog takes at the unbatched rate.

    backlog_referrals is the count. tokens_per_referral is
    the size of one referral. The rate comes from rate().
    Dividing by 3600 turns tokens per second into hours.
    The result is rounded to 4 decimal places.
    """
    referrals = int(forecast["backlog_referrals"])
    tokens_each = int(sheet["tokens_per_referral"])
    # 3600 seconds of throughput make one hour.
    return round(referrals * tokens_each / rate(sheet) / 3600, 4)
```

That was a picture. Do not paste it. The next item is number 4.

4. Open [test_batch.py](packet/tests/test_batch.py). Search for `test_the_shell_reports_the_unbatched_rate`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_batch.py](work/tests/test_batch.py) is under the Replace heading for this file.

```text
"""Tests for the starter batch rate.

The sheet holds a batched rate and an unbatched rate.
The forecast holds the backlog. These tests lock the
starter: rate is the unbatched figure, hours is 55.0,
and those hours are over 48.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from batch import hours, rate

# Both rates are on the sheet. The starter reads the unbatched one.
_SHEET = {"local_batched_tps": 100, "local_unbatched_tps": 40, "tokens_per_referral": 1000}
# The backlog passed into hours.
_FORECAST = {"backlog_referrals": 7920}


class BatchTests(unittest.TestCase):
    """The unbatched rate and the hours that rate produces."""

    def test_the_shell_reports_the_unbatched_rate(self) -> None:
        """rate is 40, hours is 55.0, and those hours are over 48."""
        self.assertEqual(rate(_SHEET), 40)
        self.assertEqual(hours(_SHEET, _FORECAST), 55.0)
        self.assertGreater(hours(_SHEET, _FORECAST), 48)


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 5.

5. Open [route.py](packet/app/route.py). Search for `Send every call to ext-large.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/route.py](work/app/route.py) is under the Replace heading for this file.

```text
"""Send every call to ext-large.

This is the starter. The row is discarded. target always
returns ext-large, so nothing on the row can change
the destination.
"""


def target(row: dict) -> str:
    """Ignore the row. Return ext-large for every call."""
    # The row is unused.
    del row
    return "ext-large"
```

That was a picture. Do not paste it. The next item is number 6.

6. Open [test_route.py](packet/tests/test_route.py). Search for `test_the_shell_sends_the_batch_to_ext_large`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_route.py](work/tests/test_route.py) is under the Replace heading for this file.

```text
"""Tests for the starter routing.

The batch row is phi and names lora-extract. The public
row is not phi. These tests lock the starter: both rows
go to ext-large.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from route import target

# A phi row. The starter does not read its adapter.
_BATCH = {"adapter": "lora-extract", "kind": "batch", "phi": True}
# A public row. It takes the same destination as the batch.
_PUBLIC = {"adapter": "", "kind": "public", "phi": False}


class RouteTests(unittest.TestCase):
    """Both rows, and the one destination the starter uses."""

    def test_the_shell_sends_the_batch_to_ext_large(self) -> None:
        """Both the phi batch and the public row are sent to ext-large."""
        self.assertEqual(target(_BATCH), "ext-large")
        self.assertEqual(target(_PUBLIC), "ext-large")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 7.

7. Open [public.py](packet/app/public.py). Search for `Call the model for a cached public answer.`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/public.py](work/app/public.py) is under the Replace heading for this file.

```text
"""Call the model for a cached public answer.

This is the starter. The store is discarded. answer
always returns the row text and a call count of 1.
A missing text becomes an empty string. A stored body
is never read.
"""


def answer(store: dict, row: dict) -> dict:
    """Ignore the store. Return the row text and one call.

    calls is 1 for every row. A missing text becomes an
    empty string.
    """
    # The store is unused, so every row spends a call.
    del store
    return {"body": str(row.get("text") or ""), "calls": 1}
```

That was a picture. Do not paste it. The next item is number 8.

8. Open [test_public.py](packet/tests/test_public.py). Search for `test_the_shell_calls_the_model_again`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_public.py](work/tests/test_public.py) is under the Replace heading for this file.

```text
"""Tests for the starter public answer.

The store already contains public-hours, and the row
asks for that same id. These tests lock the starter:
calls is 1 and the body is the row text.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from public import answer

# A stored answer for public-hours. The starter does not read it.
_STORE = {"public-hours": "Clinic hours are on the circular."}
# The row whose text the starter returns, with one call.
_ROW = {"id": "public-hours", "text": "Clinic hours are on the circular."}


class PublicTests(unittest.TestCase):
    """The call the starter spends on a stored public row."""

    def test_the_shell_calls_the_model_again(self) -> None:
        """calls is 1 and the body equals the row text."""
        got = answer(_STORE, _ROW)
        self.assertEqual(got["calls"], 1)
        self.assertEqual(got["body"], _ROW["text"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

That was a picture. Do not paste it.

You are done reading. Do not paste any block above this line. The next heading is How the replacement works. Read it. It is not a paste. The first paste is the heading Replace the adapters.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

One process, several adapters, and a rule for which traffic may leave the building.

`loaded` keeps registry rows whose status is approved and whose base is `local-small`. The candidate id and `ext-large` are excluded. Blank ids are skipped. The names come back sorted. The shell loaded the unregistered candidate because the name looked close.

`rate` reads the batched tokens per second. `hours` turns the forecast backlog into hours at that rate: referrals times tokens per referral, divided by the rate, divided by 3600. The unbatched rate is on the sheet and is not the one this function uses.

`target` keeps a phi row on the adapter named on that row. A missing adapter becomes `lora-local`. A row that is not phi goes to `ext-large`. Public text may leave. A referral batch may not, even when the external model is faster today.

`answer` returns a cached public body with zero model calls when the id is already in the store. A miss returns the row text and a call count of 1. The leaflet is the miss. The hours page is the hit.

Before you paste, say which rows `loaded` refuses, and which rows `target` refuses to send outside.

This section adds no file and no command.

## Replace the adapters

This block replaces [work/app/adapters.py](work/app/adapters.py). The full path is `Week 04/Day 03/Student_Copy/work/app/adapters.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/adapters.py](work/app/adapters.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Serve every approved adapter on one process.`.

```text
"""Serve every approved adapter on one process.

The registry lists models. A row is kept only when its
status is approved and its base is local-small. The
candidate id is excluded, and so is ext-large. A blank
id is skipped. The ids that remain come back sorted.
"""

from __future__ import annotations


def loaded(registry: dict, candidate: dict) -> list[str]:
    """Return the approved local-small ids, minus the candidate and ext-large.

    A row with any other status or base is skipped. A blank
    id is dropped. The candidate is blocked even when that
    id is not listed in the registry. The names are sorted.
    """
    # The candidate id and ext-large are not loaded.
    blocked = {str(candidate.get("id") or ""), "ext-large"}
    names = []
    for row in registry.get("models") or []:
        # Keep a row only when it is approved and local-small.
        if row.get("status") != "approved" or row.get("base") != "local-small":
            continue
        name = str(row.get("id") or "")
        if name and name not in blocked:
            names.append(name)
    return sorted(names)
```

Open [work/app/adapters.py](work/app/adapters.py). You should see `Serve every approved adapter on one process.`. You should not see `Serve ext-large and the lookalike.`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the adapters test.

## Replace the adapters test

This block replaces [work/tests/test_adapters.py](work/tests/test_adapters.py). The full path is `Week 04/Day 03/Student_Copy/work/tests/test_adapters.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/tests/test_adapters.py](work/tests/test_adapters.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_approved_adapters_share_one_process`.

```text
"""Tests for the finished adapter loader.

The registry lists three approved local-small models:
lora-local, lora-extract, and lora-intent. The candidate
id is local-smallx and its status is unregistered. The
assertion expects those three approved ids, sorted.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from adapters import loaded

# Three approved local-small models.
_REGISTRY = {
    "models": [
        {"base": "local-small", "id": "lora-local", "status": "approved"},
        {"base": "local-small", "id": "lora-extract", "status": "approved"},
        {"base": "local-small", "id": "lora-intent", "status": "approved"},
    ]
}
# An unregistered id. It is not part of the approved set.
_CANDIDATE = {"id": "local-smallx", "status": "unregistered"}


class AdapterTests(unittest.TestCase):
    """The names returned for this registry and this candidate."""

    def test_approved_adapters_share_one_process(self) -> None:
        """The result is lora-extract, lora-intent, and lora-local.

        That is the approved set, sorted. local-smallx is absent.
        """
        self.assertEqual(loaded(_REGISTRY, _CANDIDATE), ["lora-extract", "lora-intent", "lora-local"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

Open [work/tests/test_adapters.py](work/tests/test_adapters.py). You should see `test_approved_adapters_share_one_process`. You should not see `test_the_shell_loads_ext_large_and_the_lookalike`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the batch.

## Replace the batch

This block replaces [work/app/batch.py](work/app/batch.py). The full path is `Week 04/Day 03/Student_Copy/work/app/batch.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/batch.py](work/app/batch.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Report the batched rate and the hours it needs.`.

```text
"""Report the batched rate and the hours it needs.

rate reads local_batched_tps from the sheet. hours turns
the forecast backlog into hours at that rate: referrals
times tokens per referral, divided by the rate, divided
by 3600, then rounded to 4 decimal places.
"""

from __future__ import annotations


def rate(sheet: dict) -> int:
    """Return the batched tokens-per-second figure on the sheet."""
    # The batched rate is the only figure this function reads.
    return int(sheet["local_batched_tps"])


def hours(sheet: dict, forecast: dict) -> float:
    """Return how many hours the backlog takes at the batched rate.

    backlog_referrals is the count. tokens_per_referral is
    the size of one referral. The rate comes from rate().
    Dividing by 3600 turns tokens per second into hours.
    The result is rounded to 4 decimal places.
    """
    referrals = int(forecast["backlog_referrals"])
    tokens_each = int(sheet["tokens_per_referral"])
    # 3600 seconds of throughput make one hour.
    return round(referrals * tokens_each / rate(sheet) / 3600, 4)
```

Open [work/app/batch.py](work/app/batch.py). You should see `Report the batched rate and the hours it needs.`. You should not see `Report the unbatched rate.`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the batch test.

## Replace the batch test

This block replaces [work/tests/test_batch.py](work/tests/test_batch.py). The full path is `Week 04/Day 03/Student_Copy/work/tests/test_batch.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/tests/test_batch.py](work/tests/test_batch.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_the_batched_rate_clears_the_window`.

```text
"""Tests for the finished batch rate.

The sheet holds a batched rate, an unbatched rate, and
tokens per referral. The forecast holds the backlog.
The assertions expect the batched rate, the hours that
rate produces, and that those hours are at or under 48.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from batch import hours, rate

# Batched rate, unbatched rate, and tokens on one referral.
_SHEET = {"local_batched_tps": 100, "local_unbatched_tps": 40, "tokens_per_referral": 1000}
# The backlog the hours figure is checked against.
_FORECAST = {"backlog_referrals": 7920}


class BatchTests(unittest.TestCase):
    """The batched rate and the hours it needs for this backlog."""

    def test_the_batched_rate_clears_the_window(self) -> None:
        """rate is 100, hours is 22.0, and those hours are at or under 48."""
        self.assertEqual(rate(_SHEET), 100)
        self.assertEqual(hours(_SHEET, _FORECAST), 22.0)
        self.assertLessEqual(hours(_SHEET, _FORECAST), 48)


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

Open [work/tests/test_batch.py](work/tests/test_batch.py). You should see `test_the_batched_rate_clears_the_window`. You should not see `test_the_shell_reports_the_unbatched_rate`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the route.

## Replace the route

This block replaces [work/app/route.py](work/app/route.py). The full path is `Week 04/Day 03/Student_Copy/work/app/route.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/route.py](work/app/route.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Keep a phi row on its local adapter.`.

```text
"""Keep a phi row on its local adapter.

target reads phi. When phi is set, the call stays on the
adapter named on the row. A missing adapter becomes
lora-local. When phi is not set, the call goes to ext-large.
"""

from __future__ import annotations


def target(row: dict) -> str:
    """Send a phi row to its adapter. Send every other row to ext-large.

    phi is used as a true or false value. A missing adapter
    on a phi row is lora-local.
    """
    # A phi row stays on the adapter named on the row.
    if row.get("phi"):
        return str(row.get("adapter") or "lora-local")
    return "ext-large"
```

Open [work/app/route.py](work/app/route.py). You should see `Keep a phi row on its local adapter.`. You should not see `Send every call to ext-large.`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the route test.

## Replace the route test

This block replaces [work/tests/test_route.py](work/tests/test_route.py). The full path is `Week 04/Day 03/Student_Copy/work/tests/test_route.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/tests/test_route.py](work/tests/test_route.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_phi_stays_local_and_public_text_may_leave`.

```text
"""Tests for the finished routing.

The batch row is phi and names the adapter lora-extract.
The public row is not phi and names no adapter. The phi
row should stay on lora-extract. The public row should
go to ext-large.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from route import target

# A phi row whose adapter is lora-extract.
_BATCH = {"adapter": "lora-extract", "kind": "batch", "phi": True}
# A public row with phi clear and no adapter name.
_PUBLIC = {"adapter": "", "kind": "public", "phi": False}


class RouteTests(unittest.TestCase):
    """A phi batch and a public row."""

    def test_phi_stays_local_and_public_text_may_leave(self) -> None:
        """The phi batch stays on lora-extract. The public row goes to ext-large."""
        self.assertEqual(target(_BATCH), "lora-extract")
        self.assertEqual(target(_PUBLIC), "ext-large")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

Open [work/tests/test_route.py](work/tests/test_route.py). You should see `test_phi_stays_local_and_public_text_may_leave`. You should not see `test_the_shell_sends_the_batch_to_ext_large`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the public cache.

## Replace the public cache

This block replaces [work/app/public.py](work/app/public.py). The full path is `Week 04/Day 03/Student_Copy/work/app/public.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/app/public.py](work/app/public.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Return a cached public answer without a model call.`.

```text
"""Return a cached public answer without a model call.

answer looks the row id up in the store. A hit returns
the stored body and a call count of 0. A miss returns
the row text and a call count of 1. A missing id is an
empty string. A missing text is an empty string.
"""

from __future__ import annotations


def answer(store: dict, row: dict) -> dict:
    """Serve the stored body when the row id is already in the store.

    calls is 0 on a hit. calls is 1 when the id is absent,
    and the body is then the row text.
    """
    key = str(row.get("id") or "")
    # A stored id is served with no model call.
    if key in store:
        return {"body": str(store[key]), "calls": 0}
    return {"body": str(row.get("text") or ""), "calls": 1}
```

Open [work/app/public.py](work/app/public.py). You should see `Return a cached public answer without a model call.`. You should not see `Call the model for a cached public answer.`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the public cache test.

## Replace the public cache test

This block replaces [work/tests/test_public.py](work/tests/test_public.py). The full path is `Week 04/Day 03/Student_Copy/work/tests/test_public.py`. It does not replace the copy in `packet/`.

1. Open the work file named here, [work/tests/test_public.py](work/tests/test_public.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_a_cached_public_row_spends_no_call`.

```text
"""Tests for the finished public cache.

The store already contains public-hours. The first row
asks for that id. The leaflet row is not in the store.
A cached row should spend no call. A new row should
spend one call and return its own text.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from public import answer

# One stored public answer, under public-hours.
_STORE = {"public-hours": "Clinic hours are on the circular."}
# The same id as the stored answer.
_ROW = {"id": "public-hours", "text": "Clinic hours are on the circular."}
# A leaflet id that is not in the store.
_FRESH = {"id": "leaflet", "text": "Bring the card."}


class PublicTests(unittest.TestCase):
    """A cached public row and a row that is not cached yet."""

    def test_a_cached_public_row_spends_no_call(self) -> None:
        """The cached id returns the stored body and a call count of 0."""
        self.assertEqual(answer(_STORE, _ROW), {"body": _STORE["public-hours"], "calls": 0})

    def test_a_new_public_row_still_calls(self) -> None:
        """leaflet is not in the store, so calls is 1 and the body is its text."""
        self.assertEqual(answer(_STORE, _FRESH), {"body": "Bring the card.", "calls": 1})


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

Open [work/tests/test_public.py](work/tests/test_public.py). You should see `test_a_cached_public_row_spends_no_call`. You should not see `test_the_shell_calls_the_model_again`. You should also see `test_a_new_public_row_still_calls`. If you still see that shell sentence, you pasted the picture. Select all, delete the text, and paste the block under this heading again.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. That was the last paste on this page.

This page is done when the four app files and the four tests no longer show the shell sentences, and you have not run a check. The suite runs in chapter 07.

Next: [07 — The surge](07-the-surge.md).

