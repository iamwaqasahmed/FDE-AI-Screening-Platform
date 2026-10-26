# 06 — The worker

[Chapter 05](05-the-stream.md) was the reading. This chapter replaces two scripts and runs them. The check runs the worker again, so the log has to come from these files.

This page has three parts. Read what the starter gets wrong. Replace the two files. Then run the command and fill the worksheet. The file blocks are long. Keep scrolling until you reach Run it.

The starter copies are [worker.py](packet/workflow/worker.py), [calendar_count.py](packet/workflow/calendar_count.py), and [tools.py](packet/workflow/tools.py). Chapter 01 copied them to `work/workflow`. Read the packet copies. The comments say what the starter does. Leave [tools.py](packet/workflow/tools.py) as the mock. You edit the copies under `work/workflow`.

A coding assistant may see the scripts. It may not see [intake.jsonl](packet/release/events/intake.jsonl). Do not paste that file into a prompt. Do not copy it into `work/`.

## What the starter gets wrong

The check names the case. It does not name the due date, the clause, or the state that would fit. These are the misses. The two files below are the inputs that clear them. You still read what each function does, and you still label the log.

- The starter calendar counts Monday through Friday and ignores the calendar file. Friday and Saturday are the weekend. The holidays are the dates in the calendar file. The day of `referral.submitted` counts when it is a working day.
- The starter books, and it treats a queued reply as a booking. The policy says not to book. `h-ain` has no slot API, so that hold stays `none`.
- A repeated event id opens a second approval. Skip an event id you have already seen. One referral keeps one approval id.
- The starter keeps the last letter in file order. Keep the higher sequence. Start the clock from the lowest sequence.
- The starter picks the highest criteria version. Pick the document whose status is in force.
- The starter never flags a duplicate. An open row with the same patient and specialty is flagged. The referral still waits for a coordinator, and it is not booked.
- The starter ignores finish. A compensate fault releases the hold. A retry fault is tried the policy's count of times, then recorded as a dead letter and not applied.

## Replace the two files

Edit the copies chapter 01 made. Leave the packet copies unchanged.

- [work/workflow/calendar_count.py](work/workflow/calendar_count.py)
- [work/workflow/worker.py](work/workflow/worker.py)

Leave [work/workflow/tools.py](work/workflow/tools.py) unchanged.

The links open once chapter 01 has written the files. If a link does not open, run `python "Week 01/Day 03/Student_Copy/prepare_work.py"` from a terminal in the course folder, then open `Week 01/Day 03/Student_Copy/work/workflow`. A second run of that command, with no extra word, puts the starter back and erases these two files.

For each of the two files:

1. Open the file under `work/workflow`. Do not open the copy in `packet/workflow`.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy the lines inside the block below. Do not copy the line that starts with three backticks. Do not copy the closing backticks.
4. Paste. Save. The spaces at the start of a line have to stay as they are. Python reads those spaces.

If a later command prints `SyntaxError` or `IndentationError`, the paste broke. Select the whole file, delete it, and paste the block again. Do not repair the file by hand.

### The calendar count

This block replaces `work/workflow/calendar_count.py` only.

```text
"""Count working days from the business calendar.

The weekend and the holidays come from the calendar file, not from a
Monday-to-Friday list. The day of referral.submitted counts when it is
a working day. If that day is not a working day, counting begins on
the next one.
"""

from __future__ import annotations

from datetime import date, timedelta

# Python's weekday() is 0 for Monday. This tuple only supplies the name.
# The calendar file decides which names count.
_NAMES = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def add_working_days(start: date, count: int, calendar: dict) -> date:
    """Return the date that finishes `count` working days, including `start` when it counts.

    A day counts when its name is not in the calendar's weekend and its
    date is not in the calendar's holidays. The count is the policy's
    working-day count. The caller passes that count in.
    """
    weekend = set(calendar["weekend"])
    holidays = set(calendar["holidays"])
    seen = 0
    day = start
    while True:
        if _NAMES[day.weekday()] not in weekend and day.isoformat() not in holidays:
            seen += 1
            if seen == count:
                return day
        day += timedelta(days=1)
```

### The worker

This block replaces `work/workflow/worker.py` only.

