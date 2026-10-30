# 01 — Setup

[Chapter 00](00-background.md) said what this release is. Python is already checked. Skip the installer and the download. Stay in the course folder you used for the earlier release today. This chapter prepares the grader for `rel-m02-l03` and creates this folder's `work/`. The earlier release's `work/` folder is a different folder. Leave it alone.

## How to open a terminal in the course folder

You will do this again in later chapters. The course folder is the one that contains `problem_simulation` and `Module 01`.

On Windows:

1. Open the course folder in File Explorer.
2. Click the address bar at the top.
3. Type `cmd` and press Enter.

A window opens, already inside the course folder. Later chapters call this "a terminal in the course folder." If your editor already has a terminal there, you can use that instead.

On macOS, open Terminal, type `cd ` with a space after it, drag the course folder onto the window, and press Enter. Use `ls` instead of `dir` in the next step. You are looking for the same names.

## Step 1 — Check that you are in the right place

In that terminal:

```text
dir
```

You should see `problem_simulation`, `Module 01`, and `Module 02` in the list. If you do not, this window is not the course folder. Open a terminal in the folder that contains `problem_simulation` and `Module 01`.

Then check Python:

```text
python --version
```

You should see Python 3.12 or a newer 3.x.

## Step 2 — Prepare the grader

The terminal is still in the course folder. If that window is already inside `problem_simulation`, skip the `cd` line and run the python line.

```text
cd problem_simulation
python -m alwaha.build --profile practice --release rel-m02-l03
```

The build prints four lines. The first is `Wrote rel-m02-l03 for practice`. Under that, look for a line that starts with `Pack:`, a line that starts with `Truth:`, and a line that starts with `Fingerprint:`. The folders on the Pack and Truth lines can be long. You do not open them.

`practice` is the shared classroom world. `rel-m02-l03` is today's file drop. Leave the Truth folder closed. That folder is the grader's private files. The Pack line is another copy of files you already have in `packet/release`. Ignore it. Today you read this student copy. Leave the earlier packs as they were. This command writes today's pack only.

## Step 3 — Create your workspace

The build used a terminal inside `problem_simulation`. Leave that window. Open a new terminal in the course folder, the same way as the top of this chapter. Then run:

```text
python "Module 02/Lesson 03/Student_Copy/prepare_work.py"
```

You should see these lines, in this order:

```text
Created work/ from the packet.
Leave the copies in packet/ unchanged.

Chapter 05 replaces work/sprint.md.
Chapter 06 replaces work/app/calendar_count.py and work/tests/test_calendar.py.
Chapter 07 replaces work/app/schema.py, work/tests/test_schema.py, and work/tests/test_journey.py.
Chapter 08 replaces work/app/receipt.py and work/tests/test_receipt.py.
Chapter 09 replaces work/usability.md, work/dod.md, work/crossings.md, and work/fixtures.md.
Leave .github/workflows/ci.yml as it is.

A second run of this file puts the blanks and the starter suite back.
```

The prompt returns after the last line. That is the command finishing. `work/` is a new folder beside the chapters, at `Module 02/Lesson 03/Student_Copy/work`. It holds the shell, the shell tests, the workflow, and five pages that still have empty sections. You will replace [sprint.md](work/sprint.md) in [chapter 05](05-the-sprint.md). You will replace [calendar_count.py](work/app/calendar_count.py) and [test_calendar.py](work/tests/test_calendar.py) in [chapter 06](06-the-calendar.md). You will replace [schema.py](work/app/schema.py), [test_schema.py](work/tests/test_schema.py), and [test_journey.py](work/tests/test_journey.py) in [chapter 07](07-the-reply.md). You will replace [receipt.py](work/app/receipt.py) and [test_receipt.py](work/tests/test_receipt.py) in [chapter 08](08-the-receipt.md). You will replace [usability.md](work/usability.md), [dod.md](work/dod.md), [crossings.md](work/crossings.md), and [fixtures.md](work/fixtures.md) in [chapter 09](09-the-pages.md). Those links open after this command. If a link does not open, use the folder path above. Leave the copies in `packet/` unchanged. Leave [ci.yml](work/.github/workflows/ci.yml) unchanged.

Run that command once before you edit. A second run copies the starter suite again and replaces the five pages with the blanks. It copies the workflow again. It does not edit the workflow.

## If a command fails

| What you see | What to do |
| --- | --- |
| `python` is not recognized | Run `py --version`. If that prints Python 3.12 or newer, use `py` instead of `python` for the rest of the lesson |
| `command not found: python` | On macOS or Linux, run `python3 --version`. If that prints Python 3.12 or newer, use `python3` instead of `python` for the rest of the lesson |
| You cannot see `problem_simulation` in `dir` | The window is not the course folder. Open a terminal there, using the steps at the top of this chapter |
| `No module named alwaha` | The terminal is not inside `problem_simulation`. Open a new terminal in the course folder, run `cd problem_simulation`, and then the build command again |
| `The system cannot find the path specified` or `No such file or directory` on the `cd` line | This window is already inside `problem_simulation`. Skip the `cd` line and run the python line |
| The prepare script says it must stay next to `packet` | Run it as `python "Module 02/Lesson 03/Student_Copy/prepare_work.py"` from the course folder. Do not move the script |
| `can't open file` or `No such file or directory` on `prepare_work.py` | This window is not the course folder. `dir` should list `problem_simulation` and `Module 02`. Open a terminal there and run the command again |

Next: [02 — The role](02-the-role.md).
