# 03 — The calendar

Open the finished [calendar_count.py](work/app/calendar_count.py) and [test_calendar.py](work/tests/test_calendar.py) and put them beside yours.

[business-calendar.json](sources/carried/calendar/business-calendar.json) lists the working days as Sunday through Thursday. Friday and Saturday are the weekend. The holiday list is 10, 11, and 12 March 2027. [cases.json](sources/release/calendar/cases.json) has the starts and the counts. It does not have the date a case lands on.

`thursday` starts on Thursday 21 January 2027 and counts two working days. Thursday counts. Friday and Saturday do not. Sunday 24 January 2027 is the second working day. The test stores `2027-01-24` under `thursday`.

`eid` starts on Tuesday 9 March 2027 and counts three working days. Tuesday counts. The next three dates are on the holiday list. Saturday is the weekend. Sunday is the second working day. Monday 15 March 2027 is the third. The test stores `2027-03-15` under `eid`.

`NAMES` still lists Friday. The count uses `working_days` from the calendar argument. Friday remains a name. It is not counted, because the calendar does not list it.

The shell deletes the calendar argument and counts Monday through Friday. While that shell is the file that runs, the tests check says `the calendar does not match`. The message does not name a date. The shell test still expects 22 January and 11 March. Those lines are gone from the finished test.

The test reads the business calendar from `data/rel-w1d3` and the cases from `data/rel-w2d3`. `parents[5]` is the course folder, because this file sits in `work/tests` inside this solution copy.

## The path through the files

The morning chapter [06-the-calendar.md](../Student_Copy/06-the-calendar.md) has the section How the replacement works. That section is the path through the files this page compares. Read it beside the finished file. The notes above are the decisions the check names.

Next: [04 — The reply](04-the-reply.md).
