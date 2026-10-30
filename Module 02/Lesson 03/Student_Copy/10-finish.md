# 10 — Finish

The checks grade the calendar, the reply schema, the receipt clock, the journey, the scripts, the clauses, the definition of done, the zone crossings, the fixture note, the sprint, the workflow, and the shape of `knowledge.md`. The sentences in `knowledge.md` are still part of done.

Use the failure table at the bottom only when a check fails. It is not more work.

## Do this

1. Make `knowledge.md`. It sits in the same folder as `sprint.md`, `dod.md`, `crossings.md`, `usability.md`, and `fixtures.md`. The full path is `Module 02/Lesson 03/Student_Copy/work/knowledge.md`. It does not go inside `work/app`, and it does not go inside `packet/`.

   In the editor, open the `work` folder and create a new file named `knowledge.md`. If you use File Explorer instead, open that folder, right-click, choose New, then Text Document, and name it `knowledge.md`. On Windows the name sometimes becomes `knowledge.md.txt`. Click the name and remove `.txt`. If you cannot see `.txt`, in File Explorer open View and tick File name extensions, then rename the file so the name ends in `.md` only.

   Open the file. If anything is already in it, select the whole file and delete it. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. Paste. Save. These are the finished sentences. Line 1 says a fixed sleep follows the wall clock, and the receipt follows the case clock, which the switch can hold. Line 2 says the journey asserts the mock state from a recorded fixture, not the model's sentence.

```text
# Knowledge

1. A fixed sleep follows the wall clock. The receipt follows the case clock, and the switch can hold it.
2. The journey asserts the mock state from a recorded fixture, not the model's sentence.
```

2. Open a terminal in the course folder, the same way as chapter 01. `dir` should list `problem_simulation` and `Module 02`. If chapter 01 told you to use `py`, use `py` here. If that window is already inside `problem_simulation`, skip the `cd` line and run the python lines. Run the first python line. Read what it prints. Then run the second python line. A failure on the first does not stop you from running the second. They grade different files.

```text
cd problem_simulation
python -m alwaha.check tests --release rel-m02-l03 --work "../Module 02/Lesson 03/Student_Copy/work" --profile practice
python -m alwaha.check ux --release rel-m02-l03 --work "../Module 02/Lesson 03/Student_Copy/work" --profile practice
```

## You should now see

```text
chk-tests passed.
chk-ux passed.
```

`work/knowledge.md` has both answers. The first says a fixed sleep follows the wall clock and the receipt follows the case clock. The second says the journey asserts the mock state from a recorded fixture.

## If a check fails

A failed check prints `failed`, then one or more lines that start with a dash. The words after the dash are what you look up in the left column below. Do what the right column says. Then run both commands again. A line on the first check says the calendar does not match, the receipt test sleeps, the suite accepted the receipt fault, the reply schema is missing, or the journey followed the sentence. It does not name an interval, a delay, or a due date. A line on the second check says a usability script is unfinished, an accessibility clause is missing, the fault is not in the definition of done, or a zone-crossing case is missing. It does not name the script, the clause, or the case. A watermark message does not print the watermark. Where a check fails without naming the missing fact, the row gives the inputs. Then you paste the block from that chapter again.

