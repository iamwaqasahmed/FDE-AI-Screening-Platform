# 01 — Setup

[Chapter 00](00-background.md) said what the four weeks are and what today is. This chapter only sets up the machine: the classroom grader, and a `work/` folder that is yours. The client briefing starts in chapter 02.

You need Python 3.12 or newer, and the course folder from chapter 00. This student copy lives at `Week 02/Day 05/Student_Copy` inside that course folder. The two sections below get you both. Skip a section when you already have that piece.

## If `python` is not a command

On Windows:

1. Open [python.org/downloads/windows](https://www.python.org/downloads/windows/).
2. Download the newest Python 3 installer. Python 3.12 or newer is what this day uses.
3. Run the installer. On the first screen, tick **Add python.exe to PATH** at the bottom. Then click **Install Now**.
4. Close every terminal window you already had open. A terminal that was open during the install will not see Python. Open a new one after the install finishes.

On macOS, use [python.org/downloads/macos](https://www.python.org/downloads/macos/) and run the installer. Then quit Terminal and open it again.

Check with `python --version`. You should see Python 3.12 or a newer 3.x. If Windows still says `python` is not recognized, run `py --version`. When that prints a version, use `py` instead of `python` in every command today.

## If you cannot see the course folder

The course folder is the one that contains both `problem_simulation` and `Week 01`. This lesson is `Week 02/Day 05/Student_Copy` inside it. Leave `Solution_Copy` closed. That folder is for the end of the day.

Search the computer first. In File Explorer, click the search box and type `problem_simulation`. If a folder with that name appears, go up one level. The folder you land in, the one that contains `problem_simulation`, is the course folder.

If the search finds nothing, download the course:

1. Open [git-scm.com/download/win](https://git-scm.com/download/win/) and install Git. Accept the default options. On macOS, install from [git-scm.com/download/mac](https://git-scm.com/download/mac/).
2. Open a terminal in your Documents folder. On Windows, open Documents in File Explorer, click the address bar, type `cmd`, and press Enter.
3. Run:

```text
git clone https://github.com/iamwaqasahmed/FDE-AI-Screening-Platform.git
```

4. Open the new folder `FDE-AI-Screening-Platform`. That is the course folder. The lesson is `Week 02\Day 05\Student_Copy`. Start at its README. Leave `Solution_Copy` closed.

## How to open a terminal in the course folder

You will do this again in later chapters. The course folder is the one that contains `problem_simulation` and `Week 01`.

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

You should see `problem_simulation`, `Week 01`, and `Week 02` in the list. If you do not, this window is not the course folder. Use "If you cannot see the course folder" above, then open the terminal again from the folder you found or downloaded.

Then check Python:

```text
python --version
```

You should see Python 3.12 or a newer 3.x.

## Step 2 — Prepare the grader

The checks for today read two packs: yesterday's `rel-w2d4` and today's `rel-w2d5`. Build both. The terminal is still in the course folder. If that window is already inside `problem_simulation`, skip the `cd` line and run the python lines.

```text
cd problem_simulation
python -m alwaha.build --profile practice --release rel-w2d4
python -m alwaha.build --profile practice --release rel-w2d5
```

Each build prints four lines. The first line of the first build is `Wrote rel-w2d4 for practice`. The first line of the second build is `Wrote rel-w2d5 for practice`. Under each of those, look for a line that starts with `Pack:`, a line that starts with `Truth:`, and a line that starts with `Fingerprint:`. The folders on the Pack and Truth lines can be long. You do not open them.

`practice` is the shared classroom world. Leave the Truth folder closed. That folder is the grader's private files. The Pack line is another copy of files you already have in `packet/release` and `packet/day4`. Ignore it. Today you read this student copy.

## Step 3 — Create your workspace

The build used a terminal inside `problem_simulation`. Leave that window. Open a new terminal in the course folder, the same way as the top of this chapter. Then run:

```text
python "Week 02/Day 05/Student_Copy/prepare_work.py"
```

You should see these lines, in this order:

```text
Created work/ from the packet.
Leave the copies in packet/ unchanged.

Chapter 05 replaces work/sprint.md.
Chapter 06 replaces work/app/queue.py, work/app/file_ain.py, work/app/notify.py, work/tests/test_queue.py, work/tests/test_file.py, and work/tests/test_notify.py.
Chapter 07 replaces work/app/contract.py and work/tests/test_contract.py.
Chapter 08 replaces work/zones.md, work/operators.md, and work/deployment.md.
Chapter 09 replaces work/readout.md and work/retro.md.
Chapter 10 replaces work/knowledge.md.

The smoke files are copied and not replaced: admit.py, health.py, router.py, secrets.py, their tests, deploy/Dockerfile, deploy/deployment.yaml, and .github/workflows/ci.yml.

A second run of this file puts the blanks and the starter suite back.
```

The prompt returns after the last line. That is the command finishing. There is no error. In File Explorer, open `Week 02\Day 05\Student_Copy\work`. You should see `sprint.md`, a folder named `app`, a folder named `tests`, and a folder named `deploy`. If `work` is missing, this command did not run in the course folder. Run it again from that folder.

`work/` is the folder beside the chapters, at `Week 02/Day 05/Student_Copy/work`. It holds the shell, the shell tests, the image, the manifest, the workflow, and seven pages that still have empty sections. You will replace [sprint.md](work/sprint.md) in [chapter 05](05-the-sprint.md). You will replace [queue.py](work/app/queue.py), [file_ain.py](work/app/file_ain.py), [notify.py](work/app/notify.py), and their three tests in [chapter 06](06-the-booking.md). You will replace [contract.py](work/app/contract.py) and [test_contract.py](work/tests/test_contract.py) in [chapter 07](07-the-contract.md). You will replace [zones.md](work/zones.md), [operators.md](work/operators.md), and [deployment.md](work/deployment.md) in [chapter 08](08-the-pages.md). You will replace [readout.md](work/readout.md) and [retro.md](work/retro.md) in [chapter 09](09-the-readout.md). You will replace [knowledge.md](work/knowledge.md) in [chapter 10](10-finish.md). Those links open after this command. If a link does not open, use the folder path above. Leave the copies in `packet/` unchanged.

The smoke files are already the Day 4 finish. Chapter 06 names them and leaves them in place.

Run that command once before you edit. Do not run it again unless a later chapter tells you to. A second run copies the starter suite again and replaces the seven pages with the blanks. Anything you already pasted is gone. You would then paste chapters 05 through 10 again. Later chapters say to run it again only when a failure row says so.

The links in later chapters open files inside `work/`. If a link does not open, this command did not run from the course folder. Run it again from that folder, then go back to the chapter.

## If a command fails

| What you see | What to do |
| --- | --- |
| `python` is not recognized | Run `py --version`. If that prints Python 3.12 or newer, use `py` instead of `python` for the rest of the day |
| You cannot see `problem_simulation` in `dir` | The window is not the course folder. Open a terminal there, using the steps at the top of this chapter |
| `No module named alwaha` | The terminal is not inside `problem_simulation`. Open a new terminal in the course folder, run `cd problem_simulation`, and then the build command again |
| `The system cannot find the path specified` or `No such file or directory` on the `cd` line | This window is already inside `problem_simulation`. Skip the `cd` line and run the python line |
| `Build rel-w2d4 and rel-w2d5 first.` | One of the two builds in step 2 did not finish. Run both build commands again, then come back |
| The prepare script says it must stay next to `packet` | Run it as `python "Week 02/Day 05/Student_Copy/prepare_work.py"` from the course folder. Do not move the script |
| `can't open file` or `No such file or directory` on `prepare_work.py` | This window is not the course folder. `dir` should list `problem_simulation` and `Week 02`. Open a terminal there and run the command again |

This page is done when the prepare command has printed the lines above and the prompt is back, with no error.

Next: [02 — The role](02-the-role.md).
