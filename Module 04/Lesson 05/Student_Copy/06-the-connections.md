# 06 — The connections

[Chapter 05](05-the-sprint.md) replaced the sprint. This chapter replaces five app files and the work copies of their five tests. You do ten pastes, in this order. Finish one before you start the next. Do the app file and its test before you start the next pair.

1. [signin.py](work/app/signin.py), under Replace the sign-in
2. [test_signin.py](work/tests/test_signin.py), under Replace the sign-in test
3. [bus.py](work/app/bus.py), under Replace the bus
4. [test_bus.py](work/tests/test_bus.py), under Replace the bus test
5. [handoff.py](work/app/handoff.py), under Replace the handoff
6. [test_handoff.py](work/tests/test_handoff.py), under Replace the handoff test
7. [leave.py](work/app/leave.py), under Replace leave
8. [test_leave.py](work/tests/test_leave.py), under Replace the leave test
9. [warehouse.py](work/app/warehouse.py), under Replace the warehouse
10. [test_warehouse.py](work/tests/test_warehouse.py), under Replace the warehouse test

Paste only those ten blocks. The numbers in that list are the pastes. The numbers under Read these files are a different list. Those are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged.

The shell test is a picture. The filled test is the paste. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

You are reading until the heading Replace the sign-in. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. The four steps from chapter 05 are repeated above each paste. The section How the replacement works sits above the first Replace heading. Read it. Do not paste it. Every code block above that Replace heading is a picture. You do not paste a picture. If the code block in front of you is above Replace the sign-in, it is a picture. Do not paste it. If you are lost after that heading, stay on the Replace heading you have open. Finish it. Then do the next Replace heading down the page. Do not go back to the pictures. Do not run the suite on this page. [Chapter 07](07-the-proposal.md) runs it after the rest of the app files are replaced.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, paste that block again from this chapter file. Do not repair the spaces by hand. Run `prepare_work.py` again only when a failure row in [chapter 09](09-finish.md) says so. A second run puts the shell tests back.

The checks run in chapter 09. Do not run one from this page.

The rows in these tests are a small fixture. They are not the pack rows. Do not copy the attack text onto a test. Do not write a minute count onto a test.

## Read these files

You are reading. You are not pasting yet. These numbers are not the paste list at the top of the page. Open these in the packet. Read the first line of each one. Do not edit them. The next block under a number is a picture of that file. Do not paste it. This block replaces nothing. An item is done when the search finds the shell sentence in the packet file. Close that file. Then do the next number.

1. Open [signin.py](packet/app/signin.py). Search for `Treat every token as staff.` That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/signin.py](work/app/signin.py) is under the Replace heading for this file.

```text
"""Treat every token as staff.

This is the starter. It keeps the id, then marks the login as staff
without reading kind. A service token is a machine login. This shell
still accepts it. The finished module accepts a login only when
kind is staff, and it refuses a machine token.
"""


def accept(actor: dict) -> dict:
    """Record the id and mark every login as staff.

    kind and role are ignored. A service token gets the same result
    as a coordinator.
    """
    # Keep the id for the row. An absent id stays blank.
    actor_id = str(actor.get("id") or "")
    # The shell does not look at kind, so a machine token is marked staff.
    return {"actor": actor_id, "staff": True}
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 2.

2. Open [test_signin.py](packet/tests/test_signin.py). Search for `test_the_shell_treats_the_service_token_as_staff`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_signin.py](work/tests/test_signin.py) is under the Replace heading for this file.

```text
"""Tests for the starter sign-in.

The shell marks every login as staff. These tests lock that
mistake in place. They pass beside the starter module. They fail
after that module is replaced and this test file is still the starter.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from signin import accept

# A machine login. An admin role must not be what this shell checks.
_SERVICE = {"id": "svc-integration", "kind": "service", "role": "admin"}
# A person who works in the contact center.
_STAFF = {"id": "coord-1", "kind": "staff", "role": "coordinator"}


class SignInTests(unittest.TestCase):
    """Tests for the starter sign-in."""
    def test_the_shell_treats_the_service_token_as_staff(self) -> None:
        """Both the person and the service token come back as staff.

        That is the starter mistake. kind is not consulted.
        """
        self.assertTrue(accept(_STAFF)["staff"])
        self.assertTrue(accept(_SERVICE)["staff"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

That was a picture. Do not paste it. This item is done when the search finds that shell name in the packet file. Close the packet file. The next item is number 3.

3. Open [bus.py](packet/app/bus.py). Search for `Drop an unknown field, and drop a cancellation.` That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/bus.py](work/app/bus.py) is under the Replace heading for this file.

```text
"""Drop an unknown field, and drop a cancellation.