| What it prints | Where to go |
| --- | --- |
| `python` is not recognized | [Chapter 01](01-setup.md). Use `py` instead of `python` in the command |
| `No module named alwaha` | The terminal is not inside `problem_simulation`. Open a new terminal in the course folder, run `cd problem_simulation`, and run the check again |
| `Build rel-m02-l03 first.` | [Chapter 01](01-setup.md). Run the build again with `--profile practice` and `--release rel-m02-l03` |
| `No such file or directory` and the message names `data/rel-m01-l03` or `data/rel-m02-l03` | That line is from the suite in [chapter 08](08-the-receipt.md), not from these two checks. Rebuild the missing pack. From the course folder, run `cd problem_simulation`, then `python -m alwaha.build --profile practice --release rel-m01-l03` for the calendar, and `python -m alwaha.build --profile practice --release rel-m02-l03` for today's cases, clock file, and fixture. Then run the suite again |
| `the calendar does not match` | [Chapter 06](06-the-calendar.md). The message does not name a date. Open the business calendar and the case list. Count Sunday through Thursday and skip the holiday list. Paste both blocks from chapter 06 again |
| `the receipt test sleeps` | [Chapter 08](08-the-receipt.md). The letters `sleep` are in `receipt.py` or `test_receipt.py`, including inside a comment. The message does not mean the suite is still waiting. Paste both files again. The replacement blocks do not contain those letters |
| `the suite accepted the receipt fault` | [Chapter 08](08-the-receipt.md). The receipt still treats every receipt as due. Paste `receipt.py` from chapter 08. The demo's second line is the switch |
| `the receipt test does not match the clock` | [Chapter 08](08-the-receipt.md). Open `receipt.json` and read `minutes`. The test reads that field. Paste both receipt blocks again. The message does not name an interval or a delay |
| `the reply schema is missing` | [Chapter 07](07-the-reply.md). A sentence with no intent still passes, or an empty sentence with intent fails. Paste `schema.py` and `test_schema.py` |
| `the journey followed the sentence` | [Chapter 07](07-the-reply.md). The test still trusts the sentence. Paste `schema.py` and `test_journey.py`. The fixture stays in the pack |
| `the suite is missing` | A graded file is not in `work/`. Run `prepare_work.py`, then paste chapters 05 through 09 again |
| `the suite did not run` | The terminal showed `SyntaxError` or `IndentationError`. Run `prepare_work.py` and paste the Python blocks again from the chapter source |
| `a usability script is unfinished` | [Chapter 09](09-the-pages.md). The usability table needs `status-short` and `caregiver` finished, with `yes` in the finished column. Do not add the phone-only script. Paste `usability.md` again |
| `an accessibility clause is missing` | [Chapter 09](09-the-pages.md). The clause column needs the four ids from `access.md`. Paste `usability.md` again. The message does not name the clause |
| `the fault is not in the definition of done` | [Chapter 09](09-the-pages.md). Open `receipt.json` and read the switch field. Paste `dod.md` again. The sentence names that switch, and it says the suite goes red |
| `a zone-crossing case is missing` | [Chapter 09](09-the-pages.md). The receipt row leaves `zone-private` for the partner. The calendar row stays in `zone-private`. Paste `crossings.md` again. The message does not name the case |
| `the fixture note is missing` | [Chapter 09](09-the-pages.md). Paste `fixtures.md` again. The note says the journey reads the recorded fixture and asserts the mock state |
| `sprint.md does not sequence the suite before sign-off` | [Chapter 05](05-the-sprint.md). The suite sentence has to sit above the usability sentence. Paste `sprint.md` again |
| `the suite is not in CI` | The workflow was edited or is missing. Run `prepare_work.py`. Do not edit `ci.yml`. Paste chapters 05 through 09 again if the second run restored the blanks |
| `knowledge.md needs two answers` | Paste the block above again. Two numbered lines |
| `knowledge.md does not say why a sleep fails` | Line 1 of the block above says a fixed sleep follows the wall clock and the receipt follows the case clock |
| `knowledge.md does not say what an AI journey asserts` | Line 2 of the block above says the journey asserts the mock state from a recorded fixture |
| `a watermarked sample is in the work directory` | A copy of `model.json` is in `work/`. Delete that copy. The message does not print the watermark |
| `The system cannot find the path specified` or `No such file or directory` on the `cd` line | Run `dir`. If the list shows `alwaha`, you are already inside `problem_simulation`. Skip the `cd` line. If the list shows `app` and `tests`, this window is inside `work/`. Open a new terminal in the course folder, the one whose `dir` lists `problem_simulation` and `Module 02`, and run the block from the `cd` line |
| `SyntaxError` or `IndentationError` | Run `python "Module 02/Lesson 03/Student_Copy/prepare_work.py"` from the course folder. Then paste chapters 05 through 09 again from the chapter source. Do not repair the spaces by hand |

## Done

This lesson is done when both checks print `passed` and `work/knowledge.md` answers both questions.

Keep `work/` and the receipt-lines worksheet. The solution copy, when you receive it, is how you compare your pages with a finished set. Leave `problem_simulation/build` closed.

## What you open next

The Done section above is the gate. `knowledge.md` is part of that gate. The [optional review](../../../learning/review.md) is not filed. The checks do not read it.

If `Solution_Copy` is already on disk beside this folder, this is the moment it is for. Open [the solution README](../Solution_Copy/README.md) only after Done is true. Do not start in its `work/` folder. The trainer chapter there is optional.

This lesson is done. The next day deploys, then sequences Ain. The deployment standard arrives. You leave with a private-cloud URL and a health probe that reports the registered hash.

Open [the next lesson](<../../Lesson 04/Student_Copy/README.md>) and read `00-background.md` before any command.
