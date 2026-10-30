# 01 — Setup

[Chapter 00](00-background.md) said what this release is. Python is already checked. Skip the installer and the download. Stay in the course folder you used for the earlier release today. This chapter prepares the grader for `rel-m04-l05` and creates this folder's `work/`. The earlier release's `work/` folder is a different folder. Leave it alone.

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

The checks for today read one pack: `rel-m04-l05`. Build it. The terminal is still in the course folder. If `dir` already shows `alwaha`, you are inside `problem_simulation`. Skip the `cd` line and run the python line. If `dir` shows neither `alwaha` nor `Module 02`, open a new terminal in the course folder.

```text
cd problem_simulation
python -m alwaha.build --profile practice --release rel-m04-l05
```

The build prints four lines. The first line is `Wrote rel-m04-l05 for practice`. Under that, look for a line that starts with `Pack:`, a line that starts with `Truth:`, and a line that starts with `Fingerprint:`. The folders on the Pack and Truth lines can be long. You do not open them.

`practice` is the shared classroom world. Leave the Truth folder closed. That folder is the grader's private files. The Pack line is another copy of files you already have in `packet/release`. Ignore the Pack folder. Today you read this student copy.

If a check later says `Build rel-m04-l05 first.`, this build did not finish, or the grader's gold file is missing. Run the build command again.

## Step 3 — Create your workspace

The build used a terminal inside `problem_simulation`. Leave that window. Open a new terminal in the course folder, the same way as the top of this chapter. Then run:

```text
python "Module 04/Lesson 05/Student_Copy/prepare_work.py"
```

You should see these lines, in this order:

```text
Created work/ from the packet.
Leave the copies in packet/ unchanged.

Chapter 05 replaces work/sprint.md.
Chapter 06 replaces work/app/signin.py, work/app/bus.py, work/app/handoff.py, work/app/leave.py, work/app/warehouse.py, and the work copies of test_signin.py, test_bus.py, test_handoff.py, test_leave.py, and test_warehouse.py.
Chapter 07 replaces work/app/rank.py, work/app/gates.py, work/app/personal.py, and the work copies of test_rank.py, test_gates.py, and test_personal.py.
Chapter 08 replaces work/architecture-deploy.md, work/operations.md, work/rcp/proposal.md, work/readout.md, work/retro.md, work/interviews/access-mgr.notes.md, and work/interviews/ea.notes.md.
Chapter 09 replaces work/knowledge.md.

The packet tests stay the shell tests.
The question files are copied and not replaced.
The workflow is copied and not replaced.

A second run of this file puts the blanks, the starter app, and the shell tests back.
```

The prompt returns after the last line. That is the command finishing. There is no error. A command that prints nothing else is finished the same way: the prompt is back, and there is no error.

In File Explorer, open `Module 04\Lesson 05\Student_Copy\work`. You should see `sprint.md`, `architecture-deploy.md`, `operations.md`, `readout.md`, `retro.md`, `knowledge.md`, a folder named `rcp`, a folder named `interviews`, a folder named `app`, and a folder named `tests`. Inside `rcp` you should see `proposal.md`. Inside `interviews` you should see `access-mgr.questions.txt`, `ea.questions.txt`, a blank `access-mgr.notes.md`, and a blank `ea.notes.md`. If those pages, the app, and the tests are there, the command worked. `.github` can wait. On Windows that folder is hidden. In File Explorer, open View and tick Hidden items. On macOS, in Finder, press Command+Shift+period. This day does not replace the workflow. You do not open `.github` today. If `work` is missing, this command did not run in the course folder. Run it again from that folder.