This is the starter. An event is kept only when every key is id,
session, or topic, and the topic is not a cancellation. One extra
field makes the whole event look unknown, so it is dropped. A
cancellation is dropped even when its keys are on the list.
The finished module keeps every event. An unfamiliar field does
not remove it, and a cancellation stays on the bus.
"""

# Keys this shell is willing to read. Any other key is treated as unknown.
_KNOWN = {"id", "session", "topic"}


def consume(event: dict) -> dict:
    """Drop the event when a key is new, or when the topic is a cancellation.

    A dropped event comes back with an empty id, kept set to false,
    and an empty topic. The caller cannot tell a new field apart
    from a cancellation. Both disappear.
    """
    # set(event) is the keys on this row. Subtract the known names.
    unknown = set(event) - _KNOWN
    cancelled = event.get("topic") == "session.cancelled"
    if unknown or cancelled:
        return {"id": "", "kept": False, "topic": ""}
    return {
        "id": str(event.get("id") or ""),
        "kept": True,
        "topic": str(event.get("topic") or ""),
    }
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 4.

4. Open [test_bus.py](packet/tests/test_bus.py). Search for `test_the_shell_drops_the_extra_field_and_the_cancellation`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_bus.py](work/tests/test_bus.py) is under the Replace heading for this file.

```text
"""Tests for the starter bus.

The shell throws away an event that carries an extra field, and it
throws away a cancellation. These tests expect both to be dropped.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from bus import consume

# A cancellation whose keys are only the ones a strict reader expects.
_CANCEL = {"id": "evt-cancel", "session": "ses-1", "topic": "session.cancelled"}
# The same topic, plus a field a strict reader would call unknown.
_EXTRA = {"disposition": "kept", "id": "evt-extra", "session": "ses-2", "topic": "session.cancelled"}


class BusTests(unittest.TestCase):
    """Tests for the starter bus."""
    def test_the_shell_drops_the_extra_field_and_the_cancellation(self) -> None:
        """Neither row is kept.

        The extra field and the cancellation are both thrown away.
        """
        self.assertFalse(consume(_EXTRA)["kept"])
        self.assertFalse(consume(_CANCEL)["kept"])


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. This item is done when the search finds that shell name in the packet file. Close the packet file. The next item is number 5.

5. Open [handoff.py](packet/app/handoff.py). Search for `Return an agent id and an empty summary.` That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/handoff.py](work/app/handoff.py) is under the Replace heading for this file.

```text
"""Return an agent id and an empty summary.

This is the starter. It ignores the call. Every row comes back as
agent cc-1, with an empty summary, and the call is not marked
refused. The summary that was spoken is thrown away. The finished
module refuses a call whose summary is blank, and it keeps the
summary when one was given.
"""


def handoff(call: dict) -> dict:
    """Ignore the call. Return one fixed agent id and an empty summary.

    The call is discarded, so a missing summary cannot change the
    result. refused stays false even when the summary was blank.
    """
    # The argument is unused. The shell never reads the summary.
    del call
    return {"agent": "cc-1", "refused": False, "summary": ""}
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 6.

6. Open [test_handoff.py](packet/tests/test_handoff.py). Search for `test_the_shell_returns_an_empty_summary`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_handoff.py](work/tests/test_handoff.py) is under the Replace heading for this file.

```text
"""Tests for the starter handoff.

The shell returns a blank summary and does not refuse the call,
even when a summary was on the row.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from handoff import handoff

# A call that did carry a spoken summary. The shell still ignores it.
_STATUS = {"agent": "cc-1", "id": "call-status", "summary": "Referral status, still pending."}


class HandoffTests(unittest.TestCase):
    """Tests for the starter handoff."""
    def test_the_shell_returns_an_empty_summary(self) -> None:
        """The summary is blank and the call is not refused.

        The spoken text on the row never reaches the result.
        """
        got = handoff(_STATUS)
        self.assertEqual(got["summary"], "")
        self.assertFalse(got["refused"])


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. This item is done when the search finds that shell name in the packet file. Close the packet file. The next item is number 7.

7. Open [leave.py](packet/app/leave.py). Search for `Ignore leave that arrives after the session is published.` That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/leave.py](work/app/leave.py) is under the Replace heading for this file.

```text
"""Ignore leave that arrives after the session is published.