```text
"""Run wf-intake from referral.submitted to a held approval.

The workflow stops when a coordinator holds the approval.
It does not accept the referral, return it, or book a slot.
A second delivery of the same event id changes nothing.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

import tools
from calendar_count import add_working_days

# A live referral stops here. A person still has to decide.
HELD = "approval.held"

# Ain has no slot API in this release. Do not hold a slot there, and do not book.
AIN = "h-ain"


def extract(letter: str) -> tuple[str, str]:
    """Read the specialty and the facility out of the letter text.

    The letter names a hospital in words. This function turns those words
    into the facility ids the rest of the workflow uses.
    Endocrinology is the specialty this pack carries, and the id is endo.
    """
    facility = ""
    if "Ain Diabetes and Eye Center" in letter:
        facility = AIN
    elif "Wadi Specialist Hospital" in letter:
        facility = "h-wadi"
    specialty = "endo" if "endocrinology" in letter.lower() else ""
    return specialty, facility


def _in_force(docs: list[dict], specialty: str) -> str:
    """Return the criteria document whose status is in force for that specialty.

    A later draft can sit in the same folder. The version number is not
    the rule. The policy says to use the document that is in force when
    the referral starts.
    """
    for doc in docs:
        if doc["specialty"] == specialty and doc["status"] == "in_force":
            return doc["doc_id"]
    return ""


def _dead(scenario: str, referral_id: str) -> dict:
    """Record a dead letter and do not apply the event.

    No approval is opened, nothing is booked, and the hold is not left open.
    The due date, the criteria, the facility, and the clinic stay empty.
    """
    return {
        "scenario": scenario,
        "referral_id": referral_id,
        # A closed row. No approval is opened and the hold is not left open.
        "state": "dead-letter",
        # The due date, the criteria, the facility, and the clinic stay empty.
        "due": "",
        "approval_ids": [],
        "booked": False,
        "criteria_id": "",
        "suggested_facility": "",
        "clinic": "",
        "duplicate": False,
        "hold": "none",
        "dead_letter": True,
    }


def _retry(referral_id: str, retries: int) -> None:
    """Call finish until the retry stops, or until the policy count is used up.

    The count comes from the policy. Reaching the count does not apply the event.
    The caller writes the dead letter after this returns.
    """
    attempts = 0
    result = {"retry": True}
    while attempts < retries and result.get("retry"):
        result = tools.finish(referral_id)
        attempts += 1


def _row(
    items: list[dict],
    docs: list[dict],
    policy: dict,
    calendar: dict,
    open_keys: set[tuple[str, str]],
) -> dict:
    """Build one log row for one referral.

    Events that share a referral are sorted by sequence. The higher
    sequence is the letter you keep. The clock starts from the earliest
    sequence's occurred_at date, not from the later letter.
    A repeated event id never reaches this function.
    """
    ordered = sorted(items, key=lambda item: item["sequence"])
    current = ordered[-1]
    referral_id = current["referral_id"]
    # A step that keeps asking to be retried is tried the policy's count
    # of times. After that, record a dead letter and do not apply the event.
    if tools.faults().get(referral_id) == "retry":
        _retry(referral_id, policy["retries"])
        return _dead(current["scenario"], referral_id)
    specialty, facility = extract(current["letter"])
    hold = "none"
    # h-ain has no slot API. A hold there would come back queued.
    # Leave the hold as none. Do not book on any facility.
    if facility != AIN:
        tools.hold(facility, referral_id)
        hold = "open"
    # If a hold is taken and the next step fails, release the hold.
    # The referral still stops for a coordinator. It is not booked.
    if tools.finish(referral_id).get("compensate"):
        tools.release(referral_id)
        hold = "released"
    started = date.fromisoformat(ordered[0]["occurred_at"][:10])
    return {
        "scenario": current["scenario"],
        "referral_id": referral_id,
        "state": HELD,
        "due": add_working_days(started, policy["working_days"], calendar).isoformat(),
        "approval_ids": [f"apr-{referral_id}"],
        "booked": False,
        "criteria_id": _in_force(docs, specialty),
        "suggested_facility": facility,
        "clinic": tools.clinic(facility, specialty),
        "duplicate": (current["patient_key"], specialty) in open_keys,
        "hold": hold,
        "dead_letter": False,
    }


def build_rows(pack: Path) -> list[dict]:
    """Read the pack and return one row per referral, in first-seen order.

    A second delivery of the same event id is skipped. That is idempotency:
    the same event changes nothing, so it cannot open a second approval.
    """
    # Load the pack. Group events by referral, and skip an event id already seen.
    tools.load(pack)
    grouped: dict[str, list[dict]] = {}
    order: list[str] = []
    seen: set[str] = set()
    for event in tools.events():
        # The same event id changes nothing, so it cannot open a second approval.
        if event["event_id"] in seen:
            continue
        seen.add(event["event_id"])
        referral_id = event["referral_id"]
        # The first time this referral appears, remember its place in the log.
        if referral_id not in grouped:
            grouped[referral_id] = []
            order.append(referral_id)
        grouped[referral_id].append(event)
    # One row per referral, using the policy, the calendar, the criteria, and open referrals.
    policy = tools.policy()
    calendar = tools.calendar()
    docs = tools.criteria()
    open_keys = {(row["patient_key"], row["specialty_id"]) for row in tools.open_referrals()}
    return [_row(grouped[referral_id], docs, policy, calendar, open_keys) for referral_id in order]


def main(argv: list[str] | None = None) -> None:
    """Write the scenario log. The check runs this file again, so do not hand-edit the log."""
    parser = argparse.ArgumentParser(description="Run wf-intake on the event pack.")
    parser.add_argument("--pack", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    destination = Path(args.out)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(build_rows(Path(args.pack)), indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])
```

