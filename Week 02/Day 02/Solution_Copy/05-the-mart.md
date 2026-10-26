# 05 — The mart

This is the mart read from the morning. Open [mart.py](work/app/mart.py) and [mart.md](work/mart.md) and put them beside yours.

[waitlist.csv](sources/release/mart/waitlist.csv) is one header and one data row:

```text
person_key,wait_days,booking_date
pt-200,14,2026-06-01
```

`wait_days` is the wait figure. On this practice row the figure is 14. `booking_date` is the date column Week 1 already found. That column is the clock.

`read` returns `clock` `booking_date` and `trusted` false. It still reads the wait cell, so a trace can show the figure. The figure is not the clock. The shell did the opposite: it returned the wait column as the clock and set `trusted` true. While that shell runs, the check says `wait number was used as truth`. The message does not print the figure.

[mart.md](work/mart.md) says the extract is a database read, names `booking_date`, and says the wait figure is not the clock. The number 14 is not in that file. When the column name is missing, the check says `the mart clock is not named` and does not print the column. When the wait figure is in the note, the check says `wait number was used as truth`.

The sprint in [chapter 02](02-the-sprint.md) reads this extract only after the subscriptions are in place. That order is why the mart sentence sits under Later.

## The path through the files

The morning chapter [08-the-mart.md](../Student_Copy/08-the-mart.md) has the section How the replacement works. That section is the path through the file this page compares. Read it beside the finished file. The notes above are the decisions the check names.

Next: [06 — Knowledge](06-knowledge.md).
