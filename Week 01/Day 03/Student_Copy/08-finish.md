# 08 — Finish

The check grades the worker, the intake note, and the shape of the knowledge file. It runs the worker again. A log you typed by hand is not the log it grades. The sentences in `knowledge.md` are still part of done. The trainer reads them. The check only checks that both answers are there.

Use the failure table at the bottom only when a check fails. It is not more work.

## Do this

1. In the same `work` folder as `intake.md`, create a new file named `knowledge.md`. Save it as `Week 01/Day 03/Student_Copy/work/knowledge.md`. Paste the block below. Then replace each numbered line with your own sentence. Delete the words `Your answer` and write the sentence on that same line.

- Line 1 is the clock. [pol-sla.md](packet/release/policy/pol-sla.md) says the SLA clock starts at `referral.submitted`. It does not start at booking. Your line 1 says that, and it names `referral.submitted`.
- Line 2 is a second delivery. The same page says a second delivery of the same event id changes nothing. The referral keeps the one approval it already has. Your line 2 says that.

```text
# Knowledge

1. Your answer. Name the event that starts the SLA clock.

2. Your answer. Say what a second delivery of the same event id should do.
```

2. Save `knowledge.md` before the check. The check reads that file. Open a terminal in the course folder, the same way as chapter 01. Then run:

```text
cd problem_simulation
python -m alwaha.check events --work "../Week 01/Day 03/Student_Copy/work" --profile practice
```

If you already ran that command and it said `knowledge.md needs two answers`, the file was missing or the answers were still the words `Your answer`. Save the two sentences and run the same command again.

## You should now see

```text
chk-w1-events passed.
```

`work/knowledge.md` has both answers. The first names `referral.submitted`. The second says a repeated event id does not open another approval.

## If a check fails

A failed scenario names the case. It does not print the due date, the clause, or the fitting state. A watermark message does not print the watermark. Go back to the chapter that has that input.

| What it prints | Where to go |
| --- | --- |
| `python` is not recognized | [Chapter 01](01-setup.md). Use `py` instead of `python` in the command, including the worker command in chapter 06 |
| `SyntaxError` or `IndentationError` | The paste in [chapter 06](06-the-worker.md) lost its spaces. Select the whole file, delete it, and paste the block again. Do not repair it by hand |
| `No module named alwaha` | The terminal is not inside `problem_simulation`. Open a new terminal in the course folder, run `cd problem_simulation`, and run the check again |
| `Build rel-w1d3 first.` | [Chapter 01](01-setup.md). Run the build again with `--profile practice` and `--release rel-w1d3` |
| `worker.py is missing` or `worker did not run` | [Chapter 06](06-the-worker.md). `work/workflow/` needs `worker.py`, `calendar_count.py`, and `tools.py`. Replace the two files with the blocks in that chapter, and leave `tools.py` |
| `scenario log is not a list` or `scenario log is missing a field` | The worker did not write the fields in chapter 06. Paste those two files again |
| `is missing` | That scenario never reached the log. The event file stays in `packet/release`. Point the worker at that folder with the command in chapter 06 |
| `due date does not match the calendar` | The calendar block in chapter 06. The weekend and the holidays come from [business-calendar.json](packet/release/calendar/business-calendar.json). The start day counts when it is a working day. The message does not print the date |
| `criteria is not the one in force` | The worker must select the criteria page whose status is in force, not the higher version. The message does not print the clause or the document id |
| `booked a slot` | The worker called book, or it treated a queued reply as a booking. Chapter 06 sets `booked` to false and does not call book. `h-ain` is included |
| `booking does not match` | A row that should stay unbooked was marked booked, or the other way around. Today's rows are not booked |
| `opened a second approval` | The same `event_id` was applied twice. Skip an event id you have already seen. One referral keeps one approval id |
| `suggestion does not match` | The letter you kept is the wrong sequence. Sort by sequence and keep the higher one. The `order` case arrives with the higher sequence first |
| `clinic does not match` | Use `tools.clinic` for the facility you kept. Ain is not in [clinics.csv](packet/release/catalog/clinics.csv), so that clinic is empty |
| `referral was not flagged` | The patient and specialty are already in [open-referrals.csv](packet/release/events/open-referrals.csv). Flag the row. It still stops for a coordinator, and it is not booked |
| `referral was flagged` | That case is not in the open-referrals file. Leave `duplicate` false |
| `hold does not match` | `h-ain` stays `none`. A compensate fault in [faults.json](packet/release/events/faults.json) releases the hold. Any other live facility stays `open`. The message does not print the fitting hold |
| `did not stop for a person` | A live row needs one approval id, the state `approval.held`, and `dead_letter` false. The message does not print that state |
| `applied the poison event` | The retry case was applied. Try finish the policy's retry count, then write the dead-letter row from chapter 06: no approval, not booked, hold not open |
| `intake.md is missing` | [Chapter 07](07-the-note.md). From the course folder, run `python "Week 01/Day 03/Student_Copy/prepare_work.py" note`, then paste the note |
| `the diagram does not show the human step` | The note needs the word coordinator, or the word human. Use the note in chapter 07 |
| `the note does not keep the criteria version` | The in-flight section needs the words in-flight, criteria, and version. Use the note in chapter 07 |
| `knowledge.md needs two answers` | Two lines that start with `1.` and `2.` and then a word. Replace the two lines in the block above |
| `a watermarked sample is in the work directory` | The event file, or the watermark line, was copied into `work/`. The message does not print the watermark. Delete that copy. Leave the event file in `packet/release/events` |

## Done

The day is done when the check prints `passed` and `work/knowledge.md` answers both questions.

Keep `work/` and the scenario worksheet. The solution copy, when you receive it, is how you compare your pages with a finished set. Leave `problem_simulation/build` closed.

## What you open next

The Done section above is the gate. `knowledge.md` is part of that gate. The [optional review](../../../learning/review.md) is not filed. The checks do not read it.

If `Solution_Copy` is already on disk beside this folder, this is the moment it is for. Open [the solution README](../Solution_Copy/README.md) only after Done is true. Do not start in its `work/` folder. The trainer chapter there is optional.

Tomorrow the medical director's rules arrive. A patient can ask for status and book a slot. A return cannot leave without a coordinator.

Open [Week 1, Day 4](../../Day%2004/Student_Copy/README.md) and read `00-background.md` before any command.
