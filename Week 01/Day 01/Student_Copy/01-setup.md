# 01 — Setup

[Chapter 00](00-background.md) said what the four weeks are and what today is. This chapter only sets up the machine: the classroom grader, and a `work/` folder that is yours. The client briefing starts in chapter 02.

You need Python 3.12 or newer, and the course folder from chapter 00. This student copy lives at `Week 01/Day 01/Student_Copy` inside that course folder. The two sections below get you both. Skip a section when you already have that piece.

## If `python` is not a command

On Windows:

1. Open [python.org/downloads/windows](https://www.python.org/downloads/windows/).
2. Download the newest Python 3 installer. Python 3.12 or newer is what this day uses.
3. Run the installer. On the first screen, tick **Add python.exe to PATH** at the bottom. Then click **Install Now**.
4. Close every terminal window you already had open. A terminal that was open during the install will not see Python.

On macOS, use [python.org/downloads/macos](https://www.python.org/downloads/macos/) and run the installer. Then quit Terminal and open it again.

Check with `python --version`. You should see Python 3.12 or a newer 3.x. If Windows still says `python` is not recognized, run `py --version`. When that prints a version, use `py` instead of `python` in every command today.

## If you cannot see the course folder

The course folder is the one that contains both `problem_simulation` and `Week 01`. This lesson is `Week 01/Day 01/Student_Copy` inside it. Leave `Solution_Copy` closed. That folder is for the end of the day.

Search the computer first. In File Explorer, click the search box and type `problem_simulation`. If a folder with that name appears, go up one level. The folder you land in, the one that contains `problem_simulation`, is the course folder.

If the search finds nothing, download the course:

1. Open [git-scm.com/download/win](https://git-scm.com/download/win/) and install Git. Accept the default options. On macOS, install from [git-scm.com/download/mac](https://git-scm.com/download/mac/).
2. Open a terminal in your Documents folder. On Windows, open Documents in File Explorer, click the address bar, type `cmd`, and press Enter.
3. Run:

```text
git clone https://github.com/iamwaqasahmed/FDE-AI-Screening-Platform.git
```

4. Open the new folder `FDE-AI-Screening-Platform`. That is the course folder. The lesson is `Week 01\Day 01\Student_Copy`. Start at its README. Leave `Solution_Copy` closed.

## How to open a terminal in the course folder

You will do this again in later chapters. The course folder is the one that contains `problem_simulation` and `Week 01`.

On Windows:

1. Open the course folder in File Explorer.
2. Click the address bar at the top.
3. Type `cmd` and press Enter.

A window opens, already inside the course folder. Later chapters call this "a terminal in the course folder." If your editor already has a terminal there, you can use that instead.

On macOS, open Terminal, type `cd ` with a space after it, drag the course folder onto the window, and press Enter. Use `ls` instead of `dir` in the next step. You are looking for the same two names.

## Step 1 — Check that you are in the right place

In that terminal:

```text
dir
```

You should see `problem_simulation` and `Week 01` in the list. If you do not, this window is not the course folder. Use "If you cannot see the course folder" above, then open the terminal again from the folder you found or downloaded.

Then check Python:

```text
python --version
```

You should see Python 3.12 or a newer 3.x.

## Step 2 — Prepare the grader

The terminal is still in the course folder.

```text
cd problem_simulation
python -m alwaha.build --profile practice --release rel-w1d1
```

You should see four lines. The first is `Wrote rel-w1d1 for practice`. Then a Pack line, a Truth line, and a Fingerprint line.

`practice` is the shared classroom world. `rel-w1d1` is today's file drop, week 1 day 1. Leave the Truth folder closed. That folder is the grader's private files. The Pack line is another copy of files you already have in `packet/`. Ignore it. Today you read and edit only this student copy.

## Step 3 — Create your workspace

The terminal is still inside `problem_simulation`. Come back to this student copy and run the prepare script.

```text
cd ..
cd "Week 01/Day 01/Student_Copy"
python prepare_work.py
```

You should see `Created work/ from the starter.` The dev credentials are now in `work/credentials/dev.json`. Leave that file closed. Do not type the watermark anywhere.

## Step 4 — Prove the copy is green

```text
cd work
python -m unittest discover -s tests -q
python scan.py
```

The test prints `OK` under a line that says one test ran. The scan prints:

```text
scan passed.
```

`work/` now contains `app.py`, `scan.py`, `tests/test_health.py`, `policy/pol-assistant-use.md`, `.gitignore`, `.github/workflows/ci.yml`, `credentials/dev.json`, and an empty `interviews/` folder. It also contains `Dockerfile`, `compose.yaml`, and `deploy/namespace.yaml`. Those three are the shape of a later deploy. You do not run them today. Chapter 07 says what each file is for.

If the scan says that `credentials/dev.json` is not in this copy, you are not inside `work`, or step 3 did not finish. Run step 3 again from `Week 01/Day 01/Student_Copy`.

## If a command fails

| What you see | What to do |
| --- | --- |
| `python` is not recognized | Run `py --version`. If that prints Python 3.12 or newer, use `py` instead of `python` for the rest of the day |
| You cannot see `problem_simulation` in `dir` | The window is not the course folder. Open a terminal there, using the steps at the top of this chapter |
| `No module named alwaha` | The terminal is not inside `problem_simulation`. From the course folder, run `cd problem_simulation` and then the build command again |
| `No truth for practice. Build rel-w1d1 first.` | Run step 2 again |
| The test cannot find `app` | The terminal is not inside `work`. Run `cd work` from the student copy, then the test again |
| The prepare script says it must stay next to `packet` | Run it as `python prepare_work.py` from `Week 01/Day 01/Student_Copy`, not from `work` |

Next: [02 — The role](02-the-role.md).
