# 01 — Setup

[Chapter 00](00-background.md) said where this release sits, and what it is. This chapter sets up the machine: the classroom grader, and a `work/` folder that is yours. The client briefing starts in chapter 02.

You need Python 3.12 or newer, and the course folder from chapter 00. This student copy lives at `Module 01/Lesson 05/Student_Copy` inside that course folder. The two sections below get you both. Skip a section when you already have that piece.

## If `python` is not a command

On Windows:

1. Open [python.org/downloads/windows](https://www.python.org/downloads/windows/).
2. Download the newest Python 3 installer. Python 3.12 or newer is what this day uses.
3. Run the installer. On the first screen, tick **Add python.exe to PATH** at the bottom. Then click **Install Now**.
4. Close every terminal window you already had open. A terminal that was open during the install will not see Python. Open a new one after the install finishes.

On macOS, use [python.org/downloads/macos](https://www.python.org/downloads/macos/) and run the installer. Then quit Terminal and open it again.

Check with `python --version`. You should see Python 3.12 or a newer 3.x. If Windows still says `python` is not recognized, run `py --version`. When that prints a version, use `py` instead of `python` in every command today.

On macOS and Linux the python.org installer provides `python3`, and it often does not provide `python`. If `python --version` says the command is not found, run `python3 --version`. When that prints Python 3.12 or newer, use `python3` in place of `python` for every command that day. The same commands work in an editor terminal. On Windows that includes PowerShell.

## If you cannot see the course folder

The course folder is the one that contains both `problem_simulation` and `Module 01`. This lesson is `Module 01/Lesson 05/Student_Copy` inside it. Leave `Solution_Copy` closed. That folder is for the end of the lesson.

Search the computer first. In File Explorer, click the search box and type `problem_simulation`. If a folder with that name appears, go up one level. The folder you land in, the one that contains `problem_simulation`, is the course folder.

If the search finds nothing, download the course:

1. Open [git-scm.com/download/win](https://git-scm.com/download/win/) and install Git. Accept the default options. On macOS, install from [git-scm.com/download/mac](https://git-scm.com/download/mac/).
2. Open a terminal in your Documents folder. On Windows, open Documents in File Explorer, click the address bar, type `cmd`, and press Enter.
3. Run:

```text
git clone https://github.com/iamwaqasahmed/FDE-AI-Screening-Platform.git
```

4. Open the new folder `FDE-AI-Screening-Platform`. That is the course folder. The lesson is `Module 01\Lesson 05\Student_Copy`. Start at its README. Leave `Solution_Copy` closed.

## How to open a terminal in the course folder

You will do this again in later chapters. The course folder is the one that contains `problem_simulation` and `Module 01`.

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

You should see `problem_simulation` and `Module 01` in the list. If you do not, this window is not the course folder. Use "If you cannot see the course folder" above, then open the terminal again from the folder you found or downloaded.

Then check Python:

```text
python --version
```

You should see Python 3.12 or a newer 3.x.

## Step 2 — Prepare the grader

The terminal is still in the course folder. If that window is already inside `problem_simulation`, skip the `cd` line and run the two python lines.

```text
cd problem_simulation
python -m alwaha.build --profile practice --release rel-m01-l04
python -m alwaha.build --profile practice --release rel-m01-l05
```

Each build prints four lines. The first build starts with `Wrote rel-m01-l04 for practice`. The second starts with `Wrote rel-m01-l05 for practice`. Under each of those, look for a line that starts with `Pack:`, a line that starts with `Truth:`, and a line that starts with `Fingerprint:`. The folders on the Pack and Truth lines can be long. You do not open them.

`practice` is the shared classroom world. `rel-m01-l04` is yesterday's file drop. `rel-m01-l05` is today's. The agent check needs both. Leave the Truth folder closed. That folder is the grader's private files. The Pack line is another copy of files you already have in `packet/`. Ignore it. Today you read this student copy.

## Step 3 — Create your workspace

The build used a terminal inside `problem_simulation`. Leave that window. Open a new terminal in the course folder, the same way as the top of this chapter. Then run:

```text
python "Module 01/Lesson 05/Student_Copy/prepare_work.py"
```

You should see `Created work/agent from the packet.`

`work/agent` now holds [run.py](packet/agent/run.py), [model.py](packet/agent/model.py), [schema.py](packet/agent/schema.py), [memory.py](packet/agent/memory.py), and [tools.py](packet/agent/tools.py). You will replace three of those copies in [chapter 06](06-the-agent.md). Leave the copies in `packet/agent` unchanged.

Run that command once before you edit. A second run with no extra word copies the starter scripts again and replaces `model.py`, `schema.py`, and `memory.py`.

## If a command fails

| What you see | What to do |
| --- | --- |
| `python` is not recognized | Run `py --version`. If that prints Python 3.12 or newer, use `py` instead of `python` for the rest of the lesson |
| `command not found: python` | On macOS or Linux, run `python3 --version`. If that prints Python 3.12 or newer, use `python3` instead of `python` for the rest of the lesson |
| You cannot see `problem_simulation` in `dir` | The window is not the course folder. Open a terminal there, using the steps at the top of this chapter |
| `No module named alwaha` | The terminal is not inside `problem_simulation`. Open a new terminal in the course folder, run `cd problem_simulation`, and then the build command again |
| `The system cannot find the path specified` or `No such file or directory` on the `cd` line | This window is already inside `problem_simulation`. Skip the `cd` line and run the python lines |
| The prepare script says it must stay next to `packet` | Run it as `python "Module 01/Lesson 05/Student_Copy/prepare_work.py"` from the course folder. Do not move the script |

Next: [02 — The role](02-the-role.md).