This is the starter. It does not read the leave row. The session
stays at the status it already has, and no bus event is emitted.
A late leave for the same consultant should cancel that session.
This shell never does that.
"""


def apply(session: dict, leave: dict) -> dict:
    """Leave the session as it was published, and emit no event.

    The leave row is discarded. A later entry time cannot change
    the status. A missing status is reported as published.
    """
    # The shell does not compare consultants or clocks.
    del leave
    return {"event": "", "status": str(session.get("status") or "published")}
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 8.

8. Open [test_leave.py](packet/tests/test_leave.py). Search for `test_the_shell_leaves_the_session_published`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_leave.py](work/tests/test_leave.py) is under the Replace heading for this file.

```text
"""Tests for the starter leave rule.

The shell leaves the session published and emits no event, even
when the leave time is after the session was published.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from leave import apply

# Entered later than the session was published, for the same consultant.
_LEAVE = {"consultant": "con-1", "entered_at": "2027-02-04T11:00:00", "id": "lv-1"}
# Already published earlier the same morning.
_SESSION = {"consultant": "con-1", "id": "ses-9", "published_at": "2027-02-04T08:00:00", "status": "published"}


class LeaveTests(unittest.TestCase):
    """Tests for the starter leave rule."""
    def test_the_shell_leaves_the_session_published(self) -> None:
        """Status stays published. No bus event is emitted.

        The later leave row does not change the result.
        """
        got = apply(_SESSION, _LEAVE)
        self.assertEqual(got["status"], "published")
        self.assertEqual(got["event"], "")


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. This item is done when the search finds that shell name in the packet file. Close the packet file. The next item is number 9.

9. Open [warehouse.py](packet/app/warehouse.py). Search for `Read the booking date.` That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/warehouse.py](work/app/warehouse.py) is under the Replace heading for this file.

```text
"""Read the booking date.

This is the starter. It returns booking_date, the day the slot was
booked. That day is later than the day the referral was written.
The finished module returns referred_at instead.
"""


def clock(row: dict) -> str:
    """Return the booking date and ignore the referred date.

    A missing booking date is an empty string.
    """
    # referred_at is the other column. This starter does not return it.
    return str(row.get("booking_date") or "")
```

That was a picture. Do not paste it. This item is done when the search finds that shell sentence in the packet file. Close the packet file. The next item is number 10.

10. Open [test_warehouse.py](packet/tests/test_warehouse.py). Search for `test_the_shell_reads_the_booking_date`. That name is the shell test. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/tests/test_warehouse.py](work/tests/test_warehouse.py) is under the Replace heading for this file.

```text
"""Tests for the starter warehouse clock.

The shell returns the booking column on the row, not the referred date.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from warehouse import clock

# Two dates. The shell is expected to return the booking column.
_ROW = {"booking_date": "2027-01-20", "id": "wh-1", "referred_at": "2027-01-02"}


class WarehouseTests(unittest.TestCase):
    """Tests for the starter warehouse clock."""
    def test_the_shell_reads_the_booking_date(self) -> None:
        """The result is the day the slot was booked, not the referral day."""
        self.assertEqual(clock(_ROW), "2027-01-20")


if __name__ == "__main__":
    unittest.main()
```

