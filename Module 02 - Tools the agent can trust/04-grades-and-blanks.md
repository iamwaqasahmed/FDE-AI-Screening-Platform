# Grades and blanks

The workbook does not stick to the five codes. `unfinished_photos` and the queue both need one normalizer.

Follow `grade_codes.md`, document id `grade-codes`.

| What you see | Code you store |
|---|---|
| `R0`, `R1`, `R2` | That code |
| `R3` or `prolif`, or a note that says `urgent` | `R3` |
| `U` or `ungradable` | `U` |
| Empty result and empty note | unfinished |

A blank result is an unfinished screen. The data dictionary's claim that blank means normal is not the grade-code list.

`unfinished_photos()` returns the count of those rows inside the 24-month window. It should match the unfinished-photo count in the Module 01 debrief.

Keep the readable-not-referable pair (`R0` and `R1`), the ungradable count, the mild referable count (`R2`), and the sight-threatening count (`R3`). The checker expects those four piles among completed results.

Ignore the `OLD` tab. Those rows are practice data from years outside the window. `load.py` drops that sheet before the counts run.

Open `grades.py` and match `normalize` to the table above.

**Finish.** You can map `prolif`, a note of `urgent`, `ungradable`, and a blank result.

Next: [Queue and waits](05-queue-and-waits.md).
