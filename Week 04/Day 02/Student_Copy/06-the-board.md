# 06 — The board

[Chapter 05](05-the-sprint.md) sequenced the sprint. This chapter replaces three app files and the work copies of their three tests. You do six pastes, in this order. Finish one before you start the next. Do the app file and its test before you start the next pair.

1. [spans.py](work/app/spans.py), under Replace the trace
2. [test_spans.py](work/tests/test_spans.py), under Replace the trace test
3. [dashboard.py](work/app/dashboard.py), under Replace the board
4. [test_dashboard.py](work/tests/test_dashboard.py), under Replace the board test
5. [meter.py](work/app/meter.py), under Replace the meter
6. [test_meter.py](work/tests/test_meter.py), under Replace the meter test

Paste only those six blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged.

The shell test is a picture. The filled test is the paste. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

You are reading until the heading Replace the trace. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. The four steps from chapter 05 are repeated above each paste. The section How the replacement works sits above the first Replace heading. Read it. Do not paste it. Every code block above that Replace heading is a picture. You do not paste a picture. If you are lost after that heading, stay on the Replace heading you have open. Finish it. Then do the next Replace heading down the page. Do not go back to the pictures.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, paste that block again from this chapter file. Do not repair the spaces by hand. Run `prepare_work.py` again only when a failure row in [chapter 09](09-finish.md) says so. A second run puts the shell tests back.

The checks run in chapter 09. Do not run them from this page. The suite runs in chapter 07, after the hours files are replaced.

The rows in these tests are a small fixture. They are not the pack rows. Do not copy a hash from the replay onto a test. Do not copy a cost from the gateway onto a test.

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the first line of each one. Do not edit them. The next block under a number is a picture of that file. Do not paste it. This block replaces nothing.

1. Open [spans.py](packet/app/spans.py). Search for `Report CPU and drop the trace fields`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/spans.py](work/app/spans.py) is under the Replace heading for this file.

```text
"""Report CPU and drop the trace fields.

read returns a dict with only cpu. A missing cpu key becomes zero.
A cpu value that is present is returned as it is, including zero.
No other field on the span is copied.
"""

from __future__ import annotations


def read(span: dict) -> dict:
    """Return the cpu value and nothing else.

    A missing cpu is zero. The span is not changed.
    """
    # The default applies only when the key is absent. Other keys are dropped.
    return {"cpu": span.get("cpu", 0)}
```

That was a picture. Do not paste it. The next item is number 2.

2. Open [test_spans.py](packet/tests/test_spans.py). Search for `test_the_trace_fields_are_dropped`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_spans.py](work/tests/test_spans.py) is under the Replace heading for this file.

```text
"""Tests for a span reader that keeps only cpu.

The fixture span has cpu, a hash, a token count, and a tool. The
result is expected to be the cpu value alone.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from spans import read


class SpanTests(unittest.TestCase):
    """Check that the hash, tokens, and tool are not returned."""

    def test_the_trace_fields_are_dropped(self) -> None:
        """read returns the cpu from the fixture and nothing else.

        The hash, tokens, and tool are on the span. They are not in the
        result. The assertion is the cpu dict.
        """
        # A span with cpu plus hash, tokens, and tool. Only cpu is expected back.
        span = {"cpu": 0.2, "hash": "sha256:abc", "tokens": 128, "tool": "referral.status"}
        self.assertEqual(read(span), {"cpu": 0.2})


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 3.

3. Open [dashboard.py](packet/app/dashboard.py). Search for `A board that only has CPU`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/dashboard.py](work/app/dashboard.py) is under the Replace heading for this file.

```text
"""A board that only has CPU.

board reads the cpu of the first span and returns that as the only
key. An empty list returns a board whose cpu is zero. Later spans
are not read. A first span with no cpu key raises.
"""

from __future__ import annotations