`work/` is the folder beside the chapters, at `Module 04/Lesson 05/Student_Copy/work`. It holds the shell, the shell tests, the workflow, and pages that still have empty sections. You will replace [sprint.md](work/sprint.md) in [chapter 05](05-the-sprint.md). You will replace [signin.py](work/app/signin.py), [bus.py](work/app/bus.py), [handoff.py](work/app/handoff.py), [leave.py](work/app/leave.py), [warehouse.py](work/app/warehouse.py), and the work copies of their tests in [chapter 06](06-the-connections.md). You will replace [rank.py](work/app/rank.py), [gates.py](work/app/gates.py), [personal.py](work/app/personal.py), and the work copies of their tests in [chapter 07](07-the-proposal.md). You will replace [architecture-deploy.md](work/architecture-deploy.md), [operations.md](work/operations.md), [proposal.md](work/rcp/proposal.md), [readout.md](work/readout.md), [retro.md](work/retro.md), [access-mgr.notes.md](work/interviews/access-mgr.notes.md), and [ea.notes.md](work/interviews/ea.notes.md) in [chapter 08](08-the-pages.md). You will replace [knowledge.md](work/knowledge.md) in [chapter 09](09-finish.md). Those links open after this command. If a link does not open, use the folder path above. Leave the copies in `packet/` unchanged. The packet tests stay the shell tests. A second run puts the shell tests back. The workflow is copied and not replaced. The question files are copied and not replaced.

Run that command once before you edit. Do not run it again unless a later chapter tells you to. A second run copies the starter app again, puts the shell tests back, and replaces the pages with the blanks. Anything you already pasted is gone. You would then paste chapters 05 through 09 again. Later chapters say to run it again only when a failure row says so.

The links in later chapters open files inside `work/`. If a link does not open, this command did not run from the course folder. Run it again from that folder, then go back to the chapter.

## Step 4 — The shell suite

The suite starts from a new terminal in the course folder. The demo in chapter 03 uses the window that is still inside `problem_simulation`. Leave that window for the demo. Do not use it for the suite. If the `cd` line cannot find the path, this window is still inside `problem_simulation`. Open a new terminal in the course folder. Do not skip that `cd` and run the suite inside `problem_simulation`.

```text
cd "Module 04/Lesson 05/Student_Copy/work"
python -m unittest discover -s tests -q
```

You should see a line that starts with `Ran 8 tests`, then a blank line, then `OK`.

That pass is the shell. The app is still the shell. The tests are still the shell tests. It is not the finished day. A roadmap that starts with triage, or a handoff with no summary, is not done. [Chapter 07](07-the-proposal.md) runs the suite again after the app files and the filled tests are replaced.

## If a command fails

| What you see | What to do |
| --- | --- |
| `python` is not recognized | Run `py --version`. If that prints Python 3.12 or newer, use `py` instead of `python` for the rest of the lesson |
| `command not found: python` | On macOS or Linux, run `python3 --version`. If that prints Python 3.12 or newer, use `python3` instead of `python` for the rest of the lesson |
| You cannot see `problem_simulation` in `dir` | The window is not the course folder. Open a terminal there, using the steps at the top of this chapter |
| `No module named alwaha` | The terminal is not inside `problem_simulation`. Open a new terminal in the course folder, run `cd problem_simulation`, and then the build command again |
| `The system cannot find the path specified` or `No such file or directory` on `cd problem_simulation` | Run `dir`. If the list shows `alwaha`, you are already inside `problem_simulation`. Skip the `cd` line. If the list shows `app` and `tests`, this window is inside `work/`. If it shows neither, this window is not the course folder. Open a new terminal in the course folder, the one whose `dir` lists `problem_simulation` and `Module 02`, and run the block from the `cd` line |
| `The system cannot find the path specified` or `No such file or directory` on `cd "Module 04/Lesson 05/Student_Copy/work"` | This window is still inside `problem_simulation`. Open a new terminal in the course folder and run both lines of that step. Do not skip that `cd` and run the suite inside `problem_simulation` |
| `Build rel-m04-l05 first.` | The build in step 2 did not finish, or the grader's gold file is missing. Run the build command again, then come back |
| The prepare script says it must stay next to `packet` | Run it as `python "Module 04/Lesson 05/Student_Copy/prepare_work.py"` from the course folder. Do not move the script |
| `can't open file` or `No such file or directory` on `prepare_work.py` | This window is not the course folder. `dir` should list `problem_simulation` and `Module 02`. Open a terminal there and run the command again |

This page is done when the prepare command has printed the lines above, the prompt is back with no error, and the shell suite has printed `Ran 8 tests` and `OK`. That suite pass is the shell. It is not the finished day.

Next: [02 — The role](02-the-role.md).