## Run it

Open a new terminal in the course folder, the same way as chapter 01. The window you used for the build is still inside `problem_simulation`. Leave that window.

If chapter 01 told you to use `py` instead of `python`, use `py` in this command too.

```text
python "Week 01/Day 03/Student_Copy/work/workflow/worker.py" --pack "Week 01/Day 03/Student_Copy/packet/release" --out "Week 01/Day 03/Student_Copy/work/scenario-log.json"
```

The command prints nothing when it works. An empty line after the command is success. It writes [scenario-log.json](work/scenario-log.json). The link opens once the command has written the file. Open that file. The list is in the file, not in the terminal.

You should see one block per scenario, in this order: `order`, `happy`, `friday`, `holiday`, `ain`, `replay`, `duplicate`, `compensation`, `dead-letter`. Every live block has `"booked": false`. The dead-letter block has `"approval_ids": []`.

If a block says `"booked": true`, the file that ran is still the starter. Paste the two blocks again. Do not hand-edit the log. The check will not read your edit.

If the terminal prints `SyntaxError` or `IndentationError`, go back to the paste steps. If it says `python` is not recognized, use `py`.

## Label the log

Open [notes/scenario-lines.md](notes/scenario-lines.md). The check does not read this worksheet. Fill it anyway. It is how you see what each block in the log means.

Find the block whose `"scenario"` matches the row. Copy the text after each field name into the worksheet. A block looks like this. The values here are blank on purpose. Yours are filled in.

```text
"scenario": "happy",
"due": "",
"suggested_facility": "",
"booked": false,
"duplicate": false,
"hold": "",
"dead_letter": false
```

Copy `due`, `suggested_facility`, `booked`, `duplicate`, `hold`, and `dead_letter`. On the dead-letter block, `due` is two quotes with nothing between them. Leave that worksheet cell blank. Then write the rule from this table in the last column. This page does not give you the due date. The log does.

| scenario | The rule to write after the fields are copied |
| --- | --- |
| order | The higher sequence is the letter you keep, so the facility is `h-wadi`. The clock starts from the lowest sequence. |
| happy | One approval, the clinic from the catalog, and the criteria document whose status is in force. Not booked. |
| friday | The due date is where the working-day count lands. Friday and Saturday do not count. The steps under this table are how you count. |
| holiday | The same count, and the three holiday dates in the calendar do not count. The due date is not one of those three dates. |
| ain | The facility is `h-ain`. The hold is `none`. The clinic is empty. Not booked. |
| replay | The same event id arrives twice. The approval list has one id. |
| duplicate | The open-referrals row matches this patient and specialty. `duplicate` is true. The row is still held, and it is not booked. |
| compensation | The fault is compensate. The hold is `released`. The state is still `approval.held`. |
| dead-letter | The fault is retry. The event was not applied. No approval, hold `none`, and `dead_letter` true. |

## How a due date is counted

Do the policy's own example first. Then do `friday`, then `holiday`.

Open a terminal in the course folder. This command prints a date and the nine dates after it, each with its weekday name. The date in the command is the day the engagement opens, from [zones.md](packet/kickoff/world/zones.md). It is not one of today's referrals.

```text
python -c "import datetime; start=datetime.date.fromisoformat('2027-01-10'); [print((start+datetime.timedelta(days=i)).isoformat(), (start+datetime.timedelta(days=i)).strftime('%A')) for i in range(10)]"
```

You should see `2027-01-10 Sunday` on the first line.

[pol-sla.md](packet/release/policy/pol-sla.md) says a referral submitted on Sunday counts Sunday as day one and Monday as day two. On your list, Sunday is the first line and Monday is the next line. Friday and Saturday would be skipped. A date in the calendar's `holidays` list would be skipped. The count stops on day two. That is the shape of every due date today.

For the friday row, then the holiday row:

1. In [intake.jsonl](packet/release/events/intake.jsonl), search for `"scenario": "friday"`. Copy the ten characters of `occurred_at` before the letter T.
2. Run the same command with that date in place of `2027-01-10`.
3. Walk down the printed list. Skip a line whose weekday is Friday or Saturday. Skip a line whose date is in [business-calendar.json](packet/release/calendar/business-calendar.json) under `holidays`.
4. The first line you do not skip is day one. The second line you do not skip is day two. The date on day two is the due date.
5. That date should be the `due` you copied from the log. If it is not, count the list again before you touch the file. The start line counts when you did not skip it. Friday, Saturday, and a holiday date do not count. If the second count still disagrees with the log, the calendar script that ran is still the starter. Paste the calendar block again.

Use the same five steps for `"scenario": "holiday"`.

Next: [07 — The note](07-the-note.md).