def board(spans: list[dict]) -> dict:
    """Return the first span's cpu, or zero when there are no spans.

    The result has a single key, cpu. The span list is not changed.
    """
    # Only the first span is read, and only its cpu key.
    cpu = spans[0]["cpu"] if spans else 0
    return {"cpu": cpu}
```

That was a picture. Do not paste it. The next item is number 4.

4. Open [test_dashboard.py](packet/tests/test_dashboard.py). Search for `test_the_board_reports_cpu_only`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_dashboard.py](work/tests/test_dashboard.py) is under the Replace heading for this file.

```text
"""Tests for a board that reports cpu only.

The fixture includes latency, status, tools, and an alert time.
The board is expected to report the cpu of the first span and
nothing else.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from dashboard import board

# Spans with cpu, latency, status, and tools, plus an alert span.
_SPANS = [
    {"cpu": 0.2, "latency_ms": 180, "name": "model", "status": "ok", "tool": "referral.status"},
    {"cpu": 0.2, "latency_ms": 2400, "name": "tool", "status": "error", "tool": "referral.status"},
    {"at": "2027-02-01T09:15:00+03:00", "cpu": 0.2, "latency_ms": 0, "name": "alert", "status": "error", "tool": ""},
]


class BoardTests(unittest.TestCase):
    """Check that the board dict has only the first span's cpu."""

    def test_the_board_reports_cpu_only(self) -> None:
        """The board is the cpu value from the first span.

        The expected dict has that one key. Latency, status, tools, and
        the alert time are in the fixture and are not in the result.
        """
        self.assertEqual(board(_SPANS), {"cpu": 0.2})


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. The next item is number 5.

5. Open [meter.py](packet/app/meter.py). Search for `Cost for one hospital`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/meter.py](work/app/meter.py) is under the Replace heading for this file.

```text
"""Cost for one hospital.

cost sums sar for rows whose hospital is h-wadi and ignores every
other hospital. The result always has that one key. When no row
matches, the total is zero. A matching row must have sar.
"""

from __future__ import annotations


def cost(rows: list[dict]) -> dict:
    """Sum sar for h-wadi and ignore every other hospital.

    The result is a new dict with that single key. The input rows stay put.
    """
    # The hospital check runs before sar is read, so other rows need no sar.
    total = sum(int(row["sar"]) for row in rows if row.get("hospital") == "h-wadi")
    # The key is present even when the total is zero.
    return {"h-wadi": total}
```

That was a picture. Do not paste it. The next item is number 6.

6. Open [test_meter.py](packet/tests/test_meter.py). Search for `test_one_hospital_is_costed`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_meter.py](work/tests/test_meter.py) is under the Replace heading for this file.

```text
"""Tests for a cost that keeps one hospital.

The fixture has a row for h-wadi and a row for another hospital.
Only h-wadi is expected in the result, with that row's sar.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from meter import cost

# One row for h-wadi and one row for another hospital.
_ROWS = [
    {"hospital": "h-wadi", "sar": 11, "tokens": 400},
    {"hospital": "h-nakhl", "sar": 7, "tokens": 200},
]


class MeterTests(unittest.TestCase):
    """Check that the other hospital is left out of the total."""

    def test_one_hospital_is_costed(self) -> None:
        """The result is the h-wadi total, and the other hospital is absent.

        The first assertion is that total. The second checks the other
        hospital key is missing.
        """
        self.assertEqual(cost(_ROWS), {"h-wadi": 11})
        self.assertNotIn("h-nakhl", cost(_ROWS))


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it.

You are done reading. Do not paste any block above this line. The next heading is How the replacement works. Read it. It is not a paste. The first paste is the heading Replace the trace.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

The incident is in the spans, not in the CPU.

`read` copies hash, tokens, and tool off one span. A missing token count becomes zero. CPU and every other field are left behind. The span itself is not changed. The shell kept CPU and dropped the tool.

`board` separates the alert span from the body. The body is every span whose name is not `alert`. `latency_p95` is a high percentile of the body latencies. `error_rate` is the share of body spans whose status is error. Tool failures are those error spans that also name a tool. `alert_at` is the time on the alert span. A board of CPU stays flat through this replay and misses all four numbers.

`cost` sums `sar` by hospital, in the order hospitals first appear. A hospital with no rows is omitted. The total is every hospital, not one hospital billed for the cluster.

Before you paste, say which span is left out of the latency and the error rate, and which three fields `read` keeps.

This section adds no file and no command.

## Replace the trace

This block replaces [work/app/spans.py](work/app/spans.py). The full path is `Week 04/Day 02/Student_Copy/work/app/spans.py`. It does not replace the copy in `packet/app`.

1. Open the work file named here, [work/app/spans.py](work/app/spans.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Read the tool, the hash, and the token count`.