That was a picture. Do not paste it. This item is done when the search finds that shell name in the packet file. Close the packet file. The ten pictures are done. Do not paste any block above this line. The next heading is How the replacement works. Read it. It is not a paste. The first paste is the heading Replace the sign-in.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

Five connections. Each one refuses a shortcut the shell took.

`accept` counts a login as staff only when `kind` is staff. Role is not read. A service token with role admin is still a machine. It does not open the staff console. Module 2 signed a patient and a coordinator in, and kept `svc-integration` from signing a patient in. This function is the staff console. The same service id is still not staff. The shell treated every token as staff.

`consume` keeps the event, including a field this consumer does not know. Dropping an unfamiliar field also dropped `session.cancelled`, and the clinic session stayed on the book. A cancellation is an ordinary topic. It is kept.

`handoff` refuses a summary that is empty or only spaces, and it clears the agent id so nobody is assigned. A summary with text keeps the agent. The shell returned an empty summary and still assigned the call.

`apply` cancels the published session when the leave names the same consultant and the leave time is later than the publish time. The row then names the bus event `session.cancelled`. Leave for a different consultant does not cancel this session. The shell ignored late leave.

`clock` returns `referred_at`. `booking_date` is on the row and is not the referral clock. Module 1 already found that the wait chart's date column was the wrong clock. Module 2, Lesson 2's mart read that same `booking_date` column. This is the same mistake on the warehouse feed.

Before you paste, say which token is refused, what a handoff must contain, and which date the warehouse clock returns.

This section adds no file and no command.

## Replace the sign-in

This block replaces the app file [work/app/signin.py](work/app/signin.py). The full path is `Module 04/Lesson 05/Student_Copy/work/app/signin.py`. It does not replace the test. The test is the next heading.

