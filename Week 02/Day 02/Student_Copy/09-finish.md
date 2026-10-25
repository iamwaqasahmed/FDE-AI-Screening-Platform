# 09 — Finish

The check grades the sprint, the states, the zones, the SMS, the mart note, the webhook intake, the cancellation deliveries, and the mart read. It also grades the shape of `knowledge.md`. It runs the worker again. A trace you typed by hand is not what it grades. The sentences in `knowledge.md` are still part of done.

Use the failure table at the bottom only when the check fails. It is not more work.

## Do this

1. Make `knowledge.md`. It sits in the same folder as `sprint.md`, `states.md`, `zones.md`, `sms.md`, and `mart.md`. The full path is `Week 02/Day 02/Student_Copy/work/knowledge.md`. It does not go inside `work/app`, and it does not go inside `packet/`.

   In the editor, open the `work` folder and create a new file named `knowledge.md`. If you use File Explorer instead, open that folder, right-click, choose New, then Text Document, and name it `knowledge.md`. On Windows the name sometimes becomes `knowledge.md.txt`. Click the name and remove `.txt`. If you cannot see `.txt`, in File Explorer open View and tick File name extensions, then rename the file so the name ends in `.md` only.

   Open the file. If anything is already in it, select the whole file and delete it. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. Paste. Save. These are the finished sentences. Line 1 is the owner cell on the `referral.submitted` row of [topics.md](packet/release/registry/topics.md). Line 2 says what a replay does: the second delivery of the same event does not book again.

```text
# Knowledge

1. eref owns referral.submitted.
2. A replay does not book a second time.
```

2. Open a terminal in the course folder, the same way as chapter 01. `dir` should list `problem_simulation` and `Week 02`. If that window is already inside `problem_simulation`, skip the `cd` line and run the python line.

```text
cd problem_simulation
python -m alwaha.check journey --release rel-w2d2 --work "../Week 02/Day 02/Student_Copy/work" --profile practice
```

## You should now see

```text
chk-w2-journey passed.
```

`work/knowledge.md` has both answers. The first says `eref` owns `referral.submitted`. The second says a replay does not book a second time.

## If the check fails

A failed check can print more than one line. Fix every line, then run the command again. A line says the intake still polls, the replay booked again, or the wait number was used as truth. It does not name a field, a figure, or an owner. `the mart clock is not named` does not print the column. `a patient-visible state is missing` does not name the state. `zone crossing is missing` does not name the piece. A watermark message does not print the watermark. Where a check fails without naming the missing fact, use the row below. The row sends you back to the chapter that has the inputs. Then you paste the block from that chapter again.

| What it prints | Where to go |
| --- | --- |
| `python` is not recognized | [Chapter 01](01-setup.md). Use `py` instead of `python` in the command |
| `SyntaxError` or `IndentationError` | A Python file lost its spaces. Do not repair it by hand. From the course folder, run `python "Week 02/Day 02/Student_Copy/prepare_work.py"`, then paste again from [chapter 05](05-the-sprint.md), [chapter 06](06-the-worker.md), [chapter 07](07-the-pages.md), and [chapter 08](08-the-mart.md) |
| `No module named alwaha` | The terminal is not inside `problem_simulation`. Open a new terminal in the course folder, run `cd problem_simulation`, and run the check again |
| `The system cannot find the path specified` or `No such file or directory` on the `cd` line | This window is already inside `problem_simulation`. Skip the `cd` line and run the python line |
| `can't open file` or `No such file or directory` on `run.py` | That window is not the course folder. [Chapter 06](06-the-worker.md). Run `dir`. You should see `problem_simulation` and `Week 02` |
| `Build rel-w2d2 first.` | [Chapter 01](01-setup.md). Run the build again with `--profile practice` and `--release rel-w2d2` |
| `journey needs --release rel-w2d1, rel-w2d2, or rel-w2d5.` | Add `--release rel-w2d2` to the journey command above |
| `a watermarked sample is in the work directory` | Delete the webhook file from `work/`. It stays in [packet/release/webhooks](packet/release/webhooks/referral.submitted.json). The message does not print the watermark |
| `the worker is missing` | [Chapter 01](01-setup.md). Run `prepare_work.py` again, then repeat chapters 05, 06, 07, and 08 |
| `the worker did not run` | [Chapter 06](06-the-worker.md). Restore the shell with `prepare_work.py`, paste the pages and the three Python files again, and run `run.py` again |
| `intake still polls` | [Chapter 06](06-the-worker.md). Paste `intake.py` again. The shell still returns poll. The message does not name a field |
| `an unknown field stopped intake` | [Chapter 06](06-the-worker.md). Paste `intake.py` again. A key the registry does not list is ignored. The event is not rejected. The message does not name the field |
| `an unknown field was stored` | [Chapter 06](06-the-worker.md). Paste `intake.py` again. The record keeps the listed fields and leaves `letter` off. The message does not name the field |
| `the referral was not recorded` | [Chapter 06](06-the-worker.md). `referral_id` is copied from the fields the registry kept |
| `replay booked again` | [Chapter 06](06-the-worker.md). Paste `cancel.py` again. A repeated event id returns the stored row |
| `the hold was left open` | [Chapter 06](06-the-worker.md). Paste `cancel.py` again. A rejected receipt releases the hold and books nothing |
| `no-slot cancellation was booked` | [Chapter 06](06-the-worker.md). Paste `cancel.py` again. No slot returns `escalated`, with no booking and no SMS |
| `the cancellation was not notified` | [Chapter 06](06-the-worker.md). An accepted receipt stores `notified`, one booking, and one SMS |
| `a patient-visible state is missing` | [Chapter 07](07-the-pages.md). Paste the states block again. Keep the pipe characters. The message does not name the state |
| `zone crossing is missing` | [Chapter 07](07-the-pages.md). Paste the zones block again. Keep the pipe characters. The message does not name the piece |
| `sms wording is missing` | [Chapter 07](07-the-pages.md). Paste the SMS block again. The sentence contains the word booking |
| `sms wording carries a national id` | [Chapter 07](07-the-pages.md). Paste the SMS block again. The sentence has no ten-digit number |
| `the mart clock is not named` | [Chapter 08](08-the-mart.md). Paste the mart note again. The message does not print the column |
| `wait number was used as truth` | [Chapter 08](08-the-mart.md). Paste `mart.py` and the mart note again. The note names the date column and does not contain the number from the extract. The message does not print the figure |
| `sprint.md does not sequence the subscription before the mart` | [Chapter 05](05-the-sprint.md). Paste the sprint block again. The subscribe sentence stays above the mart sentence |
| `knowledge.md needs two answers` | Two lines that start with `1.` and `2.` and then a word. Use the block above |
| `knowledge.md does not name the owner` | The message does not print the owner. Paste the block above. Line 1 is the owner cell on the `referral.submitted` row |
| `knowledge.md does not say what a replay does` | Line 2 of the block above says a replay does not book a second time |

## Done

The day is done when the check prints `passed` and `work/knowledge.md` answers both questions.

Keep `work/` and the feed-lines worksheet. The solution copy, when you receive it, is how you compare your pages with a finished set. Leave `problem_simulation/build` closed.