```text
"""Read the tool, the hash, and the token count.

read copies hash, tokens, and tool into a new dict. A missing hash or
tool becomes an empty string. A missing token count becomes zero.
tokens is forced to an int. Any other field on the span is left behind.
The span itself is not changed.
"""

from __future__ import annotations


def read(span: dict) -> dict:
    """Return hash, tokens, and tool from the span.

    A missing token count becomes zero before int() runs. The span is
    not changed.
    """
    # Empty hash, tokens, and tool are stored as blanks or zero. Other keys are dropped.
    return {"hash": span.get("hash") or "", "tokens": int(span.get("tokens") or 0), "tool": span.get("tool") or ""}
```

Open [work/app/spans.py](work/app/spans.py). You should see `Read the tool, the hash, and the token count`. You should not see `Report CPU and drop the trace fields`. If you still see that shell sentence, you pasted the picture. Delete the work file and paste the block under this heading again. If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand. Stay on this page. The next heading is Replace the trace test.

## Replace the trace test

This block replaces [work/tests/test_spans.py](work/tests/test_spans.py). The full path is `Week 04/Day 02/Student_Copy/work/tests/test_spans.py`. It does not replace the copy in `packet/tests`. The row in this test is a small fixture. It is not a pack row.

1. Open the work file named here, [work/tests/test_spans.py](work/tests/test_spans.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_a_span_keeps_the_tool_the_hash_and_the_tokens`.

```text
"""Tests for a span reader that keeps the trace fields.

The fixture span has cpu, a hash, a token count, and a tool. The
reader should keep the hash, the tokens, and the tool.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from spans import read


class SpanTests(unittest.TestCase):
    """Check the hash, the token count, and the tool."""

    def test_a_span_keeps_the_tool_the_hash_and_the_tokens(self) -> None:
        """read returns hash, tokens, and tool from the fixture.

        cpu is on the span and is not in the result. The expected dict is
        the assertion.
        """
        # A span with cpu plus the hash, token count, and tool the reader should keep.
        span = {"cpu": 0.2, "hash": "sha256:abc", "tokens": 128, "tool": "referral.status"}
        self.assertEqual(read(span), {"hash": "sha256:abc", "tokens": 128, "tool": "referral.status"})


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_spans.py](work/tests/test_spans.py). You should see `test_a_span_keeps_the_tool_the_hash_and_the_tokens`. You should not see `test_the_trace_fields_are_dropped`. If you still see that shell name, you pasted the picture. Stay on this page. The next heading is Replace the board.

## Replace the board

This block replaces [work/app/dashboard.py](work/app/dashboard.py). The full path is `Week 04/Day 02/Student_Copy/work/app/dashboard.py`. It does not replace the copy in `packet/app`.

1. Open the work file named here, [work/app/dashboard.py](work/app/dashboard.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Latency, errors, tool failures, and the alert span`.

```text
"""Latency, errors, tool failures, and the alert span.

board separates the alert span from the body. The body is every span
whose name is not alert. latency_p95 is a high percentile of the body
latency values, with a missing latency read as zero. error_rate is the
share of body spans whose status is error, or zero when the body is
empty. tool_failures counts error spans that name a tool. An empty tool
does not count. alert_at is the at value of the alert span. The search
assumes that span is present.
"""

from __future__ import annotations


def _p95(values: list[int]) -> int:
    """Return the latency at the rank computed from the list length.

    An empty list returns zero. The values are sorted first. The rank
    expression lives in the body, and the selected slot is that rank
    minus one.
    """
    # Sort a copy. The caller's list order is left as it arrived.
    ordered = sorted(values)
    # An empty body has no latency to rank.
    if not ordered:
        return 0
    # One-based rank into the sorted list. The return below selects that slot.
    rank = (95 * len(ordered) + 99) // 100
    return ordered[rank - 1]


def board(spans: list[dict]) -> dict:
    """Summarize the body spans and record when the alert span fired.

    The result keys are alert_at, error_rate, latency_p95, and
    tool_failures. error_rate divides the error count by the body length
    when the body is not empty.
    """
    # The alert span is kept out of the latency, error, and tool counts.
    body = [span for span in spans if span.get("name") != "alert"]
    latencies = [int(span.get("latency_ms") or 0) for span in body]
    errors = [span for span in body if span.get("status") == "error"]
    # An error with a missing or empty tool is an error, not a tool failure.
    tools = [span for span in errors if span.get("tool")]
    # The first alert span supplies the time. A missing alert span raises.
    alert = next(span.get("at") for span in spans if span.get("name") == "alert")
    return {
        "alert_at": alert,
        "error_rate": (len(errors) / len(body)) if body else 0.0,
        "latency_p95": _p95(latencies),
        "tool_failures": len(tools),
    }
```

Open [work/app/dashboard.py](work/app/dashboard.py). You should see `Latency, errors, tool failures, and the alert span`. You should not see `A board that only has CPU`. If you still see that shell sentence, you pasted the picture. The filled module does not say CPU. [Chapter 08](08-the-pages.md) writes the dashboard page, and that page says CPU stays flat. That is expected. If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand. Stay on this page. The next heading is Replace the board test.

## Replace the board test

This block replaces [work/tests/test_dashboard.py](work/tests/test_dashboard.py). The full path is `Week 04/Day 02/Student_Copy/work/tests/test_dashboard.py`. It does not replace the copy in `packet/tests`. The rows in this test are a small fixture. They are not the pack rows.

1. Open the work file named here, [work/tests/test_dashboard.py](work/tests/test_dashboard.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_the_board_names_latency_errors_tool_failures_and_the_alert`.

```text
"""Tests for a board of latency, errors, tool failures, and the alert.

The fixture is a model span, tool spans, error spans that name a tool,
and an alert span with a time. The board should report that alert time,
the error share, the latency percentile, and the tool-failure count.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from dashboard import board

# Body spans, including tool errors, and a final span named alert.
_SPANS = [
    {"cpu": 0.2, "latency_ms": 180, "name": "model", "status": "ok", "tool": "referral.status"},
    {"cpu": 0.2, "latency_ms": 220, "name": "tool", "status": "ok", "tool": "referral.status"},
    {"cpu": 0.2, "latency_ms": 2400, "name": "tool", "status": "error", "tool": "referral.status"},
    {"cpu": 0.2, "latency_ms": 2600, "name": "tool", "status": "error", "tool": "referral.status"},
    {"cpu": 0.2, "latency_ms": 2800, "name": "tool", "status": "error", "tool": "referral.status"},
    {"at": "2027-02-01T09:15:00+03:00", "cpu": 0.2, "latency_ms": 0, "name": "alert", "status": "error", "tool": ""},
]


class BoardTests(unittest.TestCase):
    """Check the summary dict the board returns for the span fixture."""

    # The alert span supplies the time. The other spans supply the rest.
    def test_the_board_names_latency_errors_tool_failures_and_the_alert(self) -> None:
        """Each key in the expected dict is checked.

        alert_at is the time on the alert span. error_rate, latency_p95,
        and tool_failures come from the other spans. The assertion is the
        whole dict.
        """
        # The four keys are checked together as one dict.
        self.assertEqual(
            board(_SPANS),
            {
                "alert_at": "2027-02-01T09:15:00+03:00",
                "error_rate": 0.6,
                "latency_p95": 2800,
                "tool_failures": 3,
            },
        )


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_dashboard.py](work/tests/test_dashboard.py). You should see `test_the_board_names_latency_errors_tool_failures_and_the_alert`. You should not see `test_the_board_reports_cpu_only`. If you still see that shell name, you pasted the picture. The fixture still has a `cpu` field on each span. That is expected. The shell sentence `A board that only has CPU` must be gone from `dashboard.py`. Stay on this page. The next heading is Replace the meter.