1. Open the work file named here, [work/app/signin.py](work/app/signin.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Accept a staff role. Refuse a service token.`

```text
"""Accept a staff role. Refuse a service token.

Staff sign-in is for a person. The contact center sends an actor
with an id, a kind, and a role. kind "staff" is a person who works
here. kind "service" is a machine token. A machine token can carry
role "admin" and still must not pass as staff.

accept keeps the id and reports whether this login is staff.
A missing id is stored as an empty string. A missing kind is not staff.
"""


def accept(actor: dict) -> dict:
    """Record the id. Count the login as staff only when kind is staff.

    Role is not read. An admin role on a service token does not
    make that token a person.
    """
    # Keep the id for the audit row. An absent id stays blank.
    actor_id = str(actor.get("id") or "")
    # kind is the only staff test. "service" fails it.
    is_staff = actor.get("kind") == "staff"
    return {"actor": actor_id, "staff": is_staff}
```

Open [work/app/signin.py](work/app/signin.py). You should see `Accept a staff role. Refuse a service token.` You should not see `Treat every token as staff.` If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the sign-in test.

## Replace the sign-in test

This block replaces the test file [work/tests/test_signin.py](work/tests/test_signin.py). The full path is `Module 04/Lesson 05/Student_Copy/work/tests/test_signin.py`. The picture of the shell test is above. This block is the paste. It does not replace [signin.py](work/app/signin.py).

1. Open the work file named here, [work/tests/test_signin.py](work/tests/test_signin.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_staff_is_accepted_and_the_service_token_is_refused`.

```text
"""Tests for the finished staff sign-in.

A coordinator is a person and is accepted. A service token is a
machine login, even when its role says admin, and it is refused.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from signin import accept

# A machine login. role admin must not make this staff.
_SERVICE = {"id": "svc-integration", "kind": "service", "role": "admin"}
# A person who works in the contact center.
_STAFF = {"id": "coord-1", "kind": "staff", "role": "coordinator"}


class SignInTests(unittest.TestCase):
    """Tests for the finished staff sign-in."""
    def test_staff_is_accepted_and_the_service_token_is_refused(self) -> None:
        """The person is staff. The service token is not."""
        self.assertTrue(accept(_STAFF)["staff"])
        self.assertFalse(accept(_SERVICE)["staff"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
```

Open [work/tests/test_signin.py](work/tests/test_signin.py). You should see `test_staff_is_accepted_and_the_service_token_is_refused`. You should not see `test_the_shell_treats_the_service_token_as_staff`. If you still see that shell name, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the bus.

## Replace the bus

This block replaces the app file [work/app/bus.py](work/app/bus.py). The full path is `Module 04/Lesson 05/Student_Copy/work/app/bus.py`. It does not replace the test. The test is the next heading.

1. Open the work file named here, [work/app/bus.py](work/app/bus.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Keep the event, including a field this consumer does not know.`

```text
"""Keep the event, including a field this consumer does not know.

The bus carries events between the contact center, the warehouse,
and HR. A new field on an event is still part of that event.
Throwing the event away because a field is unfamiliar also throws
away a cancellation, and the session stays on the board.

consume keeps the id and the topic. kept is true for every event
this function accepts, including a cancellation.
"""


def consume(event: dict) -> dict:
    """Keep the id and the topic. An extra field does not remove the event.

    A cancellation is a normal topic. It is kept the same way as any
    other topic. A missing id or topic is stored as an empty string.
    """
    # There is no allow-list of keys. A field this consumer has not
    # seen before stays on the event, and the event is still kept.
    return {
        "id": str(event.get("id") or ""),
        "kept": True,
        "topic": str(event.get("topic") or ""),
    }
```

Open [work/app/bus.py](work/app/bus.py). You should see `Keep the event, including a field this consumer does not know.` You should not see `Drop an unknown field, and drop a cancellation.` If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the bus test.

## Replace the bus test

This block replaces the test file [work/tests/test_bus.py](work/tests/test_bus.py). The full path is `Module 04/Lesson 05/Student_Copy/work/tests/test_bus.py`. The picture of the shell test is above. This block is the paste. It does not replace [bus.py](work/app/bus.py).

1. Open the work file named here, [work/tests/test_bus.py](work/tests/test_bus.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_an_unknown_field_still_keeps_the_cancellation`.

```text
"""Tests for the finished bus consumer.

An event with an extra field is still kept. A cancellation is
still kept. Both rows use the topic session.cancelled.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from bus import consume

# A cancellation whose keys are only id, session, and topic.
_CANCEL = {"id": "evt-cancel", "session": "ses-1", "topic": "session.cancelled"}
# The same topic, plus a field a strict reader would call unknown.
_EXTRA = {"disposition": "kept", "id": "evt-extra", "session": "ses-2", "topic": "session.cancelled"}


class BusTests(unittest.TestCase):
    """Tests for the finished bus consumer."""
    def test_an_unknown_field_still_keeps_the_cancellation(self) -> None:
        """The extra field stays, and the plain cancellation stays.

        Both rows keep their id and their topic.
        """
        extra = consume(_EXTRA)
        cancel = consume(_CANCEL)
        self.assertTrue(extra["kept"])
        self.assertEqual(extra["id"], "evt-extra")
        self.assertEqual(extra["topic"], "session.cancelled")
        self.assertEqual(cancel["topic"], "session.cancelled")
        self.assertTrue(cancel["kept"])


if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_bus.py](work/tests/test_bus.py). You should see `test_an_unknown_field_still_keeps_the_cancellation`. You should not see `test_the_shell_drops_the_extra_field_and_the_cancellation`. If you still see that shell name, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the handoff.

## Replace the handoff

This block replaces the app file [work/app/handoff.py](work/app/handoff.py). The full path is `Module 04/Lesson 05/Student_Copy/work/app/handoff.py`. It does not replace the test. The test is the next heading.

1. Open the work file named here, [work/app/handoff.py](work/app/handoff.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `A handoff with no summary is refused.`

```text
"""A handoff with no summary is refused.

A handoff is the spoken summary plus the agent who owns the call.
An empty summary, or a summary that is only spaces, is not a
handoff. The call is refused and the agent id is left blank so
nobody is assigned. A summary with text is kept, and the agent
id on the call is kept with it.
"""


def handoff(call: dict) -> dict:
    """Refuse a blank summary. Keep the agent id when the summary has text.

    A missing summary is treated the same as a blank one. strip
    removes spaces so a summary of only spaces is still blank.
    """
    summary = str(call.get("summary") or "").strip()
    if not summary:
        # No words to hand on. Do not assign an agent.
        return {"agent": "", "refused": True, "summary": ""}
    return {
        "agent": str(call.get("agent") or ""),
        "refused": False,
        "summary": summary,
    }
```

Open [work/app/handoff.py](work/app/handoff.py). You should see `A handoff with no summary is refused.` You should not see `Return an agent id and an empty summary.` If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the handoff test.

## Replace the handoff test

This block replaces the test file [work/tests/test_handoff.py](work/tests/test_handoff.py). The full path is `Module 04/Lesson 05/Student_Copy/work/tests/test_handoff.py`. The picture of the shell test is above. This block is the paste. It does not replace [handoff.py](work/app/handoff.py).

1. Open the work file named here, [work/tests/test_handoff.py](work/tests/test_handoff.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_a_summary_is_kept_and_an_empty_one_is_refused`.

```text
"""Tests for the finished handoff.

A call with a summary keeps that summary and is not refused.
A call with an empty summary is refused, and the agent id is cleared.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from handoff import handoff

# No words were captured for this call.
_EMPTY = {"agent": "cc-1", "id": "call-empty", "summary": ""}
# A real status summary from the contact center.
_STATUS = {"agent": "cc-1", "id": "call-status", "summary": "Referral status, still pending."}


class HandoffTests(unittest.TestCase):
    """Tests for the finished handoff."""
    def test_a_summary_is_kept_and_an_empty_one_is_refused(self) -> None:
        """The spoken summary is kept. The blank call is refused.

        A refused call has no agent id, so nobody is assigned.
        """
        kept = handoff(_STATUS)
        refused = handoff(_EMPTY)
        self.assertEqual(kept["summary"], _STATUS["summary"])
        self.assertFalse(kept["refused"])
        self.assertTrue(refused["refused"])
        self.assertEqual(refused["agent"], "")


if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_handoff.py](work/tests/test_handoff.py). You should see `test_a_summary_is_kept_and_an_empty_one_is_refused`. You should not see `test_the_shell_returns_an_empty_summary`. If you still see that shell name, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace leave.

## Replace leave

This block replaces the app file [work/app/leave.py](work/app/leave.py). The full path is `Module 04/Lesson 05/Student_Copy/work/app/leave.py`. It does not replace the test. The test is the next heading.

1. Open the work file named here, [work/app/leave.py](work/app/leave.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Late leave cancels the published session.`

```text
"""Late leave cancels the published session.

HR can enter leave after the contact center has already published
the session. When the leave names the same consultant and the
leave time is later than the publish time, the session is
cancelled. The row then names the bus event session.cancelled.
Leave for a different consultant, or leave entered earlier, does
not change the session.
"""


def apply(session: dict, leave: dict) -> dict:
    """Cancel when this consultant's leave was entered after publish.

    The two times are compared as text. The pack writes them in the
    same form, so a later clock sorts after an earlier one. A
    different consultant does not cancel this session.
    """
    published = str(session.get("published_at") or "")
    entered = str(leave.get("entered_at") or "")
    same = leave.get("consultant") == session.get("consultant")
    # Late means the leave clock is after the session was published.
    if same and entered > published:
        return {"event": "session.cancelled", "status": "cancelled"}
    # Anyone else, or an earlier leave, leaves the status unchanged.
    return {"event": "", "status": str(session.get("status") or "")}
```

Open [work/app/leave.py](work/app/leave.py). You should see `Late leave cancels the published session.` You should not see `Ignore leave that arrives after the session is published.` If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the leave test.

## Replace the leave test

This block replaces the test file [work/tests/test_leave.py](work/tests/test_leave.py). The full path is `Module 04/Lesson 05/Student_Copy/work/tests/test_leave.py`. The picture of the shell test is above. This block is the paste. It does not replace [leave.py](work/app/leave.py).

1. Open the work file named here, [work/tests/test_leave.py](work/tests/test_leave.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_late_leave_cancels_the_session`.

```text
"""Tests for the finished leave rule.

The leave row is the same consultant, and its time is after the
session was published. The session becomes cancelled and the
event is session.cancelled.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from leave import apply

# Entered later than the session was published, for the same consultant.
_LEAVE = {"consultant": "con-1", "entered_at": "2027-02-04T11:00:00", "id": "lv-1"}
# Already published earlier the same morning.
_SESSION = {"consultant": "con-1", "id": "ses-9", "published_at": "2027-02-04T08:00:00", "status": "published"}


class LeaveTests(unittest.TestCase):
    """Tests for the finished leave rule."""
    def test_late_leave_cancels_the_session(self) -> None:
        """The status is cancelled and the bus event is named."""
        got = apply(_SESSION, _LEAVE)
        self.assertEqual(got["status"], "cancelled")
        self.assertEqual(got["event"], "session.cancelled")


if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_leave.py](work/tests/test_leave.py). You should see `test_late_leave_cancels_the_session`. You should not see `test_the_shell_leaves_the_session_published`. If you still see that shell name, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the warehouse.

## Replace the warehouse

This block replaces the app file [work/app/warehouse.py](work/app/warehouse.py). The full path is `Module 04/Lesson 05/Student_Copy/work/app/warehouse.py`. It does not replace the test. The test is the next heading.

1. Open the work file named here, [work/app/warehouse.py](work/app/warehouse.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `The referral clock is the referred date.`

```text
"""The referral clock is the referred date.

The warehouse feed has two dates on one row. booking_date is when
the slot was booked. referred_at is when the referral was written.
The clock for this connection is the referral. The booking column
is later, and it is not returned.
"""


def clock(row: dict) -> str:
    """Return the referred date. Leave the booking column unread.

    A missing referred date is an empty string.
    """
    # booking_date is on the row and is intentionally not this clock.
    return str(row.get("referred_at") or "")
```

Open [work/app/warehouse.py](work/app/warehouse.py). You should see `The referral clock is the referred date.` You should not see `Read the booking date.` If you still see that shell sentence, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. The next heading is Replace the warehouse test.

## Replace the warehouse test

This block replaces the test file [work/tests/test_warehouse.py](work/tests/test_warehouse.py). The full path is `Module 04/Lesson 05/Student_Copy/work/tests/test_warehouse.py`. The picture of the shell test is above. This block is the paste. It does not replace [warehouse.py](work/app/warehouse.py).

1. Open the work file named here, [work/tests/test_warehouse.py](work/tests/test_warehouse.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `test_the_clock_is_the_referred_date`.

```text
"""Tests for the finished warehouse clock.

The row carries a booking column and a referred date. The clock
this module returns is the referred date.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from warehouse import clock

# Two dates. The finished clock is the referred date, not the booking column.
_ROW = {"booking_date": "2027-01-20", "id": "wh-1", "referred_at": "2027-01-02"}


class WarehouseTests(unittest.TestCase):
    """Tests for the finished warehouse clock."""
    def test_the_clock_is_the_referred_date(self) -> None:
        """The result is the day the referral was written."""
        self.assertEqual(clock(_ROW), "2027-01-02")


if __name__ == "__main__":
    unittest.main()
```

Open [work/tests/test_warehouse.py](work/tests/test_warehouse.py). You should see `test_the_clock_is_the_referred_date`. You should not see `test_the_shell_reads_the_booking_date`. If you still see that shell name, you pasted the picture.

If the terminal shows `SyntaxError` or `IndentationError`, paste this block again. Do not repair the spaces by hand.

Stay on this page. That was the last paste on this page. The line that starts with Next is the end of this page.

This page is done when the five work app files and their five work tests show the filled sentences, and you do not see the shell sentences named above. Do not run the suite on this page. If you run it anyway, it can still print `Ran 8 tests` and `OK`. That is not the finished suite. `rank.py`, `gates.py`, and `personal.py` are still the shell, and their tests are still the shell tests. [Chapter 07](07-the-proposal.md) replaces those files, then runs the suite. That later run also prints `Ran 8 tests` and `OK`. The search table in chapter 07 is how you tell the two runs apart. Do not run a check from this page.

Next: [07 — The proposal](07-the-proposal.md).
