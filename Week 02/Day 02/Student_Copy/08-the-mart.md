# 08 — The mart

[Chapter 07](07-the-pages.md) wrote the states, the zones, and the SMS. This chapter labels the clock on the wait-time extract and replaces the mart shell. The check runs in chapter 09. Do not run it from this page.

## Read the extract

Open [waitlist.csv](packet/release/mart/waitlist.csv). The file has this shape. One header line, then one data line. This block is a picture of that file. Do not paste it into `mart.py` or `mart.md`. The blocks that replace those files are under the headings below.

```text
person_key,wait_days,booking_date
pt-200,14,2026-06-01
```

Three columns. `person_key` is the person. `wait_days` is the wait figure. The number under that column on this line is 14. `booking_date` is the date column Week 1 already found. That date column is the clock.

The mart note names `booking_date`. It does not contain the number 14, and it does not contain any other wait figure. The check says the wait number was used as truth when that number is in the note or when the shell still trusts the wait column. The message does not print the figure. It says the mart clock is not named when the date column's name is missing. The message does not print the column.

## Replace mart.py

Chapter 01 copied the shell to [work/app/mart.py](work/app/mart.py). The full path is `Week 02/Day 02/Student_Copy/work/app/mart.py`. The packet copy, [packet/app/mart.py](packet/app/mart.py), stays the shell. Search that packet file for `trusted` if you want to see the shell: it marks the wait column trusted.

This block replaces the work copy only.

Open `work/app/mart.py`. Select the whole file. Delete it. Copy from this chapter file, not from a preview. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. Paste as plain text. Save.

The line `def read` starts at the left edge. The lines inside a function start with four spaces. If the spaces disappear, use Paste Without Formatting, the same way as [chapter 06](06-the-worker.md).

If the terminal later shows `SyntaxError` or `IndentationError`, do not repair the spaces by hand. Go to "If the shell was edited" in [chapter 06](06-the-worker.md), then paste this file again.

```text
"""Read the wait-time extract. The wait figure is not the clock.

Chapter 08 replaces work/app/mart.py with this file.
The packet copy stays the shell that trusts the wait column.

The clock name is the date column on the extract. trusted is
false. The wait cell is still read so a trace can show the
figure, and the figure is not treated as truth.
"""

from __future__ import annotations


def _cell(text: str, column: str) -> str:
    """Return the first data cell under column.

    The extract is one header line and one data line. Both are
    split on commas. column must be a header cell, or this raises.
    """
    lines = [line for line in text.splitlines() if line.strip()]
    header = lines[0].split(",")
    values = lines[1].split(",")
    return values[header.index(column)]


def read(text: str) -> dict:
    """Name the date column as the clock and do not trust the wait figure.

    text is the wait-time extract. clock is booking_date, the date
    column on the header. trusted is false. The wait cell is
    returned as an integer and is not the clock.
    """
    return {"clock": "booking_date", "trusted": False, "wait": int(_cell(text, "wait_days"))}
```

Read the file back. Search for `"clock": "booking_date"`. Search for `"trusted": False`. Both have to be there. The name `wait_days` is still in the file, on the wait cell only. That is expected. If `"clock"` is still `"wait_days"`, this paste did not replace the file. Select the whole file, delete it, and paste the block again.

Leave every other file under `work/app` as it was after chapter 06.

## See the clock on the trace

Open a terminal in the course folder. `dir` should list `problem_simulation` and `Week 02`. Run the same command as chapter 06. It prints nothing. The prompt comes back, and there is no error.

```text
python "Week 02/Day 02/Student_Copy/work/app/run.py" --pack "Week 02/Day 02/Student_Copy/packet/release" --db "Week 02/Day 02/Student_Copy/work/sessions.db" --out "Week 02/Day 02/Student_Copy/work/trace.json"
```

Open [work/trace.json](work/trace.json). Search for `booking_date`. That string is the clock. On the same mart object, `trusted` is false. The wait figure is still on that object. Leave it in the trace. Do not copy it into `mart.md`.

## Replace the mart note

Chapter 01 copied [mart.md](packet/templates/mart.md) to [work/mart.md](work/mart.md). The full path is `Week 02/Day 02/Student_Copy/work/mart.md`. The copy is only a heading. Do not type under that heading. This block replaces the whole file. It does not replace the template.

Open `work/mart.md`. Select the whole file. Delete it. Copy the lines inside the block below. Do not copy the fence lines. Paste. Save.

```text
# Mart

The wait-time extract is a database read. The clock column is booking_date. The wait figure is not the clock.
```

Read the file back. The sentence names `booking_date`. The number from the extract is not in the file. If the number is there, select the whole file, delete it, and paste the block again.

Next: [09 — Finish](09-finish.md).