## Replace the meter

This block replaces [work/app/meter.py](work/app/meter.py). The full path is `Week 04/Day 02/Student_Copy/work/app/meter.py`. It does not replace the copy in `packet/app`.

1. Open the work file named here, [work/app/meter.py](work/app/meter.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Sum gateway cost by hospital`.

```text
"""Sum gateway cost by hospital.

cost adds each row's sar into a total for that hospital. Hospitals
appear in the order they are first seen. A hospital with no rows is
omitted. The row must have hospital and sar. The totals start at zero
for a hospital's first row.
"""

from __future__ import annotations


def cost(rows: list[dict]) -> dict:
    """Return hospital names mapped to the sum of their sar values.

    int() reads sar. The result is a new dict. The input rows are not changed.
    """
    totals: dict[str, int] = {}
    for row in rows:
        # The hospital is stored as text. A missing key raises.
        hospital = str(row["hospital"])
        # Later rows for the same hospital add to the total already stored.
        totals[hospital] = totals.get(hospital, 0) + int(row["sar"])
    return totals
```

Open [work/app/meter.py](work/app/meter.py). You should see `Sum gateway cost by hospital`. You should not see `Cost for one hospital`. If you still see that shell sentence, you pasted the picture. If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand. Stay on this page. The next heading is Replace the meter test.

## Replace the meter test

This block replaces [work/tests/test_meter.py](work/tests/test_meter.py). The full path is `Week 04/Day 02/Student_Copy/work/tests/test_meter.py`. It does not replace the copy in `packet/tests`. The rows in this test are a small fixture. They are not the pack rows. Do not copy a cost from the gateway onto this file.

1. Open the work file named here, [work/tests/test_meter.py](work/tests/test_meter.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_every_hospital_is_summed`.

```text
"""Tests for hospital cost summed across every hospital in the fixture.

Some hospitals have more than one row. cost should add sar by
hospital and include every hospital.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from meter import cost

# Sar rows for several hospitals. One hospital appears twice.
_ROWS = [
    {"hospital": "h-wadi", "sar": 11, "tokens": 400},
    {"hospital": "h-wadi", "sar": 4, "tokens": 100},
    {"hospital": "h-nakhl", "sar": 7, "tokens": 200},
    {"hospital": "h-safra", "sar": 4, "tokens": 90},
]


class MeterTests(unittest.TestCase):
    """Check the per-hospital sar totals."""

    def test_every_hospital_is_summed(self) -> None:
        """Each hospital key is the sum of its sar values.

        The expected dict is the assertion. Every hospital in the fixture
        is a key. Token counts are not part of the result.
        """
        self.assertEqual(cost(_ROWS), {"h-nakhl": 7, "h-safra": 4, "h-wadi": 15})


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_meter.py](work/tests/test_meter.py). You should see `test_every_hospital_is_summed`. You should not see `test_one_hospital_is_costed`. If you still see that shell name, you pasted the picture. That was the last paste on this page.

This page is done when the three work app files and their three work tests no longer show the shell sentences, and you have not run a check. [Chapter 07](07-the-hours.md) replaces the other four modules and then runs the suite.

Next: [07 — The hours](07-the-hours.md).
